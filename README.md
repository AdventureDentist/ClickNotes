# Treatment Notes

Free, tap-through clinical note templates for dental appointments: restorations,
extractions, indirect preps and fits, endo and dentures. Tap the options that match
what you did, press **Copy note**, and paste a clear, consistently structured note
into your practice management software.

It's a single file that runs in your web browser. There's nothing to install, no
login and no subscription, and nothing about patients is ever saved or sent anywhere.

---

## Set it up (about 3 minutes)

### 1. Download the file

1. Open this link: **[dental-notes.html](https://github.com/AdventureDentist/ClickNotes/blob/main/dental-notes.html)**
2. Near the top right of the page, click the **Download raw file** button (a small
   arrow pointing down into a tray).
3. Your browser saves `dental-notes.html` to your **Downloads** folder.

### 2. Move it somewhere permanent

Move the file out of Downloads to your **Desktop** or **Documents** folder, so it's
easy to find and doesn't get cleared out.

- **Windows:** open File Explorer, go to Downloads, and drag the file onto your Desktop.
- **Mac:** open Finder, go to Downloads, and drag the file onto your Desktop.

### 3. Open it in Chrome or Edge

Double-click the file. It opens in your web browser and works without the internet.

If it opens in a different browser, right-click the file, choose **Open with**, and
pick **Google Chrome** or **Microsoft Edge**.

### 4. Add your details

Click the **⚙ cog** at the top right. Enter your clinician name and your dental
assistants' names (one per line), then press **Save details**. They'll be filled in
automatically every time you open the page on this computer.

### 5. Keep it one click away

- **Bookmark it:** with the page open, press **Ctrl + D** (**⌘ + D** on a Mac).
- **Or pin the tab:** right-click the page's tab and choose **Pin**.

That's it. The ⚙ settings page has more tips, such as opening it automatically when
the browser starts.

---

## Using it

1. Pick a tab at the top: Restoration, Extraction, Indirect prep, Indirect fit, Endo or Dentures.
2. Tap the options that match the appointment. The note builds on the right as you go.
3. Anything still to choose is marked **needed** in amber and listed above the note.
4. Press **Copy note** and paste it into your patient's notes.
5. Press **New note** for the next patient.

Double-click any option or sentence to change its wording for that note.

**Privacy:** the note only exists on your screen. Closing the page or pressing
**New note** clears it. Only your own name and your DAs' names are remembered, by
your browser, on that computer.

## Getting updates

Download the file again (step 1) and save it over your old copy. Your details carry over.

## Changing the options

You can add or change any option, sentence or default with help from an AI assistant:

1. Go to [claude.ai](https://claude.ai) and start a new chat.
2. Attach your `dental-notes.html` file.
3. Describe the change in plain words, for example: *"In the Extraction tab, add
   Coronectomy to the method options, and make Lidocaine 2% the default anaesthetic."*
4. Ask for the complete updated file back, download it, and save it over your old copy.

Keep a copy of the old file until you've checked the new one.

## Support

If it saves you time, a coffee is much appreciated: **[buymeacoffee.com/adventuredentist](https://buymeacoffee.com/adventuredentist)**

---

## For developers

The templates live in `src/`, one standalone HTML page each, with `src/shell.html`
holding the tab bar and settings. After changing any of them, rebuild the combined
file and commit it:

    python build.py

Each page in `src/` can also be opened on its own for testing.
