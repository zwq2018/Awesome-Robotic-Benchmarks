import yaml, os, re
from pathlib import Path
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
BENCH = ROOT / "benchmarks"

README = ROOT / "README.md"

# Streamlined domain taxonomy
DOMAIN_ORDER = [
    "Manipulation",
    "Locomotion", 
    "Navigation",
    "HRI",
    "Safety",
    "Simulation",
    "Other"
]

# Subtypes for each domain
SUBTYPE_MAP = {
    "Manipulation": ["table-top", "dexterous-hand", "dual-arm", "mobile-manipulation"],
    "Locomotion": ["humanoid", "bipedal", "quadrupedal", "wheeled"],
    "Navigation": ["social-navigation", "outdoor", "indoor", "multi-robot"],
    "HRI": ["collaboration", "communication", "social-interaction"],
    "Safety": ["collision-avoidance", "fail-safe", "human-safety"],
    "Simulation": ["sapien", "isaac-sim", "gazebo", "mujoco", "pybullet"],
    "Other": ["mixed", "interdisciplinary", "novel"]
}

def slug(s: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

def parse_date(date_str):
    """Parse date with multiple format support"""
    if not date_str:
        return None
    
    # Handle different date formats
    for fmt in ["%Y-%m-%d", "%Y-%m", "%Y"]:
        try:
            return datetime.strptime(str(date_str), fmt)
        except (ValueError, TypeError):
            continue
    return None

def load_entries():
    rows = []
    for yml in sorted(BENCH.glob("*.yaml")):
        try:
            with open(yml, "r", encoding="utf-8") as f:
                # Handle multiple documents, take first one
                documents = list(yaml.safe_load_all(f))
                entry = documents[0] if documents else {}
        except Exception as e:
            print(f"Error loading {yml}: {e}")
            continue
        
        if not entry:
            continue
            
        # Parse date
        dt = parse_date(entry.get("first_release_date"))
        
        # Count robot configurations
        robot_configs = entry.get("robot_config", [])
        num_robot_configs = len(robot_configs) if robot_configs else 0
        
        # Determine data collection method
        data_source_info = entry.get("data_source", {})
        if isinstance(data_source_info, dict):
            collection_method = data_source_info.get("collection_method", "unknown")
            dataset_size = data_source_info.get("size", "unknown")
        else:
            collection_method = "unknown"
            dataset_size = "unknown"
        
        rows.append({
            "name": entry.get("name", ""),
            "domain": entry.get("domain", "Other"),
            "subtype": entry.get("subtype", ""),
            "first_release_date": entry.get("first_release_date", ""),
            "dt": dt,
            "year": dt.year if dt else None,
            "description": entry.get("description", ""),
            "tasks": entry.get("tasks", []),
            "num_tasks": len(entry.get("tasks", [])),
            "metrics": entry.get("metrics", []),
            "num_metrics": len(entry.get("metrics", [])),
            "robot_config": robot_configs,
            "num_robot_configs": num_robot_configs,
            "modality": entry.get("modality", []),
            "setting": entry.get("setting", []),
            "collection_method": collection_method,
            "dataset_size": dataset_size,
            "homepage": entry.get("resources", {}).get("homepage", ""),
            "paper": entry.get("resources", {}).get("paper", ""),
            "code": entry.get("resources", {}).get("code", ""),
            "data": entry.get("resources", {}).get("data", ""),
            "leaderboard": entry.get("resources", {}).get("leaderboard", ""),
        })
    return pd.DataFrame(rows)




def linkify(text, url):
    return f"[{text}]({url})" if url else ""

def make_comparison_table(domain_df: pd.DataFrame, domain_name: str) -> str:
    """Create detailed comparison table for benchmarks within a domain"""
    if domain_df.empty:
        return ""
    
    # Sort by date, then name
    domain_df = domain_df.sort_values(by=["dt", "name"], ascending=[True, True], na_position="last")
    
    # Add subtype column for Manipulation domain
    if domain_name == "Manipulation":
        table_lines = [
            "| Benchmark | Year | Subtype | Tasks | Metrics | Robot Configs | Data Source | Links |",
            "|---|---:|---|---:|---:|---:|---|---|"
        ]
    else:
        table_lines = [
            "| Benchmark | Year | Tasks | Metrics | Robot Configs | Data Source | Links |",
            "|---|---:|---:|---:|---:|---|---|"
        ]
    
    for _, r in domain_df.iterrows():
        # Build links with emojis
        links_bits = []
        if r["homepage"]: links_bits.append(linkify("🏠", r["homepage"]))
        if r["paper"]: links_bits.append(linkify("📄", r["paper"]))
        if r["code"]: links_bits.append(linkify("💻", r["code"]))
        if r["data"]: links_bits.append(linkify("📊", r["data"]))
        if r["leaderboard"]: links_bits.append(linkify("🏆", r["leaderboard"]))
        links = " ".join(links_bits) if links_bits else "-"
        
        year_str = str(int(r["year"])) if pd.notna(r["year"]) else "N/A"
        
        if domain_name == "Manipulation":
            subtype = r["subtype"] if r["subtype"] else "-"
            table_lines.append(
                f"| {r['name']} | {year_str} | {subtype} | {r['num_tasks']} | {r['num_metrics']} | {r['num_robot_configs']} | {r['collection_method']} | {links} |"
            )
        else:
            table_lines.append(
                f"| {r['name']} | {year_str} | {r['num_tasks']} | {r['num_metrics']} | {r['num_robot_configs']} | {r['collection_method']} | {links} |"
            )
    
    return "\n".join(table_lines)

def build_readme(df: pd.DataFrame):
    """Build enhanced README with streamlined organization"""
    def order_key(x):
        return (DOMAIN_ORDER.index(x) if x in DOMAIN_ORDER else 999, x)
    
    domains = sorted(df["domain"].dropna().unique(), key=order_key)
    
    # Table of contents
    toc_lines = [f"- [{d}](#{slug(d)})" for d in domains]
    
    # Statistics
    total_benchmarks = len(df)
    domains_count = len(domains)
    
    header = f"""# Awesome Robotics Benchmarks

A curated, comprehensive collection of robotics benchmarks with detailed analysis and comparisons.

## Overview
- **{total_benchmarks}** benchmarks across **{domains_count}** domains
- Detailed metrics and robot configuration analysis


## Domains
{chr(10).join(toc_lines)}

---
"""
    
    body_parts = []
    for domain in domains:
        body_parts.append(f"\n## {domain}\n")
        
        domain_df = df[df["domain"] == domain].copy()
        benchmark_count = len(domain_df)
        
        body_parts.append(f"**{benchmark_count} benchmarks**\n")
        
        
        # Comparison table
        comparison_table = make_comparison_table(domain_df, domain)
        if comparison_table:
            body_parts.append("### Comparison\n")
            body_parts.append(comparison_table + "\n")
        
        # Benchmark descriptions
        body_parts.append("### Benchmarks\n")
        domain_df_sorted = domain_df.sort_values(by=["dt", "name"], ascending=[True, True], na_position="last")
        
        for _, r in domain_df_sorted.iterrows():
            # Build resource links
            links_parts = []
            if r["paper"]: links_parts.append(linkify("Paper", r["paper"]))
            if r["homepage"]: links_parts.append(linkify("Website", r["homepage"]))
            if r["code"]: links_parts.append(linkify("Code", r["code"]))
            if r["data"]: links_parts.append(linkify("Data", r["data"]))
            if r["leaderboard"]: links_parts.append(linkify("Leaderboard", r["leaderboard"]))
            
            links_str = " | ".join(links_parts) if links_parts else ""
            year_str = f" ({int(r['year'])})" if pd.notna(r["year"]) else ""
            
            body_parts.append(f"**{r['name']}**{year_str}: {r['description']}")
            if links_str:
                body_parts.append(f"  \n*Resources*: {links_str}")
            body_parts.append("")  # Empty line
    
    # Write the complete README
    README.write_text(header + "\n".join(body_parts), encoding="utf-8")

def main():
    df = load_entries()
    if df.empty:
        print("No entries found in benchmarks/.")
        return
    
    print(f"Loaded {len(df)} benchmarks")
    print(f"Domains: {', '.join(sorted(df['domain'].unique()))}")
    
    # Debug date parsing
    print(f"Dates parsed successfully: {df['dt'].notna().sum()}/{len(df)}")
    if df['dt'].notna().sum() > 0:
        print(f"Year range: {df['year'].min():.0f} - {df['year'].max():.0f}")
    
    build_readme(df)
    
    print(f"✅ Built README with {len(df)} benchmarks across {df['domain'].nunique()} domains.")

if __name__ == "__main__":
    main()