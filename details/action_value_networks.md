# Action-Value Networks (Q(s, a))

Action-Value Networks estimate the expected cumulative future reward of taking action $a$ in state $s$ and then following policy $\pi$.

### Key Concepts
- **Q-Function:** Estimating $Q(s, a) = \mathbb{E}[\sum_t \gamma^t r_t | s_0 = s, a_0 = a]$.
- **DDPG / TD3:** Continuous control algorithms rely on Action-Value Networks to optimize continuous policies directly via the chain rule.

### System Diagram
```mermaid
graph LR
    State[State s] & Action[Action a] -->|Q-Network Q_theta| QValue[Estimated Q(s, a)]
```
