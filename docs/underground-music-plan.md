# Underground Music in America: Project Plan

*Last updated: October 24, 2026*

This file is the shared to-do list and memory for the course archive. It lives
in the repository but is not part of the website (see `exclude` in
`_config.yml`). Micah can read and edit it on GitHub. Claude should read it at
the start of any session about the microsite.

Companion files in the same folder:

- `underground-music-topics.md`: the master list of every lesson, theme and
  topic taught, with readings, films and where the notes cover each
- `underground-music-listening.md`: the 78-song listening list, cleaned up

## The goal

An archive of the undergraduate course "Underground Music in America: 1980 to
Present," which Micah taught at Florida State University (AMS 3810) over
several semesters. It is for Micah's own archival purposes, not part of his
professional profile. It lives at `micahvandegrift.github.io/underground-music/`,
shares the main site's look and dark mode, and is not in the main menu.

Principles:

- **Keep all the content.** Nothing valuable gets thrown away because it only
  appeared in one version of the course.
- **One combined list of topics, no semesters.** The course changed each time
  it ran. The archive doesn't track which semester said what; it lists
  everything that was taught, by topic or theme.
- **Link out, don't host.** Songs and videos link to YouTube. Readings link to
  the book or article. Recordings need a home outside GitHub (see decisions).
- **Micah's voice.** Notes are edited for readability, not rewritten.

## Where things stand

Done and live (pull request 22 merged October 24, 2026):

- [x] Course layout (`_layouts/class.html`) with its own small menu and the
      main site's dark-mode toggle
- [x] Course home page: description, objectives, texts, films, themes, bands,
      promo flyer, and an automatic list of pages
- [x] A prototype page converted from the notes, with gray "old link" tags
      where 2009 web addresses stood
- [x] A saved converter for the notes (`tools/convert-notes.py`)
- [x] All the syllabi read and merged into one topic list (16 topics)
- [x] The listening list found, cleaned up and merged with the 1994-2001 list

**October 28, 2026:** the Texts and Films pages are live (pull requests 26 and
27). A Listening List page (78 songs, a YouTube link each) is built; about 26
of its links are marked CHECK or WEAK in
`docs/underground-music-listening-links.md` and still need Micah's listen.
Micah also renamed "topics" to **lessons** everywhere on the site; the files
keep the names `topic-01.md` to `topic-16.md`.

**October 27, 2026:** all 16 topics are written as stand-alone text, live at
`underground-music/topic-01.md` to `topic-16.md` (pull request 25, merged and
deployed). The text was
edited from the lecture notes, run through a research agent (web sources only,
no books), and finished on this basis, decided by Micah: **he accepts the risk
that quotations and citations from his lecture notes are unverified.** Where
the agent could only say "not confirmed," the text keeps his notes' wording;
where the agent found evidence that a note was wrong, the text uses the
corrected fact. The agent's work and the list of unsettled items are in
`docs/underground-music-text/audit/`.

## What Micah has, and what's still to come

The original files live on Micah's computer. **Files shared in a Claude session
do not carry over to the next one. Bring them again when we resume.** Don't
commit the original Word files or syllabi to GitHub: the repository is public,
and the Spring 2009 syllabus contains an old FSU email and a campus phone
number.

| Material | Status |
|---|---|
| Syllabi (four; that is all Micah has) | Done. Merged into the topic list |
| Lecture notes (one Word file, about 26,000 words, one long outline) | Received again October 24, 2026. Topic 1 edited. **Needed again** in a new session to do the rest |
| Book list, Fall 2008 | Used on the home page |
| Listening list "1994-2001" and the found list (78 songs together) | Merged in the listening file. No links yet |
| Promo flyer | On the site |
| Two newspaper clippings (FSView, April 6, 2009, "Pop culture in the classroom") | Received, **not used** (see decisions) |
| Lecture recordings | **Not yet sent**; hosting undecided |

## The topics

The master list is in `underground-music-topics.md`. In short:

1. Introduction, roots and historical context
2. No Wave and Sonic Youth
3. Hardcore
4. Scenes and labels
5. Politics and communication
6. DIY, indie and the business of music
7. Metal
8. The transition to the 1990s
9. Emo
10. New scenes, labels, clubs and sounds
11. Gender in the underground
12. Religion in the underground
13. New Weird America and the folk re-revival
14. Visual art and authenticity
15. Is "underground" still possible?
16. Florida's underground music scenes

This is a working list. When we edit the notes we may merge or split topics
(for example, folding 15 and 16 into others, or giving a long topic two
pages).

## Decisions we still need to make

Each has my recommendation. Micah decides.

