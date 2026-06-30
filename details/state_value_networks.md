# State-Value Networks (V(s))

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
