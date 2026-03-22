# Original 4×4 grid logic puzzles (three difficulties)

Three **original** puzzles for the *Logic Puzzle Generation and Analysis* project. Each uses **four categories with four items each**, **one-to-one** pairings, and a **unique** solution.

**Premise:** Four friends—**Ava**, **Ben**, **Cleo**, and **Dana**—each have exactly one **pet**, one favorite **drink**, and one **day off** this week. They sit in **four seats in a row**: **seat 1** is the **west (left) end**, then **2**, **3**, and **seat 4** is the **east (right) end**. Each seat has one person.

---

## Categories (all puzzles)

| # | Category | Items (each appears exactly once in the solution) |
|---|----------|---------------------------------------------------|
| 1 | **Name** | Ava, Ben, Cleo, Dana |
| 2 | **Pet** | Cat, Dog, Fish, Bird |
| 3 | **Drink** | Tea, Coffee, Juice, Water |
| 4 | **Day off** | Monday, Tuesday, Wednesday, Thursday |

*(Seats 1–4 are used in clues as **ordered positions** so you can use “immediately east of” logic; every name still sits in exactly one seat.)*

---

## Legend — Module 1 JSON (`E` / `A` / `V`)

| Symbol | Meaning |
|--------|---------|
| `E1` … `E4` | Ava, Ben, Cleo, Dana (fixed order) |
| `A1` | Seat: `V1`…`V4` = seats 1…4 (west → east) |
| `A2` | Pet: `V1` Cat, `V2` Dog, `V3` Fish, `V4` Bird |
| `A3` | Drink: `V1` Tea, `V2` Coffee, `V3` Juice, `V4` Water |
| `A4` | Day: `V1` Mon, `V2` Tue, `V3` Wed, `V4` Thu |

`relative_position` on **A1**: `index(Ea’s seat) = index(Eb’s seat) + offset` (see [LOGIC_PUZZLE_EXAMPLES.md](LOGIC_PUZZLE_EXAMPLES.md)).

---

## Blank logic grid

<div align="center">

<table>
<tbody>
<tr>
<td valign="top">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</td>
<td valign="top">

<table border="1" cellpadding="12" cellspacing="0">
  <thead>
    <tr>
      <th colspan="2" scope="col"></th>
      <th colspan="4" scope="colgroup">Name</th>
      <th colspan="4" scope="colgroup">Pet</th>
      <th colspan="4" scope="colgroup">Drink</th>
      <th colspan="4" scope="colgroup">Day off</th>
    </tr>
    <tr>
      <th colspan="2" scope="col">row \ col</th>
      <th scope="col">Ava</th>
      <th scope="col">Ben</th>
      <th scope="col">Cleo</th>
      <th scope="col">Dana</th>
      <th scope="col">Cat</th>
      <th scope="col">Dog</th>
      <th scope="col">Fish</th>
      <th scope="col">Bird</th>
      <th scope="col">Tea</th>
      <th scope="col">Coffee</th>
      <th scope="col">Juice</th>
      <th scope="col">Water</th>
      <th scope="col">Mon</th>
      <th scope="col">Tue</th>
      <th scope="col">Wed</th>
      <th scope="col">Thu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="rowgroup" rowspan="4">Name</th>
      <th scope="row">Ava</th>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
    </tr>
    <tr>
      <th scope="row">Ben</th>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
    </tr>
    <tr>
      <th scope="row">Cleo</th>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
    </tr>
    <tr>
      <th scope="row">Dana</th>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
    </tr>
    <tr>
      <th scope="rowgroup" rowspan="4">Pet</th>
      <th scope="row">Cat</th>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
    </tr>
    <tr>
      <th scope="row">Dog</th>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
    </tr>
    <tr>
      <th scope="row">Fish</th>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
    </tr>
    <tr>
      <th scope="row">Bird</th>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
    </tr>
    <tr>
      <th scope="rowgroup" rowspan="4">Drink</th>
      <th scope="row">Tea</th>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
    </tr>
    <tr>
      <th scope="row">Coffee</th>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
    </tr>
    <tr>
      <th scope="row">Juice</th>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
    </tr>
    <tr>
      <th scope="row">Water</th>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
    </tr>
    <tr>
      <th scope="rowgroup" rowspan="4">Day off</th>
      <th scope="row">Mon</th>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
    </tr>
    <tr>
      <th scope="row">Tue</th>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
    </tr>
    <tr>
      <th scope="row">Wed</th>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
    </tr>
    <tr>
      <th scope="row">Thu</th>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">?</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
    </tr>
  </tbody>
