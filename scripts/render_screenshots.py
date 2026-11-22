"""Render the terminal output of scripts/report_tables.py for Tables 1 to 3 as PNG screenshots.

Usage:
    .venv/bin/python scripts/render_screenshots.py      # writes docs/screenshots/table{1,2,3}.png
"""

import subprocess
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def render(text, path, title):
    lines = [f"$ python scripts/report_tables.py {title}"] + text.rstrip().splitlines()
    width = max(len(line) for line in lines)
    fig = plt.figure(figsize=(0.075 * width + 0.4, 0.19 * len(lines) + 0.3))
    fig.patch.set_facecolor("#1e1e1e")
    for i, line in enumerate(lines):
        fig.text(0.01, 1 - (i + 0.8) / (len(lines) + 0.5), line, family="DejaVu Sans Mono",
                 fontsize=9, color="#9cdcfe" if i == 0 else "#e6e6e6", va="top")
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=110, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"wrote {path.relative_to(ROOT)}")


def main():
    for t in ("1", "2", "3"):
        out = subprocess.run([sys.executable, str(ROOT / "scripts" / "report_tables.py"), t],
                             capture_output=True, text=True, check=True, cwd=ROOT).stdout
        render(out, ROOT / "docs" / "screenshots" / f"table{t}.png", t)


if __name__ == "__main__":
    main()
