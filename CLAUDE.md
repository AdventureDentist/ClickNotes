# Project notes for Claude Code

Dental note builder used chairside by a general dentist in Auckland, New Zealand.

## Structure
- `src/*-note.html`: one self-contained template per appointment type (HTML, CSS and JS in one file, no dependencies, works offline from file://).
- `src/shell.html`: tab bar, Your details tab (dentist and DA names in localStorage key `dentalnotes.settings`), and `{{key}}` placeholders where each template is embedded as an iframe srcdoc.
- `build.py`: produces `dental-notes.html` (public) and `dental-notes-editor.html` (private, not committed). Always rebuild after editing anything in `src/`, and commit the public built file.

## Conventions (keep these)
- Section titles in the copied note use `** Title Case **` with spaces inside the asterisks.
- Teeth in FDI notation; tooth picker has a primary-teeth toggle.
- New Zealand English. "DA", never "nurse". No UK-specific references (NHS, UK labs, DBOH, ACORN).
- Nothing is saved about patients: no localStorage, cookies or network calls for note content.
- Lines only appear in the note when something is selected or a fixed sentence is ticked.
- Every option button and fixed sentence can be double-clicked to edit its wording for the current note.
- Editor-only tools: code between `EDITOR-ONLY START` / `EDITOR-ONLY END` markers in `src/` goes only into `dental-notes-editor.html` (gitignored, private, for the dentist's own wording edits). `build.py` strips it from the public `dental-notes.html` and fails if any is left. Keep the public build free of it. Standalone `src/` pages run with the editor code.
- In the editor build, the edit box offers "This note only", "Save to template" or "Cancel". Saved wording (template text only, localStorage key `dentalnotes.wording`) is listed on the Changes tab, which builds a "Copy for Claude" message.
- Applying a pasted change list: each line names the template, option or sentence, the field (last part of the state key, e.g. `prev` maps to the `PREV` list, `riskLine` to `RISK_TEXT`), and the old and new wording. Change that string in the constant in `src/`, rebuild, commit and push. Send the dentist the rebuilt `dental-notes-editor.html` when they want it.
- Option lists sit as constants at the top of each template's script; edit them there.
- Dentist and DA names default to blank and come from the Your details tab.

## Defaults the dentist asked for
- LA: Articaine 4% 1:100,000 first and preselected; 1.8ml cartridges.
- C/O Nil; MH checked No changes.
- Filling: one tooth per restoration with per-tooth surfaces; moisture control cotton wool rolls + HVS; liner not required; Greater Curve standard band with stainless steel and contact opening drilled ticked, ultra thin and wedge unticked; composite brand 3M Filtek (Empress Direct as alternative) plus the flowable base and snowplough protocol line.
- Extraction: multiple teeth with an optional per-tooth split.
- Indirect: multiple teeth with an optional per-tooth restoration and material; occlusal scheme hidden unless ticked; fit protocol as tick boxes.
- Endo: one template covering first visit or continuing treatment, with an interim dressing tick box; ProTaper Next default with per-system final shaping sizes; single cone and AH Plus defaults.