</table>

</td>
<td valign="top">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</td>
</tr>
</tbody>
</table>

</div>

---

## Puzzle 1 — Easy: *West-to-east lunch*

### Puzzle title

**West-to-east lunch** (Easy)

### Categories and items

Use the **four categories** in the table at the top (**Name, Pet, Drink, Day off**) with their four items each. Seats **1–4** (west → east) appear only in clues to fix **where** each person sits.

### Clues (9)

1. Ava sits in **seat 1** (the west end).
2. Ben sits in the seat **immediately east** of Ava.
3. Dana sits in the seat **immediately east** of Cleo.
4. Ava owns the **Cat** and drinks **Tea**.
5. Ben drinks **Coffee** and does **not** drink Water.
6. Cleo owns the **Fish**, drinks **Juice**, and has **Wednesday** off.
7. Dana owns the **Bird**, drinks **Water**, and has **Thursday** off.
8. Ben has **Tuesday** off.
9. Ava has **Monday** off.

### Solution

**Seats (1 = west … 4 = east):** Ava 1, Ben 2, Cleo 3, Dana 4.

**Legend:** **✓** = same person; **×** = ruled out; **—** = same category.

<div align="center">

<table>
<tbody>
<tr>
<td valign="top">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</td>
<td valign="top">

<table border="1" cellpadding="12" cellspacing="0">
  <thead>
    <tr>
      <th colspan="2" scope="col"></th>
      <th colspan="4" scope="colgroup">Name</th>
      <th colspan="4" scope="colgroup">Pet</th>
      <th colspan="4" scope="colgroup">Drink</th>
      <th colspan="4" scope="colgroup">Day off</th>
    </tr>
    <tr>
      <th colspan="2" scope="col">row \ col</th>
      <th scope="col">Ava</th>
      <th scope="col">Ben</th>
      <th scope="col">Cleo</th>
      <th scope="col">Dana</th>
      <th scope="col">Cat</th>
      <th scope="col">Dog</th>
      <th scope="col">Fish</th>
      <th scope="col">Bird</th>
      <th scope="col">Tea</th>
      <th scope="col">Coffee</th>
      <th scope="col">Juice</th>
      <th scope="col">Water</th>
      <th scope="col">Mon</th>
      <th scope="col">Tue</th>
      <th scope="col">Wed</th>
      <th scope="col">Thu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="rowgroup" rowspan="4">Name</th>
      <th scope="row">Ava</th>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Ben</th>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Cleo</th>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Dana</th>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
    </tr>
    <tr>
      <th scope="rowgroup" rowspan="4">Pet</th>
      <th scope="row">Cat</th>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Dog</th>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Fish</th>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Bird</th>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
    </tr>
    <tr>
      <th scope="rowgroup" rowspan="4">Drink</th>
      <th scope="row">Tea</th>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Coffee</th>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Juice</th>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Water</th>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
    </tr>
    <tr>
      <th scope="rowgroup" rowspan="4">Day off</th>
      <th scope="row">Mon</th>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
    </tr>
    <tr>
      <th scope="row">Tue</th>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
    </tr>
    <tr>
      <th scope="row">Wed</th>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
    </tr>
    <tr>
      <th scope="row">Thu</th>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
    </tr>
  </tbody>
</table>

</td>
<td valign="top">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</td>
</tr>
</tbody>
</table>

