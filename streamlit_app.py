"""
Streamlit UI for the Logic Puzzle Generation and Analysis System.

Runs the Module 1 → 2 → 3 → 4 → 5 → 6 pipeline and displays outputs in a user-friendly way.

Start:
  PYTHONPATH=src streamlit run streamlit_app.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict

import streamlit as st

# Ensure `src/` is importable when running via Streamlit from repo root.
SRC_DIR = Path(__file__).parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from module1_puzzle_generator import generate_puzzle  # noqa: E402
from module2_logic_representation import module1_to_module2  # noqa: E402
from module3_puzzle_solving import module2_to_module3  # noqa: E402
from module4_solution_verification import verification_dict_to_text, verify_to_dict  # noqa: E402
from module5_complexity_analysis import module1_2_3_4_to_module5  # noqa: E402
from module6_solution_explanation import module1_2_3_5_to_module6  # noqa: E402


def _safe_json(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)


def _render_verification(report: Dict[str, Any]) -> None:
    overall = bool(report.get("overall_pass"))
    st.subheader("Verification (Module 4)")
    st.write(f"Overall result: **{'PASS' if overall else 'FAIL'}**")

    errors = report.get("errors") or []
    if errors:
        st.error("Errors:\n" + "\n".join(f"- {e}" for e in errors))

    entailment = report.get("entailment", {})
    st.write(
        f"Entailment: **{'PASS' if entailment.get('pass') else 'FAIL'}** — {entailment.get('details')}"
    )

    hidden = report.get("hidden_solution_match", {})
    st.write(f"Hidden solution match: **{'MATCH' if hidden.get('pass') else 'MISMATCH'}**")

    violations = report.get("violation_summary", [])
    if violations:
        st.warning(f"Violations: **{len(violations)}**")
    else:
        st.success("Violations: **0**")

    with st.expander("Per-constraint results"):
        rows = []
        for r in report.get("constraint_results", []):
            rows.append(
                {
                    "index": r.get("index"),
                    "type": r.get("type"),
                    "attribute": r.get("attribute"),
                    "pass": r.get("pass"),
                    "details": r.get("details"),
                }
            )
        st.dataframe(rows, use_container_width=True)

    with st.expander("Raw Module 4 JSON"):
        st.code(_safe_json(report), language="json")


st.set_page_config(page_title="Logic Puzzle Generator", layout="wide")
st.title("Logic Puzzle Generation and Analysis System")
st.caption(
    "Generate → Represent (KB) → Solve → Verify → Complexity analysis → Solution explanation"
)

with st.sidebar:
    st.header("Inputs")
    grid_size = st.slider("Grid size", min_value=3, max_value=6, value=4, step=1)
    difficulty = st.selectbox("Difficulty", ["easy", "medium", "hard"], index=1)
    use_real_names = st.checkbox("Use real names", value=False)
    run = st.button("Run pipeline", type="primary")

if not run:
    st.info("Set inputs in the sidebar, then click **Run pipeline**.")
    st.stop()

col1, col2 = st.columns(2, gap="large")

with st.spinner("Generating puzzle (Module 1)…"):
    puzzle = generate_puzzle(grid_size=grid_size, difficulty=difficulty, use_real_names=use_real_names)
    puzzle_dict = puzzle.to_dict()

with col1:
    st.subheader("Puzzle (Module 1 JSON)")
    stats = puzzle_dict.get("generation_stats")
    if stats:
        st.write(
            f"Generation stats: attempts={stats.get('attempts')}, "
            f"regenerations={stats.get('regenerations')}, "
            f"time={stats.get('generation_time_seconds')}s"
        )
    st.code(_safe_json(puzzle_dict), language="json")
    st.download_button(
        "Download puzzle JSON",
        data=_safe_json(puzzle_dict),
        file_name="puzzle.json",
        mime="application/json",
    )

with st.spinner("Creating knowledge base (Module 2)…"):
    kb_text = module1_to_module2(puzzle_dict)

with col2:
    st.subheader("Knowledge Base (Module 2)")
    st.code(kb_text, language="text")
    st.download_button(
        "Download KB text",
        data=kb_text,
        file_name="knowledge_base.txt",
        mime="text/plain",
    )

with st.spinner("Solving (Module 3)…"):
    module3_output = module2_to_module3(kb_text)

st.subheader("Solution + Proof (Module 3)")
st.code(module3_output, language="text")
st.download_button(
    "Download Module 3 output",
    data=module3_output,
    file_name="module3_output.txt",
    mime="text/plain",
)

with st.spinner("Verifying (Module 4)…"):
    report = verify_to_dict(
        solution_text=module3_output,
        constraints_data=puzzle_dict["constraints"],
        knowledge_base=kb_text,
        hidden_solution=puzzle_dict["solution"],
    )

_render_verification(report)

module4_text = verification_dict_to_text(report)

with st.spinner("Complexity analysis (Module 5)…"):
    module5_output = module1_2_3_4_to_module5(
        puzzle_dict,
        kb_text,
        module3_output,
        module4_text,
    )

st.subheader("Complexity report (Module 5)")
st.code(module5_output, language="text")
st.download_button(
    "Download Module 5 report",
    data=module5_output,
    file_name="module5_complexity.txt",
    mime="text/plain",
)

with st.spinner("Solution explanation (Module 6)…"):
    module6_output = module1_2_3_5_to_module6(
        puzzle_dict,
        kb_text,
        module3_output,
        module5_output,
    )

st.subheader("Solution explanation (Module 6)")
st.code(module6_output, language="text")
st.download_button(
    "Download Module 6 explanation",
    data=module6_output,
    file_name="module6_explanation.txt",
    mime="text/plain",
)

