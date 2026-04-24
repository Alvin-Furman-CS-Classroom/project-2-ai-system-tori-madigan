from pathlib import Path
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
    d.text((40, 25), "Figure 2: Streamlit Gameplay Screen (Representative)", font=get_font(42, bold=True), fill="black")

    d.rounded_rectangle((40, 100, 1200, 1040), radius=16, outline=(140, 140, 140), width=3, fill=(248, 250, 255))
    d.text((70, 130), "Logic Grid Workspace", font=get_font(30, bold=True), fill=(20, 20, 20))

    gx, gy = 70, 190
    cw, ch = 170, 85
    for r in range(0, 7):
        d.line((gx, gy + r * ch, gx + 6 * cw, gy + r * ch), fill=(120, 120, 120), width=2)
    for c in range(0, 7):
        d.line((gx + c * cw, gy, gx + c * cw, gy + 6 * ch), fill=(120, 120, 120), width=2)
    d.text((gx + 20, gy + 18), "Person", font=get_font(20, bold=True), fill="black")
    d.text((gx + 190, gy + 18), "Pet", font=get_font(20, bold=True), fill="black")
    d.text((gx + 360, gy + 18), "Movie", font=get_font(20, bold=True), fill="black")
    d.text((gx + 530, gy + 18), "Hobby", font=get_font(20, bold=True), fill="black")
    d.text((gx + 20, gy + 102), "Ava", font=get_font(20), fill="black")
    d.text((gx + 20, gy + 187), "Ben", font=get_font(20), fill="black")
    d.text((gx + 20, gy + 272), "Cara", font=get_font(20), fill="black")
    d.text((gx + 210, gy + 102), "O", font=get_font(26, bold=True), fill=(0, 120, 0))
    d.text((gx + 380, gy + 102), "X", font=get_font(26, bold=True), fill=(180, 0, 0))
    d.text((gx + 550, gy + 187), "O", font=get_font(26, bold=True), fill=(0, 120, 0))

    d.rounded_rectangle((1240, 100, 1840, 720), radius=16, outline=(140, 140, 140), width=3, fill=(253, 253, 253))
    d.text((1270, 130), "Clues", font=get_font(30, bold=True), fill="black")
    clues = [
        "1. The person with the black hair enjoys reading.",
        "2. Ben is not the one who likes gardening.",
        "3. Either Ava watches mystery movies or",
        "   she has the dog.",
        "4. The person with the cat also prefers action.",
    ]
    y = 190
    for line in clues:
        d.text((1270, y), line, font=get_font(22), fill=(30, 30, 30))
        y += 58

    d.rounded_rectangle((1240, 760, 1840, 1040), radius=16, outline=(140, 140, 140), width=3, fill=(245, 252, 245))
    d.text((1270, 795), "Progress", font=get_font(30, bold=True), fill="black")
    d.text((1270, 855), "Correct guesses: 5", font=get_font(24), fill=(20, 90, 20))
    d.text((1270, 905), "Remaining unknowns: 4", font=get_font(24), fill=(40, 40, 40))
    d.text((1270, 955), "Status: In progress", font=get_font(24), fill=(40, 40, 40))
    img.save(path)


def figure3_analysis(path: Path):
    img = Image.new("RGB", (1900, 1100), "white")
    d = ImageDraw.Draw(img)
    d.text((40, 25), "Figure 3: Complexity + Explanation Artifact (Representative)", font=get_font(42, bold=True), fill="black")

    d.rounded_rectangle((40, 110, 900, 1040), radius=14, outline=(120, 120, 120), width=3, fill=(250, 250, 255))
    d.text((70, 145), "Module 5 Difficulty Report", font=get_font(30, bold=True), fill="black")
    metrics = [
        ("Constraint count", "18"),
        ("Search space size", "729"),
        ("Inference step count", "42"),
        ("Constraint density", "0.67"),
        ("Formula complexity", "Medium"),
        ("Branching factor", "2.1"),
        ("Solution uniqueness", "Unique"),
        ("Overall difficulty", "Medium"),
    ]
    y = 220
    for k, v in metrics:
        d.text((80, y), f"{k}:", font=get_font(24, bold=True), fill=(20, 20, 20))
        d.text((420, y), v, font=get_font(24), fill=(30, 30, 30))
        y += 86

    d.rounded_rectangle((960, 110, 1840, 1040), radius=14, outline=(120, 120, 120), width=3, fill=(255, 252, 248))
    d.text((990, 145), "Module 6 Reasoning Summary", font=get_font(30, bold=True), fill="black")
    explanation = [
        "Overall strategy:",
        "Use direct clues first, then eliminate with",
        "negative constraints, and resolve final ties",
        "with either/or clues.",
        "",
        "Step highlights:",
        "- Ava cannot have Gardening from clue 2.",
        "- Cat owner is linked to Action movie.",
        "- Remaining value assignments become unique",
        "  after propagation plus one branch choice.",
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
            ["Correctness", "Unit + integration tests", "pytest test suite"],
            ["Uniqueness", "Bounded solution counting", "Module 1 + Module 3 checks"],
            ["Verification", "Per-constraint pass/fail", "Module 4 report"],
            ["Difficulty quality", "Metric completeness/sanity", "Module 5 report"],
            ["User behavior", "Hint/check/reveal loop", "Streamlit interactive test"],
        ],
        [420, 470, 520],
    )

    draw_table(
        OUT_DIR / "table2_module_outcomes.png",
        "Table 2: Module-Level Outcomes and Evidence",
        ["Module", "Primary Output", "Evidence"],
        [
            ["Module 1", "Puzzle JSON + unique solution", "Generator and uniqueness checks"],
            ["Module 2", "KB text formulas", "Deterministic conversion tests"],
            ["Module 3", "Solution + proof trace", "Solver tests and trace checks"],
            ["Module 4", "Verification report", "Constraint + entailment validation"],
            ["Module 5", "Difficulty metrics", "Metric and label checks"],
            ["Module 6", "Readable explanation", "Phase grouping/output tests"],
        ],
        [280, 580, 550],
    )

    print(f"Created artifacts in: {OUT_DIR}")


if __name__ == "__main__":
    main()
