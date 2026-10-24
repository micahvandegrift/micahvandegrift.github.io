# Underground Music in America: Project Plan

*Last updated: October 24, 2026*

This file is the shared to-do list and memory for the course archive. It lives
in the repository but is not part of the website (see `exclude` in
`_config.yml`). Micah can read and edit it on GitHub. Claude should read it at
the start of any session about the microsite.

## The goal

An archive of the undergraduate course "Underground Music in America: 1980 to
Present," which Micah taught at Florida State University (AMS 3810) for five
semesters. It is for Micah's own archival purposes, not part of his
professional profile. It lives at `micahvandegrift.github.io/underground-music/`,
shares the main site's look and dark mode, and is not in the main menu.

Principles:

- **Keep all the content.** Nothing valuable gets thrown away because it no
  longer fits one syllabus.
- **Organize by topic and theme, not week number.** Micah changed the course
  over five semesters, so weeks don't line up. Each topic page can say which
  semesters covered it.
- **Link out, don't host.** Songs and videos link to YouTube. Readings link to
  the book or article. Recordings need a home outside GitHub (see decisions).
- **Micah's voice.** Notes are edited for readability, not rewritten.

## Where things stand

Done, on the branch `claude/underground-music-scaffold` (pushed, **no pull
request opened yet**, so nothing is live):

- [x] Course layout (`_layouts/class.html`) with its own small menu and the
      main site's dark-mode toggle
- [x] Course home page: description, objectives, texts, films, themes, bands,
      promo flyer, and an automatic list of pages
- [x] `week-01.md`: a prototype page converted from the notes, with gray
      "old link" tags where 2009 web addresses stood
- [x] A saved converter for the notes (`tools/convert-notes.py`)

Week 1 is a prototype. It will become a topic page ("Roots and context")
once we settle the page template below.

## What Micah has, and what's still to come

The original files live on Micah's computer. **Files shared in a Claude session
do not carry over to the next one. Bring them again when we resume.** Don't
commit the original Word files or syllabi to GitHub: the repository is public,
and the Spring 2009 syllabus contains an old FSU email and a campus phone
number.

| Material | Status |
|---|---|
| Spring 2009 syllabus (AMS 3810-01) | Received, used for the home page |
| Syllabi for Spring 2008, Summer 2008, Fall 2008 (and Spring 2009, above) | Received, compared in `underground-music-semesters.md` |
| Syllabus for the fifth semester | **Micah to send** (which semester was it?) |
| Lecture notes (one Word file, about 26,000 words, one long outline running through a whole semester) | Received. Week 1 converted |
| Book list, Fall 2008 | Received |
| Listening list "1994-2001" (31 songs) | Received, not yet on the site. Likely the second half of the course |
| Listening list for the first half | Doesn't exist as a file. Rebuild from the "Play..." cues in the notes |
| Promo flyer | On the site |
| Two newspaper clippings (FSView, April 6, 2009, "Pop culture in the classroom") | Received, **not used** (see decisions) |
| Lecture recordings | **Not yet sent**; hosting undecided |

Size of the notes, by the headings in the file: about 190 old web links,
spread over roughly 11 blocks of about 900 to 3,800 words each.

## Draft topic map

A first guess from the Spring 2009 syllabus and the headings in the notes.
**Expect it to change** once the fifth syllabus arrives. The four syllabi
received so far mostly confirm it; `underground-music-semesters.md` lists the
topic-by-semester matrix and the few extras (Florida scenes, zine culture,
early indie, a guest speaker).

1. Roots and context: American experimental music, proto-punk, the 1980s
   (this is the Week 1 prototype)
2. No Wave and Sonic Youth
3. Hardcore: roots of the genre (and the film *American Hardcore*)
4. DIY: principles, scenes vs. subcultures, identity
5. Scenes and labels: Berkeley, Mordam Records, 924 Gilman, zines
6. Politics in the underground: radical vs. personal
7. Pop culture vs. underground: indie vs. major
8. Metal and the Melvins
9. The transition to the 1990s: lo-fi, early indie, 1994
10. Emo: Sunny Day Real Estate, Jawbreaker, technology and communication
11. New scenes, labels and sounds: Vagrant, Chicago, Saddle Creek
12. Gender in the underground: riot grrrl, queercore
13. Religion in the underground: Krishnacore, Christian hardcore, Pedro the Lion
14. New Weird America and the folk re-revival (and *Danielson: A Family Movie*)
15. Art in the underground: Pettibon, Winston Smith, Art Chantry
16. Is "underground" still possible? Indie and the future

## Decisions we still need to make

Each has my recommendation. Micah decides.

1. **Page template for a topic.** Recommended: a short overview in Micah's
   voice; key ideas; who's who (bands, dates); listen and watch; readings;
   films; discussion questions (the notes have some); "Taught in: Fall 2008,
   Spring 2009..." and, at the bottom, the original notes folded away under
   a "Show the original lecture notes" toggle so the archive stays faithful.
2. **Semester differences.** Recommended: one "Syllabi" page per semester
   (course-level details only: description, texts, schedule), plus the
   "Taught in" line on each topic.
3. **Old links (about 190).** For each gray tag Micah chooses keep or drop.
   Recommended process: Claude produces one table with each link, the
   sentence it sat in, and whether it still works or has a Wayback Machine
   copy. Micah marks the table. See "Link checking" below.
