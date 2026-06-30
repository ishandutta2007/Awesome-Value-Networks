import os

details_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Value-Networks\details"
os.makedirs(details_dir, exist_ok=True)

details = {
    "tabular_era": {
        "title": "The Foundational Tabular Era (Temporal Difference Learning)",
        "content": """# The Foundational Tabular Era (Temporal Difference Learning)

The Tabular Era represents the dawn of reinforcement learning, where state spaces were small enough to be represented explicitly in memory as matrices or look-up tables. Each unique state of the environment corresponds to a specific cell in a table containing its estimated value.

### Key Concepts
- **State Utility:** Representing $V(s)$ or $Q(s, a)$ as discrete entries in a table.
- **TD Learning:** Updating estimates based on the difference between successive predictions (temporal difference error).
- **Curse of Dimensionality:** As the number of state variables increases, the size of the state space grows exponentially, making tabular storage and exploration impossible for complex environments like Go or chess.

### System Diagram
```mermaid
graph TD
    S[Current State s] -->|Lookup| T[Tabular Value V(s)]
    T -->|Compute TD Error| E[TD Error: r + V(s') - V(s)]
    E -->|Update Table| T
```
"""
    },
    "deep_geometric_era": {
        "title": "The Deep Geometric Board Evaluation Era (AlphaGo / Deep Q-Networks)",
        "content": """# The Deep Geometric Board Evaluation Era (AlphaGo / Deep Q-Networks)

This era combined value estimation with deep convolutional neural networks (CNNs), allowing RL agents to scale to high-dimensional state spaces like pixel inputs or complex board configurations without manual feature engineering.

### Key Concepts
- **Deep Q-Networks (DQN):** Approximating $Q(s, a)$ using multi-layer neural networks (CNNs) trained with experience replay and target networks.
- **Geometric Board Evaluation:** In AlphaGo, a Value Network was trained to evaluate board states by treating the Go board as an image grid, extracting spatial features to predict the final winning probability.

### System Diagram
```mermaid
graph LR
    Input[Raw Pixels / Board Configuration] -->|Convolutions| Latent[Feature Map]
    Latent -->|Fully Connected| Output[Scalar Win Probability / Q-Values]
```
"""
    },
    "process_supervised_step_verifier_era": {
        "title": "The Process-Supervised Step Verifier Era",
        "content": """# The Process-Supervised Step Verifier Era

The step verifier era marks a transition from evaluating final outputs (Outcome-supervised Reward Models, or ORMs) to evaluating individual steps of reasoning (Process-supervised Reward Models, or PRMs) in large language models.

### Key Concepts
- **Step-by-Step Supervision:** Labeling the correctness of each intermediate step of a reasoning path.
- **Reducing Hallucinations:** By verifying intermediate steps, models can be guided along correct logical paths during test-time search.

### System Diagram
```mermaid
graph TD
    Step1[Reasoning Step 1] -->|Verify| PRM1{PRM Score}
    PRM1 -->|Good| Step2[Reasoning Step 2]
    PRM1 -->|Bad| Prune[Prune Path]
    Step2 -->|Verify| PRM2{PRM Score}
```
"""
    },
    "state_value_networks": {
        "title": "State-Value Networks (V(s))",
        "content": """# State-Value Networks (V(s))

State-Value Networks estimate the expected cumulative future reward starting from a given state $s$ under a policy $\pi$.

### Key Concepts
- **State Utility:** Calculating $V^{\pi}(s) = \mathbb{E}[\sum_t \gamma^t r_t | s_0 = s]$.
- **Baseline for Policy Gradients:** In Actor-Critic methods, $V(s)$ serves as a baseline to compute the Advantage $A(s, a) = Q(s, a) - V(s)$, reducing gradient variance.

### System Diagram
```mermaid
graph TD
    State[State s] -->|Value Network V_theta| Value[Estimated Value V(s)]
    State -->|Policy Network pi_phi| Policy[Action Distribution]
    Value & Policy -->|Compute Advantage| Adv[Advantage A(s,a)]
```
"""
    },
    "action_value_networks": {
        "title": "Action-Value Networks (Q(s, a))",
        "content": """# Action-Value Networks (Q(s, a))

Action-Value Networks estimate the expected cumulative future reward of taking action $a$ in state $s$ and then following policy $\pi$.

### Key Concepts
- **Q-Function:** Estimating $Q(s, a) = \mathbb{E}[\sum_t \gamma^t r_t | s_0 = s, a_0 = a]$.
- **DDPG / TD3:** Continuous control algorithms rely on Action-Value Networks to optimize continuous policies directly via the chain rule.

### System Diagram
```mermaid
graph LR
    State[State s] & Action[Action a] -->|Q-Network Q_theta| QValue[Estimated Q(s, a)]
```
"""
    },
    "soft_value_functions": {
        "title": "Soft Value Functions (Maximum Entropy)",
        "content": """# Soft Value Functions (Maximum Entropy)

Soft Value Functions incorporate a policy entropy term to promote exploration and robustness by rewarding agents for choosing diverse strategies.

### Key Concepts
- **Entropy Regularization:** The objective scales rewards by adding policy entropy: $r(s, a) + \alpha H(\pi(\cdot|s))$.
- **Soft Actor-Critic (SAC):** Maximizing both expected reward and policy entropy, leading to more robust policies that do not collapse prematurely.

### System Diagram
```mermaid
graph TD
    State[State s] -->|SAC Critic| SoftV[Soft Value V(s)]
    SoftV -->|Entropy Penalty| Regularizer[\alpha H(pi)\]
    Regularizer -->|Optimize| Actor[Stochastic Policy]
```
"""
    },
    "process_supervised_reward_models": {
        "title": "Process-Supervised Reward Models (PRMs)",
        "content": """# Process-Supervised Reward Models (PRMs)

PRMs evaluate intermediate steps of reasoning rather than just the final answer, making them highly effective for multi-step reasoning tasks like math and coding.

### Key Concepts
- **Granular Supervision:** Evaluates step-by-step logic, assigning a reward or probability of correctness to each step.
- **Search Guidance:** Integrates with beam search or MCTS to select the best reasoning paths at test-time.

### System Diagram
```mermaid
graph TD
    Input[Problem Prompt] --> Step1[Step 1 Generation]
    Step1 -->|PRM Evaluation| Score1[Score 1]
    Score1 -->|High Score| Step2[Step 2 Generation]
    Score1 -->|Low Score| Alternate[Retry Step 1]
```
"""
    },
    "mcts_evaluation": {
        "title": "Monte Carlo Tree Search (MCTS) Evaluation",
        "content": """# Monte Carlo Tree Search (MCTS) Evaluation

MCTS combined with Value Networks allows agents to plan ahead by looking into future scenarios, utilizing the value network to evaluate non-terminal states.

### Key Concepts
- **Selection & Expansion:** Traversed using a policy network.
- **Evaluation:** Value networks evaluate new leaf states directly, replacing long rollouts.
- **Backup:** Updating values of visited nodes along the trajectory path.

### System Diagram
```mermaid
graph TD
    Root[Root Node] -->|Select| Branch[Branch Node]
    Branch -->|Expand| Leaf[Leaf Node]
    Leaf -->|Value Network Evaluation| Value[Scalar Value V]
    Value -->|Backup| Root
```
"""
    },
    "best_of_n_sampling": {
        "title": "Best-of-N Sampling & Reranking",
        "content": """# Best-of-N Sampling & Reranking

Best-of-N sampling (or reranking) is a inference-time generation strategy where multiple candidates are sampled and then scored using a reward model.

### Key Concepts
- **Generative Sampling:** Generate $N$ diverse paths using a language model.
- **Value Scoring:** Use a value network or PRM to score each path.
- **Selection:** Serve the path with the highest score.

### System Diagram
```mermaid
graph TD
    Prompt[User Prompt] -->|Generate N Paths| Paths[Path 1, Path 2, ..., Path N]
    Paths -->|Scored by Value Network| Scores[Score 1, Score 2, ..., Score N]
    Scores -->|Select Max| Output[Highest-Scoring Output]
```
"""
    },
    "lookahead_pruning": {
        "title": "Inference-Time Lookahead Pruning",
        "content": """# Inference-Time Lookahead Pruning

Inference-time lookahead pruning leverages value networks to estimate the long-term safety or viability of states in real-time, proactively cutting off dangerous branches.

### Key Concepts
- **Safety Filtering:** Evaluates if a state could lead to an unavoidable failure mode (e.g., collisions in autonomous driving).
- **Receding Horizon Planning:** Continuously plans short sequences of actions, discarding plans that result in poor value scores.

### System Diagram
```mermaid
graph TD
    Current[Current State] --> Action1[Action Candidate A]
    Current --> Action2[Action Candidate B]
    Action1 -->|Lookahead Cost / Value| V1{V(s') > Threshold}
    Action2 -->|Lookahead Cost / Value| V2{V(s'') < Threshold}
    V1 -->|Keep| Plan1[Execute Path]
    V2 -->|Prune| Pruned[Safety Filter Triggered]
```
"""
    },
    "moving_target_overestimation": {
        "title": "The Moving Target and Overestimation Bias Bottleneck",
        "content": """# The Moving Target and Overestimation Bias Bottleneck

A core engineering challenge in value learning is that updating a value network using bootstrapping creates a moving target and propagates overestimation errors.

### Key Concepts
- **Bootstrapping:** Updating $Q(s, a)$ towards $r + \gamma \max_{a'} Q(s', a')$.
- **Overestimation Bias:** Systematic overestimation of action-values due to the maximization operator.
- **Target Networks:** Using a slow-updating copy of the network to compute target values, stabilizing training.
- **Twin-Critics:** Maintaining two independent value estimators and using the minimum of their predictions.

### System Diagram
```mermaid
graph TD
    State[State s] --> Q1[Q-Network 1] & Q2[Q-Network 2]
    Q1 & Q2 -->|Take Minimum| MinQ[Min Q Value]
    MinQ -->|Compute Target| Target[Slow Target Network]
```
"""
    },
    "high_compute_latency": {
        "title": "High Test-Time Search Compute Latency",
        "content": """# High Test-Time Search Compute Latency

Running deep neural networks repeatedly inside high-frequency planning loops (like MCTS or token generation) introduces significant latency bottlenecks.

### Key Concepts
- **Kernel Fusion:** Compiling matrix operations into custom Triton or TensorRT kernels to maximize memory bandwidth.
- **Model Distillation:** Distilling large evaluation models into smaller, faster architectures or single linear heads.

### System Diagram
```mermaid
graph LR
    PlanLoop[Planning Loop] -->|High Latency| LargeNet[Large Value Model]
    PlanLoop -->|Optimized Latency| FusedKernel[Fused Triton/TensorRT Kernel]
```
"""
    },
    "step_level_alignment": {
        "title": "Step-Level Alignment for Large Reasoning Models",
        "content": """# Step-Level Alignment for Large Reasoning Models

Step-Level Alignment applies process-supervised reward feedback to language model training, teaching models to think systematically.

### Key Concepts
- **Reinforcement Learning from Process Feedback (RLPF):** Using step-level reward signals to guide policy gradient algorithms.
- **Logical Verifiers:** Automatically checking intermediate reasoning steps against formal proofs or execution environments.

### System Diagram
```mermaid
graph TD
    Agent[Reasoning Agent] -->|Generates Step t| Step[Step t]
    Step -->|Evaluated by PRM| Reward[Step Reward]
    Reward -->|Update Policy| Agent
```
"""
    },
    "autonomous_flight_locomotion": {
        "title": "Autonomous Flight and Humanoid Locomotion Guidance Loops",
        "content": """# Autonomous Flight and Humanoid Locomotion Guidance Loops

In physical robotics, value networks serve as critical components for calculating control stability and safe flight trajectories under high-frequency constraints.

### Key Concepts
- **Joint-Torque Boundaries:** Estimating viability of dynamic foot placements or aerodynamic states.
- **High-Frequency Stacks:** Combining low-level high-frequency controllers with high-level value-guided path planning.

### System Diagram
```mermaid
graph TD
    Sensors[Robot Sensors] -->|State s| ValueNet[Value Network]
    ValueNet -->|Safe Horizon Evaluation| MPC[Model Predictive Controller]
    MPC -->|Joint Torques| Motors[Actuators / Motors]
```
"""
    },
    "quantitative_portfolio_risk": {
        "title": "High-Volume Quantitative Portfolio Risk Management",
        "content": """# High-Volume Quantitative Portfolio Risk Management

Distributed value networks estimate future portfolio variance and financial risk parameters under shifting macroeconomic factors.

### Key Concepts
- **Portfolio Optimization:** Estimating long-term risk-adjusted returns (Sharpe ratio) as a value function.
- **Distributed Risk Analysis:** Running parallel value evaluations across multi-asset options portfolios.

### System Diagram
```mermaid
graph TD
    Market[Market Data Streams] -->|Macro Parameters| ValueNet[Distributed Value Network]
    ValueNet -->|Risk/Reward Estimation| Execution[Automated Trade Execution]
```
"""
    }
}

for filename, data in details.items():
    filepath = os.path.join(details_dir, f"{filename}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(data["content"])
    print(f"Created {filepath}")
