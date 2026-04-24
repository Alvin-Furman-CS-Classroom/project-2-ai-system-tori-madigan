from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "paper_artifacts"


def get_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    names = ["arialbd.ttf", "DejaVuSans-Bold.ttf"] if bold else ["arial.ttf", "DejaVuSans.ttf"]
    for name in names:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_multiline(draw: ImageDraw.ImageDraw, text: str, x: int, y: int, font, fill=(0, 0, 0), spacing=6):
    draw.multiline_text((x, y), text, font=font, fill=fill, spacing=spacing)


def figure1_pipeline(path: Path):
    img = Image.new("RGB", (2200, 900), "white")
    d = ImageDraw.Draw(img)
    title_font = get_font(46, bold=True)
    box_font = get_font(24, bold=True)
    sub_font = get_font(20)
    d.text((60, 30), "Figure 1: Six-Module Pipeline and Data Flow", font=title_font, fill="black")

    modules = [
        ("M1 Generator", "Puzzle JSON"),
        ("M2 Logic KB", "KB Text"),
        ("M3 Solver + Proof", "Solution/Proof Text"),
        ("M4 Verifier", "Verification Report"),
        ("M5 Complexity", "Difficulty Metrics"),
        ("M6 Explanation", "Readable Explanation"),
    ]
    start_x, y = 70, 280
    box_w, box_h, gap = 300, 220, 45
    for i, (name, out_fmt) in enumerate(modules):
        x = start_x + i * (box_w + gap)
        d.rounded_rectangle((x, y, x + box_w, y + box_h), radius=16, outline=(30, 70, 150), width=4, fill=(236, 243, 255))
        d.text((x + 18, y + 25), name, font=box_font, fill=(20, 40, 90))
        d.text((x + 18, y + 88), "Output:", font=sub_font, fill="black")
        d.text((x + 18, y + 122), out_fmt, font=sub_font, fill="black")
        if i < len(modules) - 1:
            ax = x + box_w + 10
            ay = y + box_h // 2
            bx = x + box_w + gap - 8
            by = ay
            d.line((ax, ay, bx, by), fill=(0, 0, 0), width=4)
            d.polygon([(bx, by), (bx - 18, by - 12), (bx - 18, by + 12)], fill=(0, 0, 0))

    draw_multiline(
        d,
        "Streamlit UI consumes module outputs for gameplay.\n"
        "Core logic remains in src/ modules for modular testing.",
        70,
        610,
        get_font(26),
        fill=(40, 40, 40),
    )
    img.save(path)


def draw_table(path: Path, title: str, headers: list[str], rows: list[list[str]], col_widths: list[int]):
    row_h = 80
    width = sum(col_widths) + 80
    height = 180 + row_h * (len(rows) + 1) + 40
    img = Image.new("RGB", (width, height), "white")
    d = ImageDraw.Draw(img)
    d.text((40, 30), title, font=get_font(42, bold=True), fill="black")
    x0, y0 = 40, 120

    d.rectangle((x0, y0, x0 + sum(col_widths), y0 + row_h), fill=(225, 235, 252), outline="black", width=2)
    x = x0
    for i, h in enumerate(headers):
        d.line((x, y0, x, y0 + row_h + row_h * len(rows)), fill="black", width=2)
        d.text((x + 12, y0 + 20), h, font=get_font(22, bold=True), fill="black")
        x += col_widths[i]
    d.line((x0 + sum(col_widths), y0, x0 + sum(col_widths), y0 + row_h + row_h * len(rows)), fill="black", width=2)

    for r, row in enumerate(rows):
        y = y0 + row_h * (r + 1)
        d.rectangle((x0, y, x0 + sum(col_widths), y + row_h), fill="white", outline="black", width=2)
        x = x0
        for c, cell in enumerate(row):
            d.text((x + 12, y + 16), cell, font=get_font(21), fill="black")
            x += col_widths[c]

    img.save(path)


