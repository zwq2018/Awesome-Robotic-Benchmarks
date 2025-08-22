
import yaml, os, re
from pathlib import Path
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
BENCH = ROOT / "benchmarks"
CHARTS = ROOT / "charts"
README = ROOT / "README.md"

DOMAIN_ORDER = [
    "Manipulation",
    "Navigation/SLAM",
    "Locomotion",
    "HRI",
    "Multitask/Embodied",
    "Industrial/Surgical",
    "Perception",
    "Simulation",
]

def slug(s: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

def load_entries():
    rows = []
    for yml in sorted(BENCH.glob("*.yaml")):
        with open(yml, "r", encoding="utf-8") as f:
            entry = yaml.safe_load(f)
        d = entry.get("first_release_date", "")
        dt = None
        if d:
            for fmt in ("%Y-%m-%d", "%Y"):
                try:
                    dt = datetime.strptime(d, fmt)
                    break
                except Exception:
                    pass
        rows.append({
            "name": entry.get("name",""),
            "domain": entry.get("domain","Other"),
            "first_release_date": entry.get("first_release_date",""),
            "dt": dt,
            "year": dt.year if dt else None,
            "tasks": ", ".join(entry.get("tasks",[])[:5]),
            "metrics": ", ".join(entry.get("metrics",[])[:5]),
            "homepage": entry.get("resources",{}).get("homepage",""),
            "paper": entry.get("resources",{}).get("paper",""),
            "code": entry.get("resources",{}).get("code",""),
        })
    return pd.DataFrame(rows)

def make_charts(df: pd.DataFrame):
    CHARTS.mkdir(exist_ok=True, parents=True)
    def order_key(x):
        return (DOMAIN_ORDER.index(x) if x in DOMAIN_ORDER else 999, x)
    for domain in sorted(df["domain"].dropna().unique(), key=order_key):
        ddf = df[df["domain"]==domain].copy()
        if ddf.empty:
            continue
        year_counts = ddf.dropna(subset=["year"]).groupby("year").size().sort_index()
        if year_counts.empty:
            continue
        plt.figure()
        year_counts.plot(kind="bar")
        plt.title(domain + " benchmarks per year")
        plt.xlabel("Year")
        plt.ylabel("Count")
        out = CHARTS / (slug(domain) + "_per_year.png")
        plt.tight_layout()
        plt.savefig(out, dpi=200)
        plt.close()

def linkify(text, url):
    return "[" + text + "](" + url + ")" if url else text

def build_readme(df: pd.DataFrame):
    def order_key(x):
        return (DOMAIN_ORDER.index(x) if x in DOMAIN_ORDER else 999, x)
    domains = sorted(df["domain"].dropna().unique(), key=order_key)
    toc_lines = ["- [" + d + "](#" + slug(d) + ")" for d in domains]
    header = (
        "# Robotics Benchmark Collection\n\n"
        "A curated, practical index of robotics benchmarks with usage notes and caveats.\n\n"
        "Sections are grouped by type and each list is sorted by first release date.\n\n"
        "> PRs welcome - see [CONTRIBUTING](CONTRIBUTING.md).\n\n"
        "## Types\n" + "\n".join(toc_lines) + "\n\n---\n"
    )
    body_parts = []
    for domain in domains:
        body_parts.append("\n## " + domain + "\n")
        chart_file = "charts/" + slug(domain) + "_per_year.png"
        if (CHARTS / (slug(domain) + "_per_year.png")).exists():
            body_parts.append("![" + domain + " per year](" + chart_file + ")\n")
        ddf = df[df["domain"]==domain].copy()
        ddf = ddf.sort_values(by=["dt","name"], ascending=[True, True], na_position="last")
        body_parts.append("| Benchmark | First Release | Tasks | Metrics | Links |")
        body_parts.append("|---|---:|---|---|---|")
        for _, r in ddf.iterrows():
            links_bits = []
            if r["homepage"]: links_bits.append(linkify("home", r["homepage"]))
            if r["paper"]: links_bits.append(linkify("paper", r["paper"]))
            if r["code"]: links_bits.append(linkify("code", r["code"]))
            links = " · ".join(links_bits) if links_bits else ""
            body_parts.append(f"| {r['name']} | {r['first_release_date']} | {r['tasks']} | {r['metrics']} | {links} |")
        body_parts.append("\n")
    README.write_text(header + "\n".join(body_parts), encoding="utf-8")

def main():
    df = load_entries()
    if df.empty:
        print("No entries found in benchmarks/.")
        return
    make_charts(df)
    build_readme(df)
    print("Built README with", len(df), "benchmarks across", df['domain'].nunique(), "types.")

if __name__ == "__main__":
    main()
