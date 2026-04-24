# Module Grid Examples

These examples are generated with `scripts/ascii_grid_generator.py` and illustrate what each module contributes in the pipeline.

## Module 1 Example (CSP Puzzle Generation)

Generated candidate puzzle grid with unknown comparisons before any logical transformation.

## Module 1 Grid

### Inputs

- **A**: `Ann`, `Ben`, `Cam`
- **B**: `Red`, `Blu`, `Grn`
- **C**: `Cat`, `Dog`, `Fox`
- **D**: `Mon`, `Tue`, `Wed`

- **Column order**: `A`, `C`, `B`
- **Row order**: `D`, `C`, `B`
- **Unknown symbol**: `.`

### Output

```text
+----------+---+---+---+---+---+---+---+---+---+
|          |A  |   |   |C  |   |   |B  |   |   |
+----------+---+---+---+---+---+---+---+---+---+
|          |Ann|Ben|Cam|Cat|Dog|Fox|Red|Blu|Grn|
+----------+---+---+---+---+---+---+---+---+---+
|D Mon     |.  |.  |.  |.  |.  |.  |.  |.  |.  |
|D Tue     |.  |.  |.  |.  |.  |.  |.  |.  |.  |
|D Wed     |.  |.  |.  |.  |.  |.  |.  |.  |.  |
+----------+---+---+---+---+---+---+---+---+---+
|C Cat     |.  |.  |.  |   |   |   |   |   |   |
|C Dog     |.  |.  |.  |   |   |   |   |   |   |
|C Fox     |.  |.  |.  |   |   |   |   |   |   |
+----------+---+---+---+---+---+---+---+---+---+
|B Red     |.  |.  |.  |   |   |   |   |   |   |
|B Blu     |.  |.  |.  |   |   |   |   |   |   |
|B Grn     |.  |.  |.  |   |   |   |   |   |   |
+----------+---+---+---+---+---+---+---+---+---+
```

## Module 2 Example (Propositional Logic Representation)

Same puzzle structure, now interpreted as symbolic relationships to be encoded as propositions.

## Module 2 Grid

### Inputs

- **A**: `Ann`, `Ben`, `Cam`
- **B**: `Red`, `Blu`, `Grn`
- **C**: `Cat`, `Dog`, `Fox`
- **D**: `Mon`, `Tue`, `Wed`

- **Column order**: `A`, `C`, `B`
- **Row order**: `D`, `C`, `B`
- **Unknown symbol**: `.`

### Output

```text
+----------+---+---+---+---+---+---+---+---+---+
|          |A  |   |   |C  |   |   |B  |   |   |
+----------+---+---+---+---+---+---+---+---+---+
|          |Ann|Ben|Cam|Cat|Dog|Fox|Red|Blu|Grn|
+----------+---+---+---+---+---+---+---+---+---+
|D Mon     |.  |.  |.  |.  |.  |.  |.  |.  |.  |
|D Tue     |.  |.  |.  |.  |.  |.  |.  |.  |.  |
|D Wed     |.  |.  |.  |.  |.  |.  |.  |.  |.  |
+----------+---+---+---+---+---+---+---+---+---+
|C Cat     |.  |.  |.  |   |   |   |   |   |   |
|C Dog     |.  |.  |.  |   |   |   |   |   |   |
|C Fox     |.  |.  |.  |   |   |   |   |   |   |
+----------+---+---+---+---+---+---+---+---+---+
|B Red     |.  |.  |.  |   |   |   |   |   |   |
|B Blu     |.  |.  |.  |   |   |   |   |   |   |
|B Grn     |.  |.  |.  |   |   |   |   |   |   |
+----------+---+---+---+---+---+---+---+---+---+
```

## Module 3 Example (Inference/Solving)

Inference reasons over the same comparison space to derive a full assignment.

## Module 3 Grid

### Inputs

- **A**: `Ann`, `Ben`, `Cam`
- **B**: `Red`, `Blu`, `Grn`
- **C**: `Cat`, `Dog`, `Fox`
- **D**: `Mon`, `Tue`, `Wed`

- **Column order**: `A`, `C`, `B`
- **Row order**: `D`, `C`, `B`
- **Unknown symbol**: `.`

### Output

```text
+----------+---+---+---+---+---+---+---+---+---+
|          |A  |   |   |C  |   |   |B  |   |   |
+----------+---+---+---+---+---+---+---+---+---+
|          |Ann|Ben|Cam|Cat|Dog|Fox|Red|Blu|Grn|
+----------+---+---+---+---+---+---+---+---+---+
|D Mon     |.  |.  |.  |.  |.  |.  |.  |.  |.  |
|D Tue     |.  |.  |.  |.  |.  |.  |.  |.  |.  |
|D Wed     |.  |.  |.  |.  |.  |.  |.  |.  |.  |
+----------+---+---+---+---+---+---+---+---+---+
|C Cat     |.  |.  |.  |   |   |   |   |   |   |
|C Dog     |.  |.  |.  |   |   |   |   |   |   |
|C Fox     |.  |.  |.  |   |   |   |   |   |   |
+----------+---+---+---+---+---+---+---+---+---+
|B Red     |.  |.  |.  |   |   |   |   |   |   |
|B Blu     |.  |.  |.  |   |   |   |   |   |   |
|B Grn     |.  |.  |.  |   |   |   |   |   |   |
+----------+---+---+---+---+---+---+---+---+---+
```