def figure2_ui_mock(path: Path):
    img = Image.new("RGB", (1900, 1100), "white")
    d = ImageDraw.Draw(img)
    d.text((40, 25), "Figure 2: Real Puzzle Instance Artifact (Module 1 -> Module 2)", font=get_font(42, bold=True), fill="black")

    puzzle_path = ROOT / "module1_puzzle.json"
    kb_path = ROOT / "module2_kb.txt"
    puzzle_text = "{}"
    kb_text = ""
    if puzzle_path.exists():
        puzzle_obj = json.loads(puzzle_path.read_text(encoding="utf-8"))
        puzzle_text = json.dumps(puzzle_obj, indent=2)
    if kb_path.exists():
        kb_text = kb_path.read_text(encoding="utf-8")

    puzzle_lines = puzzle_text.splitlines()[:24]
    kb_lines = kb_text.splitlines()[:24]

    d.rounded_rectangle((40, 100, 930, 1040), radius=16, outline=(140, 140, 140), width=3, fill=(248, 250, 255))
    d.text((70, 130), "Left: module1_puzzle.json (actual file snippet)", font=get_font(28, bold=True), fill=(20, 20, 20))
    y = 190
    for line in puzzle_lines:
        d.text((70, y), line[:82], font=get_font(19), fill=(30, 30, 30))
        y += 33

    d.rounded_rectangle((970, 100, 1860, 1040), radius=16, outline=(140, 140, 140), width=3, fill=(253, 253, 253))
    d.text((1000, 130), "Right: module2_kb.txt (actual file snippet)", font=get_font(28, bold=True), fill=(20, 20, 20))
    y = 190
    for line in kb_lines:
        d.text((1000, y), line[:82], font=get_font(19), fill=(30, 30, 30))
        y += 33

    d.text((40, 1060), "This artifact shows a real generated puzzle and its propositional KB translation from the project files.", font=get_font(20), fill=(50, 50, 50))
    img.save(path)


def figure3_analysis(path: Path):
    img = Image.new("RGB", (1900, 1100), "white")
    d = ImageDraw.Draw(img)
    d.text((40, 25), "Figure 3: Real Module Output Artifact", font=get_font(42, bold=True), fill="black")

    d.rounded_rectangle((40, 110, 900, 1040), radius=14, outline=(120, 120, 120), width=3, fill=(250, 250, 255))
    d.text((70, 145), "Module 5 Report (from module5_report.txt)", font=get_font(30, bold=True), fill="black")
    metrics = [
        ("Overall status", "PASS"),
        ("Difficulty score", "66.0"),
        ("Difficulty label", "medium"),
        ("Constraint count", "9"),
        ("Search space size", "19683"),
        ("Inference step count", "9"),
        ("Constraint density", "1.0"),
        ("Solution uniqueness", "unique"),
    ]
    y = 220
    for k, v in metrics:
        d.text((80, y), f"{k}:", font=get_font(24, bold=True), fill=(20, 20, 20))
        d.text((420, y), v, font=get_font(24), fill=(30, 30, 30))
        y += 86

    d.rounded_rectangle((960, 110, 1840, 1040), radius=14, outline=(120, 120, 120), width=3, fill=(255, 252, 248))
    d.text((990, 145), "Module 3 Proof Snippet (module3_output.txt)", font=get_font(30, bold=True), fill="black")
    explanation = [
        "=== SOLUTION ===",
        "E1: A1=V3, A2=V3, A3=V3",
        "E2: A1=V2, A2=V2, A3=V1",
        "E3: A1=V1, A2=V1, A3=V2",
        "",
        "INFERENCE STEP COUNT: 9",
        "=== PROOF ===",
        "1. [deduction] E1 A1 must be V3",
        "2. [deduction] E1 A2 must be V3",
        "3. [deduction] E1 A3 must be V3",
    ]
    y = 230
    for line in explanation:
        d.text((995, y), line, font=get_font(23), fill=(35, 35, 35))
        y += 58
    img.save(path)


def main():
    OUT_DIR.mkdir(exist_ok=True)

    figure1_pipeline(OUT_DIR / "figure1_pipeline.png")
    figure2_ui_mock(OUT_DIR / "figure2_ui_mock.png")
    figure3_analysis(OUT_DIR / "figure3_analysis_artifact.png")

    draw_table(
        OUT_DIR / "table1_evaluation_mapping.png",
        "Table 1: Evaluation Dimensions and Evidence",
        ["Objective", "Artifact/Metric", "Evidence Source"],
        [
            ["Correctness", "126 passed, 0 failed", "whole_system_system_report.md"],
            ["Coverage", "8 unit + 5 integration files", "unit_tests/ and integration_tests/"],
            ["Uniqueness", "Bounded solution counting", "Module 1 + Module 3 implementation"],
            ["Difficulty quality", "9 metrics + label", "module5_report.txt"],
            ["User behavior", "Hint/check/reveal workflow", "streamlit_app.py UI behavior"],
        ],
        [420, 470, 520],
    )

    draw_table(
        OUT_DIR / "table2_module_outcomes.png",
        "Table 2: Module-Level Outcomes and Evidence",
        ["Module", "Primary Output", "Evidence"],
        [
            ["Module 1", "Puzzle JSON", "module1_puzzle.json"],
            ["Module 2", "KB text formulas", "module2_kb.txt"],
            ["Module 3", "Solution + proof trace", "module3_output.txt"],
            ["Module 4", "Verification status", "Integrated in full-system tests"],
            ["Module 5", "Difficulty metrics", "module5_report.txt"],
            ["Module 6", "Readable explanation", "test_module1_to_module6.py"],
        ],
        [280, 580, 550],
    )

    print(f"Created artifacts in: {OUT_DIR}")


if __name__ == "__main__":
    main()
