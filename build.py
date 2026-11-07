"""Build dental-notes.html (public) and dental-notes-editor.html (private) from src/.

Run:  python build.py
Each template in src/ is a complete standalone page. The shell (src/shell.html)
holds the tab bar and the Your details tab, and embeds each template in an iframe.

Code between EDITOR-ONLY START and EDITOR-ONLY END markers (the "Save to template"
tools and the Changes tab) goes only into dental-notes-editor.html. That file is
for the dentist's own wording edits, is not committed, and is never published.
"""
import html
import re
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
EDITOR_BLOCK = re.compile(
    r"^[ \t]*(?:/\*|<!--) EDITOR-ONLY START.*?EDITOR-ONLY END (?:\*/|-->)\n", re.S | re.M)
MARKER_LINE = re.compile(r"^[ \t]*(?:/\*|<!--) EDITOR-ONLY (?:START|END) (?:\*/|-->)\n", re.M)


def build(editor):
    def prep(text):
        return MARKER_LINE.sub("", text) if editor else EDITOR_BLOCK.sub("", text)

    shell = prep((SRC / "shell.html").read_text(encoding="utf-8"))
    for key, name in TEMPLATES.items():
        page = prep((SRC / name).read_text(encoding="utf-8"))
        shell = shell.replace("{{" + key + "}}", html.escape(page, quote=True))
    if not editor:
        assert "EDITOR-ONLY" not in shell and "DN_WORDING" not in shell, "editor code left in the public build"
    out = ROOT / ("dental-notes-editor.html" if editor else "dental-notes.html")
    out.write_text(shell, encoding="utf-8")
    print(f"Built {out.name} ({out.stat().st_size // 1024} KB)")


build(editor=False)
build(editor=True)