## Module 4 Example (Solution Verification)

Verification checks solved assignments against constraints and entailment expectations across this grid structure.

## Module 4 Grid

### Inputs

- **A**: `Ann`, `Ben`, `Cam`
- **B**: `Red`, `Blu`, `Grn`
- **C**: `Cat`, `Dog`, `Fox`
- **D**: `Mon`, `Tue`, `Wed`

- **Column order**: `A`, `C`, `B`
- **Row order**: `D`, `B`, `C`
- **Unknown symbol**: `.`

### Output

```text
+----------+---+---+---+---+---+---+---+---+---+
|          |A  |   |   |C  |   |   |B  |   |   |
+----------+---+---+---+---+---+---+---+---+---+
|          |Ann|Ben|Cam|Cat|Dog|Fox|Red|Blu|Grn|
+----------+---+---+---+---+---+---+---+---+---+
|D Mon     |.  |.  |.  |.  |.  |.  |.  |.  |.  |
|D Tue     |.  |.  |.  |.  |.  |.  |.  |.  |.  |
|D Wed     |.  |.  |.  |.  |.  |.  |.  |.  |.  |
+----------+---+---+---+---+---+---+---+---+---+
|B Red     |.  |.  |.  |.  |.  |.  |   |   |   |
|B Blu     |.  |.  |.  |.  |.  |.  |   |   |   |
|B Grn     |.  |.  |.  |.  |.  |.  |   |   |   |
+----------+---+---+---+---+---+---+---+---+---+
|C Cat     |.  |.  |.  |   |   |   |   |   |   |
|C Dog     |.  |.  |.  |   |   |   |   |   |   |
|C Fox     |.  |.  |.  |   |   |   |   |   |   |
+----------+---+---+---+---+---+---+---+---+---+
```

## Module 5 Example (Complexity Analysis)

Complexity metrics (density, branching, search space) are computed from the same variable/value comparison footprint.

## Module 5 Grid

### Inputs

- **A**: `Ann`, `Ben`, `Cam`
- **B**: `Red`, `Blu`, `Grn`
- **C**: `Cat`, `Dog`, `Fox`
- **D**: `Mon`, `Tue`, `Wed`

- **Column order**: `A`, `C`, `B`
- **Row order**: `D`, `C`, `B`
- **Unknown symbol**: `.`

### Output

```text
+----------+---+---+---+---+---+---+---+---+---+
|          |A  |   |   |C  |   |   |B  |   |   |
+----------+---+---+---+---+---+---+---+---+---+
|          |Ann|Ben|Cam|Cat|Dog|Fox|Red|Blu|Grn|
+----------+---+---+---+---+---+---+---+---+---+
|D Mon     |.  |.  |.  |.  |.  |.  |.  |.  |.  |
|D Tue     |.  |.  |.  |.  |.  |.  |.  |.  |.  |
|D Wed     |.  |.  |.  |.  |.  |.  |.  |.  |.  |
+----------+---+---+---+---+---+---+---+---+---+
|C Cat     |.  |.  |.  |   |   |   |   |   |   |
|C Dog     |.  |.  |.  |   |   |   |   |   |   |
|C Fox     |.  |.  |.  |   |   |   |   |   |   |
+----------+---+---+---+---+---+---+---+---+---+
|B Red     |.  |.  |.  |   |   |   |   |   |   |
|B Blu     |.  |.  |.  |   |   |   |   |   |   |
|B Grn     |.  |.  |.  |   |   |   |   |   |   |
+----------+---+---+---+---+---+---+---+---+---+
```

## Module 6 Example (Knowledge Representation / Explanation)

Human-readable reasoning can reference this grid as the visual narrative for how conclusions are justified.

## Module 6 Grid

### Inputs

- **A**: `Ann`, `Ben`, `Cam`
- **B**: `Red`, `Blu`, `Grn`
- **C**: `Cat`, `Dog`, `Fox`
- **D**: `Mon`, `Tue`, `Wed`

- **Column order**: `A`, `C`, `B`
- **Row order**: `D`, `C`, `B`
- **Unknown symbol**: `.`

### Output

```text
+----------+---+---+---+---+---+---+---+---+---+
|          |A  |   |   |C  |   |   |B  |   |   |
+----------+---+---+---+---+---+---+---+---+---+
|          |Ann|Ben|Cam|Cat|Dog|Fox|Red|Blu|Grn|
+----------+---+---+---+---+---+---+---+---+---+
|D Mon     |.  |.  |.  |.  |.  |.  |.  |.  |.  |
|D Tue     |.  |.  |.  |.  |.  |.  |.  |.  |.  |
|D Wed     |.  |.  |.  |.  |.  |.  |.  |.  |.  |
+----------+---+---+---+---+---+---+---+---+---+
|C Cat     |.  |.  |.  |   |   |   |   |   |   |
|C Dog     |.  |.  |.  |   |   |   |   |   |   |
|C Fox     |.  |.  |.  |   |   |   |   |   |   |
+----------+---+---+---+---+---+---+---+---+---+
|B Red     |.  |.  |.  |   |   |   |   |   |   |
|B Blu     |.  |.  |.  |   |   |   |   |   |   |
|B Grn     |.  |.  |.  |   |   |   |   |   |   |
+----------+---+---+---+---+---+---+---+---+---+
```