4. **Copyrighted text pasted into the notes.** The notes include full lyrics
   (for example Bad Brains, "Pay to Cum"), a full allmusic review of "Teenage
   Riot," and a long bio blurb. Recommended: replace with a short quote, credit
   and a link.
5. **Recordings.** Recommended: upload to YouTube as unlisted, or Archive.org,
   and embed. Think first about whether student voices are in them, and
   whether Micah is comfortable publishing that.
6. **Visibility.** The microsite isn't linked from the main site. Options:
   keep it that way; link it from the homepage or Projects page; add a
   "please don't index" tag so search engines skip it. Recommended: decide
   at launch.
7. **Newspaper clippings.** The paper owns the article. Options: image on the
   site, link to the paper's own archive if one exists, or leave it in
   Micah's files.
8. **Flyer photo credit.** Who took the stage-dive photo?
9. **Book links.** Bookshop.org, WorldCat, or Open Library. Currently the
   texts show ISBNs only.

## The plan

Each step is one small pull request, in this order. Micah reviews screenshots
(desktop, phone, dark mode) before each one.

### Phase 0: Housekeeping
- [ ] Open a pull request for the current branch (home page and Week 1
      prototype). Micah says when to merge.

### Phase 1: Gather
- [x] Micah sends syllabi (four received; the fifth semester is still
      missing)
- [x] Claude builds a comparison: which topics were taught in which
      semesters, which readings, films and songs changed
      (`underground-music-semesters.md`)
- [ ] Micah sends the fifth syllabus and confirms the semester labels
      (Spring 2008, Summer 2008, Fall 2008, Spring 2009 were inferred)
- [ ] Micah sends any other listening lists
- [ ] Settle decisions 1 and 2, and approve the topic map

### Phase 2: Pilot one topic together
- [ ] Take "Roots and context" from raw notes to a finished page,
      editing it together. This sets the template and the editing rules
- [ ] Rename `week-01.md` to the topic page and update the course home
      list to group pages by theme
- [ ] Add the "Taught in" line and the folded original notes

### Phase 3: Topic pages, one at a time
Repeat for each topic in the map. For each page:
- [ ] Convert the raw notes (`tools/convert-notes.py`)
- [ ] Edit into readable form with Micah (see ground rules)
- [ ] Pull the "Play..." cues into a Listen and watch list
- [ ] List readings and films, by semester where they differ
- [ ] Mark every old link with a gray tag; Micah decides keep or drop
- [ ] Trim pasted copyrighted text (decision 4)
- [ ] Build locally, check desktop, phone and dark mode, then PR

### Phase 4: Course-level pages
- [ ] Syllabi pages (one per semester)
- [ ] Books page with links (decision 9)
- [ ] Films page
- [ ] Listening: put the 1994-2001 list on the right topic pages, and find
      a YouTube link for each song (Micah confirms each is the right version)

### Phase 5: Recordings
- [ ] Choose where they live (decision 5)
- [ ] Add a Recording section to the topics they belong to

### Phase 6: Launch
- [ ] Final privacy sweep: no phone numbers, no email except
      `micahvandegrift (at) gmail.com`, no student names
- [ ] Decide visibility (decision 6) and add any link from the main site
- [ ] Proofread the home page and every topic page
- [ ] Merge, then confirm the "pages build and deployment" action succeeds

## Start here when Micah is back at the laptop

1. Open a new Claude session on this repository and ask Claude to read this
   file.
2. Re-attach the notes (`AMS3810-REAL.doc`). The syllabi are already
   summarized in `underground-music-semesters.md`; send the fifth one.
3. Answer decisions 1 and 2 (page template and semester differences).
4. Review the draft topic map and say what to move, merge, add or cut.
5. Begin Phase 2: edit "Roots and context" together.

Optional, any time: answers to decisions 7 to 9 (clippings, photo credit, book
links).

## Ground rules for editing the notes

- Keep Micah's voice. Don't add facts that aren't in the notes or syllabi.
- Fix obvious typos (for example "Phillip Glass," "Detriot"), and keep a list
  of anything that looks like a factual doubt (dates, names, quotes) for Micah
  to confirm.
- Quotes stay word for word, with their source.
- Claude can't check facts online reliably from the cloud environment.
  Micah's sources win.
- Never turn an old link into a real link without Micah's say-so.

## Link checking

The cloud environment Claude runs in blocks many websites (it couldn't reach
Open Library, for example), so checking 190 links there may not work. If that's
the case, do it in a session running on Micah's own computer, or Micah checks
the table by hand.

## How the pieces work

- `underground-music/index.md` is the course home. Pages named `week-XX.md`
  in that folder are listed on it automatically (this will change to grouping
  by theme in Phase 2).
- `_layouts/class.html` is the course layout. `_config.yml` applies it to
  everything in the folder and sets the `course` styling class.
- `stylesheets/site.css` has a "Course microsite" section at the bottom for
  the course-only styles, including the gray `old-link` tags.
- `tools/convert-notes.py` turns a slice of the converted notes into a first
  draft. It's a helper and isn't published.
- To preview the site locally: install the `github-pages` gem, build, and
  open the result. Claude does this before every pull request.