</div>

### Answer explanation

From **1–3**, the only way to seat four people with Ava at 1, Ben directly east of Ava, and Dana directly east of Cleo is **Ava 1, Ben 2, Cleo 3, Dana 4**. Clues **4–7** fix Ava, Cleo, and Dana on pet, drink, and day; **8–9** fix Ben’s and Ava’s days. The only pet left for Ben is the **Dog** (each pet once). All rows are consistent and **unique** (see verification).

---

## Puzzle 2 — Medium: *Rotating preferences*

### Puzzle title

**Rotating preferences** (Medium)

### Categories and items

Same **four categories** and item lists as in the introduction (Name, Pet, Drink, Day off).

### Clues (12)

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

*(Dana is fully determined: seat 4, Cat, Coffee, Wednesday.)*

### Solution

**Seats (1 = west … 4 = east):** Ava 1, Ben 2, Cleo 3, Dana 4.

**Legend:** **✓** = same person; **×** = ruled out; **—** = same category.

<div align="center">

<table>
<tbody>
<tr>
<td valign="top">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</td>
<td valign="top">

<table border="1" cellpadding="12" cellspacing="0">
  <thead>
    <tr>
      <th colspan="2" scope="col"></th>
      <th colspan="4" scope="colgroup">Name</th>
      <th colspan="4" scope="colgroup">Pet</th>
      <th colspan="4" scope="colgroup">Drink</th>
      <th colspan="4" scope="colgroup">Day off</th>
    </tr>
    <tr>
      <th colspan="2" scope="col">row \ col</th>
      <th scope="col">Ava</th>
      <th scope="col">Ben</th>
      <th scope="col">Cleo</th>
      <th scope="col">Dana</th>
      <th scope="col">Cat</th>
      <th scope="col">Dog</th>
      <th scope="col">Fish</th>
      <th scope="col">Bird</th>
      <th scope="col">Tea</th>
      <th scope="col">Coffee</th>
      <th scope="col">Juice</th>
      <th scope="col">Water</th>
      <th scope="col">Mon</th>
      <th scope="col">Tue</th>
      <th scope="col">Wed</th>
      <th scope="col">Thu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="rowgroup" rowspan="4">Name</th>
      <th scope="row">Ava</th>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
    </tr>
    <tr>
      <th scope="row">Ben</th>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Cleo</th>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Dana</th>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="rowgroup" rowspan="4">Pet</th>
      <th scope="row">Cat</th>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Dog</th>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
    </tr>
    <tr>
      <th scope="row">Fish</th>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Bird</th>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="rowgroup" rowspan="4">Drink</th>
      <th scope="row">Tea</th>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Coffee</th>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Juice</th>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
    </tr>
    <tr>
      <th scope="row">Water</th>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="rowgroup" rowspan="4">Day off</th>
      <th scope="row">Mon</th>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
    </tr>
    <tr>
      <th scope="row">Tue</th>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
    </tr>
    <tr>
      <th scope="row">Wed</th>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
    </tr>
    <tr>
      <th scope="row">Thu</th>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
    </tr>
  </tbody>
</table>

</td>
<td valign="top">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</td>
</tr>
</tbody>
</table>

</div>

### Answer explanation

**1–3** with four distinct seats force **Ava 1, Ben 2, Cleo 3, Dana 4** (the only arrangement with Ava westmost, Ben next east, and Dana east of Cleo). Clues **4–12** pin Ava, Ben, and Cleo on pet, drink, and day; **Dana** is the last person in seat **4** and takes the only unused pet (**Cat**), drink (**Coffee**), and day (**Wednesday**). **Unique** (see `MEDIUM_MIN` in `scripts/verify_hand_puzzles.py`).

---

## Puzzle 3 — Hard: *Chain of seats*

### Puzzle title

**Chain of seats** (Hard)

### Categories and items

Same **four categories** and item lists as in the introduction (Name, Pet, Drink, Day off).

