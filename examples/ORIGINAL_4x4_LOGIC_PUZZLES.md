# Original 4x4 Logic Grid Puzzles (Three Difficulties)

Three original puzzles for the Logic Puzzle Generation and Analysis project.  
Each puzzle uses:

- four categories,
- four items per category,
- one-to-one matching,
- a unique solution.

**Premise:** Four friends - **Ava**, **Ben**, **Cleo**, and **Dana** - each have exactly one **pet**, one favorite **drink**, and one **day off** this week. They sit in four seats in a row: **seat 1** is the west (left) end, then **2**, **3**, and **seat 4** is the east (right) end.

---

## Categories (All Puzzles)

| Category | Items |
|---|---|
| **Name** | Ava, Ben, Cleo, Dana |
| **Pet** | Cat, Dog, Fish, Bird |
| **Drink** | Tea, Coffee, Juice, Water |
| **Day off** | Monday, Tuesday, Wednesday, Thursday |

---

## Grid Legend

- **✓** = confirmed match
- **×** = ruled out
- **—** = same-category cell (unused)

---

## Standard Blank Grid (Use for Any Puzzle)

### Name x Pet

| Name \ Pet | Cat | Dog | Fish | Bird |
|---|---|---|---|---|
| Ava |  |  |  |  |
| Ben |  |  |  |  |
| Cleo |  |  |  |  |
| Dana |  |  |  |  |

### Name x Drink

| Name \ Drink | Tea | Coffee | Juice | Water |
|---|---|---|---|---|
| Ava |  |  |  |  |
| Ben |  |  |  |  |
| Cleo |  |  |  |  |
| Dana |  |  |  |  |

### Name x Day Off

| Name \ Day | Monday | Tuesday | Wednesday | Thursday |
|---|---|---|---|---|
| Ava |  |  |  |  |
| Ben |  |  |  |  |
| Cleo |  |  |  |  |
| Dana |  |  |  |  |

### Pet x Drink

| Pet \ Drink | Tea | Coffee | Juice | Water |
|---|---|---|---|---|
| Cat |  |  |  |  |
| Dog |  |  |  |  |
| Fish |  |  |  |  |
| Bird |  |  |  |  |

### Pet x Day Off

| Pet \ Day | Monday | Tuesday | Wednesday | Thursday |
|---|---|---|---|---|
| Cat |  |  |  |  |
| Dog |  |  |  |  |
| Fish |  |  |  |  |
| Bird |  |  |  |  |

### Drink x Day Off

| Drink \ Day | Monday | Tuesday | Wednesday | Thursday |
|---|---|---|---|---|
| Tea |  |  |  |  |
| Coffee |  |  |  |  |
| Juice |  |  |  |  |
| Water |  |  |  |  |

---

## Puzzle 1 (Easy)

### Puzzle Title

**West-to-East Lunch**

### Clues

1. Ava sits in **seat 1** (the west end).
2. Ben sits in the seat **immediately east** of Ava.
3. Dana sits in the seat **immediately east** of Cleo.
4. Ava owns the **Cat** and drinks **Tea**.
5. Ben drinks **Coffee** and does **not** drink Water.
6. Cleo owns the **Fish**, drinks **Juice**, and has **Wednesday** off.
7. Dana owns the **Bird**, drinks **Water**, and has **Thursday** off.
8. Ben has **Tuesday** off.
9. Ava has **Monday** off.

### Blank Grid

Use the **Standard Blank Grid** above.

### Solution Grid

**Seats:** Ava 1, Ben 2, Cleo 3, Dana 4.

| Name \ Category | Cat | Dog | Fish | Bird | Tea | Coffee | Juice | Water | Monday | Tuesday | Wednesday | Thursday |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ava | ✓ | × | × | × | ✓ | × | × | × | ✓ | × | × | × |
| Ben | × | ✓ | × | × | × | ✓ | × | × | × | ✓ | × | × |
| Cleo | × | × | ✓ | × | × | × | ✓ | × | × | × | ✓ | × |
| Dana | × | × | × | ✓ | × | × | × | ✓ | × | × | × | ✓ |

| Pet \ Drink/Day | Tea | Coffee | Juice | Water | Monday | Tuesday | Wednesday | Thursday |
|---|---|---|---|---|---|---|---|---|
| Cat | ✓ | × | × | × | ✓ | × | × | × |
| Dog | × | ✓ | × | × | × | ✓ | × | × |
| Fish | × | × | ✓ | × | × | × | ✓ | × |
| Bird | × | × | × | ✓ | × | × | × | ✓ |

