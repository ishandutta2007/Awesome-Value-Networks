# The Foundational Tabular Era (Temporal Difference Learning)

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
