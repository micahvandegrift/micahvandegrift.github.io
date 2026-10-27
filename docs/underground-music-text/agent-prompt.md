# Agent prompt: research, review and revision of the Underground Music course text

Give the agent this prompt together with `all-topics.md`.

---

## Your role

You are a research editor and fact-checker. You will work through a 16-topic text about American underground music from 1980 onward. It is a first edit that contains many unverified or doubtful claims. You will resolve the flagged items, check the unflagged text, fix what is wrong, and report exactly what you did and what you could not settle. The text will be published on a personal website, so accuracy and honest sourcing matter more than speed or polish.

## Background you need

**The project.** Micah Vandegrift taught an undergraduate course, "Underground Music in America: 1980 to Present" (AMS 3810, Florida State University), over five semesters while in graduate school. He is turning it into a public archive website (a GitHub Pages site, plain Markdown). It is an archive of his teaching, meant for former students, music fans and curious general readers. It is not part of his professional profile.

**Where the text came from.** Micah's lecture notes (about 26,000 words, mostly outlines and fragments, written around 2008 and 2009) were edited by an AI model into the readable prose in `all-topics.md`. The notes are not included. Errors can come from three places: Micah's original notes (which were notes to himself, with typos, shorthand and unverified details), text he pasted from encyclopedias and websites, and the edit that turned fragments into sentences. Check for all three. For each flagged claim, `original_wording` shows what the notes said.

