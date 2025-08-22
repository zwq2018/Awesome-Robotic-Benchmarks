# Awesome Robotics Benchmarks

A curated collection of robotics benchmarks organized by domain with concise, comparable tables.

Counts (tasks / metrics / robot configs) are recorded as numbers; modalities are listed in detail; SIM shows the simulator backend (e.g., CoppeliaSim, SAPIEN, MuJoCo).

## Domains
- [Manipulation](#manipulation)
- [EmbodiedAI (Generalist)](#embodiedai-generalist)
- [Navigation/SLAM](#navigation-slam)

---

## Manipulation

**7 benchmarks**

- **RLBench** (2019): A large-scale learning environment featuring 100 unique vision-guided manipulation tasks of varying difficulty:contentReference[oaicite:13]{index=13}. RLBench provides multimodal observations (RGB, depth, segmentation, proprioception) from multiple camera angles and an *infinite* supply of demonstration trajectories generated via built-in motion planners:contentReference[oaicite:14]{index=14}:contentReference[oaicite:15]{index=15}.
  
  *Resources*: [Paper](https://arxiv.org/abs/1909.12271 :contentReference[oaicite:21]{index=21}:contentReference[oaicite:22]{index=22}) | [Website](https://sites.google.com/view/rlbench :contentReference[oaicite:20]{index=20}) | [Code](https://github.com/stepjam/RLBench :contentReference[oaicite:23]{index=23}) | [Data](N/A (demos are generated on-the-fly by simulator):contentReference[oaicite:24]{index=24})

- **CALVIN** (2021): An open-source simulated benchmark for learning long-horizon language-conditioned robot manipulation tasks:contentReference[oaicite:0]{index=0}. It features a Franka Emika Panda arm in four tabletop environments and 34 distinct manipulation tasks with unconstrained language instructions:contentReference[oaicite:1]{index=1}.
  
  *Resources*: [Paper](https://arxiv.org/abs/2112.03227 :contentReference[oaicite:9]{index=9}) | [Website](https://calvin.cs.uni-freiburg.de (offline, see GitHub):contentReference[oaicite:8]{index=8}) | [Code](https://github.com/mees/calvin :contentReference[oaicite:10]{index=10}:contentReference[oaicite:11]{index=11}) | [Data](https://github.com/mees/calvin/tree/main/dataset (download scripts):contentReference[oaicite:12]{index=12})

- **LIBERO** (2023): A benchmark for lifelong robot learning featuring multitask manipulation with language conditioning. Focuses on knowledge transfer and generalization across diverse manipulation tasks.
  
  *Resources*: [Paper](https://arxiv.org/abs/2310.08531) | [Website](https://libero-project.github.io/) | [Code](https://github.com/Lifelong-Robot-Learning/LIBERO) | [Data](https://libero-project.github.io/)

- **RoboCasa** (2024): A large-scale simulation framework for generalist household robots, focusing on diverse kitchen environments:contentReference[oaicite:25]{index=25}. RoboCasa’s initial release includes 100 tasks (25 atomic foundational skills + 75 composite multi-skill activities) in realistic simulated kitchens, supported by thousands of 3D objects and high-quality human demonstrations:contentReference[oaicite:26]{index=26}:contentReference[oaicite:27]{index=27}.
  
  *Resources*: [Paper](https://arxiv.org/abs/2406.02523 :contentReference[oaicite:36]{index=36}:contentReference[oaicite:37]{index=37}) | [Website](https://robocasa.ai :contentReference[oaicite:35]{index=35}) | [Code](https://github.com/robcasa-team/robocasa (coming soon)) | [Data](Available on project website (human + generated demos):contentReference[oaicite:38]{index=38})

- **RoboTwin** (2024): A dual-arm manipulation benchmark and data-generation framework that uses generative 3D models and LLMs to create diverse bimanual task scenarios:contentReference[oaicite:53]{index=53}. RoboTwin provides a real-to-sim “digital twin” pipeline to generate varied object models and expert demonstrations, and an evaluation platform aligned with a real dual-arm robot (COBOT Magic platform):contentReference[oaicite:54]{index=54}:contentReference[oaicite:55]{index=55}. It combines simulated expert data with real-world teleoperated demos for coordinated two-arm tasks.
  
  *Resources*: [Paper](https://arxiv.org/abs/2409.02920 :contentReference[oaicite:63]{index=63}:contentReference[oaicite:64]{index=64}) | [Website](https://robotwin-benchmark.github.io :contentReference[oaicite:61]{index=61}:contentReference[oaicite:62]{index=62}) | [Code](https://github.com/RoboTwin-Platform/RoboTwin :contentReference[oaicite:65]{index=65}:contentReference[oaicite:66]{index=66}) | [Data](https://github.com/RoboTwin-Platform/RoboTwin/tree/main/data (simulated & real data):contentReference[oaicite:67]{index=67})

- **VLABench** (2024): A large-scale language-conditioned robotics benchmark for long-horizon reasoning tasks:contentReference[oaicite:69]{index=69}. VLABench defines 100 task categories (60 single-step “Primitive” tasks and 40 multi-step “Composite” tasks) spanning 2000+ distinct objects:contentReference[oaicite:70]{index=70}:contentReference[oaicite:71]{index=71}. Tasks involve understanding natural-language instructions with implicit intentions, requiring world-knowledge, commonsense, and multi-step planning beyond template commands:contentReference[oaicite:72]{index=72}:contentReference[oaicite:73]{index=73}.
  
  *Resources*: [Paper](https://arxiv.org/abs/2412.18194 :contentReference[oaicite:81]{index=81}) | [Website](https://vlabench.github.io :contentReference[oaicite:80]{index=80}) | [Code](https://github.com/OpenMOSS/VLABench :contentReference[oaicite:82]{index=82}) | [Data](https://huggingface.co/datasets/VLABench (official datasets):contentReference[oaicite:83]{index=83}:contentReference[oaicite:84]{index=84})

- **RoboCerebra** (2025): A benchmark for evaluating high-level reasoning in long-horizon manipulation:contentReference[oaicite:39]{index=39}. RoboCerebra provides a large-scale simulation dataset of complex household tasks with extended subtask sequences, generated by GPT-based instruction decomposition and executed by human operators in simulation:contentReference[oaicite:40]{index=40}:contentReference[oaicite:41]{index=41}. It emphasizes “System 2” planning skills (deliberative, goal-directed thinking) in vision-language-conditioned manipulation.
  
  *Resources*: [Paper](https://arxiv.org/abs/2506.06677 :contentReference[oaicite:49]{index=49}:contentReference[oaicite:50]{index=50}) | [Website](https://robocerebra.github.io (if available)) | [Code](https://huggingface.co/datasets/qiukingballball/RoboCerebra :contentReference[oaicite:51]{index=51}) | [Data](https://huggingface.co/datasets/qiukingballball/RoboCerebra :contentReference[oaicite:52]{index=52})

### Summary Comparison

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---:|---:|---:|---|---|---|---|
| RLBench | table-top | 100:contentReference[oaicite:16]{index=16} | 1 (task success rate) | 1 | - | CoppeliaSim (V-REP):contentReference[oaicite:17]{index=17}:contentReference[oaicite:18]{index=18} | motion_planner | 100 tasks × infinite demos (motion planner can generate unlimited trajectories):contentReference[oaicite:19]{index=19} |
| CALVIN | table-top | 34:contentReference[oaicite:2]{index=2} | 1 (primary metric: success rate):contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4} | 1 | - | PyBullet:contentReference[oaicite:5]{index=5} | human_teleoperation | Hours of teleoperated play data (20K language instructions):contentReference[oaicite:6]{index=6}; 4 environments (A–D) with ~23K trajectories for training:contentReference[oaicite:7]{index=7} |
| LIBERO | table-top | 50 | 4 | 3 | RGB, depth, proprioceptive, language | RoboSuite (MuJoCo) | human_teleoperation | 130+ tasks, with demonstrations |
| RoboCasa | mobile-manipulation (household) | 100 (25 atomic + 75 composite):contentReference[oaicite:28]{index=28} | 1 (success rate for task completion):contentReference[oaicite:29]{index=29} | 3 (supports single-arm mobiles, humanoids, quadruped-with-arm):contentReference[oaicite:30]{index=30} | - | PhysX (NVIDIA Omniverse):contentReference[oaicite:31]{index=31}:contentReference[oaicite:32]{index=32} | both | 100+K demonstration trajectories (e.g. 50 human demos ×25 skills + 72K generated):contentReference[oaicite:33]{index=33}:contentReference[oaicite:34]{index=34} |
| RoboTwin | dual-arm | ~14 (diverse dual-arm tasks used for benchmarking):contentReference[oaicite:56]{index=56} | 1 (task success rate) | 1 | - | Custom (generative pipeline with spatial planner; real robot: COBOT Magic):contentReference[oaicite:57]{index=57}:contentReference[oaicite:58]{index=58} | both | Synthetic dataset (hundreds of expert demos) + limited real demos per task:contentReference[oaicite:59]{index=59}:contentReference[oaicite:60]{index=60} |
| VLABench | table-top | 100:contentReference[oaicite:74]{index=74}:contentReference[oaicite:75]{index=75} | 1 (overall task success rate) | 1 | - | Custom simulator (Python-based, with physics and randomization):contentReference[oaicite:76]{index=76}:contentReference[oaicite:77]{index=77} | motion_planner | ≈50,000 expert episodes (≈500 demonstrations per task):contentReference[oaicite:78]{index=78}:contentReference[oaicite:79]{index=79} |
| RoboCerebra | table-top | 1,000 training tasks + 60 held-out tasks (1,060 total):contentReference[oaicite:42]{index=42}:contentReference[oaicite:43]{index=43} | 2 (sequence success rate and subtask completion):contentReference[oaicite:44]{index=44} | 1 | - | Not specified (custom sim with human teleoperation for data):contentReference[oaicite:45]{index=45}:contentReference[oaicite:46]{index=46} | both | 100k+ trajectories (e.g. 50 human demos ×25 skills + synthetic expansions):contentReference[oaicite:47]{index=47}:contentReference[oaicite:48]{index=48} |


## EmbodiedAI (Generalist)

**1 benchmarks**

- **EmbodiedBench** (2025): A comprehensive benchmark to evaluate vision-driven embodied agents (multi-modal LLM-based) across both high-level and low-level tasks:contentReference[oaicite:86]{index=86}. EmbodiedBench spans four simulated environments – EB-ALFRED and EB-Habitat (high-level household tasks), and EB-Navigation and EB-Manipulation (low-level navigation and robotic manipulation) – comprising 1,128 diverse test instances in total:contentReference[oaicite:87]{index=87}:contentReference[oaicite:88]{index=88}. It also defines six capability-oriented evaluation subsets to assess commonsense reasoning, complex instruction understanding, spatial awareness, visual perception, long-horizon planning, etc.:contentReference[oaicite:89]{index=89}:contentReference[oaicite:90]{index=90}
  
  *Resources*: [Paper](https://arxiv.org/abs/2502.09560 :contentReference[oaicite:100]{index=100}:contentReference[oaicite:101]{index=101}) | [Website](https://embodiedbench.github.io :contentReference[oaicite:98]{index=98}:contentReference[oaicite:99]{index=99}) | [Code](https://github.com/embodiedbench/EmbodiedBench :contentReference[oaicite:102]{index=102}:contentReference[oaicite:103]{index=103}) | [Data](https://huggingface.co/embodiedbench (evaluation data):contentReference[oaicite:104]{index=104})

### Summary Comparison

| Benchmark | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---:|---:|---:|---|---|---|---|
| EmbodiedBench | 1128 (testing tasks across 4 envs):contentReference[oaicite:91]{index=91} | 2 (e.g., success rate and subgoal success):contentReference[oaicite:92]{index=92}:contentReference[oaicite:93]{index=93} | 4 | - | Multiple – AI2-THOR (Unity) for EB-ALFRED, Habitat-Sim for EB-Habitat/Navigation, and a robotics simulator for EB-Manipulation:contentReference[oaicite:94]{index=94}:contentReference[oaicite:95]{index=95} | both (uses existing human-collected and synthetic tasks) | 1,128 evaluation scenarios (drawn from ALFRED, Habitat, etc.):contentReference[oaicite:96]{index=96}:contentReference[oaicite:97]{index=97} |


## Navigation/SLAM

**1 benchmarks**

- **KITTI** (2012): 
  
  *Resources*: [Paper](https://doi.org/10.1109/CVPR.2012.6248074) | [Website](http://www.cvlibs.net/datasets/kitti/) | [Data](http://www.cvlibs.net/datasets/kitti/)

### Summary Comparison

| Benchmark | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---:|---:|---:|---|---|---|---|
| KITTI | 4 | 4 |  | RGB, lidar, GPS/IMU | - | - | - |
