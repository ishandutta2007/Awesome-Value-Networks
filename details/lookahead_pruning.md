# Inference-Time Lookahead Pruning

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
