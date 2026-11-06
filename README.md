# ECE444 PRA7 — Static Analysis and CI with Ruff

Fork this repository to begin the practical. The starter includes a calculator,
two tests, and pinned development dependencies. You will configure Ruff,
pre-commit, and GitHub Actions during the lab.

## Environment

This lab was tested with **Python 3.15.2**. The commands below use Python 3.15.

## Start

### 1. Fork and clone locally

Fork this repository into your personal GitHub account.

In your terminal, clone your fork and enter its folder. Replace `YOUR_USERNAME`
with your GitHub username:

```sh
git clone https://github.com/YOUR_USERNAME/ece444-pra7-starter.git
cd ece444-pra7-starter
```

### 2. Set up the environment

Choose **one** command block for your platform. Each creates an isolated environment and
installs the pinned tools.

**macOS / Linux**

```sh
python3.15 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

**Windows — PowerShell**

```powershell
py -3.15 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
```

**Windows — Command Prompt**

```bat
py -3.15 -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements-dev.txt
```

Keep the environment active. You will run the tests as part of the activities
in the handout.

## Contents

- `calculator.py` and `test_calculator.py`: starter code and tests.
- `requirements-dev.txt`: development dependencies.
- [lab-assets/](lab-assets/): configuration templates and the flawed code sample.

## Attribution

This practical is adapted in structure from
[STAT 4160: Data Science Productivity Tools, Session 14 — pre-commit & GitHub Actions CI](https://ywanglab.github.io/STAT4160/lec14.html).
The calculator examples and ECE444 instructions were prepared for this practical.