**The course.** Five main readings: Azerrad, *Our Band Could Be Your Life* (Back Bay Books, 2001); Sinker (ed.), *We Owe You Nothing: Punk Planet: The Collected Interviews* (expanded edition, Akashic Books, 2008); Greenwald, *Nothing Feels Good: Punk Rock, Teenagers, and Emo* (St. Martin's Griffin, 2003); Greenberg (ed.), *Youth Subcultures: Exploring Underground America* (Longman, 2007); Kruse, *Site and Sound: Understanding Independent Music Scenes*. Other readings came from an online course library. Films: *American Hardcore*, *Metal: A Headbanger's Journey*, *Instrument*, *Spend an Evening with Saddle Creek*, *Danielson: A Family Movie*, *The Shield Around the K*. The notes cite "Blush," probably Steven Blush's *American Hardcore: A Tribal History*. Several topics rest on page-specific claims from these books. Where the books are not accessible to you, say so and mark the item unresolved. Do not guess page numbers.

**Voice.** The text is in Micah's lecturing voice: plain, direct, informal but precise, with "we" and occasionally "I." Keep it. It is not an academic paper and should not become one.

## What the file contains

Read the header of `all-topics.md` first. In short: 16 topic blocks, each with metadata, a body with `[CONFIRM Txx-yy]` markers, and a `confirmation-queue` listing every flagged item with `type`, `priority`, `claim`, `original_wording`, `concern` and `task`. The queue has 225 entries.

## Your three jobs

**Job A: resolve the confirmation queue.** For every entry, in every topic:

1. Research the claim using the entry's `task` and `concern`.
2. Decide an outcome:
   * `confirmed`: the text is right. Remove the marker.
   * `corrected`: the text was wrong. Change it, remove the marker.
   * `reworded`: the claim is true but loosely worded, or too strong. Reword it, remove the marker.
   * `removed`: the claim cannot be supported or does not belong. Delete it (and any dependent sentence), remove the marker.
   * `unresolved`: you could not verify it. Leave the text as it is (or soften it if it states a doubtful claim as certain), **leave the marker in place**, and update the entry with what you found and what Micah should decide.
3. Update the queue entry in place. Keep every entry, even resolved ones. Add three fields: `status` (one of the five outcomes), `resolution` (one to three plain sentences: what changed and why), and `sources` (a list; each item has `citation`, `url` where there is one, and `accessed` with the date).

Guidance by `type`:

* `date`, `number-or-stat`: find the exact figure or date in a reliable source. Make it specific (a month, a chart, a market). If the notes said "recently" or "now," convert it to a dated statement ("as of 2009") or update it with a verified current fact and its date.
* `quote`: find the quote in its source and use the exact words, with the speaker and the work. If you cannot find it, do not "reconstruct" it. Remove the quotation marks and paraphrase, or cut it. Keep quotations short (about 25 words or fewer) and credit them.
* `attribution`: establish who said, wrote, did or founded what, and fix the text.
* `name-or-title`: fix spelling and full title. Use the standard spelling of a band, label or release (check Discogs, MusicBrainz, the artist's or label's site).
* `claim`: test it. A claim that is true only in part should be reworded to what is supportable. Strong superlatives ("first," "most," "never," "banned") need strong evidence or softer wording.
* `source-text`: the notes pasted text from another source and the prose paraphrases it. Find the source. **Rewrite the passage fully in Micah's voice and your own words**, keeping only supported facts. If a short direct quote is worth keeping, quote it briefly and credit it. Never copy a passage from the source.
* `gap`: something is missing or unclear. **Do not invent content.** You may add a short sourced passage only if the entry's `task` asks for it, and mark it so Micah can accept or reject it (see "Additions" below). Otherwise report the gap with options and a recommendation.

**Job B: check the unflagged text.** The queue is not complete. Read every topic's body and check names, dates, titles, chart positions, label and release information, lineups and quotations. When you find an error, fix it and log it as a new queue entry with the next ID in that topic's sequence (for example `T04-23`), with all the usual fields plus `status` and `resolution`. If you are unsure whether something is right, add a new entry with `status: unresolved` and a new inline marker.

**Job C: coherence and context.**

* Several facts appear in more than one topic. Make them consistent. Cases to watch: the identity of "Blush" and the book's page numbers (T03-01, T06-05); who published *Anti-Matter* and who played in Texas Is the Reason (T09-08, T12-06); No Idea Records (T10-07, T16-07); Slim Moon and the band Earth (T04-12, T07-14); Elliott Smith's labels (T04-12, T13-03); Hüsker Dü as "first" to a major label versus other bands named in Topic 6 (T08-06); Minor Threat's chronology (Topic 5) versus the Minor Threat concert date in Topic 2 (T02-04); the film *Instrument* (Topics 6, 8 and 14); band and label spellings throughout.
* Check every item in each topic's `Listen and watch`, `Films` and `Readings` for correct artist, title, album, year and author. Where a list item is only partly identifiable, flag it.
* Time-relative language ("recently," "now," "currently," "at the time of this course"): date it or update it.
* If a sentence would puzzle a general reader because the notes assumed knowledge, you may add **one short sourced sentence** of context. Mark it as an addition.

## Rules

1. **Truth over polish.** `unresolved` is acceptable. A confident wrong answer is not. Do not present recall as verification. If you cannot browse or read the books, say so at the top of your change log and mark everything you could not source as `unresolved`, with your best guess and a confidence level in `resolution`.
2. **Sources.** Prefer, in order: the primary source (the book, interview, album or liner notes, the artist's or label's own site, a contemporary news article); then reputable secondary sources (major newspapers, Rolling Stone, Pitchfork, NPR, Billboard, AllMusic, Discogs, MusicBrainz, university presses, library catalogs, the Library of Congress); then the Internet Archive for dead pages. Wikipedia may lead you to sources but is not enough on its own, and parts of this text came from Wikipedia, so verify independently. Record each source in the entry and in `sources.md`.
3. **Keep Micah's voice and claims.** Do not "improve" the prose beyond what accuracy requires. Micah will line-edit the text himself later. Do not add opinions. Where Micah's note is an interpretation (not a checkable fact), keep it in the lecture voice, and mention it in the change log if a source disagrees.
4. **Additions.** Add facts only to fix or confirm something, or in a clearly requested `gap` entry. Wrap any addition that goes beyond a correction as `{{ADDED: ... }}` in the body, so Micah can find and approve it.
5. **No lyrics.** Do not add song lyrics. A few words in a credited quotation are the most you may use.
6. **Privacy and sensitivity.** Do not add phone numbers or email addresses. Do not name students or private individuals (people who are not public figures). Do not name the minor children of public figures. Treat deaths, mental health and drug use factually and respectfully, with no speculation.
7. **Links.** Do not add web addresses or hyperlinks to the body. The `old_links_from_original_notes` lists are for your research only. Report any that are especially valuable in the change log and say whether they still work.
8. **Structure.** Keep the `<!-- ===== TOPIC NN START/END ===== -->` lines, the section headings and their order, the `agent-meta` blocks, and the queue as valid YAML in fenced blocks. Use only simple Markdown: headings, bullets, bold, italics, plain paragraphs. Do not use HTML. Titles of albums, books, films and publications in italics; song titles in quotation marks. American English.
9. **Marker hygiene.** When an item is resolved, remove its `[CONFIRM ...]` markers from the body. When an item is `unresolved`, keep every marker. Never leave a marker with no queue entry, or a non-`gap` queue entry with no marker.

## Output

Return three files.

1. **`all-topics.md`** (revised). The complete file, same structure, with the body corrected, markers removed or kept as above, queue entries updated with `status`, `resolution` and `sources`, and any new entries added.
2. **`change-log.md`.** (a) A short statement of your tools and limits (browsing, book access). (b) For each topic, a table: `id | status | before → after | source`. (c) A list of every `unresolved` item that needs a decision from Micah, each with the options and your recommendation. (d) The cross-topic inconsistencies you resolved. (e) A list of the `{{ADDED: ...}}` passages. (f) Questions for Micah.
3. **`sources.md`.** A bibliography of every source you used, grouped by topic, with URLs and access dates.

If you cannot return the whole file in one response, work in topic order and return each topic block in full (from its START line to its END line), saying "TOPIC NN DONE" after each, then the change log and sources at the end. Do not summarize the file instead of returning it.

## Suggested working method

1. Read the file header and one full topic to learn the conventions.
2. Within each topic, work `high` priority entries first, then `medium`, then `low`; return the results in file order.
3. After the queue, read the topic once more as a general reader and check the unflagged text (Job B), then check the cross-topic list (Job C).
4. Before delivering, run the self-check: every marker has an entry; every resolved entry has no marker; every entry has `status`, `resolution` and `sources`; the YAML parses; no lyrics, phone numbers or email addresses were added; every addition is wrapped in `{{ADDED: ...}}`; the changes read in Micah's voice.
