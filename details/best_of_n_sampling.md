# Best-of-N Sampling & Reranking

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