| Drink \ Day | Monday | Tuesday | Wednesday | Thursday |
|---|---|---|---|---|
| Tea | ✓ | × | × | × |
| Coffee | × | ✓ | × | × |
| Juice | × | × | ✓ | × |
| Water | × | × | × | ✓ |

| Same-category cells | Name | Pet | Drink | Day off |
|---|---|---|---|---|
| Name | — |  |  |  |
| Pet |  | — |  |  |
| Drink |  |  | — |  |
| Day off |  |  |  | — |

---

## Puzzle 2 (Medium)

### Puzzle Title

**Rotating Preferences**

### Clues

1. Ava sits in **seat 1** (west end).
2. Ben sits **immediately east** of Ava.
3. Dana sits **immediately east** of Cleo.
4. Ava owns the **Dog**.
5. Ava drinks **Juice**.
6. Ava has **Thursday** off.
7. Ben owns the **Fish**.
8. Ben drinks **Water**.
9. Ben has **Monday** off.
10. Cleo owns the **Bird**.
11. Cleo drinks **Tea**.
12. Cleo has **Tuesday** off.

### Blank Grid

Use the **Standard Blank Grid** above.

### Solution Grid

**Seats:** Ava 1, Ben 2, Cleo 3, Dana 4.

| Name \ Category | Cat | Dog | Fish | Bird | Tea | Coffee | Juice | Water | Monday | Tuesday | Wednesday | Thursday |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ava | × | ✓ | × | × | × | × | ✓ | × | × | × | × | ✓ |
| Ben | × | × | ✓ | × | × | × | × | ✓ | ✓ | × | × | × |
| Cleo | × | × | × | ✓ | ✓ | × | × | × | × | ✓ | × | × |
| Dana | ✓ | × | × | × | × | ✓ | × | × | × | × | ✓ | × |

| Pet \ Drink/Day | Tea | Coffee | Juice | Water | Monday | Tuesday | Wednesday | Thursday |
|---|---|---|---|---|---|---|---|---|
| Cat | × | ✓ | × | × | × | × | ✓ | × |
| Dog | × | × | ✓ | × | × | × | × | ✓ |
| Fish | × | × | × | ✓ | ✓ | × | × | × |
| Bird | ✓ | × | × | × | × | ✓ | × | × |

| Drink \ Day | Monday | Tuesday | Wednesday | Thursday |
|---|---|---|---|---|
| Tea | × | ✓ | × | × |
| Coffee | × | × | ✓ | × |
| Juice | × | × | × | ✓ |
| Water | ✓ | × | × | × |

| Same-category cells | Name | Pet | Drink | Day off |
|---|---|---|---|---|
| Name | — |  |  |  |
| Pet |  | — |  |  |
| Drink |  |  | — |  |
| Day off |  |  |  | — |

---

## Puzzle 3 (Hard)

### Puzzle Title

**Chain of Seats**

### Clues

1. Ava sits in **seat 1** (west end).
2. Ben sits **immediately east** of Ava.
3. Dana sits **immediately east** of Cleo.
4. Ava owns the **Fish**.
5. Ava drinks **Coffee**.
6. Ava has **Thursday** off.
7. Ben owns the **Bird**.
8. Ben drinks **Juice**.
9. Ben has **Monday** off.
10. Cleo owns the **Cat**.
11. Cleo drinks **Water**.
12. Cleo has **Tuesday** off.

### Blank Grid

Use the **Standard Blank Grid** above.

### Solution Grid

**Seats:** Ava 1, Ben 2, Cleo 3, Dana 4.

| Name \ Category | Cat | Dog | Fish | Bird | Tea | Coffee | Juice | Water | Monday | Tuesday | Wednesday | Thursday |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ava | × | × | ✓ | × | × | ✓ | × | × | × | × | × | ✓ |
| Ben | × | × | × | ✓ | × | × | ✓ | × | ✓ | × | × | × |
| Cleo | ✓ | × | × | × | × | × | × | ✓ | × | ✓ | × | × |
| Dana | × | ✓ | × | × | ✓ | × | × | × | × | × | ✓ | × |

| Pet \ Drink/Day | Tea | Coffee | Juice | Water | Monday | Tuesday | Wednesday | Thursday |
|---|---|---|---|---|---|---|---|---|
| Cat | × | × | × | ✓ | × | ✓ | × | × |
| Dog | ✓ | × | × | × | × | × | ✓ | × |
| Fish | × | ✓ | × | × | × | × | × | ✓ |
| Bird | × | × | ✓ | × | ✓ | × | × | × |

