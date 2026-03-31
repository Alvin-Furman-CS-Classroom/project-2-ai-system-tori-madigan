"""Brute-force uniqueness check for 4x4 hand puzzles (column bijections)."""
from itertools import permutations


def check(sol, clues):
    for cl in clues:
        t = cl[0]
        if t == "eq":
            e, a, v = cl[1], cl[2], cl[3]
            if sol[e][a] != v:
                return False
        elif t == "neq":
            e, a, v = cl[1], cl[2], cl[3]
            if sol[e][a] == v:
                return False
        elif t == "diff":
            e1, e2, a = cl[1], cl[2], cl[3]
            if sol[e1][a] == sol[e2][a]:
                return False
        elif t == "rel":
            e1, e2, a, off = cl[1], cl[2], cl[3], cl[4]
            if sol[e1][a] != sol[e2][a] + off:
                return False
        elif t == "same":
            e1, e2, a = cl[1], cl[2], cl[3]
            if sol[e1][a] != sol[e2][a]:
                return False
    return True


def iter_grids():
    for c0 in permutations(range(4)):
        for c1 in permutations(range(4)):
            for c2 in permutations(range(4)):
                for c3 in permutations(range(4)):
                    sol = [[c0[e], c1[e], c2[e], c3[e]] for e in range(4)]
                    yield sol


def count_solutions(clues, limit=2):
    cnt = 0
    samples = []
    for sol in iter_grids():
        if check(sol, clues):
            cnt += 1
            samples.append([row[:] for row in sol])
            if cnt >= limit:
                break
    return cnt, samples


# E0=Ava, E1=Ben, E2=Cleo, E3=Dana
# A0=Seat 0..3 west-east, A1=Pet, A2=Drink, A3=Day off
# EASY target: Ei has all value i (same index in each category)

EASY = [
    ("eq", 0, 0, 0),
    ("rel", 1, 0, 0, 1),
    ("rel", 3, 2, 0, 1),
    ("eq", 0, 1, 0),
    ("eq", 0, 2, 0),
    ("neq", 1, 2, 3),
    ("eq", 1, 2, 1),
    ("eq", 1, 3, 1),
    ("eq", 2, 1, 2),
    ("eq", 2, 2, 2),
    ("eq", 2, 3, 2),
    ("eq", 3, 1, 3),
    ("eq", 3, 2, 3),
    ("eq", 3, 3, 3),
]

# Cyclic shift (medium)
MEDIUM_TARGET = [[0, 1, 2, 3], [1, 2, 3, 0], [2, 3, 0, 1], [3, 0, 1, 2]]
# Hard: mixed permutation
HARD_TARGET = [[0, 2, 1, 3], [1, 3, 2, 0], [2, 0, 3, 1], [3, 1, 0, 2]]

# Uniqueness-minimized equality + seat clues (matches Puzzle 3 markdown / JSON)
MEDIUM_MIN = [
    ("eq", 0, 0, 0),
    ("rel", 1, 0, 0, 1),
    ("rel", 3, 2, 0, 1),
    ("eq", 0, 1, 1),
    ("eq", 0, 2, 2),
    ("eq", 0, 3, 3),
    ("eq", 1, 1, 2),
    ("eq", 1, 2, 3),
    ("eq", 1, 3, 0),
    ("eq", 2, 1, 3),
    ("eq", 2, 2, 0),
    ("eq", 2, 3, 1),
]

HARD_MIN = [
    ("eq", 0, 0, 0),
    ("rel", 1, 0, 0, 1),
    ("rel", 3, 2, 0, 1),
    ("eq", 0, 1, 2),
    ("eq", 0, 2, 1),
    ("eq", 0, 3, 3),
    ("eq", 1, 1, 3),
    ("eq", 1, 2, 2),
    ("eq", 1, 3, 0),
    ("eq", 2, 1, 0),
    ("eq", 2, 2, 3),
    ("eq", 2, 3, 1),
]


