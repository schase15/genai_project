# COMS 6998 Intro to DL and GenAI Fall 2024 Project
Authors:
- Steven Chase (sc4859)
- Sid Ijju (si2462)

## Automated Red Teaming for LLMs

## Key Components:
- `data/`: Contains the Jailbreak Benchmark dataset used for testing
- `main.py`: Primary script for running attacks, combining pre-attack and in-attack stages
- `preattack.py`: Generates actor networks and initial attack queries
- `inattack.py`: Executes attacks against target models with dynamic modifications
- `prompts/`: Template files for different stages of the attack and GOAT strategies
- `final_results/`: Output files containing evaluation metrics and comparisons
- `analysis/`: Contains scripts and outputs for the analysis of the final results

## Supported Models
Supported models via APIs
- OpenAI models (e.g., gpt-4o)
- DeepInfra models (e.g., meta-llama/Meta-Llama-3.1-405B-Instruct)

## Dependencies
1) Create environment
2) Install required packages

`pip install -r requirements.txt`

3) Make sure you have a `creds.env` file with the following api keys:
    - Openai: GPT_API_KEY=******
    - Deepinfra: DEEPINFRA_API_KEY=******

## Basic Usage (main.py)

Run a single attack:
```
python main.py
```

Parameters:
- `--questions`: Number of test questions to run. Default is 1
- `--actors`: Number of actors for each question, Default is 3
- `--behavior`: Path to CSV file containing test cases. Default is the jailbreak_bench.csv dataset
- `--attack_model_name`: Model used for generating attacks. Defualt is GPT-4o
- `--target_model_name`: Model being evaluated. Defualt is GPT-4o
- `--early_stop`: Stop if judge determines success. Default is True
- `--dynamic_modify`: Allow dynamic modification of queries. Default is True
- `--evaluate`: Generate evaluation metrics. Default is False

#### Output Files
Output files are created in the following directories:
- `pre_attack_result/`: Contains query chain planned by the attacker before engaging with the target
- `attack_result/`: Contains final attack results. The history of the dialog and the final score
- If evaluation is enabled (`--evaluate`):
  - `evaluation_result/eval_metrics_{timestamp}.json`: Parameters used for the evaluation as well as ASR
  - `evaluation_result/eval_detailed_{timestamp}.json`: Max score and final LLM response for each question

## Multiple Evaluations (run_evaluation.py)

To run multiple evaluations across different models:

```
python run_evaluation.py
```
Parameters:
- `--runs`: Number of evaluation runs per model. Default is 2
- `--questions`: Number of questions per run. Default is 100 (length of jailbreak bench dataset)
- `--actors`: Number of actors per question. Default is 3
- `--behavior`: Path to test cases CSV. Default is jailbreak_bench.csv dataset
- `--attack_model`: Model used for generating attacks. Default is gpt-4o
- `--target_models`: Space-separated list of models to evaluate. e.g. gpt-4o claude-sonnet-3-5-20241022
    - Default is gpt-4o
- `--early_stop`: Stop if judge determines success. Default is True
- `--dynamic_modify`: Allow dynamic modification of queries. Default is True
- `--evaluate`: Generate evaluation metrics. Default is True

#### Output Files
Creates aggregated results for each model in:
- `evaluation_result/aggregated_eval_{model_name}_{timestamp}.json`
  - Contains mean/std/min/max attack success rates
  - Includes parameters used across all runs

## Test Suite (test_models.py)

Run automated test suites across multiple models with both standard and GOAT attacks:

```
python test_models.py
```

The test suite configuration can be modified in the config dictionary within test_models.py:

Parameters:
- `--runs`: Number of evaluation runs per model. Default is 2
- `--questions`: Number of questions per run. Default is 100
- `--actors`: Number of actors per question. Default is 3
- `--behavior`: Path to test cases CSV. Default is "./data/jailbreakbench_harmful.csv"
- `--attack_model`: Model used for generating attacks. Default is "gpt-4o"
- `--target_models`: List of models to evaluate. Default includes:
  - gpt-4o-mini
  - gpt-4o
  - meta-llama/Meta-Llama-3.1-8B-Instruct
- `--early_stop`: Stop if judge determines success. Default is True
- `--dynamic_modify`: Allow dynamic modification of queries. Default is True
- `--evaluate`: Generate evaluation metrics. Default is True
- `--goat`: Enable GOAT attacks. Default is False

The test suite will:
1. Run evaluations without GOAT attacks
2. Run evaluations with GOAT attacks enabled
3. Generate comparison metrics between GOAT and non-GOAT performance


