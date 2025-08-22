# Awesome Robotics Benchmarks

A curated collection of robotics benchmarks organized by domain with detailed comparisons.

## Overview
- **9** benchmarks across **4** domains
- Each section includes benchmark descriptions and comparison summary

## Domains
- [Manipulation](#manipulation)
- [Simulation](#simulation)
- [Other](#other)
- [Navigation/SLAM](#navigation-slam)

---

## Manipulation

**6 benchmarks**

- **RLBench** (2019): A large-scale simulation benchmark with 100 hand-designed manipulation tasks across varied difficulty. Provides scripted demos via motion planning and is widely used for RL, imitation learning, multi-task, and few-shot studies.
  
  *Resources*: [Paper](https://arxiv.org/abs/1909.12271) | [Website](https://sites.google.com/view/rlbench) | [Code](https://github.com/stepjam/RLBench)

- **CALVIN** (2021): A benchmark for long-horizon, language-conditioned manipulation: agents follow sequences of unconstrained natural-language instructions. Released with teleoperated play data and language directives.
  
  *Resources*: [Paper](https://arxiv.org/abs/2112.03227) | [Website](https://calvin.cs.uni-freiburg.de/) | [Code](https://github.com/mees/calvin) | [Data](https://github.com/mees/calvin/tree/main/dataset)

- **LIBERO** (2023): A benchmark for lifelong robot learning featuring multitask manipulation with language conditioning. Focuses on knowledge transfer and generalization across diverse manipulation tasks.
  
  *Resources*: [Paper](https://arxiv.org/abs/2310.08531) | [Website](https://libero-project.github.io/) | [Code](https://github.com/Lifelong-Robot-Learning/LIBERO) | [Data](https://libero-project.github.io/)

- **RoboTwin** (2024): A generative digital-twin data generator and benchmark for bimanual (dual-arm) manipulation, using 3D generative models and LLMs to create diverse expert datasets and evaluation scenarios. RoboTwin 2.0 expands object libraries and unifies dual-arm evaluation.
  
  *Resources*: [Paper](https://arxiv.org/abs/2409.02920) | [Website](https://robotwin-platform.github.io/) | [Data](https://robotwin-platform.github.io/)

- **VLABench** (2024): A large-scale benchmark for language-conditioned manipulation with long-horizon reasoning: 100 task categories with strong randomization and 2,000+ objects. Evaluates both interactive VLA policies and non-interactive VLM reasoning.
  
  *Resources*: [Paper](https://arxiv.org/abs/2412.18194) | [Website](https://vlabench.github.io/) | [Code](https://github.com/OpenMOSS/VLABench) | [Data](https://vlabench.github.io/)

- **RoboCerebra** (2025): A long-horizon manipulation benchmark targeting System-2 abilities (planning, reflection, memory) with extended subtask sequences in household environments. Tasks/instructions are LLM-generated; trajectories are executed by humans in simulation.
  
  *Resources*: [Paper](https://arxiv.org/abs/2506.06677)

### Summary Comparison

| Benchmark | Subtype | Tasks | Metrics | Robot Configs | Data Source |
|---|---|---:|---:|---:|---|
| RLBench | table-top | 5 | 3 | 3 | motion_planner |
| CALVIN | table-top | 3 | 3 | 2 | human_teleoperation |
| LIBERO | table-top | 4 | 4 | 3 | human_teleoperation |
| RoboTwin | dual-arm | 3 | 3 | 3 | synthetic |
| VLABench | table-top | 3 | 3 | 1 | motion_planner |
| RoboCerebra | table-top | 3 | 3 | 1 | both |


## Simulation

**1 benchmarks**

- **RoboCasa** (2024): A large-scale simulation framework for training generalist robots in realistic kitchen environments: 120 scenes, 2,500+ objects, and 100 tasks (25 atomic + 75 composite). Includes 100K+ trajectories from human teleop and automated generation.
  
  *Resources*: [Paper](https://arxiv.org/abs/2406.02523) | [Website](https://robocasa.ai/) | [Code](https://github.com/robocasa/robocasa) | [Data](https://robocasa.ai/docs/introduction/installation.html)

### Summary Comparison

| Benchmark | Tasks | Metrics | Robot Configs | Data Source |
|---|---:|---:|---:|---|
| RoboCasa | 4 | 3 | 4 | both |


## Other

**1 benchmarks**

- **EmbodiedBench** (2025): A comprehensive benchmark to assess MLLM-based embodied agents across 1,128 tasks in four simulated environments—from high-level household semantics to low-level navigation/manipulation. Initial results show leading MLLMs still struggle (best ≈28.9% avg.).
  
  *Resources*: [Paper](https://openreview.net/forum?id=DgGF2LEBPS) | [Website](https://embodiedbench.github.io) | [Code](https://github.com/EmbodiedBench/EmbodiedBench) | [Data](https://embodiedbench.github.io)

### Summary Comparison

| Benchmark | Tasks | Metrics | Robot Configs | Data Source |
|---|---:|---:|---:|---|
| EmbodiedBench | 4 | 3 | 1 | synthetic |


## Navigation/SLAM

**1 benchmarks**

- **KITTI** (2012): 
  
  *Resources*: [Paper](https://doi.org/10.1109/CVPR.2012.6248074) | [Website](http://www.cvlibs.net/datasets/kitti/) | [Data](http://www.cvlibs.net/datasets/kitti/)

### Summary Comparison

| Benchmark | Tasks | Metrics | Robot Configs | Data Source |
|---|---:|---:|---:|---|
| KITTI | 4 | 4 | 0 | unknown |
