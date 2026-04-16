# Logic grid — monospaced ASCII (stair-step)

Use `scripts/ascii_grid_generator.py` to generate this visualization from input data.

Module-style output (same style as module visualization markdown docs):

```bash
py -3 scripts/ascii_grid_generator.py scripts/example_ascii_grid_input.json --module-format --title "Module Grid Visualization"
```

Specification for generators:

1. **Inputs:** VARIABLES in order (2–6), VALUES per variable (2–8 each). Variable A = first, B = second, … F = sixth (optional).
2. **Column group order:** A, then stepping backward through the rest: A, D, C, B, F, E, … (indices 0, n−1, n−2, …, 1).
3. **Row blocks (top to bottom):** One block per variable from the **last** down to **B**. Variable **A** never appears as rows (columns only).
4. **Which column groups appear in each row block (outer-edge stair, trimming from the right of the column order):**
   - Block for the **last** variable: all column groups in order.
   - Each block below: **one fewer** group from the **right** (drop B, then C, then D, …).
   - Block for **B**: **only** the column group for **A**.
5. **Same-variable regions:** Where the row variable equals the column group’s variable, there is **no** comparison — fill with **spaces** (not `.`).
6. **Known-unknown cells:** Use `.` for unknown comparison cells.
7. **Right padding:** After the active groups for that row block, use **spaces** so every line has the same width as the widest block (full first block), forming the outer-right stair.
8. **Output:** GitHub fenced code block (triple backticks), monospaced; include group header row, value header row, `+`/`-` separators, and aligned rows.

---

## Sample (4 variables — illustrative only)

Variables and order:

- **A** — Tool: `axe`, `bow`, `cup`  
- **B** — Hue: `red`, `grn`, `blu`  
- **C** — Rank: `rk1`, `rk2`, `rk3`  
- **D** — Zone (3-letter headers): `Est` (east), `Wst` (west), `Nth` (north)  

Column order: **A | C | B**. Row blocks top→bottom: **D**, then **B**, then **C**.

Each data cell is exactly three characters between `|` (use ` . ` for unknown, three spaces where no comparison exists). Every line is 48 characters wide (9 value columns) so the outer-right stair lines up.

```text
+----------+---+---+---+---+---+---+---+---+---+
|          | A |   |   | C |   |   | B |   |   |
+----------+---+---+---+---+---+---+---+---+---+
|          |axe|bow|cup|rk1|rk2|rk3|red|grn|blu|
+----------+---+---+---+---+---+---+---+---+---+
| D Est    | . | . | . | . | . | . | . | . | . |
| D Wst    | . | . | . | . | . | . | . | . | . |
| D Nth    | . | . | . | . | . | . | . | . | . |
+----------+---+---+---+---+---+---+---+---+---+
| B red    | . | . | . | . | . | . |   |   |   |
| B grn    | . | . | . | . | . | . |   |   |   |
| B blu    | . | . | . | . | . | . |   |   |   |
+----------+---+---+---+---+---+---+---+---+---+
| C rk1    | . | . | . |   |   |   |   |   |   |
| C rk2    | . | . | . |   |   |   |   |   |   |
| C rk3    | . | . | . |   |   |   |   |   |   |
+----------+---+---+---+---+---+---+---+---+---+
```
