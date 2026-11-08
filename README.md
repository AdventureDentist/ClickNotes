# Treatment notes (beta)

Tap-to-build clinical note templates for general dentistry: filling, extraction,
indirect prep, indirect fit and endodontic treatment. Pick options, then copy a
formatted note into the practice management system.

## Using it

Open `dental-notes.html` in Chrome or Edge. It works offline, needs no login and
saves nothing about patients: closing the page clears every note. The **Your
details** tab stores the dentist and dental assistant names in that browser only.

## Editing

The templates live in `src/`, one standalone HTML page each. After changing any of
them, rebuild the combined file:

    python build.py

Each page can also be opened on its own for testing.
