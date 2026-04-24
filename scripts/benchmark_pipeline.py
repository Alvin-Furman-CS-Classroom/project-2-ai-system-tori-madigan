"""Quick timing script for puzzle generation, solving, and uniqueness checks.

Run:
    python scripts/benchmark_pipeline.py
"""
from __future__ import annotations

import statistics as st
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

# Module 4 imports module3 with a top-level absolute import, so ensure src is on path.
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from src.module1_puzzle_generator import generate_puzzle
from src.module2_logic_representation import module1_to_module2
from src.module3_puzzle_solving import module2_to_module3
from src.module4_solution_verification import module1_2_3_to_module4


def benchmark_make_and_solve() -> None:
    configs = [
        (4, "easy", 200),
        (4, "medium", 200),
        (4, "hard", 200),
        (5, "easy", 120),
        (5, "medium", 120),
        (5, "hard", 80),
    ]
    print("=== Module 1 + 2 + 3 timing (ms) ===")
    print("grid diff   make_ms  solve_ms  make+solve_ms")
    for grid_size, difficulty, runs in configs:
        make_ms: list[float] = []
        solve_ms: list[float] = []
        total_ms: list[float] = []
        for _ in range(runs):
            t0 = time.perf_counter()
            puzzle = generate_puzzle(grid_size, difficulty)
            t1 = time.perf_counter()
            kb = module1_to_module2(puzzle.to_dict())
            _ = module2_to_module3(kb)
            t2 = time.perf_counter()
            make_ms.append((t1 - t0) * 1000)
            solve_ms.append((t2 - t1) * 1000)
            total_ms.append((t2 - t0) * 1000)
        print(
            f"{grid_size:>4} {difficulty:<6} "
            f"{st.mean(make_ms):8.2f} {st.mean(solve_ms):9.2f} {st.mean(total_ms):13.2f}"
        )
    print()


def benchmark_end_to_end_with_verification() -> None:
    grid_size, difficulty, runs = 4, "medium", 80
    times_ms: list[float] = []
    for _ in range(runs):
        t0 = time.perf_counter()
        puzzle = generate_puzzle(grid_size, difficulty)
        puzzle_dict = puzzle.to_dict()
        kb = module1_to_module2(puzzle_dict)
        solution = module2_to_module3(kb)
        _ = module1_2_3_to_module4(solution, puzzle_dict, kb)
        t1 = time.perf_counter()
        times_ms.append((t1 - t0) * 1000)
    print("=== Module 1 -> 2 -> 3 -> 4 timing (ms) ===")
    print(
        f"grid_size={grid_size} difficulty={difficulty} runs={runs} "
        f"avg_ms={st.mean(times_ms):.2f}"
    )
    print()


def benchmark_uniqueness_script() -> None:
    t0 = time.perf_counter()
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "verify_hand_puzzles.py")],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    t1 = time.perf_counter()
    print("=== Uniqueness check timing (brute force) ===")
    print(f"verify_hand_puzzles_ms={(t1 - t0) * 1000:.2f}")


def main() -> None:
    benchmark_make_and_solve()
    benchmark_end_to_end_with_verification()
    benchmark_uniqueness_script()


if __name__ == "__main__":
    main()
