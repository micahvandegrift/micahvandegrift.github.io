# Notes for Claude

This is Micah Vandegrift's personal website, published with GitHub Pages at
https://micahvandegrift.github.io from the `master` branch.

Micah is not a coder. Explain changes in plain language, avoid jargon (or
define it), and keep each change small and easy to review.

## How the site is built

- `index.html` is the homepage. It is plain HTML with no Jekyll front matter,
  so GitHub Pages serves it as-is.
- `CV.md`, `Resume.md` and `Projects.md` are Markdown pages. GitHub Pages
  (Jekyll) turns them into `/CV`, `/Resume` and `/Projects` using
  `_layouts/default.html`.
- `_config.yml` sets each Markdown page's title, and `body_class` for
  page-specific styling (the Projects page uses `projects`).
- `stylesheets/site.css` holds all styling for every page, including dark mode
  colors. `javascripts/theme.js` is the dark-mode toggle.
- The menu (Home, CV, Resume, Projects) appears in both `index.html` and
  `_layouts/default.html`. Update both when adding a page.
- `underground-music/` is a microsite archiving Micah's grad-school course
  "Underground Music in America: 1980 - Present". It uses its own layout,
  `_layouts/class.html` (menu: Course home, Micah's site), selected for the
  whole folder in `_config.yml`. The course units are called
  "lessons" on the site (Micah's choice, October 28, 2026), though the files
  keep the old name, `topic-XX.md`, so saved links don't break. Each lesson
  file has a `title` and `summary` at the top, and the course home page lists
  them automatically. It is an archive, so it is not in the main menu.
  Micah's original lecture notes are not published; each lesson page is an
  edited, stand-alone version of them, written as plain prose in Micah's lecture
  voice, so it should never say "the notes." Micah line-edits these Markdown
  files directly on GitHub. Their quotations and citations come from his notes
  and were not independently verified (his decision, October 27, 2026); the
  research pass and the list of unsettled items are in
  `docs/underground-music-text/audit/`. Web addresses from the original 2009 notes are
  unverified, so don't turn them into links without asking (the `old-link`
  style in `site.css` shows one as a gray, non-clickable tag).
  The project plan, open decisions and task list are in
  `docs/underground-music-plan.md`; read it first. Its companions in `docs/`
  list every lesson taught and the cleaned-up listening list. The site is organized by
  lesson or theme, not by week. Say "lesson," not "topic," in anything published. `tools/convert-notes.py` is a
  helper for converting notes (neither folder is published).
- `images/headshot-square.jpg` is a face-centered crop of `Headshot.jpg`.
- `stylesheets/stylesheet.css`, `github-dark.css`, `print.css`,
  `javascripts/main.js` and `params.json` are leftovers from an old theme and
  are not used.

## Content Micah edits directly on GitHub

- `CV.md`: the full academic/professional CV. Lines like `Title | 2020` are
  read by Jekyll as one-row tables; `site.css` styles them as plain lines, so
  don't rewrite them.
- `Resume.md`: currently a placeholder. Micah plans to write the new resume
  here in Markdown. Do not add resume PDFs back.
- `Projects.md`: one `## Title` block per project, newest first.

## Privacy rules

- Never put a phone number anywhere on the site. Check any new resume or CV
  text for one before it goes live.
- Write the email as `micahvandegrift (at) gmail.com`, plain text, never a
  `mailto:` link or the full address.
- Old resume PDFs (some with a phone number) still exist in git history.
  Micah chose not to rewrite history. Don't do it without asking.

## How we work

- One small change per pull request. Say when it is ready to merge; don't keep
  pushing to a PR after it has been merged (start a fresh branch from `master`
  instead).
- Before opening a PR, build the site locally with the `github-pages` gem and
  send Micah screenshots (desktop, phone, and dark mode when relevant).
- Micah may ask Claude to merge. Merge only when asked, then confirm the
  "pages build and deployment" GitHub Action succeeds.
- Write PR descriptions in plain English: what changed and why.