| Drink \ Day | Monday | Tuesday | Wednesday | Thursday |
|---|---|---|---|---|
| Tea | × | × | ✓ | × |
| Coffee | × | × | × | ✓ |
| Juice | ✓ | × | × | × |
| Water | × | ✓ | × | × |

| Same-category cells | Name | Pet | Drink | Day off |
|---|---|---|---|---|
| Name | — |  |  |  |
| Pet |  | — |  |  |
| Drink |  |  | — |  |
| Day off |  |  |  | — |

---

## Module 1 JSON (Pipeline)

### Legend (`E` / `A` / `V`)

| Symbol | Meaning |
|---|---|
| `E1` to `E4` | Ava, Ben, Cleo, Dana (fixed order) |
| `A1` | Seat: `V1` to `V4` = seats 1 to 4 (west to east) |
| `A2` | Pet: `V1` Cat, `V2` Dog, `V3` Fish, `V4` Bird |
| `A3` | Drink: `V1` Tea, `V2` Coffee, `V3` Juice, `V4` Water |
| `A4` | Day: `V1` Mon, `V2` Tue, `V3` Wed, `V4` Thu |

`relative_position` on `A1`: `index(Ea seat) = index(Eb seat) + offset`.

### Easy - `original_4x4_easy_bench`

```json
{
  "puzzle_id": "original_4x4_easy_bench",
  "entities": ["E1", "E2", "E3", "E4"],
  "attributes": {
    "A1": ["V1", "V2", "V3", "V4"],
    "A2": ["V1", "V2", "V3", "V4"],
    "A3": ["V1", "V2", "V3", "V4"],
    "A4": ["V1", "V2", "V3", "V4"]
  },
  "constraints": [
    {"type": "equality", "entity": "E1", "attribute": "A1", "value": "V1"},
    {"type": "relative_position", "entity1": "E2", "entity2": "E1", "attribute": "A1", "offset": 1},
    {"type": "relative_position", "entity1": "E4", "entity2": "E3", "attribute": "A1", "offset": 1},
    {"type": "equality", "entity": "E1", "attribute": "A2", "value": "V1"},
    {"type": "equality", "entity": "E1", "attribute": "A3", "value": "V1"},
    {"type": "equality", "entity": "E1", "attribute": "A4", "value": "V1"},
    {"type": "inequality", "entity": "E2", "attribute": "A3", "value": "V4"},
    {"type": "equality", "entity": "E2", "attribute": "A3", "value": "V2"},
    {"type": "equality", "entity": "E2", "attribute": "A4", "value": "V2"},
    {"type": "equality", "entity": "E2", "attribute": "A2", "value": "V2"},
    {"type": "equality", "entity": "E3", "attribute": "A2", "value": "V3"},
    {"type": "equality", "entity": "E3", "attribute": "A3", "value": "V3"},
    {"type": "equality", "entity": "E3", "attribute": "A4", "value": "V3"},
    {"type": "equality", "entity": "E4", "attribute": "A2", "value": "V4"},
    {"type": "equality", "entity": "E4", "attribute": "A3", "value": "V4"},
    {"type": "equality", "entity": "E4", "attribute": "A4", "value": "V4"}
  ],
  "solution": {
    "E1": {"A1": "V1", "A2": "V1", "A3": "V1", "A4": "V1"},
    "E2": {"A1": "V2", "A2": "V2", "A3": "V2", "A4": "V2"},
    "E3": {"A1": "V3", "A2": "V3", "A3": "V3", "A4": "V3"},
    "E4": {"A1": "V4", "A2": "V4", "A3": "V4", "A4": "V4"}
  }
}
```

### Medium - `original_4x4_medium_rotate`

