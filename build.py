"""Build dental-notes.html from the templates in src/.

Run:  python build.py
Each template in src/ is a complete standalone page. The shell (src/shell.html)
holds the tab bar and the Your details tab, and embeds each template in an iframe.

If a private editor/overlay.json is present (it is gitignored and never
published), this also writes dental-notes-editor.html with the overlay's extra
code inserted. The public dental-notes.html never includes it.
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"
OVERLAY = ROOT / "editor" / "overlay.json"
TEMPLATES = {
    "filling": "filling-note.html",
    "extraction": "extraction-note.html",
    "prep": "indirect-prep-note.html",
    "fit": "indirect-fit-note.html",
    "endo": "endo-note.html",
    "denture": "denture-note.html",
}


def build(out_name, inserts=()):
    def read(name):
        text = (SRC / name).read_text(encoding="utf-8")
        for ins in inserts:
            if ins["file"] == name:
                if text.count(ins["before"]) != 1:
                    raise SystemExit(f"overlay anchor not found once in {name}: {ins['before'][:60]!r}")
                text = text.replace(ins["before"], ins["text"] + ins["before"])
        return text

    shell = read("shell.html")
    for key, name in TEMPLATES.items():
        shell = shell.replace("{{" + key + "}}", html.escape(read(name), quote=True))
    out = ROOT / out_name
    out.write_text(shell, encoding="utf-8")
    print(f"Built {out.name} ({out.stat().st_size // 1024} KB)")
    return shell


public = build("dental-notes.html")
if OVERLAY.exists():
    inserts = json.loads(OVERLAY.read_text(encoding="utf-8"))["inserts"]
    for ins in inserts:
        assert html.escape(ins["text"], quote=True) not in public and ins["text"] not in public, "private code found in the public build"
    build("dental-notes-editor.html", inserts)
