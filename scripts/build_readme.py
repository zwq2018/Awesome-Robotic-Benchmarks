import yaml, re
from pathlib import Path
from datetime import datetime
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
BENCH = ROOT / "benchmarks"
README = ROOT / "README.md"

DOMAIN_ORDER = [
    "Manipulation",
    "Locomotion",
    "Navigation",
    "HRI",
    "Safety",
    "Simulation",
    "Generalist",
    "Other",
]

def slug(s: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

def parse_date(date_str):
    if not date_str:
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
        try:
            return datetime.strptime(str(date_str), fmt)
        except Exception:
            continue
    return None

def fmt_bool(v):
    if v is True:
        return "✓"
    if v is False:
        return "—"
    return "-"

def load_entries():
    rows = []
    for yml in sorted(BENCH.glob("*.yaml")):
        with open(yml, "r", encoding="utf-8") as f:
            entry = yaml.safe_load(f) or {}

        dt = parse_date(entry.get("first_release_date"))
        ds = entry.get("data_source", {}) or {}
        resources = entry.get("resources", {}) or {}

        # Fallback counts for non-simulation benchmarks
        task_count = entry.get("task_count")
        if task_count is None:
            task_count = len(entry.get("tasks", []) or [])
        metric_count = entry.get("metric_count")
        if metric_count is None:
            metric_count = len(entry.get("metrics", []) or [])
        robot_config_count = entry.get("robot_config_count")
        if robot_config_count is None:
            robot_config_count = len(entry.get("robot_config", []) or [])

        # Simulation-capability fields (used only when domain == "Simulation")
        physics_engine = entry.get("physics_engine", "")
        renderer = entry.get("renderer", "")
        gpu_support = entry.get("gpu_support", None)          # bool preferred
        os_field = entry.get("os", [])                        # list or str
        realtime = entry.get("realtime", None)                # bool preferred
        multi_agent = entry.get("multi_agent", None)          # bool preferred
        license_field = entry.get("license", "")

        rows.append({
            "name": entry.get("name",""),
            "domain": entry.get("domain","Other"),
            "subtype": entry.get("subtype",""),
            "first_release_date": entry.get("first_release_date",""),
            "dt": dt,
            "year": dt.year if dt else None,
            "description": entry.get("description",""),

            # non-simulation summary fields
            "task_count": task_count,
            "metric_count": metric_count,
            "robot_config_count": robot_config_count,
            "modality": ", ".join(entry.get("modality", []) or []),
            "setting": ", ".join(entry.get("setting", []) or []),
            "sim_backend": entry.get("sim_backend",""),
            "collection_method": ds.get("collection_method",""),
            "data_size": ds.get("size",""),

            # links
            "homepage": resources.get("homepage",""),
            "paper": resources.get("paper",""),
            "code": resources.get("code",""),
            "data": resources.get("data",""),
            "leaderboard": resources.get("leaderboard",""),

            # simulation capability fields
            "physics_engine": physics_engine,
            "renderer": renderer,
            "gpu_support": gpu_support,
            "os": os_field,
            "realtime": realtime,
            "multi_agent": multi_agent,
            "license": license_field,
        })
    return pd.DataFrame(rows)

def linkify(text, url):
    return f"[{text}]({url})" if url else ""

def make_summary_table(domain_df: pd.DataFrame, domain_name: str) -> str:
    if domain_df.empty:
        return ""
    domain_df = domain_df.sort_values(by=["dt","name"], ascending=[True, True], na_position="last")

    if domain_name != "Simulation":
        head = "| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |"
        sep  = "|---|---|---:|---:|---:|---|---|---|---|"
    else:
        # Capability-focused comparison for simulators
        head = "| Simulation | Physics Engine | Renderer | GPU Support | OS | Real-Time | Multi-Agent | License |"
        sep  = "|---|---|---|:---:|---|:---:|:---:|---|"

    lines = [head, sep]

    for _, r in domain_df.iterrows():
        if domain_name != "Simulation":
            cells = [
                r['name'],
                r.get('subtype') or "-",
                str(r['task_count'] or ""),
                str(r['metric_count'] or ""),
                str(r['robot_config_count'] or ""),
                r['modality'] or "-",
                r['sim_backend'] or "-",
                r['collection_method'] or "-",
                r['data_size'] or "-",
            ]
        else:
            os_val = r.get('os')
            if isinstance(os_val, list):
                os_cell = ", ".join(os_val) if os_val else "-"
            else:
                os_cell = os_val or "-"
            cells = [
                r['name'],
                r.get('physics_engine') or "-",
                r.get('renderer') or "-",
                fmt_bool(r.get('gpu_support')),
                os_cell,
                fmt_bool(r.get('realtime')),
                fmt_bool(r.get('multi_agent')),
                r.get('license') or "-",
            ]
        lines.append("| " + " | ".join(cells) + " |")

    return "\n".join(lines)

def build_readme(df: pd.DataFrame):
    def order_key(x):
        return (DOMAIN_ORDER.index(x) if x in DOMAIN_ORDER else 999, x)

    domains = sorted(df["domain"].dropna().unique(), key=order_key)
    toc = "\n".join([f"- [{d}](#{slug(d)})" for d in domains])

    header = (
        "# Awesome Robotics Benchmarks\n\n"
        "A curated collection of robotics benchmarks organized by domain with concise, comparable tables.\n\n"
        "Counts (tasks / metrics / robot configs) are recorded as numbers; modalities are listed in detail; "
        "SIM shows the simulator backend (e.g., CoppeliaSim, SAPIEN, MuJoCo).\n\n"
        "_For the **Simulation** domain, the summary table compares capabilities: physics engine, renderer, GPU support, OS, real-time, multi-agent, and license._\n\n"
        "human_teleoperation — trajectories recorded from a human controlling the robot/simulator (e.g., teleop, VR).\n\n"
        "motion_planner — trajectories generated/executed by a planner/IK/trajectory optimizer (e.g., MoveIt, RRT, CHOMP).\n\n"
        "synthetic — trajectories or episodes created programmatically or by generative scripts/LLMs without a physics-aware planner or human.\n\n"
        "NOTE: currently this repo is underdevelopment, any pr is welcomed.\n\n"
        "## Domains\n" + toc + "\n\n---\n"
    )

    body = []
    for domain in domains:
        ddf = df[df["domain"]==domain].copy()
        body.append(f"\n## {domain}\n")
        body.append(f"**{len(ddf)} benchmarks**\n")

        ddf = ddf.sort_values(by=["dt","name"], ascending=[True, True], na_position="last")
        for _, r in ddf.iterrows():
            year = f" ({int(r['year'])})" if pd.notna(r['year']) else ""
            line = f"- **{r['name']}**{year}: {r['description']}"
            links = [linkify('Paper', r['paper']), linkify('Website', r['homepage']), linkify('Code', r['code']), linkify('Data', r['data'])]
            links = " | ".join([x for x in links if x])
            if links:
                line += f"\n  \n  *Resources*: {links}"
            body.append(line)
            body.append("")

        body.append("### Summary Comparison\n")
        body.append(make_summary_table(ddf, domain))
        body.append("")

    README.write_text(header + "\n".join(body), encoding="utf-8")

def main():
    df = load_entries()
    if df.empty:
        print("No entries found in benchmarks/.")
        return
    build_readme(df)
    print("Built README for", len(df), "benchmarks.")

if __name__ == "__main__":
    main()
