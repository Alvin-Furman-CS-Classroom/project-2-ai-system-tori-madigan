# Module 6: Data Flow Visualization

This document visualizes how data flows through **Module 6 (Solution Explanation)**—the stage that turns formal solver output and analysis artifacts into a **human-readable narrative** (overall strategy + step-by-step reasoning).

## Data Flow Diagram

```mermaid
flowchart LR
    M1["Module 1<br/>Puzzle JSON"] --> M6[Module 6<br/>Solution Explanation]
    M2["Module 2<br/>Knowledge Base<br/>(text)"] --> M6
    M3["Module 3<br/>Solution + Proof<br/>(text)"] --> M6
    M5["Module 5<br/>Complexity Report<br/>(text)"] --> M6
    M6 --> Out["Explanation Report<br/>(text)"]

    style M1 fill:#e1f5ff
    style M2 fill:#e1f5ff
    style M3 fill:#e1f5ff
    style M5 fill:#e1f5ff
    style M6 fill:#fff4e1
    style Out fill:#e8f5e9
```

> **Note:** Module 4 is not a direct input to Module 6 in the table-driven design; its effect is already reflected in Module 5’s report and in whether the upstream pipeline is consistent.

## Detailed Data Flow

```mermaid
flowchart TD
    Start([Inputs]) --> ParseP[Parse puzzle<br/>JSON / dict]
    ParseP --> Parse3[Parse Module 3 text<br/>INFERENCE STEP COUNT<br/>numbered proof lines]
    Parse3 --> Parse5[Scan Module 5 text<br/>difficulty label / score]
    Parse5 --> Strat[Build Overall Strategy<br/>entities, clue mix,<br/>deduction vs decision,<br/>difficulty snippets]
    Strat --> Steps[Build Step-by-Step<br/>paraphrase each<br/>proof line]
    Steps --> Out([Explanation text])
    ParseP -->|invalid puzzle| Err([ValueError])

    style Start fill:#e1f5ff
    style ParseP fill:#fff4e1
    style Parse3 fill:#fff4e1
    style Parse5 fill:#fff4e1
    style Strat fill:#fff4e1
    style Steps fill:#fff4e1
    style Out fill:#e8f5e9
    style Err fill:#ffebee
```

## Primary entry point (Python)

```python
from module6_solution_explanation import module1_2_3_5_to_module6

explanation_text = module1_2_3_5_to_module6(
    puzzle_structure=puzzle_dict,       # dict or JSON string
    knowledge_base=kb_text,
    solution_proof_text=module3_output,
    complexity_report_text=module5_text,
)
```

| Input | Source | Role in Module 6 |
|--------|--------|------------------|
| Puzzle structure | Module 1 | Entity/attribute counts; summarize constraint **types** for strategy |
| Knowledge base | Module 2 | Confirms standard KB markers; narrative about facts + rules |
| Solution + proof | Module 3 | Parsed proof lines (`[deduction]`, `[decision]`) → step section |
| Complexity report | Module 5 | Difficulty score/label snippets → strategy section |

## Output shape (text report)

Conceptual layout:

```
=== SOLUTION EXPLANATION REPORT ===

=== OVERALL SOLUTION STRATEGY ===
<narrative paragraphs>

=== STEP-BY-STEP REASONING ===
### Step 1
**Propagation:** ...
### Step 2
**Search decision:** ...
...
```

## CLI

```bash
python -m src.module6_solution_explanation puzzle.json kb.txt module3.txt module5_report.txt
```

## Related docs

- Contract: [`module6_io_contract.md`](module6_io_contract.md)
- Easy explanation: [`MODULE_EXPLANATIONS.md`](MODULE_EXPLANATIONS.md) (Module 6 section)