def verify_target(clues, target, name):
    ok = check(target, clues)
    c, samples = count_solutions(clues, 5)
    print(f"{name}: matches_target={ok} solution_count={c}")
    if c == 1 and samples:
        print("  unique grid:", samples[0])
    elif samples:
        print("  sample:", samples[0])


def build_unique_clues(target, max_clues=12):
    """Greedy: add diverse clues true of target until solution is unique."""
    clues: list = [
        ("eq", 0, 0, 0),
        ("rel", 1, 0, 0, 1),
        ("rel", 3, 2, 0, 1),
    ]
    # Candidate pool: equalities from target; neq for one wrong value; diffs between entities
    pool: list = []
    for e in range(4):
        for a in range(4):
            v = target[e][a]
            pool.append(("eq", e, a, v))
            for wrong in range(4):
                if wrong != v:
                    pool.append(("neq", e, a, wrong))
    for a in range(4):
        for e1 in range(4):
            for e2 in range(e1 + 1, 4):
                if target[e1][a] != target[e2][a]:
                    pool.append(("diff", e1, e2, a))
    # De-duplicate while preserving order
    seen = set()
    uniq_pool = []
    for c in pool:
        if c in seen:
            continue
        seen.add(c)
        uniq_pool.append(c)
    # Remove already in clues
    base_set = set(clues)
    for c in uniq_pool:
        if c in base_set:
            continue
        ctry = clues + [c]
        n, _ = count_solutions(ctry, 2)
        if n < 2 or len(clues) >= max_clues - 1:
            clues.append(c)
            n2, _ = count_solutions(clues, 2)
            if n2 == 1:
                return clues
    # Fallback: add remaining equalities from target
    for e in range(4):
        for a in range(4):
            t = ("eq", e, a, target[e][a])
            if t not in clues:
                clues.append(t)
                if count_solutions(clues, 2)[0] == 1:
                    return clues
    return clues


def all_equalities(target):
    return [("eq", e, a, target[e][a]) for e in range(4) for a in range(4)]


def minimize_clues(target, seed_relatives=True):
    """Drop equalities while solution stays unique (greedy removal)."""
    clues = all_equalities(target)
    if seed_relatives:
        clues = [
            ("eq", 0, 0, 0),
            ("rel", 1, 0, 0, 1),
            ("rel", 3, 2, 0, 1),
        ] + [c for c in all_equalities(target) if c != ("eq", 0, 0, 0)]
    assert count_solutions(clues, 2)[0] == 1
    changed = True
    while changed:
        changed = False
        for i in range(len(clues) - 1, -1, -1):
            if clues[i][0] == "rel":
                continue
            trial = clues[:i] + clues[i + 1 :]
            if count_solutions(trial, 2)[0] == 1:
                clues = trial
                changed = True
                break
    return clues


if __name__ == "__main__":
    verify_target(EASY, [[i, i, i, i] for i in range(4)], "EASY")
    verify_target(MEDIUM_MIN, MEDIUM_TARGET, "MEDIUM_MIN_INLINE")
    verify_target(HARD_MIN, HARD_TARGET, "HARD_MIN_STATIC")

    print("\n--- Greedy unique sets ---")
    for name, tgt in [
        ("MEDIUM_BUILT", MEDIUM_TARGET),
        ("HARD_BUILT", HARD_TARGET),
    ]:
        cl = build_unique_clues(tgt, max_clues=14)
        verify_target(cl, tgt, name)
        print(f"  num_clues={len(cl)}")

    print("\n--- Minimized (house chain + eq) ---")
    for name, tgt in [
        ("MEDIUM_MIN", MEDIUM_TARGET),
        ("HARD_MIN", HARD_TARGET),
    ]:
        cl = minimize_clues(tgt)
        verify_target(cl, tgt, name)
        print(f"  num_clues={len(cl)}")
        print("  clues:", cl)