### Clues (12)

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

*(Dana: seat 4, Dog, Tea, Wednesday.)*

### Solution

**Seats (1 = west … 4 = east):** Ava 1, Ben 2, Cleo 3, Dana 4.

**Legend:** **✓** = same person; **×** = ruled out; **—** = same category.

<div align="center">

<table>
<tbody>
<tr>
<td valign="top">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</td>
<td valign="top">

<table border="1" cellpadding="12" cellspacing="0">
  <thead>
    <tr>
      <th colspan="2" scope="col"></th>
      <th colspan="4" scope="colgroup">Name</th>
      <th colspan="4" scope="colgroup">Pet</th>
      <th colspan="4" scope="colgroup">Drink</th>
      <th colspan="4" scope="colgroup">Day off</th>
    </tr>
    <tr>
      <th colspan="2" scope="col">row \ col</th>
      <th scope="col">Ava</th>
      <th scope="col">Ben</th>
      <th scope="col">Cleo</th>
      <th scope="col">Dana</th>
      <th scope="col">Cat</th>
      <th scope="col">Dog</th>
      <th scope="col">Fish</th>
      <th scope="col">Bird</th>
      <th scope="col">Tea</th>
      <th scope="col">Coffee</th>
      <th scope="col">Juice</th>
      <th scope="col">Water</th>
      <th scope="col">Mon</th>
      <th scope="col">Tue</th>
      <th scope="col">Wed</th>
      <th scope="col">Thu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="rowgroup" rowspan="4">Name</th>
      <th scope="row">Ava</th>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
    </tr>
    <tr>
      <th scope="row">Ben</th>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Cleo</th>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Dana</th>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="rowgroup" rowspan="4">Pet</th>
      <th scope="row">Cat</th>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Dog</th>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Fish</th>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
    </tr>
    <tr>
      <th scope="row">Bird</th>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="rowgroup" rowspan="4">Drink</th>
      <th scope="row">Tea</th>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Coffee</th>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
    </tr>
    <tr>
      <th scope="row">Juice</th>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="row">Water</th>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
    </tr>
    <tr>
      <th scope="rowgroup" rowspan="4">Day off</th>
      <th scope="row">Mon</th>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
    </tr>
    <tr>
      <th scope="row">Tue</th>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
    </tr>
    <tr>
      <th scope="row">Wed</th>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
    </tr>
    <tr>
      <th scope="row">Thu</th>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#10003;</td>
      <td align="center">&#215;</td>
      <td align="center">&#215;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
      <td align="center">&#8212;</td>
    </tr>
  </tbody>
</table>

</td>
<td valign="top">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</td>
</tr>
</tbody>
</table>

</div>

### Answer explanation

**1–3** fix **Ava 1, Ben 2, Cleo 3, Dana 4**. Clues **4–12** fix Ava, Ben, and Cleo; **Dana** takes the remaining pet, drink, and day in seat **4**. **Unique** (see `HARD_MIN` in `scripts/verify_hand_puzzles.py`).

---

## Module 1 JSON (pipeline)

### Easy — `original_4x4_easy_bench`

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

### Medium — `original_4x4_medium_rotate`

Constraint set is **uniqueness-minimized** in `scripts/verify_hand_puzzles.py` (`MEDIUM_MIN`); narrative clues **1–12** match this solution.

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

### Hard — `original_4x4_hard_chain`

Matches **`HARD_MIN`** in `scripts/verify_hand_puzzles.py` (unique grid).

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

Brute-force uniqueness (column bijections on four attributes) lives in [`scripts/verify_hand_puzzles.py`](../scripts/verify_hand_puzzles.py):

- **EASY** — diagonal solution, **1** grid.
- **MEDIUM_MIN** — cyclic shift, **1** grid (matches Puzzle 2).
- **HARD_MIN** — mixed permutation, **1** grid (matches Puzzle 3).

Run: `python scripts/verify_hand_puzzles.py`
