# Soft Value Functions (Maximum Entropy)

Soft Value Functions incorporate a policy entropy term to promote exploration and robustness by rewarding agents for choosing diverse strategies.

### Key Concepts
- **Entropy Regularization:** The objective scales rewards by adding policy entropy: $r(s, a) + lpha H(\pi(\cdot|s))$.
- **Soft Actor-Critic (SAC):** Maximizing both expected reward and policy entropy, leading to more robust policies that do not collapse prematurely.

### System Diagram
```mermaid
graph TD
    State[State s] -->|SAC Critic| SoftV[Soft Value V(s)]
    SoftV -->|Entropy Penalty| Regularizer[lpha H(pi)\]
    Regularizer -->|Optimize| Actor[Stochastic Policy]
```