1. **Page template for a topic. DECIDED (October 27, 2026).** In this
   order: a short overview in Micah's voice; listen and watch; readings;
   discussion questions (the notes have some); class sessions; key ideas;
   who's who (bands, dates); a summary of the era where the topic needs one;
   films. `topic-01.md` is the model for the other pages. The original
   lecture notes are **not** published on the site: the edited page replaces
   them. (The unedited Week 1 notes were live from October 24 to 27, 2026 and
   remain in the repository's history.)
2. **Old links (about 190).** Since the original notes are no longer shown,
   the old links no longer appear on the site. They still matter where a
   song, clip or article is worth linking from a topic's Listen and watch
   list. For those, Claude produces one table with each link, the sentence it
   sat in, and whether it still works or has a Wayback Machine copy. Micah
   marks the table. See "Link checking" below.
3. **Copyrighted text pasted into the notes.** The notes include full lyrics
   (for example Bad Brains, "Pay to Cum"), a full allmusic review of "Teenage
   Riot," and a long bio blurb. Since the notes aren't published, this only
   matters if an edited page would quote them. Rule: use a short quote,
   credit and a link, never the full text.
4. **Recordings.** Recommended: upload to YouTube as unlisted, or Archive.org,
   and embed. Think first about whether student voices are in them, and
   whether Micah is comfortable publishing that.
5. **Visibility.** The microsite isn't linked from the main site. Options:
   keep it that way; link it from the homepage or Projects page; add a
   "please don't index" tag so search engines skip it. Recommended: decide
   at launch.
6. **Newspaper clippings.** The paper owns the article. Options: image on the
   site, link to the paper's own archive if one exists, or leave it in
   Micah's files.
7. **Flyer photo credit.** Who took the stage-dive photo?
8. **Book links.** Bookshop.org, WorldCat, or Open Library. Currently the
   texts show ISBNs only.
9. **The listening list.** Review the "likely topic" guesses and the open
   questions at the bottom of `underground-music-listening.md`.

## The plan

Each step is one small pull request, in this order. Micah reviews screenshots
(desktop, phone, dark mode) before each one.

### Phase 0: Housekeeping
- [x] Pull request for the home page and Week 1 prototype, merged

### Phase 1: Gather (done)
- [x] Syllabi read and merged into one topic list
- [x] Listening list found and cleaned up

### Phase 2: Pilot one topic together (done)
- [x] Topic 1 edited and published; it set the template and the editing rules
      (decision 1)
- [x] `week-01.md` renamed to `topic-01.md`; the course home page lists topics
      instead of weeks
- [x] Original notes are not published (Micah's decision, October 27, 2026),
      so no toggle

### Phase 2b: Edit the text first (done October 27, 2026)

Micah wanted every page to stand alone, with no references to "the notes" or
the syllabus. The notes were edited into prose, flagged for fact-checking,
checked by a research agent, and finished (see "Where things stand").

- [x] All 16 topics edited (`docs/underground-music-text/all-topics.md` is the
      version that went to the agent; the agent's prompt is `agent-prompt.md`).
- [x] Research pass done; the agent's files are in `docs/underground-music-text/audit/`.
- [x] Spot-check of 20 of the agent's corrections: 14 fully right, 5 right in
      substance with a flawed detail (fixed), 1 wrong (fixed).
- [x] Micah's decision to accept the risk on unverified quotes and citations.
- [x] Final text poured into the site pages `topic-01.md` to `topic-16.md`.
- [x] Pull request 25 merged and deployed (October 27, 2026).

Remaining content gaps, found while editing: Topic 15 is thin; Topic 14 has
nothing on Raymond Pettibon or Scott Sinclair; Topic 7 does not cover black
metal; Topic 16 has no symposium or readings; the "Listen and watch" lists
have no links yet (Phase 4).

### Phase 3: Topic pages (done, replaced by Phase 2b)

All 16 topics were written in one round (Phase 2b) instead of one at a time.
Left over from this phase:
- [ ] Add links to each topic's "Listen and watch" lists (follows the Listening
      List in Phase 4; Micah confirms each link)
- [ ] Fill the content gaps listed under Phase 2b (Micah's call)

### Phase 4: Course-level pages
- [x] A Texts and readings page with links (decision 8)
- [x] A Films page
- [x] A full Listening List page: all songs with a YouTube link for each
      (built October 28; Micah still confirms the CHECK/WEAK links)

### Phase 5: Recordings
- [ ] Choose where they live (decision 4)
- [ ] Add a Recording section to the topics they belong to

### Phase 6: Launch
- [ ] Final privacy sweep: no phone numbers, no email except
      `micahvandegrift (at) gmail.com`, no student names
- [ ] Decide visibility (decision 5) and add any link from the main site
- [ ] Proofread the home page and every topic page
- [ ] Merge, then confirm the "pages build and deployment" action succeeds

## Start here when Micah is back at the laptop

1. Open a new Claude session on this repository and ask Claude to read this
   file.
2. Re-attach the lecture notes (`AMS3810-REAL.doc`). Everything else is
   already summarized in the three files in `docs/`.
3. Answer decision 1 (page template) and skim the topic list and the listening
   list for corrections.
4. Begin Phase 2: edit topic 1 together.

Optional, any time: decisions 6 to 8 (clippings, photo credit, book links),
and the open questions in the listening file.

## Ground rules for editing the notes

- Keep Micah's voice. Don't add facts that aren't in the notes or syllabi.
- Fix obvious typos (for example "Phillip Glass," "Detriot"), and keep a list
  of anything that looks like a factual doubt (dates, names, quotes) for Micah
  to confirm.
- Quotes stay word for word, with their source.
- Claude can't check facts online reliably from the cloud environment.
  Micah's sources win.
- Never turn an old link into a real link without Micah's say-so.

## Facts to confirm with Micah

Superseded. The research pass settled many of the earlier flags and Micah
accepted the risk on the rest. The items still unsettled are listed in
`docs/underground-music-text/audit/unresolved-items.md`, for anyone who later
wants to check them against the books.

## Link checking

The cloud environment Claude runs in blocks many websites (it couldn't reach
Open Library, for example), so checking 190 links there may not work. If that's
the case, do it in a session running on Micah's own computer, or Micah checks
the table by hand.

## How the pieces work

- `underground-music/index.md` is the course home. Pages named `topic-XX.md`
  in that folder are listed on it automatically.
- `_layouts/class.html` is the course layout. `_config.yml` applies it to
  everything in the folder and sets the `course` styling class.
- `stylesheets/site.css` has a "Course microsite" section at the bottom for
  the course-only styles, including the gray `old-link` tags.
- `tools/convert-notes.py` turns a slice of the converted notes into a first
  draft. It's a helper and isn't published.
- To preview the site locally: install the `github-pages` gem, build, and
  open the result. Claude does this before every pull request.