```json
{
  "puzzle_id": "original_4x4_medium_rotate",
  "entities": ["E1", "E2", "E3", "E4"],
  "attributes": {
    "A1": ["V1", "V2", "V3", "V4"],
    "A2": ["V1", "V2", "V3", "V4"],
    "A3": ["V1", "V2", "V3", "V4"],
    "A4": ["V1", "V2", "V3", "V4"]
  },
  "constraints": [
    {"type": "equality", "entity": "E1", "attribute": "A1", "value": "V1"},
    {"type": "relative_position", "entity1": "E2", "entity2": "E1", "attribute": "A1", "offset": 1},
    {"type": "relative_position", "entity1": "E4", "entity2": "E3", "attribute": "A1", "offset": 1},
    {"type": "equality", "entity": "E1", "attribute": "A2", "value": "V2"},
    {"type": "equality", "entity": "E1", "attribute": "A3", "value": "V3"},
    {"type": "equality", "entity": "E1", "attribute": "A4", "value": "V4"},
    {"type": "equality", "entity": "E2", "attribute": "A2", "value": "V3"},
    {"type": "equality", "entity": "E2", "attribute": "A3", "value": "V4"},
    {"type": "equality", "entity": "E2", "attribute": "A4", "value": "V1"},
    {"type": "equality", "entity": "E3", "attribute": "A2", "value": "V4"},
    {"type": "equality", "entity": "E3", "attribute": "A3", "value": "V1"},
    {"type": "equality", "entity": "E3", "attribute": "A4", "value": "V2"},
    {"type": "equality", "entity": "E4", "attribute": "A1", "value": "V4"},
    {"type": "equality", "entity": "E4", "attribute": "A2", "value": "V1"},
    {"type": "equality", "entity": "E4", "attribute": "A3", "value": "V2"},
    {"type": "equality", "entity": "E4", "attribute": "A4", "value": "V3"}
  ],
  "solution": {
    "E1": {"A1": "V1", "A2": "V2", "A3": "V3", "A4": "V4"},
    "E2": {"A1": "V2", "A2": "V3", "A3": "V4", "A4": "V1"},
    "E3": {"A1": "V3", "A2": "V4", "A3": "V1", "A4": "V2"},
    "E4": {"A1": "V4", "A2": "V1", "A3": "V2", "A4": "V3"}
  }
}
```

### Hard - `original_4x4_hard_chain`

```json
{
  "puzzle_id": "original_4x4_hard_chain",
  "entities": ["E1", "E2", "E3", "E4"],
  "attributes": {
    "A1": ["V1", "V2", "V3", "V4"],
    "A2": ["V1", "V2", "V3", "V4"],
    "A3": ["V1", "V2", "V3", "V4"],
    "A4": ["V1", "V2", "V3", "V4"]
  },
  "constraints": [
    {"type": "equality", "entity": "E1", "attribute": "A1", "value": "V1"},
    {"type": "relative_position", "entity1": "E2", "entity2": "E1", "attribute": "A1", "offset": 1},
    {"type": "relative_position", "entity1": "E4", "entity2": "E3", "attribute": "A1", "offset": 1},
    {"type": "equality", "entity": "E1", "attribute": "A2", "value": "V3"},
    {"type": "equality", "entity": "E1", "attribute": "A3", "value": "V2"},
    {"type": "equality", "entity": "E1", "attribute": "A4", "value": "V4"},
    {"type": "equality", "entity": "E2", "attribute": "A2", "value": "V4"},
    {"type": "equality", "entity": "E2", "attribute": "A3", "value": "V3"},
    {"type": "equality", "entity": "E2", "attribute": "A4", "value": "V1"},
    {"type": "equality", "entity": "E3", "attribute": "A2", "value": "V1"},
    {"type": "equality", "entity": "E3", "attribute": "A3", "value": "V4"},
    {"type": "equality", "entity": "E3", "attribute": "A4", "value": "V2"},
    {"type": "equality", "entity": "E4", "attribute": "A1", "value": "V4"},
    {"type": "equality", "entity": "E4", "attribute": "A2", "value": "V2"},
    {"type": "equality", "entity": "E4", "attribute": "A3", "value": "V1"},
    {"type": "equality", "entity": "E4", "attribute": "A4", "value": "V3"}
  ],
  "solution": {
    "E1": {"A1": "V1", "A2": "V3", "A3": "V2", "A4": "V4"},
    "E2": {"A1": "V2", "A2": "V4", "A3": "V3", "A4": "V1"},
    "E3": {"A1": "V3", "A2": "V1", "A3": "V4", "A4": "V2"},
    "E4": {"A1": "V4", "A2": "V2", "A3": "V1", "A4": "V3"}
  }
}
```

---

## Verification

Brute-force uniqueness (column bijections on four attributes) is in `scripts/verify_hand_puzzles.py`:

- `EASY` -> 1 valid grid
- `MEDIUM_MIN` -> 1 valid grid (Puzzle 2)
- `HARD_MIN` -> 1 valid grid (Puzzle 3)

Run:

```bash
python scripts/verify_hand_puzzles.py
```
