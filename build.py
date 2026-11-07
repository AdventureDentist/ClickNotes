"""Build dental-notes.html from the templates in src/.

Run:  python build.py
Each template in src/ is a complete standalone page. The shell (src/shell.html)
holds the tab bar and the Your details tab, and embeds each template in an iframe.
"""
import html
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"
TEMPLATES = {
    "filling": "filling-note.html",
    "extraction": "extraction-note.html",
    "prep": "indirect-prep-note.html",
    "fit": "indirect-fit-note.html",
    "endo": "endo-note.html",
}

shell = (SRC / "shell.html").read_text(encoding="utf-8")
for key, name in TEMPLATES.items():
    page = (SRC / name).read_text(encoding="utf-8")
    shell = shell.replace("{{" + key + "}}", html.escape(page, quote=True))
out = ROOT / "dental-notes.html"
out.write_text(shell, encoding="utf-8")
print(f"Built {out.name} ({out.stat().st_size // 1024} KB)")
