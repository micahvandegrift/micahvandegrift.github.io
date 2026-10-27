# Underground Music in America: Edited Course Text

**Working file for research, review and revision. Written for an LLM agent, not a human reader.**

## What this file is

This file holds the edited text of 16 topics from an undergraduate course, "Underground Music in America: 1980 to Present" (AMS 3810, Florida State University, taught by Micah Vandegrift over five semesters while he was in graduate school). The text was edited from Micah's lecture notes (about 26,000 words, mostly outlines and fragments, written around 2008 and 2009 and revised over the semesters) into readable prose for a public website. The original notes are **not** included. For every claim that needs checking, the queue entry quotes the original wording in `original_wording`.

The text is a **first edit, not a verified text**. It keeps Micah's claims, dates, quotes and page references as the notes gave them, except where a mistake was obvious. Many details in the notes are wrong, vague, pasted from other sources or unverified. Your job (see the separate agent prompt, `agent-prompt.md`) is to check them, fix them, and report what you did.

## Structure

The file is a sequence of 16 topic blocks. Each block is wrapped by comment lines:

```
<!-- ===== TOPIC NN START ===== -->
... block ...
<!-- ===== TOPIC NN END ===== -->
```

Inside each block, in order:

1. `# Topic N: Title`
2. A fenced `yaml agent-meta` block with `topic`, `slug`, `title`, `syllabus_lessons`, `syllabus_readings`, `syllabus_film`, and `old_links_from_original_notes`. The syllabus fields come from the course syllabi, and the old links are every web address that appeared in the original notes for that topic. Those links are from about 2008 to 2009 and many are dead; use them as research leads (try the Internet Archive's Wayback Machine). They are **not** to be added to the prose.
3. The body, in `##` sections: Overview, Listen and watch, Films (if any), Readings, Discussion questions, then the topic's content under further `##` and `###` headings. Do not rename, reorder or merge these sections.
4. `## Confirmation queue (Topic N)` and a fenced `yaml confirmation-queue` block.

## Confirmation markers

In the body, `[CONFIRM T04-07]` is a marker. It sits right after the sentence or claim it refers to. Some markers cover a whole paragraph. The ID matches an entry in that topic's confirmation queue. The same ID may appear in more than one place in a topic when one issue affects several sentences.

Each queue entry has these fields:

| Field | Meaning |
|---|---|
| `id` | `T` + two-digit topic number + `-` + two-digit sequence number, for example `T04-07` |
| `type` | one of: `date`, `quote`, `attribution`, `name-or-title`, `number-or-stat`, `claim`, `source-text`, `gap` (definitions below) |
| `priority` | `high` (probably wrong, or a strong claim); `medium` (needs checking); `low` (probably right, quick check) |
| `claim` | the claim as it now appears in the body |
| `original_wording` | what Micah's notes said, close to verbatim, so you can see what was meant |
| `concern` | why the claim is doubtful |
| `task` | what to research and what to produce |

Types:

* `date`: a date, year or sequence of events.
* `quote`: a quotation whose exact words, speaker or source need checking.
* `attribution`: who said, wrote or did something.
* `name-or-title`: the spelling or identity of a person, band, release, publication or reading.
* `number-or-stat`: a figure, ranking or statistic.
* `claim`: a factual statement that may be inaccurate, too strong or garbled.
* `source-text`: the original notes pasted text from another source (an encyclopedia, a website, a textbook) instead of writing it in Micah's voice. The prose paraphrases it. Find the source, check it, and either rewrite it fully in Micah's voice or credit it.
* `gap`: something is missing or unclear. The notes do not support a statement, or a syllabus item has no notes behind it. A `gap` entry does not always have an inline marker. **Do not invent content to fill a gap.** Report it.

## Conventions in the body

* Quotations in quotation marks are from the notes' sources, kept as the notes had them, and are unverified until you check them.
* Page numbers in parentheses, such as "(Azerrad, p. 238)," refer to the readings named in the text: Azerrad, *Our Band Could Be Your Life*; Sinker (ed.), *We Owe You Nothing: Punk Planet: The Collected Interviews*; Greenwald, *Nothing Feels Good: Punk Rock, Teenagers, and Emo*; Greenberg, *Youth Subcultures: Exploring Underground America*; Kruse, *Site and Sound: Understanding Independent Music Scenes*; Blush, which is probably *American Hardcore*.
* "I" and "we" are Micah's voice as a lecturer. Keep it.
* Song lyrics are deliberately left out (some were pasted in full in the notes). Do not add lyrics beyond a very short, credited quote.

## What not to change

Do not add facts that you cannot source. Any addition you make beyond a correction must be wrapped as `{{ADDED: ...}}` so that it can be found and approved. Do not delete a section. Do not add any phone number or email address, and do not add the names of students or of private individuals who are not public figures. Do not turn the old links into hyperlinks.

Everything else is in the agent prompt.

<!-- ===== TOPIC 01 START ===== -->

# Topic 1: Introduction, Roots and Historical Context

```yaml agent-meta
topic: 1
slug: topic-01
title: Introduction, Roots and Historical Context
syllabus_lessons: 'why have a course on underground music; defining underground, indie and DIY; subcultural studies (discussion of readings, defining the terms of the discourse); historical precedents (the New York School composers, John Cage, Glass, La Monte Young; the Velvet Underground; Iggy and the Stooges; proto-punk); the 1980s: music, society and culture.'
syllabus_readings: introductions to Azerrad, Sinker and Greenberg; Holly Kruse, "Telling the Story of Independent Music," pp. 5-13.
syllabus_film: (none recorded)
old_links_from_original_notes:
- http://www.youtube.com/watch?v=57ZHYLrUvXA
- http://www.tate.org.uk/tateetc/issue8/images/erasuregenteel_eraseddekooning.jpg
- http://www.youtube.com/watch?v=TUihm4u2-ok
- http://www.youtube.com/watch?v=erjksafj_Jw
- http://www.youtube.com/watch?v=sqHz7cUw4Ls
- http://kclibrary.nhmccd.edu/decade80.html
- http://www.nostalgiacentral.com/index.htm
- http://findarticles.com/p/articles/mi_m2822/is_1_24/ai_73712455
- http://www.vh1.com/shows/dyn/i_love_the_80s/62135/episode_about.jhtml
- http://youtube.com/watch?v=vq0ZkW-Q49s
- http://youtube.com/watch?v=EU-IBF8nwSY
```

## Overview

Why have a course on underground music? This first topic sets up the big questions, then goes looking for the music's roots. For our purposes, underground music was born out of two distinctly American streams of music: experimental classical music and punk. It has a dual nature, both intellectual and aggressive, and it grew out of a long American habit of being experimental and progressive.

The story of this music works in and out of chronological order. There are brief periods where you can see a movement, and then it disappears. We look at it over time, and now and again pause to look at the culture that grew up alongside the music. The important thing to remember is that this music is about progression, pushing the envelope and stretching the ear.

The second half of the topic is context. Art is always a product of its time, so to understand it we start with the age it came from: the 1980s, which are known for two things, politics and entertainment. Underneath all of it came a reaction, an underground that was aesthetically, philosophically and politically opposed to the mainstream.

## Listen and watch

* John Cage, *4'33"*
* The Velvet Underground, "I'm Waiting for the Man"
* The Stooges, "I Wanna Be Your Dog"
* Glenn Branca, Symphony No. 5, fifth movement
* Apple's "1984" commercial
* 1980s commercials, to show the glitzy picture of the decade that the underground rejected

## Readings

* The Introduction in Azerrad, *Our Band Could Be Your Life*
* The Introduction in Sinker, *We Owe You Nothing*
* The Introduction in Greenberg, *Youth Subcultures*
* Holly Kruse, "Telling the Story of Independent Music," pp. 5-13

Further reading: Kyle Gann, *American Music in the 20th Century*; Lester Bangs, pp. 34, 39, 44 and 45 (on the Stooges).

## Discussion questions

* Why have a course on underground music?
* How would you define "underground," "indie" and "DIY"? These definitions will change and grow over the timeline of this music.
* In the Azerrad introduction, who is "we"?
* What was the socio-cultural context? What was happening in the world?
* Who decides which values are the "fundamental values" of America?
* Was the underground a counterculture in the beginning that became a subculture?

## Roots: two American streams

There is a precedent in American music for being experimental and progressive, a case Kyle Gann makes in *American Music in the 20th Century*. Over the course of the twentieth century, America became the torch-bearer of new cultural movements, and the rugged individualism and think-for-yourself attitude of its people spurred that on.

### John Cage and the question "What is music?"

John Cage (1912-1992) was one of the first to ask, "What is music?" On August 29, 1952, *4'33"* was first performed. It consisted of whatever unintentional and ambient sounds the audience heard during the framed time period. Cage was inspired by his friend Robert Rauschenberg's white paintings.

Cage saw where this was heading: "I believe that the use of noise to make music will continue and increase until we reach a music produced through the aid of electrical instruments which will make available for musical purposes any and all sounds that can be heard… whereas, in the past, the point of disagreement has been between dissonance and consonance, it will be, in the immediate future, between noise and so-called musical sounds." (Gann, p. 130) [CONFIRM T01-01] Indeterminacy, he said, is an invitation not to anarchy but to freedom. [CONFIRM T01-02] "Music is continuous, it is we who turn away." [CONFIRM T01-03]

The idea of minimalism begins to seep into art during this period. The audacity of the American experimentalists to question centuries of musical tradition set the world on a course that eventually led to punk and post-punk being accepted as some form of art. That trend can be traced through the entire twentieth century.

### The New York School

Cage was the first generation of the New York School, and Philip Glass and La Monte Young (minimalism) were part of it too: "Faith in the liberation of the unconscious and an excitement drawn from the street energies of the city." [CONFIRM T01-04] [CONFIRM T01-05] The label later became synonymous with avant-garde and minimalism. Glass was an inspiration to David Bowie, Harry Partch, Milton Babbitt, Brian Eno and John Zorn. [CONFIRM T01-06]

### From experiment to rock: the Velvet Underground

In 1965, John Cale and Lou Reed formed the Velvet Underground. Cale had come to America to study and play with La Monte Young, who was also interested in new rock. The Velvets were inspired by experimental composers but began to use their ideas in rock. They were the foundation for 1960s garage rock. Brian Eno put it this way: while only 1,000 people bought the Velvet record, almost all of them were inspired to start a band. [CONFIRM T01-07]

### Punk

Punk was short, fast, loud and angry. It came from New York and the Midwest: The Stooges (Ann Arbor, Michigan), the MC5 (Motor City 5, Detroit), The Ramones, Patti Smith.

The Stooges' debut album came out in 1969, produced by John Cale. They made three studio albums and then burned out on drugs. (Lester Bangs wrote about them; see his pp. 34, 39, 44 and 45.)

In New York, the scene included The Ramones, Patti Smith, and Richard Hell and The Voidoids. Hell played with the band Television and released "Blank Generation" in 1977. It is said that he created the look of punk, and that Malcolm McLaren modeled the Sex Pistols on him. [CONFIRM T01-10]

The brazen attitude of punk, and its bold, know-nothing, just-do-it mentality, feeds into the underground, especially in the early 1980s.

### Where from there

Three bands matter most: the Velvet Underground, The Stooges and Black Sabbath. And in the early 1980s, Glenn Branca began composing for guitar orchestras, or, as we call them, "guitarchestras." Symphony No. 5, fifth movement, is the example we listen to.

## The 1980s: music, society and culture

The 1980s are known for two things: politics and entertainment. Art is always a product of its time, so to understand it accurately you must start with the context of the age. What was the socio-cultural context? What was happening in the world?

### Politics

The country faced high inflation and unemployment, "the Misery Index," which led many to vote for Reagan. He was popular with many groups despite his policies.

The New Conservatism came out of the New Right, or New Christian Right, which grew from the evangelical movements that were big in the 1970s. It called for a return to fundamental values in America. Who decides what those fundamental values are?

Reaganomics meant victory over inflation, deregulation of industry, a moratorium on social spending, enormous tax cuts and a staggering budget deficit. It brought great wealth to some, but the percentage of Americans in poverty increased.

This was also the birth of the Yuppies, Young Urban Professionals: mostly white, well educated, living in urban condos, on fast-track careers, with leisure time spent on a lavish lifestyle. They established consumption patterns that many people tried to copy (see *American Psycho*).

Rights for women and gays had another rise. AIDS was identified in 1981. In 1984, the U.S. was involved in civil wars in El Salvador and Nicaragua, banks were failing, homelessness was on the rise and crack had been introduced to the streets, while Reagan's campaign slogan declared, "It is morning in America!"

### Music and media

The music business was in a slump, and it began to ride on the shoulders of a few: Michael Jackson, Whitney Houston, Madonna, Prince, Bruce Springsteen, Phil Collins, Janet Jackson. It faced new competition from videos, video games and cable, and from "pirating" by copying tapes on cassette recorders.

MTV launched on August 1, 1981, with "Video Killed the Radio Star," and totally changed the way music was marketed. *Thriller* in 1982 forced MTV to change its format to include Black artists. [CONFIRM T01-08] The production of celebrity became a huge business and began to drive the commercialization of American culture.

In 1984, Springsteen released *Born in the USA*, with songs about working-class people around thirty-five years old, facing economic or personal difficulties, with a sense of better times past.

### Technology and globalization

This was the birth of the information age: the personal computer in 1977, cell phones in 1983, the space race, video games, MTV. The first CDs went on sale in 1983, and by 1988 they had surpassed vinyl in sales. Tapes passed vinyl for the first time, thanks to boomboxes and Walkmen. [CONFIRM T01-11] The rate of change, in technology and in trends and fads, was exponentially faster than in earlier decades.

The world got smaller. Economists used the term "globalization" in 1981 to describe how the countries of the world were coming to terms with being connected to one earth, in business, entertainment, technology and culture. [CONFIRM T01-12]

### The picture on TV

The commercials of the decade, and the Apple "1984" ad, present a glitzy, glamorous world. That is not how it was, and much of underground culture is based on the idea of negation: things are not the way they seem.

### The underground answers

It is interesting that the epicenters of the underground sat in the same regions that produced the political and popular culture of the decade: Washington, DC, the political capital, and Los Angeles, home of Hollywood.

While all this was happening, there was a reaction underneath it all, in the form of underground music. It was aesthetically opposed, philosophically opposed and politically opposed to the mainstream. Was it a counterculture in the beginning that became a subculture?

The early 1980s mark the point in American culture where Big Media was so concentrated on pushing the top level of pop culture that, underneath it, an entirely different culture developed. This underground formed the framework for disenchanted youth, and they built it from the ground up. The split between pop culture and the underground, and the utter rejection of "the norm" by these youths, set up the intellectual and philosophical space where ideas like DIY and indie came into existence, along with the question of how to define what was included in or excluded from the underground.

## Terms of discourse

The readings begin to introduce the language of the subculture: what it says, and how it says it. The phrases to become familiar with are DIY, indie, underground, mainstream, community, authenticity, and the responsibility of the audience.

**Underground.** In the Azerrad introduction: who is "we"?

**Independent.** Not released through a major distributor; developed on a grassroots level; retaining control; political radicalism.

**DIY.**
* Modest: a moral imperative, a necessity rather than a statement.
* Quality and importance.
* Sticking with the vision.
* Connection to the audience, as in the 1960s. [CONFIRM T01-09]
* Purism and authenticity; idealism about the power of music; a reaction to shallow times and entertainment; populist roots commandeered by middle-class white kids.
* The audience is as much a part of it as the producers.
* A leap of faith.
* Diversity in sound, which attracts a certain type of person.

**Negation.** A cycle of rebellion that America experiences. The connection between the beginning of the underground and the 1960s is an important point to keep in mind.

## Confirmation queue (Topic 1)

```yaml confirmation-queue
- id: T01-01
  type: attribution
  priority: high
  claim: The "noise versus so-called musical sounds" passage is by John Cage (cited as Gann, p. 130).
  original_wording: '"I believe that the use of noise to make music will continue and increase until we reach a music produced through the aid of electrical instruments... Gann , 130" (no speaker named)'
  concern: The source note names only "Gann, 130." The speaker was assumed to be Cage.
  task: Identify the speaker, the original source and date, and the exact wording. Confirm Gann's page number. Fix the attribution and quote if needed.
- id: T01-02
  type: attribution
  priority: medium
  claim: '"Indeterminacy is an invitation not to anarchy but to freedom," attributed to Cage.'
  original_wording: indeterminacy is an invitation not to anarchy but to freedom.
  concern: No speaker or source in the original.
  task: Find who said it and where. Attribute it or reword.
- id: T01-03
  type: attribution
  priority: medium
  claim: '"Music is continuous, it is we who turn away."'
  original_wording: Music is continuous, it is we who turn away – from India
  concern: The original says only "from India." Unclear whether this is a quote from Cage, a proverb Cage cited, or something else.
  task: Find the origin and the person who used it in this context. Quote exactly with attribution, or reword.
- id: T01-04
  type: quote
  priority: medium
  claim: '"Faith in the liberation of the unconscious and an excitement drawn from the street energies of the city" describes the New York School (Cage, Glass, Young).'
  original_wording: '"Faith in the liberation of the unconscious and an excitement drawn from the street energies of the city." Later became synonymous with avant-garde and minimalism.'
  concern: No source in the original.
  task: Find the source and the subject of the quote. Check whether it describes the New York School or a different group.
- id: T01-05
  type: claim
  priority: high
  claim: Cage was the first generation of the New York School, and Philip Glass and La Monte Young (minimalism) were part of it too.
  original_wording: John Cage (1st gen) Phillip Glass and La Monte Young part of the New York School.
  concern: '"New York School" usually names Cage''s circle of the 1950s (Feldman, Brown, Wolff). Glass and Young are usually called minimalists.'
  task: State the standard usage with sources. Propose the most accurate wording that stays close to the intended point (an experimental lineage running from Cage to minimalism to rock).
- id: T01-06
  type: claim
  priority: high
  claim: Glass was an inspiration to David Bowie, Harry Partch, Milton Babbitt, Brian Eno and John Zorn.
  original_wording: Phillip Glass- inspiration to Bowie, Harry Partch, Milton Babbit, Brian Eno, John Zorn
  concern: Partch (b. 1901) and Babbitt (b. 1916) are older than Glass (b. 1937), so Glass could not have inspired them. The list may mean the wider experimental lineage, or only some of the names.
  task: Work out which names plausibly belong and in what relationship to Glass. Propose a corrected sentence.
- id: T01-07
  type: quote
  priority: medium
  claim: Brian Eno said only 1,000 people bought the Velvet Underground record, but almost all of them started a band.
  original_wording: quote about Velvet by Brian Eno "while only 1000 people bought the Velvet record, almost all of them were inspired to start a band."
  concern: Widely repeated as a paraphrase; exact wording, source and date are uncertain.
  task: Find the earliest attributable source and the exact wording. Quote it exactly or mark it as a commonly repeated paraphrase.
- id: T01-08
  type: date
  priority: medium
  claim: '*Thriller* in 1982 forced MTV to change its format to include Black artists.'
  original_wording: Thriller- 1982 forced MTV to change its format to include Black artists.
  concern: The change at MTV is usually tied to the 1983 videos from the album ("Billie Jean," "Beat It"), not to the 1982 release.
  task: Establish the correct sequence and fix the wording.
- id: T01-09
  type: quote
  priority: medium
  claim: 'DIY: "Connection to the audience, as in the 1960s."'
  original_wording: Connection to the audience / Like the 60s- Guy quote
  concern: The original mentions a quote from "Guy" (probably Guy Picciotto) with no text or citation. The sentence has no quote right now.
  task: Find the quote Micah probably meant (Picciotto on the 1960s and audience connection, likely in Azerrad or Sinker). If found, add it with source. If not, say so.
- id: T01-10
  type: claim
  priority: low
  claim: It is said that Richard Hell created the look of punk, and that Malcolm McLaren modeled the Sex Pistols on him. Hell released "Blank Generation" in 1977.
  original_wording: Richard Hell- played with the band Television and released 'Blank Generation' 1977. It is said that he inspired or created the look of punk and that Malcolm Mclaren created the Sex Pistols off of Richard Hells model.
  concern: Dates and wording of the McLaren claim are loose ("Blank Generation" single 1976, album 1977).
  task: Verify the dates, the Television connection, and whether the McLaren claim is well documented. Reword with hedging as needed.
- id: T01-11
  type: date
  priority: medium
  claim: Cell phones 1983, personal computer 1977, first CDs on sale 1983, CDs surpass vinyl in sales by 1988, tapes pass vinyl for the first time.
  original_wording: PC 1977, cell phones 1983 ... 1983 first CDs on sale, 1988 they surpass vinyl in sales ... tapes pass vinyl for the first time in history due to boomboxes and Walkmen.
  concern: Several dates and "surpass" claims need checking (market, format, and year; US vs. worldwide).
  task: Verify each date and statement for the US market. Fix and add the year or market where needed.
- id: T01-12
  type: claim
  priority: low
  claim: Economists used the term "globalization" in 1981.
  original_wording: Term used by economists in 1981 to describe how the countries in the world were beginning to come to terms with being connected to one earth.
  concern: Possibly inaccurate or too specific.
  task: Check the history of the word and fix.
```

<!-- ===== TOPIC 01 END ===== -->

<!-- ===== TOPIC 02 START ===== -->

# Topic 2: No Wave and Sonic Youth

```yaml agent-meta
topic: 2
slug: topic-02
title: No Wave and Sonic Youth
syllabus_lessons: No Wave and New York City; Sonic Youth.
syllabus_readings: Thurston Moore in Sinker; Sonic Youth in Azerrad.
syllabus_film: (none recorded)
old_links_from_original_notes:
- http://en.wikipedia.org/wiki/Image:Blondie_-_Parallel_Lines.jpg
- http://nowave.pair.com/no_wave/nycnowave_index.html
- http://www.allmusic.com/cg/amg.dll?p=amg&sql=10:h9fuxqehldse
- http://en.wikipedia.org/wiki/Sonic_Youth
- http://en.wikipedia.org/wiki/Richard_Kern
- http://en.wikipedia.org/wiki/Bob_Bert
- http://en.wikipedia.org/wiki/Steve_Shelley
- http://www.youtube.com/watch?v=YnzZ6J8BjOo
- http://www.allmusic.com/cg/amg.dll?p=amg&sql=33:wzfixxr0ldje
- http://www.sonicyouth.com/mustang/cc/sytour.html
- http://www.allmusic.com/cg/amg.dll?p=amg&sql=11:hifuxqr5ld0e~T5
- http://www.last.fm/music/Sonic+Youth/+wiki
- http://www.sonicyouth.com/main/index.html
```

## Overview

This topic starts in New York with No Wave, an offshoot of late-1970s punk that rejected melody and technique, and then follows Sonic Youth, a band that came out of punk, mixed it with No Wave and tied it to experimental music. Formed in New York in 1981, they went from dissonant tunings and "prepared" instruments to a major label deal, and in 2007 one of their albums was added to the Library of Congress. [CONFIRM T02-01]

Sonic Youth are a case study in what the underground could do. They asked to be taken seriously as art, reached back before punk for influence, treated relationships and networking as currency, and brought the idea of "negation" back into rock. In the words of the reading, they were "more an inspiration than an influence."

## Listen and watch

* Sonic Youth, "Death Valley '69" (video, directed by Richard Kern, 1985)
* Sonic Youth, "Kill Yr. Idols"
* Sonic Youth, "Teen Age Riot"
* Sonic Youth, "Kool Thing" (a sample, with Chuck D as a guest)

## Films

* *The Year Punk Broke*, a documentary of Sonic Youth's 1991 tour with Nirvana [CONFIRM T02-11]

## Readings

* Thurston Moore in Sinker, *We Owe You Nothing*
* Sonic Youth in Azerrad, *Our Band Could Be Your Life*

Further reading: Greil Marcus's 1983 *Artforum* piece on Sonic Youth. Azerrad pages cited in this topic: 232, 238, 243, 249, 254-256, 262-265 and 273.

## Discussion questions

* What were Sonic Youth's contributions to American underground music?
* Negation: how does this concept come up in other art forms and time periods?
* What is the "Daydream Nation"?
* How do these bands begin to challenge ideas about America? Who has access to the American Dream? What is it, and why are the youth so upset about it?

## No Wave and *No New York*

No Wave was an offshoot of late-1970s punk, concentrated mainly in New York, from 1978 to 1982. The name played off the New Wave bands of the day: The B-52's, The Cars, Devo, Talking Heads. The fashion was choppy haircuts and skinny suits and ties.

It was different from punk. No Wave rejected melody as well as technique, and it put musical texture ahead of tone or style. It was atonal and dissonant. It was as much performance art as music, and it was iconoclastic, all about tearing down the foundations of music.

Brian Eno put together *No New York* (1978) to document the scene. He first considered ten bands but ended up with four, four songs each: The Contortions, Teenage Jesus and the Jerks, Mars and DNA. [CONFIRM T02-02]

## Sonic Youth

Sonic Youth are Thurston Moore, Kim Gordon, Lee Ranaldo and Steve Shelley. Former members include Bob Bert, Richard Edson (the first drummer), Jim O'Rourke and Jim Sclavunos. [CONFIRM T02-03] They formed in 1981 in New York City.

They came out of punk, mixed it with No Wave and tied it to experimental music. They named their influences as Glenn Branca, The Stooges, The Velvet Underground, Black Sabbath, MC5 and the Grateful Dead. They were also deeply affected by seeing Minor Threat perform in May 1982 (Azerrad, p. 238). [CONFIRM T02-04]

Their sound came from a variety of different tunings and from "prepared" instruments, much like the experiments of Henry Cowell and John Cage. They specialized in dissonant tones, so a quick music theory review of consonance versus dissonance helps here.

### The story

In December 1981 they recorded an EP for Glenn Branca's Neutral Records. In November 1982 they toured with the Swans, on what was called the Savage Blunder Tour. In 1983, Jim Sclavunos joined on drums and the band released *Confusion Is Sex*. A two-week European tour that summer was well received. Moore began publishing a fanzine called *Killer*, and interviewed Ian MacKaye in the first issue. [CONFIRM T02-05]

In 1984, a disastrous show in London led to good press in the English magazines *Sounds* and *NME*. That year's album, *Bad Moon Rising*, commented on American culture at the time, and negation was part of it.

In 1985 they made the video for "Death Valley '69," directed by Richard Kern. It was their first music video. It shows most of the band in various states of bloody dismemberment, mixed with live footage, and features both the recently departed drummer Bob Bert and the new member Steve Shelley. [CONFIRM T02-06] In January 1985 they played in Seattle and met Bruce Pavitt, who paid $100 to use "Kill Yr. Idols" on a compilation called *Sub Pop 100*. [CONFIRM T02-07]

In early 1986 they signed to SST Records (Greg Ginn of Black Flag's label) and recorded *EVOL* in March. It is an album obsessed with celebrity, and it got good press in the U.S., in *People* and the *New York Times*. It was an artistic breakthrough for the band (Azerrad, p. 263).

In 1987 came *Sister*, partly inspired by the life and works of Philip K. Dick. It sold 60,000 copies and cracked the *Village Voice* Pazz & Jop top 20. [CONFIRM T02-08]

In 1988 they released the double LP *Daydream Nation* on Enigma, distributed by Capitol, which was partly owned by EMI. CMJ, *Rolling Stone* and others lauded it as one of the best albums of the year. Distribution problems arose, and the band began to look for a major label deal. Its opening track, "Teen Age Riot," is a pivotal song in their career.

In 1990 they released *Goo* on Geffen Records, with the single "Kool Thing," featuring Chuck D as a guest. It is considered a more accessible album. In 1991 came the documentary of their tour with Nirvana, *The Year Punk Broke*. In 1992 they released *Dirty* on DGC; the video for "100%" was by the newly discovered Spike Jonze and featured Jason Lee skateboarding.

*Experimental Jet Set* followed in 1994 on DGC, with "Bull in the Heather" as a pseudo-hit. [CONFIRM T02-09] There was no full tour for it, because Kim Gordon was pregnant. In 1995 they headlined Lollapalooza, and in 1996 they appeared on *The Simpsons*, in the episode "Homerpalooza."

They began releasing albums on their own label, SYR Records, based in Hoboken, New Jersey. *SYR3* was the first to feature Jim O'Rourke as a full member. *SYR4*, released in 1999, is made up of covers of avant-garde composers: John Cage, Steve Reich and Yoko Ono. Later albums include *NYC Ghosts and Flowers* (2000), *Murray Street* (2002), *Sonic Nurse* (2004) and *Rather Ripped* (2006).

On May 24, 2007, *Daydream Nation* was added to the Library of Congress. [CONFIRM T02-01]

## What they brought to the underground

These points come from Azerrad's chapter on the band.

**Timbre, texture and rhythm.** Sonic Youth put a premium on timbre, harmonic texture and rhythm. Timbre is the character or quality of a musical sound as distinct from its pitch and intensity.

**Art.** They asked to be taken seriously as art. They bridged the worlds of high art and low art: like Warhol, they mixed pop culture with high art. Arty versus edgy (p. 264).

**Nostalgia.** They allowed their music to be nostalgic, reaching back before punk for influence.

**Relationships as currency.** Empowerment came through grassroots connections, as opposed to the mainstream, where bands are marketed into existence. They recognized the importance of networking and put it into practice, carrying many other bands to notoriety alongside them (pp. 254-256).

**A framework for indie rock.** They carried the music from punk's working-class roots to urban high art, and pioneered the search for new sounds in rock (p. 243).

**Negation.** They brought the concept of "negation" back into rock (p. 249). Negation is the refusal to ignore harsh realities: the world is not as it seems. Greil Marcus coined the term in a 1983 *Artforum* piece on Sonic Youth. It had been used by 1960s bands such as CCR, MC5, The Stooges and The Velvet Underground, and it was a reaction against Tom Petty, John Mellencamp and Bruce Springsteen. [CONFIRM T02-10]

**Physical versus cerebral.** This is the line drawn between hardcore and pre-indie, for instance Minor Threat compared with The Flaming Lips. It plays into underground music for the rest of its life.

**Inspiration more than influence.** In Azerrad's phrase, they were more an inspiration than an influence (p. 273).

## Confirmation queue (Topic 2)

```yaml confirmation-queue
- id: T02-01
  type: claim
  priority: medium
  claim: On May 24, 2007, Daydream Nation was added to the Library of Congress.
  original_wording: May 24, 2007 Daydream Nation was added to the Library of Congress, National Recording Preservation Board.
  concern: The usual phrasing is that the album was selected for the National Recording Registry. The original names the "National Recording Preservation Board." Date and body need checking.
  task: Verify the date and the exact body or registry. Fix the wording in both places the claim appears.
- id: T02-02
  type: claim
  priority: low
  claim: 'No New York (1978); Eno first considered ten bands and ended with four, four songs each: The Contortions, Teenage Jesus and the Jerks, Mars and DNA.'
  original_wording: Originally considered 10 bands but ended up with 4 bands, 4 songs each.
  concern: Verify the history of the compilation, band list and date.
  task: Verify and add detail only if clearly sourced.
- id: T02-03
  type: claim
  priority: low
  claim: Former members include Bob Bert, Richard Edson (first drummer), Jim O'Rourke and Jim Sclavunos.
  original_wording: Former members- Bob Bert, Richard Edson (1st drummer), Jim O'Rourke, Jim Sclavunos.
  concern: O'Rourke is also called a full member from SYR3 later in the text. Check the lineup history, and the status of Sclavunos (the text also says he joined on drums in 1983).
  task: Verify the lineup history and make the text consistent.
- id: T02-04
  type: claim
  priority: low
  claim: Sonic Youth were deeply affected by seeing Minor Threat perform in May 1982 (Azerrad, p. 238).
  original_wording: Also, very affected when seeing a performance by Minor Threat in May 1982 (pg 238 in Azzerrad)
  concern: Check the date against Minor Threat's history and Azerrad's page.
  task: Verify date, page, and what Azerrad says.
- id: T02-05
  type: date
  priority: medium
  claim: In 1983 Moore began publishing the fanzine Killer and interviewed Ian MacKaye in the first issue.
  original_wording: 'Moore begins publishing a fanzine called Killer: interviews Ian MacKaye in the first issue'
  concern: The fanzine date and which issue had the MacKaye interview are uncertain. Also check the summer 1983 European tour, and Sclavunos on "Confusion Is Sex."
  task: Verify dates and details for 1983.
- id: T02-06
  type: claim
  priority: low
  claim: '"Death Valley ''69" (1985, directed by Richard Kern) was their first music video and features Bob Bert and Steve Shelley.'
  original_wording: The video for 'Death Valley '69' was filmed in 1985 was the first music video by Sonic Youth and was directed by Richard Kern. The video features the majority of the band in various states of bloody dismemberment... both the recently departed drummer Bob Bert, and then new member Steve Shelley.
  concern: This part of the original appears to be pasted from an encyclopedia entry rather than written by Micah.
  task: Verify the facts. Rewrite in Micah's plain voice or credit the source in a way suitable for a website.
- id: T02-07
  type: claim
  priority: medium
  claim: In January 1985 in Seattle, Bruce Pavitt paid $100 to use "Kill Yr. Idols" on Sub Pop 100.
  original_wording: January 1985- play in Seattle and meet Bruce Pavitt who pays $100 to use their song Kill Yr. Idols for a comp called Sub Pop 100
  concern: Sub Pop 100 was released in 1986. The date, place and amount need checking against Azerrad.
  task: Verify and fix.
- id: T02-08
  type: number-or-stat
  priority: low
  claim: Sister sold 60,000 copies and cracked the Village Voice Pazz & Jop top 20.
  original_wording: sold 60,000; cracks Village Voice Top 20 Jop and Pazz chart.
  concern: Verify the sales figure and poll position and year.
  task: Verify and fix.
- id: T02-09
  type: name-or-title
  priority: low
  claim: Experimental Jet Set (1994).
  original_wording: 1994 Experimental Jet Set, DGC
  concern: The full title may be longer ("Experimental Jet Set, Trash and No Star").
  task: Verify title and fix. Also check "Bull in the Heather" and the 1994 tour detail.
- id: T02-10
  type: attribution
  priority: medium
  claim: Greil Marcus coined "negation" in a 1983 Artforum piece on Sonic Youth; used by CCR, MC5, The Stooges and The Velvet Underground; a reaction against Petty, Mellencamp and Springsteen.
  original_wording: Pg. 249 they brought the concept of negation back into rock. Negation- refusal to ignore harsh realities, the world is not as it seems. Coined by Greil Marcus in 1983 Artforum piece on Sonic Youth. Employed by 60's bands CCR, MC5, The Stooges, and The Velvet Underground. Reaction against Tom Petty, John Mellencamp, Bruce Springsteen.
  concern: Attribution to Marcus and the Artforum piece should be checked against Azerrad. Whether this is Azerrad's claim or Micah's gloss is unclear.
  task: Check against Azerrad and Marcus's essay. Fix wording and attribution.
- id: T02-11
  type: name-or-title
  priority: low
  claim: The Year Punk Broke, a documentary of the 1991 tour with Nirvana.
  original_wording: 1991, The Year Punk Broke, documentary of their tour that year with Nirvana
  concern: 'The title is usually given as "1991: The Year Punk Broke". Unclear whether it was shown in class.'
  task: Verify title and details.
```

<!-- ===== TOPIC 02 END ===== -->

<!-- ===== TOPIC 03 START ===== -->

# Topic 3: Hardcore

```yaml agent-meta
topic: 3
slug: topic-03
title: Hardcore
syllabus_lessons: intro to hardcore; roots of the genres; skate culture.
syllabus_readings: '"American Hardcore" (course library).'
syllabus_film: '*American Hardcore.*'
old_links_from_original_notes:
- http://www.mrbalihai.com/goof/Flipside/Flipside_Story.html
- http://www.angelfire.com/ca/X8/Biography.html
- http://www.angelfire.com/ca/X8/X81977.html
- http://flipsidefanzine.com/PaisanoArticle.html
- http://flipsidefanzine.com/Framespage.html
- http://www.amazon.com/Best-Rodney-ROQ-Bingenheimer/dp/B0000032WI
- http://video.google.com/videoplay?docid=3053404663638592813
- http://www.youtube.com/watch?v=RCYddx4nyhA
```

## Overview

Sonic Youth were an idealistic influence on the underground. So what was the musical influence? Where did this new sound come from, who were its progenitors, and what were they doing to make it different?

In the early 1980s, kids were looking for a style with the ferocity of punk, minus the fashion of New Wave. Hardcore punk was the answer: a bastard child of punk rock. It took its influence from British and American punk bands, stripping bare the song structure and the fashion of the mainstream. This topic looks at where hardcore started in Southern California and the East Coast, the fanzines, record labels and radio shows that spread it, and the skateboard culture that grew up beside it.

## Listen and watch

* Bad Brains, "Pay to Cum" (1979)
* Fear, performing on *Saturday Night Live* [CONFIRM T03-04]
* A clip from *Dogtown*, chapters 20 and 21 (skateboard culture)
* Excerpts from an article about the fanzine *Flipside*, read in class
* Black Flag, "Nervous Breakdown"

## Films

* *American Hardcore* (DVD)

## Readings

* "American Hardcore" (course library) [CONFIRM T03-01]

Further reading: Blush, pp. 16 and 17 (the meaning of "hardcore," and a Greg Graffin quote about Rodney on the ROQ).

## Discussion questions

* Where Sonic Youth were considered more of an idealistic influence, what was the musical influence?
* Where did this new sound come from?
* Who were its progenitors, and what were they doing to make it different?

## Where the word comes from

The term "hardcore" is said to come from D.O.A.'s album *Hardcore 81*. It also took meaning from its common use, "to the most extreme." Hardcore punk "was the absolute most Punk" (Blush, p. 16). [CONFIRM T03-02]

## Southern California

Hardcore started in Southern California, out of a middle-class utopia. Across the Atlantic, British bands like 999 and Sham 69 were the underside of the Sex Pistols, and they released records like "If the Kids Are United." On the American side, The Ramones and The Germs were highly influential.

**The Germs** were Darby Crash, Pat Smear, Lorna Doom and seven different drummers, one of them named Cliff Hanger. Belinda Carlisle, later of The Go-Go's, also played with them for some time. They put out the bulk of their work on Slash Records. Their album *GI* came out on Slash in 1979, produced by Joan Jett. They reformed with Shane West as the lead singer. [CONFIRM T03-03]

**Slash Records** was founded by Bob Biggs in 1978 as an outgrowth of his zine of the same name. It also put out **Fear**'s *The Record* (1979). [CONFIRM T03-05] Fear's Lee Ving just wanted to piss everyone off. The band later featured a young bass player named Flea.

### Flipside

*Flipside* was a fanzine made in Whittier, California, east of Los Angeles. It was started by Al, Dean Dead, Larry Lash, X-8 and Pooch, students at Whittier High School and fans of punk rock, who were inspired by UK zines like *Sniffin' Glue*. X-8 was the school newspaper editor and an artist. It premiered in August 1977 at 25 cents, originally covering just the L.A. scene, and ran until around 2000. In the mid-1980s it began putting out Flipside Video and a BBS (Bulletin Board System): a chat room and video podcast. [CONFIRM T03-06]

### Rodney on the ROQ

L.A. DJ Rodney Bingenheimer hosted a show on KROQ on Sundays, from 8 pm to midnight.

## Skate culture

*Skateboarder* magazine focused on the area around San Diego and folded in 1982. [CONFIRM T03-07] *Thrasher* was San Francisco-based and covered skate culture along with hardcore. Brian "Pushead" Schroeder was its music editor, and his column *Puszone* was a minefield for new music.

"Skatecore" bands like The Scoundrels (Tony Alva) and Gang Green (Boston) started the term "Skate or Die!"

## The first hardcore album?

Two records are in the running. On the West Coast, The Middle Class's *Out of Vogue* (1978, Joke Records). On the East Coast, Bad Brains' "Pay to Cum" (1979, on Bad Brains' own label). [CONFIRM T03-08]

## Confirmation queue (Topic 3)

```yaml confirmation-queue
- id: T03-01
  type: attribution
  priority: medium
  claim: The syllabus reading titled "American Hardcore" is the same work cited elsewhere in the notes as "Blush."
  original_wording: 'Syllabus: "American Hardcore" (course library). Lecture notes: "Blush p. 16", "Blush pg. 17", "Blush P. 275" (Topic 6).'
  concern: 'The notes cite "Blush" but never give the title. The reading may be Steven Blush''s book *American Hardcore: A Tribal History* or an excerpt.'
  task: Identify the Blush work (full title, publisher, year, edition) and confirm that pages 16, 17 and 275 match the quoted claims. Update the readings entry with the full citation.
- id: T03-02
  type: claim
  priority: medium
  claim: The term "hardcore" is said to come from D.O.A.'s album Hardcore 81; also from common use "to the most extreme"; hardcore punk "was the absolute most Punk."
  original_wording: The term hardcore is said to come out of DOA's Hardcore 81 album, also took meaning from its common use "to the most extreme." Hardcore Punk "was the absolute most Punk." Blush p. 16
  concern: Verify the etymology claim and the quote against Blush p. 16.
  task: Check against Blush and other sources. Fix quote and wording.
- id: T03-03
  type: claim
  priority: medium
  claim: The Germs members (Darby Crash, Pat Smear, Lorna Doom, seven drummers incl. Cliff Hanger, Belinda Carlisle); GI (1979, Slash, produced by Joan Jett); reformed with Shane West.
  original_wording: Darby Crash, Pat Smear, Lorna Doom, and 7 different drummers one named cliff hanger. Belinda Carlisle (The Go Gos) also played with them for some time. Reformed recently with Shane West as the lead singer.
  concern: The reformation note is from about 2009 and needs a date. "Seven drummers" and other details need checking. Slash label dates are given elsewhere.
  task: Verify and date the reformation and the lineup claims.
- id: T03-04
  type: date
  priority: medium
  claim: Fear performed on Saturday Night Live (the notes say 1980).
  original_wording: performance on Sat Night Live in 1980
  concern: Fear's SNL appearance is commonly dated to 1981. The date is left out of the prose for now.
  task: Verify the date and add it to the text if confirmed.
- id: T03-05
  type: date
  priority: medium
  claim: Fear's The Record (1979, Slash Records).
  original_wording: Fear *The Record* 1979 on Slash Records
  concern: The album may be dated 1982. The original lists it under the Slash discussion with the year 1979.
  task: Verify the release year and label, and fix.
- id: T03-06
  type: claim
  priority: low
  claim: 'Flipside details: founders Al, Dean Dead, Larry Lash, X-8, Pooch; August 1977; 25 cents; ran until around 2000; Flipside Video and BBS in the mid-1980s.'
  original_wording: 'Started by Al, Dean Dead, Larry Lash, X-8 and Pooch students at Whittier High School... Aug. 77 premiered: 25 cents originally covered just the L.A. scene. Ran until around 2000... During the mid 80s Flipside began putting out Flipside Video and BBS (Bulliten Board System). Chat room, video podcast.'
  concern: Verify founders, dates and the BBS/video claims. "Video podcast" is an anachronistic phrase.
  task: Verify and fix. Rephrase "video podcast" if needed.
- id: T03-07
  type: date
  priority: low
  claim: Skateboarder magazine folded in 1982.
  original_wording: Skateboarder magazine focused on the area around San Diego, folded in 1982
  concern: The magazine's history includes a rename and relaunch; the fold date may be different.
  task: Verify and fix.
- id: T03-08
  type: claim
  priority: high
  claim: The Middle Class, Out of Vogue (1978, Joke Records); Bad Brains, "Pay to Cum" (1979, on Bad Brains' own label), as candidates for the first hardcore album.
  original_wording: 'The 1st hardcore album? West Coast: The Middle Class- Out of Vougue, 1978 on Joke Records. East Coast: Bad Brains- Pay to Cum, 1979 on Bad Brains records'
  concern: '"Out of Vogue" may be an EP, and "Pay to Cum" may be a single (not an album). Dates and labels need checking. The lyrics of "Pay to Cum" appear in the original notes and must NOT be reproduced.'
  task: Verify each release (format, year, label) and rewrite the heading and sentences accurately (for example "first hardcore record").
```

<!-- ===== TOPIC 03 END ===== -->

<!-- ===== TOPIC 04 START ===== -->

# Topic 4: Scenes and Labels

```yaml agent-meta
topic: 4
slug: topic-04
title: Scenes and Labels
syllabus_lessons: 'what is a scene; regional and major American scenes of the 1980s and the labels they spawned; Anatomy of a Scene: Berkeley, CA (924 Gilman, Operation Ivy, Fifteen, Maximumrocknroll).'
syllabus_readings: Kruse pp. 14-28; Sara Cohen, "Scenes"; the Sub Pop oral history; Mordam Records in Sinker; Operation Ivy and 924 Gilman (course library).
syllabus_film: (none recorded)
old_links_from_original_notes:
- http://www.dischord.com/history/
- http://www.desotorecords.com/downloads/index.shtml#ja
- http://www.furious.com/perfect/sst3.html
- http://www.dinosaurjr.com/
- http://www.touchandgorecords.com/info/index.php
- http://www.touchandgorecords.com/songs_videos/index.php#
- http://www.touchandgorecords.com/songs_videos/index.php
- http://en.wikipedia.org/wiki/Sub_Pop_Records
- http://www.subpop.com/about
- http://ogami.subpop.com/history/toc.html
- http://www.killrockstars.com/about/timeline.php
- http://podcast.krs5rc.com/
- http://www.krecs.com/html/info/
- http://www.krecs.com/html/info/#whatis
- http://www.kyledraws.com/
- http://www.lumberjackmordam.com/labels
- http://en.wikipedia.org/wiki/Mordam_Records
- http://www.924gilman.org/index.html
- http://www.wiretapmag.org/stories/17081
- http://lookoutrecords.com/blogcms/
- http://www.maximumrocknroll.com/mainpage/index.html
- http://www.skatedork.org/fifteen/releases/lucky.htm
- http://home.mchsi.com/~15xv/
- http://lookout.littletype.com/fifteen-lkb-grpcat.php#band_bio_full
- http://lookout.littletype.com/operation-ivy-lkb-grpcat.php
- http://www.punkrockcds.com/images/OperationIvy.jpg
- http://www.operationivy.com/index.php?l=1
- http://www.seeklyrics.com/lyrics/Operation-Ivy/Unity.html
```

## Overview

Often there is a specific sound associated with a scene. This topic asks how a scene differs from a subculture, and how we construct scene identity as opposed to subcultural identity. A scene can be talked about as a collective of people, as an ideal, or as a fashion and marketing statement, and it is worth asking whether any one of these is more authentic than the others.

We look at the major American scenes and record labels of the 1980s: Dischord in Washington, DC; SST in Southern California; Touch and Go in Michigan and Chicago; Sub Pop in Seattle; Kill Rock Stars and K Records in the Pacific Northwest; and Mordam, the distribution company that tied many of them together. Then we look closely at one scene, Berkeley, California, through the all-ages club 924 Gilman and two of its bands, Fifteen and Operation Ivy.

## Listen and watch

* S.O.A. (Dischord), played in class
* Operation Ivy, "Freeze Up" and "Unity"; "Bombshell" is also on the listening list
* Bad Religion, played in class
* Rancid, "Journey to the End of East Bay"
* Fifteen, "Welcome to Berkeley"

## Readings

* Holly Kruse, *Site and Sound*, pp. 14-28
* Sara Cohen, "Scenes"
* The Sub Pop oral history
* Mordam Records, in Sinker, *We Owe You Nothing*
* Operation Ivy and 924 Gilman (course library)

Further reading: the book of stories about 924 Gilman, with entries by Matt Freeman (p. 45), Brian Edge (p. 67) and Hawk (pp. 200-201), the last from the D.C. scene. [CONFIRM T04-01]

## Discussion questions

* What is a scene? Is it different from a subculture, and if so, how and why?
* Scene can be talked about as a collective of people, as an ideal, or as a fashion and marketing statement. Is any one of these more authentic?
* How does 924 Gilman represent the idea of a scene?
* What should we infer about the problems rising from labels being sued by their former bands? What does this say about a scene?
* The Berkeley scene is held up as a punk mecca, yet those involved often discount those claims. What does that say about the nature of a scene?
* What about all the rules? Don't we get involved with punk to avoid rules?
* The political angle taken by groups like *Maximum Rocknroll* and Hardline Straight Edge can be called right wing or conservative (resisting change, a moral agenda). Does this complicate the model of punk or counterculture in America? Or is it representative of the best aspects of American culture and politics?
* Counterculture versus subculture.

## What a scene is made of

A scene is made up of bands and music, a sense of community, a venue, a record store, and a zine or label. Punks often form a local scene, which can have as few as half a dozen or as many as thousands of members. A typical punk scene is made up of bands, fans, music venues, independent record labels, zine publishers, visual artists and clothing makers, with a small group of dedicated punks at the center and a more casual periphery around them. [CONFIRM T04-02]

## The labels

### Dischord (Washington, DC)

Dischord was started by Jeff Nelson and Ian MacKaye after the breakup of the Teen Idles. Its first release was the Teen Idles' *Minor Disturbance* EP, followed by Government Issue, S.O.A., Minor Threat and Youth Brigade. In October 1981 the label moved to Arlington, Virginia, to a place called the Dischord House, though its address is still Beecher Street, the house of Ian's parents in DC. [CONFIRM T04-03]

The label's own description says it was created in 1980 to document the music coming out of the Washington, DC punk community, and that it approached the label as a mission of documentation and a community-based entity, avoiding many industry-standard practices. It has put out the work of more than forty bands, and it pays royalties to the bands and supports the people who work for it, which is proof that this approach is possible. [CONFIRM T04-04] Notable bands include Beefeater, Fugazi, Jawbox and Q and Not U. Dischord created the model of independent record labels that many others followed.

### SST (Southern California)

SST was run by Greg Ginn of Black Flag. It was formed in 1978 in Long Beach, California, originally as "Solid State Transmitters," where Ginn worked with his father. Its first record was Black Flag's *Nervous Breakdown* EP. It became a prominent figure in L.A. punk, releasing the Descendents, the Minutemen and many more, and in the mid-1980s it began working with bands from outside L.A., including Hüsker Dü and Sonic Youth. [CONFIRM T04-05]

SST differed from labels like Touch and Go in several ways. It was not afraid to be unfashionable. Its owners were slightly older than the average punk, so they were more willing to show their pre-punk roots. Its roster was more varied and eclectic than other labels', thanks to the owners' love of everything from the Seeds and the Stooges to Hendrix, Black Sabbath, Hawkwind and Coltrane. And it was committed to musical and personal individualism, rejecting any attempt to link its bands to a larger "movement." [CONFIRM T04-06]

Notable bands include Black Flag, Dinosaur Jr., Hüsker Dü, the Meat Puppets and Soundgarden. Mike Watt, of the Minutemen, Stooges and fIREHOSE, said of Dinosaur Jr.: "Being an SST band had nothing to do with the sound, it just meant you knew there were going to be some weirdos involved." [CONFIRM T04-07] SST later got into legal disputes with many of its former bands, including Hüsker Dü, the Meat Puppets, Sonic Youth and Dinosaur Jr. [CONFIRM T04-08] Spot was the engineer on many SST releases.

### Touch and Go (Michigan, then Chicago)

Touch and Go was founded by Tesco Vee and Corey Rusk. It began in 1979 as a zine. Its first record was a 7-inch EP by the Necros, and it concentrated on hardcore bands from Michigan and Ohio: the Necros, the Meatmen and Negative Approach. In 1983 it added Big Black and the Butthole Surfers. It moved from Detroit to Chicago and released records by Slint, The Jesus Lizard, the Butthole Surfers and more. [CONFIRM T04-09]

Touch and Go was known for fair business practices: 50/50 deals, in which half the profits go to the artists after the label recoups promotion and production costs, and oral contracts, "handshake deals." It did all its own pressing and distribution. In 1990 it began manufacturing and distributing for other labels, including KRS, Thrill Jockey, Merge and Le Tigre. Corey and his wife founded the club Graystone in Detroit, which hosted many early hardcore bands through the 1980s; it was funded by Russ Gibb, who had run the Grande Ballroom in the 1960s, where the MC5 and The Stooges played. [CONFIRM T04-10] Notable bands include Big Black, Die Kreuzen, Pinback, Ted Leo and !!!.

### Sub Pop (Seattle)

Sub Pop began as a fanzine called *Subterranean Pop*, started by Bruce Pavitt in Olympia, Washington, in 1979, and became a label in 1986, with the *Sub Pop 100* compilation. Its early releases were Soundgarden and Mudhoney, and it was looked at as the grunge label. Later signings included Sunny Day Real Estate, Sebadoh, Iron and Wine, The Postal Service, The Shins, Holopaw and The Album Leaf. At the time of this course, Warner Music Group owned 49 percent of the label. [CONFIRM T04-11]

Its one platinum record was Nirvana's *Bleach*; its one gold record was The Postal Service's *Give Up*; and The Shins' "New Slang" went gold as a digital download. Holopaw, from Gainesville, Florida, released a self-titled EP in 2003, after their singer collaborated on Ugly Casanova's *Sharpen Your Teeth* with Isaac Brock of Modest Mouse. Notable bands also include Beat Happening, Mudhoney, Modest Mouse and Iron and Wine.

### Kill Rock Stars (Seattle and Olympia)

Kill Rock Stars was founded in 1991 by Slim Moon. Its first release was a spoken-word split with Slim and Kathleen Hanna. A compilation followed featuring Bikini Kill, the Melvins and Bratmobile, and the label is most notable for its riot grrrl releases. In 1995 it released Elliott Smith's self-titled album, in 1997 Sleater-Kinney, and later The Decemberists and The Gossip. Slim Moon left in 2006 to work for Nonesuch Records, and his wife runs the label now. [CONFIRM T04-12] Notable bands include Bikini Kill, The Decemberists, Elliott Smith, Team Dresch and Br. Danielson.

### K Records (Olympia, Washington)

K Records was founded in 1982 in Olympia as a cassette-only label by Calvin Johnson, who had worked at Sub Pop with Pavitt. Its first release was an EP, *Supreme Cool Beings*. [CONFIRM T04-13] It is the home of Beat Happening and Dub Narcotic, and groups that have worked with K include Built to Spill, Little Wings, The Make-Up, Mirah and Modest Mouse. Its motto is "exploding the teenage underground into passionate revolt against the corporate ogre since 1982." The label has been so influential in anti-corporate independent music and DIY punk culture, particularly in Olympia, that it was the subject of a documentary, *The Shield Around the K*, whose tagline is "Do It Yourself." [CONFIRM T04-14]

In 1987 K started a series of 7-inch records called "International Pop Underground," featuring underground artists from around the globe. Beat Happening are the foundation of the "twee pop" or "lo-fi" genre. Little Wings is Kyle Field.

### Mordam Records

Mordam was a distribution company founded in 1982. It served many independent labels, and Sinker's collection includes an interview with the people behind it. [CONFIRM T04-15]

## Case study: 924 Gilman

924 Gilman Street in Berkeley opened with its first show on December 31, 1986. Tim Yohannon of *Maximum Rocknroll* was one of its founders. It runs on a strict DIY code of ethics. All ages is one of its basic concerns, because there were so few all-ages venues in Northern California. There are three basic rules: no violence, no drugs, no alcohol. Patrons buy a membership card, which gives them a sense of ownership. The club is entirely volunteer-run, and membership meetings on the first and third Saturday of every month discuss issues, vote on them and make them law.

Bands must send their lyrics before playing there. No racist, homophobic or misogynistic band has ever played there. No band on a major label has played there either, and Green Day, Rancid and AFI are banned because of MTV videos or major label contracts. [CONFIRM T04-16] The music is mostly pop punk and hardcore, and past bands include Bad Religion, the Dead Kennedys, Jawbreaker, the Mr. T Experience, Operation Ivy, the Ramones, Samiam and more. [CONFIRM T04-17] Money is split half and half between the band and the club. The club is also used by political groups and for art shows and films.

Max Ravnard says, "DIY is about empowerment." That is part of how Gilman works, by giving power to the people. [CONFIRM T04-18]

## The Berkeley scene

### Lookout Records

Larry Livermore and David Hayes founded Lookout Records in 1987. It specialized in punk, pop punk and hardcore, and in the late 1980s and early 1990s the Lookout name would sell records on its reputation. Its bands included Crimpshrine, Fifteen, Isocracy, the Mr. T Experience, Operation Ivy, Samiam and Screeching Weasel. At the time of this course the label was in legal trouble with many former bands over royalties, and Green Day and others had recalled their master tapes. [CONFIRM T04-19]

### *Maximum Rocknroll*

*Maximum Rocknroll* is possibly the most widely recognized fanzine of the punk subculture. Its coverage is wide-ranging, and it has lasted as the scene has changed. Tim Yohannon founded it in 1982 as a newsprint booklet in the compilation *Not So Quiet on the Western Front* (Alternative Tentacles). It has a strong focus on international scenes, it is all-volunteer, non-profit and strictly independent, and it will not interview bands that are on or distributed by major labels.

### Fifteen

Fifteen were Jeff Ott, John Ogle, Chris Flanagan and Mark Moreno. Jeff Ott and Aaron Cometbus came from Crimpshrine, one of the most important Northern California bands of the 1980s. [CONFIRM T04-20] Their subject matter typically includes homelessness, drug abuse, needle exchange, environmental destruction and the government's use of counter-intelligence measures to violate activists' civil rights. They self-released the 12-inch *Swain's First Bike* in 1991. *Lucky* (1999, Subcity Records) is their most influential album: very political and to the point.

### Operation Ivy

Operation Ivy were Jesse Michaels, Tim Armstrong, Matt Freeman and Dave Mello. They played ska-punk from 1987 to 1989. They debuted in 1987 on a *Maximum Rocknroll* compilation, *Turn It Around*, and in 1988 signed with Lookout and put out the *Hectic* EP. There was pressure to sign with a major label, because the genre was growing in popularity at the time. They put out *Energy* in 1989, and their last show was on May 28, 1989, which was also Green Day's first show as a band. [CONFIRM T04-21] In all, they played 185 shows and recorded 32 songs. Their lyrics and tone portray a youthful desire for social justice and a strong distrust of mainstream or conformist culture. *Energy* was reissued on November 6, 2007, on Hellcat Records, a division of Epitaph. [CONFIRM T04-22]

## Confirmation queue (Topic 4)

```yaml confirmation-queue
- id: T04-01
  type: name-or-title
  priority: medium
  claim: A book of stories about 924 Gilman, with entries by Matt Freeman (p. 45), Brian Edge (p. 67) and Hawk (pp. 200-201, from the D.C. scene).
  original_wording: Read some stories from the book. Matt Freeman pg 45. Brian Edge pg 67 favorite memories of Gilman. Hawk pg. 200-201 from DC scene
  concern: The book is not named in the original.
  task: Identify the book (title, editor, publisher, year) and verify the contributor names and pages.
- id: T04-02
  type: source-text
  priority: medium
  claim: A paragraph describing punk local scenes.
  original_wording: Punks often form a local scene, which can have as few as half a dozen, or as many as thousands of members. A typical punk scene is made up of bands, fans, and music venues, as well as independent record labels, zine publishers, visual artists, and clothing makers...
  concern: This passage appears to be pasted from an encyclopedia article on the punk subculture, not Micah's wording.
  task: Find the original, confirm, and either rewrite it fully in Micah's voice or attribute it properly.
- id: T04-03
  type: claim
  priority: medium
  claim: 'Dischord: started by Jeff Nelson and Ian MacKaye after the Teen Idles; first release Teen Idles'' Minor Disturbance EP; then Government Issue, S.O.A., Minor Threat, Youth Brigade; October 1981 move to Arlington, VA (Dischord House); address still Beecher Street (Ian''s parents'' house).'
  original_wording: Formed after the breakup of the Teen Idles. First release Teen Idles Minor Disturbance EP. Then Government Issue, SOA, Minor Threat and Youth Brigade. Oct 1981 moved to Arlington VA Dischord House. Address still Beecher Street, Ians parents house in DC.
  concern: The original is confusing about which place is the label's address, and the order of releases. Check the label's history.
  task: Verify and rewrite clearly.
- id: T04-04
  type: source-text
  priority: medium
  claim: Dischord's self-description (founded 1980; documents the DC punk community; over forty bands; avoids many industry-standard practices; pays royalties).
  original_wording: 'From the website: Dischord Records was created in 1980 to document the music coming out of the Washington, D.C. punk community. The label has put out the work of over 40 bands... Because we have tried to approach the label as a mission of documentation...'
  concern: Pasted from the label's website and now paraphrased; "over forty bands" is dated.
  task: Verify against the label's history page and update or date the figure. Decide whether a short, credited quote is better than the paraphrase.
- id: T04-05
  type: claim
  priority: low
  claim: 'SST: formed 1978 in Long Beach as "Solid State Transmitters"; Black Flag Nervous Breakdown EP first record; Descendents, Minutemen; mid-1980s bands outside L.A.'
  original_wording: Formed 1978 Long Beach, CA. Originally "Solid State Transmitters" Greg Ginn worked with his father there. Black Flag "Nervous Breakdown" EP, first record released. Became a prominent figure in LA punk releasing The Descendants, The Minutemen and many more. mid-80s began to do work with bands outside of LA, Husker Du, Sonic Youth.
  concern: Check the founding year and place, the origin of the name, and the "first record" claim. "Descendants" in the original is presumably the Descendents.
  task: Verify and fix.
- id: T04-06
  type: source-text
  priority: medium
  claim: A comparison of SST with Touch and Go (unfashionable, older owners, eclectic roster, rejection of any "movement").
  original_wording: 'SST also had some important differences from the likes of Touch & Go: firstly, SST wasn''t afraid to be completely unfashionable... From furious.com/perfect/sst3.html'
  concern: Paraphrased from an online history of SST by another writer. Includes opinions about Black Flag's looks, which are left out.
  task: Locate the source, check the claims, and either credit it or rewrite so that it reflects Micah's lecture point.
- id: T04-07
  type: quote
  priority: medium
  claim: 'Mike Watt on Dinosaur Jr.: "Being an SST band had nothing to do with the sound, it just meant you knew there were going to be some weirdos involved."'
  original_wording: Mike Watt ... laughs, "Greg Ginn must've liked their long hair or the guitar jams. I know the Dino guys told me their whole goal in life was to make an SST record... Being an SST band had nothing to do with the sound, it just meant you knew there were going to be some weirdos involved...."
  concern: Verify the quote and the source (probably Azerrad or an interview).
  task: Find the source and check the exact wording.
- id: T04-08
  type: date
  priority: medium
  claim: SST later got into legal disputes with many former bands (Hüsker Dü, Meat Puppets, Sonic Youth, Dinosaur Jr.).
  original_wording: Recently SST has gotten into legal issues with a lot of its former bands. Husker Du, Meat puppets, Sonic Youth, Dino Jr.
  concern: '"Recently" refers to about 2009.'
  task: Verify and give years and facts.
- id: T04-09
  type: claim
  priority: medium
  claim: 'Touch and Go history: founded by Tesco Vee and Corey Rusk, began 1979 as a zine, first record by the Necros, 1983 Big Black and Butthole Surfers, moved from Detroit to Chicago.'
  original_wording: 'Tesco Vee and Corey Rusk... Began 1979 as a zine. First record by Necros, a 7'''' EP. Concentrated on Michigan Ohio hardcore bands: Necros, The Meatmen, and Negative Approach. 1983 Big Black, Butthole Surfers... From detriot it moved to Chicago...'
  concern: Verify the founding story, dates and the order.
  task: Verify and fix.
- id: T04-10
  type: claim
  priority: medium
  claim: Corey Rusk and his wife founded the club Graystone in Detroit, funded by Russ Gibb of the Grande Ballroom.
  original_wording: Corey and his wife founded the club Graystone which hosted many of the early hardcore bands throughout the 80s. Funded by Russ Gibb who ran the Grande Ballroom in the 60s where bands like MC5 and The Stooges played.
  concern: Verify the claim, the club's name and the ownership.
  task: Verify and fix.
- id: T04-11
  type: claim
  priority: medium
  claim: 'Sub Pop details: Subterranean Pop zine in 1979 in Olympia; label in 1986; Sub Pop 100; Warner owned 49 percent.'
  original_wording: Bruce Pavitt, Olympia WA zine called Subterannean Pop. 1979 fanzine, 1986 label... 49% owned by Warner Music Group
  concern: The Warner stake figure is as of about 2009; the label's early history (location, dates) needs checking.
  task: Verify and date the Warner figure. Verify the rest.
- id: T04-12
  type: claim
  priority: medium
  claim: 'Kill Rock Stars: founded 1991 by Slim Moon; first release a spoken-word split with Kathleen Hanna; 1995 Elliott Smith; 1997 Sleater-Kinney; Slim Moon left in 2006 for Nonesuch; his wife runs the label.'
  original_wording: Slim Moon (Earth). Founded 1991. First release was a spoken word split with Slim and Kathleen Hanna... 1997 Sleater-Kinney... 2006 Slim Moon left the Company to work for Nonesuch records, his wife runs it now.
  concern: Check each date, and the claim about the current head of the label. "Slim Moon (Earth)" in the original also appears in the Metal topic as a member of Earth; check.
  task: Verify and date or correct.
- id: T04-13
  type: claim
  priority: medium
  claim: 'K Records: founded 1982 in Olympia as a cassette-only label by Calvin Johnson; Johnson worked at Sub Pop with Pavitt; first release an EP, Supreme Cool Beings.'
  original_wording: Calvin Johnson worked at Sub/Pop with Pavitt. Founded 1982 in Olympia, WA as a cassette only label. First release Supreme Cool Beings, EP
  concern: Verify. The first K release may have been a cassette compilation.
  task: Verify and fix.
- id: T04-14
  type: source-text
  priority: medium
  claim: K's motto; the documentary The Shield Around the K (tagline "Do It Yourself").
  original_wording: The K motto is "exploding the teenage underground into passionate revolt against the corporate ogre since 1982." ... subject of a documentary directed by Heather Rose Dominic entitled The Shield Around the K, with a tagline of "Do It Yourself". From wikipedia
  concern: Pasted from an encyclopedia entry. The director's name is dropped from the prose; verify the film's director, year and tagline.
  task: Verify and decide whether to name the director.
- id: T04-15
  type: claim
  priority: medium
  claim: Mordam was a distribution company founded in 1982; Sinker's collection includes an interview with its founders.
  original_wording: '"Mordam Records- distro company founded in 1982" (reading: Mordam Records in Sinker)'
  concern: The original has almost nothing beyond the founding date. The prose guesses at what the Sinker reading covers.
  task: Check the Sinker chapter and the label's history. Replace this paragraph with accurate content (who founded it, what it did, which labels it distributed).
- id: T04-16
  type: claim
  priority: medium
  claim: '924 Gilman house rules: lyrics must be sent in advance; no racist, homophobic or misogynistic band has played; no major-label band has played; Green Day, Rancid and AFI are banned.'
  original_wording: Bands must send lyrics before playing there. No rascist, homophobic, or misogynistic band has ever played there. Also, no band on a major label has played there. Green Day, Rancid, and AFI are banned due to MTV videos and/or major label contracts.
  concern: Sweeping claims ("ever," "banned") should be checked and dated.
  task: Verify against the club's own rules and histories and soften or date as needed.
- id: T04-17
  type: claim
  priority: low
  claim: Past bands at 924 Gilman include Bad Religion, the Dead Kennedys, Jawbreaker, the Mr. T Experience, Operation Ivy, the Ramones, Samiam.
  original_wording: 'Past bands include: Bad religion, DK, Jawbreaker, Mr T. experience, Op Ivy, The Ramones, Samiam and more.'
  concern: The Ramones and the Dead Kennedys appearing at Gilman is questionable. Bad Religion's status, given that the club bans major-label bands, also needs checking.
  task: Verify each band's connection with the club.
- id: T04-18
  type: name-or-title
  priority: low
  claim: Max Ravnard says, "DIY is about empowerment."
  original_wording: 'Max Raynard says "DIY is about empowerment." (source: wiretapmag.org)'
  concern: The name is spelled differently in the original; the speaker and source need checking.
  task: Find the interview and verify name, role and quote.
- id: T04-19
  type: date
  priority: medium
  claim: 'Lookout Records: founded 1987 by Larry Livermore and David Hayes; bands; legal troubles over royalties and masters recalled by Green Day and others.'
  original_wording: 1987 by Larry Livermore and David Hayes... recently gotten into legal issues with a lot of its former bands over royalties. Green Day and more recalled their master tapes.
  concern: '"Recently" refers to about 2009; check the founding date and founders.'
  task: Verify and date.
- id: T04-20
  type: claim
  priority: low
  claim: 'Fifteen: Jeff Ott, John Ogle, Chris Flanagan, Mark Moreno; Jeff Ott and Aaron Cometbus came from Crimpshrine.'
  original_wording: Jeff Ott, John Ogle, Chris Flanagan, Mark Moreno. Jeff Ott and Aaron Cometbus from Crimpshrine- one of the most important NoCal bands of the 80's
  concern: The original implies that Ott and Cometbus were in Fifteen; check the lineup and whether Cometbus was a Fifteen member, and Ott's role in each band.
  task: Verify and clarify.
- id: T04-21
  type: date
  priority: medium
  claim: Operation Ivy's last show was May 28, 1989, which was also Green Day's first show; 185 shows and 32 songs; debuted 1987 on the MRR comp "Turn It Around"; 1988 Lookout and the Hectic EP.
  original_wording: put out Energy in 1989, last show may 28th 1989. This was also Green Days first show as a band. Op Ivy had played 185 shows and recorded 32 songs.
  concern: Verify the dates and counts.
  task: Verify and fix.
- id: T04-22
  type: source-text
  priority: medium
  claim: Op Ivy's lyrics and tone portray a youthful desire for social justice and a strong distrust of mainstream or conformist culture; Energy reissued November 6, 2007, on Hellcat.
  original_wording: The lyrics and tone of Operation Ivy's music portray a youthful desire for social justice and a strong distrust of mainstream or conformist culture. Energy reissued Nov 6th 2007 on Hellcat Records- a division of Epitaph
  concern: The first sentence appears to be taken from an encyclopedia entry.
  task: Verify the reissue date and label and rewrite the first sentence in Micah's voice or credit it.
```

<!-- ===== TOPIC 04 END ===== -->

<!-- ===== TOPIC 05 START ===== -->

# Topic 5: Politics and Communication

```yaml agent-meta
topic: 5
slug: topic-05
title: Politics and Communication
syllabus_lessons: political culture of the 1980s; Dead Kennedys and Minor Threat; radical vs. personal politics; zine culture.
syllabus_readings: Jello Biafra and Noam Chomsky in Sinker; Minor Threat in Azerrad; Dead Kennedys and Minor Threat (course library).
syllabus_film: '*The Shield Around the K.*'
old_links_from_original_notes:
- http://en.wikipedia.org/wiki/Punk_subculture#Ideology
- http://www.mediahistory.umn.edu/timeline/1980-1989.html
- http://www.conservativepunk.com/index.asp
- http://profile.myspace.com/index.cfm?fuseaction=user.viewprofile&friendid=200868858
- http://www.youtube.com/watch?v=iVrTW7AUkoM
- http://www.bbc.co.uk/radio1/documentaries/060829_straightedge.shtml
- http://www.youtube.com/watch?v=rNJ9eSqVhKk
- http://www.youtube.com/watch?v=ZHZMp7o3Py4&mode=related&search
```

## Overview

America is a country obsessed with its politics, and for good reason: democracy gives us the opportunity to choose. This topic asks how that choice filters down through different levels of society, and what it meant for the underground in the 1980s. The important shift for this subculture, again a reflection of the 1960s counterculture, is the emphasis on cultural change that would in turn change the political structures of the nation. The mere formation of an "underground" in opposition to a "mainstream" is a culturally progressive movement that affected the political ideas of everyone in it. The "damn the man" attitude carries over into politics.

We look at two kinds of politics in hardcore punk. The first is the outward-facing, satirical politics of the Dead Kennedys and their singer, Jello Biafra. The second is the "personal politics" of Minor Threat, and the straight edge movement that grew out of their songs.

## Listen and watch

* Dead Kennedys, "Kill the Poor" (played in class)
* Dead Kennedys, "A Child and His Lawn Mower" and "Buzzbomb"
* The Teen Idles, "Get Up and Go" (played in class)
* Minor Threat, "Seeing Red" and "Straight Edge"
* A video interview with Jello Biafra, discussed in class
* A radio documentary on straight edge

## Films

* *The Shield Around the K*, a documentary about K Records (see Topic 4) [CONFIRM T05-01]

## Readings

* Jello Biafra and Noam Chomsky, in Sinker, *We Owe You Nothing*
* Minor Threat, in Azerrad, *Our Band Could Be Your Life*
* The Dead Kennedys and Minor Threat (course library)

## Discussion questions

* Can radical culture replace political practice? ("We are punk, we are underground, we are different, and therefore the world should change.")
* Jello Biafra says, "People have to remain curious and get their brain-activity food from other places besides punk." What does this look like in action? Where else?
* "I'm down with both radical resistance and trying to do what can be done through the system." Is this an "un-punk" thing to encourage?
* What are the implications of what Biafra says on page 29 of the Sinker interview?
* On page 32, Biafra equates *Maximum Rocknroll* with fundamentalist Christians. Is that fair?
* In the 1980s there was no organized left. Was hardcore punk the leftist movement?
* What are the political implications of underground music, especially in the early 1980s?
* What stereotypes about the politics of punk do you know? How accurate are they?

## Politics in the early underground

The political context of the 1980s is described in Topic 1: the Misery Index, Reagan, the New Conservatism, Reaganomics and the Yuppies.

In the punk subculture there are often stereotypical associations of political leanings that may or may not be accurate: anarchist (punk of the 1970s), left wing, radical. These labels fit some people and are complicated to define for others, especially in the political world after 1980. The meaning of "left wing" and "right wing" varies considerably between countries and at different times. Broadly, the right wing is linked to moral and social conservatism, law and order, and religion, and the left wing is linked to redistributing wealth toward the less successful and to secularism. The right is more often linked to the idea of social equity, and the left to the idea of social equality. [CONFIRM T05-03]

The radicals in the underground ran the gamut of politicization, from anarchy to patriotism. They were most often associated with left-wing politics: opposition to war and support for equality, racial and gender. The 1980s underground took up the process of writing a history of rebellion through action, not just words. It took the best parts of the 1960s and combined them with the attitude of 1970s punk.

Negation gave way to dissent. Negation, a cultural concept, informed a lifestyle of dissent, which is a political ideology, and it gave the underrepresented a voice.

## The Dead Kennedys

The Dead Kennedys formed in 1978: East Bay Ray, Jello Biafra, Klaus Flouride and 6025. [CONFIRM T05-04] Their technique is the same as Stephen Colbert's. Satire and a sarcastic tone run through many of their songs, along with various literary references.

Their first single was "California Über Alles." It outlines a bizarre hippie-fascist vision for America, in which Biafra's "suede denim secret police" kill uncool people in "organic poison gas" chambers. It illustrates his concern with the dilution of the radical tendencies of the 1960s by "yuppies" and their representatives, such as, one presumes, California governor Jerry Brown. [CONFIRM T05-05] The Alternative Tentacles label was founded to put out this record. [CONFIRM T05-06]

The second single, a 7-inch released in 1980, was "Holiday in Cambodia." The song attacks Eastern totalitarianism, Western complacency, and the direct relation between the two through American military intervention. It gives a satirical view of young, self-righteous Americans and contrasts that lifestyle with a brutal depiction of Pol Pot's Cambodia. [CONFIRM T05-05]

Their first album, *Fresh Fruit for Rotting Vegetables* (1980), is a staple of American punk and a swan song for political punk. It was lumped in with hardcore, but the music itself isn't similar to hardcore. It includes "Kill the Poor," "Let's Lynch the Landlord" and "California Über Alles."

Next came *In God We Trust, Inc.*, with artwork by Winston Smith. By now the group had become a de facto political force, pitting itself against rising elements of American social and political life such as the religious right, Ronald Reagan and the idle rich. Songs include "Moral Majority" and "We've Got a Bigger Problem Now."

With *Frankenchrist* (1985), the band got into legal trouble over the artwork in the packaging. This was the height of their conflict with the forces they had opposed for so long, notably the PMRC, headed by Tipper Gore. [CONFIRM T05-07] *Bedtime for Democracy* followed in 1986, and the band broke up after it. Cover art was always an important part of the Dead Kennedys' approach to the consumer.

### Jello Biafra

Biafra, the band's lead singer, ran for mayor of San Francisco in fall 1979. [CONFIRM T05-08] As the Sinker collection puts it: "The DK's were instrumental in providing American punk with a leftist political philosophy that transcended the nihilism, ignorance, and stupidity of the early hardcore scene… DK's tried to encourage people to think for themselves by making it safe, however uncomfortable, to question the limits of countercultural politics and anti-establishment behavior." [CONFIRM T05-09]

### Skinheads

Very few people embraced the skinhead style without being affected by its politics. For most of these kids it was shock value, and it often reflected youthful anti-socialist inclinations rather than a coherent racialist doctrine. [CONFIRM T05-10] There were Nazi skins and anti-Nazi skins, right-wing skins and left-wing skins. Every action requires an equal and opposite reaction: the politicization of hardcore polarized it, with the extreme left pulling against the extreme right, and may have been its undoing.

## Personal politics: Minor Threat and straight edge

Minor Threat epitomized one of hardcore's major strengths: it was underground music by, for and about independent-minded kids. They were really inspired by Ted Nugent, who didn't smoke, drink or do drugs. [CONFIRM T05-11]

### The Teen Idles

Ian MacKaye met Jeff Nelson when he set off a pipe bomb outside their school. [CONFIRM T05-12] They saw the Cramps in January 1979. [CONFIRM T05-13] Before that came White Boy, a local father-and-son band that played proto-punk songs. [CONFIRM T05-14] The Teen Idles were Ian, Jeff, Georgie Grindle and Nathan Strejek. The themes of their music were what was happening around them: high school and friendships.

They did two demo sessions, in February and April 1980, and in August 1980 took a bus to California to play. Their last show was on November 6, 1980, at the 9:30 Club. [CONFIRM T05-15] At that show they first suggested putting X's on their hands, to show they were underage. It became the mark of straight edge. Their *Minor Disturbance* 7-inch EP was released in January 1981 as Dischord #1. They sent it to Tesco Vee at the *Touch and Go* fanzine, and "Get Up and Go" was number one for a few weeks on the *Maximum Rocknroll* radio show. [CONFIRM T05-16]

### Minor Threat

Minor Threat were formed out of the ashes of the Teen Idles: Ian, Jeff, Lyle Preslar and Brian Baker. Their first show was on December 17, 1980, opening for Bad Brains. MacKaye says, "I was 19 and about to leave the ranks of teenagers and I was furious." [CONFIRM T05-17] They debuted as Dischord #3, an untitled 7-inch recorded in May 1981. [CONFIRM T05-18]

Their themes were less about outside politics and more about personal politics. These were middle-class and upper-middle-class kids, not much worried about "the system," but concerned with how politics affected their lifestyles. Ian: "I didn't know enough about politics to really sing about them. And I didn't know enough about the world to really sing about it. But I knew enough about MY world to sing about it." And: "Free choice and independent thinking were the real point of straight edge. FLEX YOUR HEAD!" Controlling things, not having them control you. [CONFIRM T05-19]

In August 1981 they toured with Youth Brigade and recorded *In My Eyes*, a four-song EP. At Christmas 1981 they played what was meant to be their final gig, because Preslar was moving away. [CONFIRM T05-20] They reformed in April 1982, with Baker becoming the second guitarist and Steve Hansgen taking over on bass. They recorded *Out of Step* in January 1983, and in spring 1983 did a 49-day, 33-show tour of the U.S. and Canada. [CONFIRM T05-21]

By the summer of 1983, regional pride in DC had become territorial, a matter of turf. The band started to come apart, not only because of the breakdown of their scene but also because of the feelings of the band members toward Ian. They felt he was too preachy and was losing sight of fun. The rest of the band was getting into U2 and also wanted to go more mainstream, in sound and ideals. They played their last show on September 23, 1983, and recorded the *Salad Days* single on December 14, 1983.

## Straight edge

Straight edge was one of the most influential social, cultural and political movements of the 1980s underground. It came out of two songs written and performed by Minor Threat: "Straight Edge" and "Out of Step."

The basic idea is abstinence from alcohol, tobacco and drugs. Sometimes it also includes caffeine, vegetarianism, veganism, and abstaining from promiscuity. [CONFIRM T05-22] The reasons for being edge are philosophical, social or religious, and often just to become an active member of the scene. Some people kept it as a personal ideal; others used it as a militaristic code of solidarity.

**Boston** is the example of the second kind. SSD and Al Barile formed the first legitimate hardcore crew there. Barile took what was going on in DC to the next step. The "Boston Crew" is named on the cover of SSD's album *The Kids Will Have Their Say* (1982), and the crew would travel with the band and represent the area. Boston was the most violent scene, with pig piling, and it is where straight edge got its militant edge: people would knock beers out of other people's hands. It was a closed-off, elitist scene. [CONFIRM T05-23]

Large straight edge scenes grew up in other cities: Salt Lake City (the Monster Crew), Louisville (the Courage Crew) and Tampa (the Chaos Crew).

## Confirmation queue (Topic 5)

```yaml confirmation-queue
- id: T05-01
  type: claim
  priority: low
  claim: The Shield Around the K is the film for this topic.
  original_wording: 'Syllabus lists "Film: The Shield Around the K" with the politics topic; the lecture notes mention the film only in the K Records discussion (Topic 4).'
  concern: The notes do not say when the film was shown.
  task: Confirm the film (director, year, runtime) and whether it belongs with Topic 4 or Topic 5. Ask Micah if it cannot be settled.
- id: T05-02
  type: gap
  priority: medium
  claim: The syllabus lists "zine culture" under this topic, but the lecture notes for this topic do not cover it.
  original_wording: '(syllabus lesson list: political culture of the 1980s; Dead Kennedys and Minor Threat; radical vs. personal politics; zine culture)'
  concern: Zine material appears in other topics (Flipside in 3, Maximum Rocknroll in 4, riot grrrl and queercore zines in 11, a zines-to-blogs section in 9).
  task: Do not invent content. Note in the change log whether to cross-reference those topics or drop "zine culture" from this topic's description.
- id: T05-03
  type: source-text
  priority: medium
  claim: A paragraph defining "left wing" and "right wing" (moral and social conservatism, law and order, religion versus redistribution and secularism; social equity versus social equality).
  original_wording: The meaning of left-wing and right-wing varies considerably between different countries and at different times, but broadly speaking, it can be said that the right wing is often linked to moral and social conservatism...
  concern: Appears to be pasted from an encyclopedia article.
  task: Identify the source. Rewrite in Micah's voice or credit it. Check the equity/equality sentence.
- id: T05-04
  type: claim
  priority: low
  claim: 'The Dead Kennedys formed in 1978: East Bay Ray, Jello Biafra, Klaus Flouride and 6025. Their technique is the same as Stephen Colbert''s.'
  original_wording: Dead Kennedys – same technique as Stephen Colbert. Formed in 1978 by East Bay Ray, Jello Biafra, Klaus Flouride and 6025
  concern: Check the founding lineup. The Colbert comparison is a short classroom aside, kept as written.
  task: Verify the lineup (including who 6025 is). Suggest clearer wording for the Colbert comparison (satire delivered straight), if appropriate.
- id: T05-05
  type: source-text
  priority: medium
  claim: Descriptions of "California Über Alles" and "Holiday in Cambodia" (themes and satire).
  original_wording: Outlines a bizarre hippie-fascist vision for America, in which his "suede denim secret police" kill un-cool people with "organic poison gas" chambers... The song appears to be an attack upon both Eastern totalitarianism, Western complacency...
  concern: Both descriptions appear to be pasted from encyclopedia entries and include lyric excerpts, which are omitted here.
  task: Find the sources, verify the claims, and rewrite in Micah's voice (or credit). Do not add lyrics beyond short credited quotes.
- id: T05-06
  type: claim
  priority: low
  claim: The Alternative Tentacles label was founded to put out "California Über Alles."
  original_wording: Alternative Tentacles label founded to put out this album.
  concern: The original says "this album" under the discussion of the first single. The label's first release was the single.
  task: Verify and fix.
- id: T05-07
  type: claim
  priority: medium
  claim: 'Frankenchrist (1985): legal trouble over the artwork in the packaging; the PMRC, headed by Tipper Gore.'
  original_wording: The band got involved in legal issues over the artwork included in the packaging. This represents the height of their interaction with the forces that were against for so long as the PMRC headed by Tipper Gore.
  concern: The original sentence is garbled. The legal case is usually associated with an insert (a poster), and the prosecutors were not the PMRC itself.
  task: Verify the history and rewrite accurately.
- id: T05-08
  type: date
  priority: low
  claim: Biafra ran for mayor of San Francisco in fall 1979.
  original_wording: Fall '79 ran for mayor of San Fran
  concern: Verify.
  task: Verify and add the outcome only if useful.
- id: T05-09
  type: quote
  priority: medium
  claim: A quote about the Dead Kennedys providing American punk with a leftist political philosophy, from the Sinker collection.
  original_wording: From Sinker "The DK's were instrumental in providing American punk with a leftist political philosophy that transcended the nihilism, ignorance, and stupidity of the early hardcore scene… DK's tried to encourage people to think for themselves by making it safe, however uncomfortable, to question the limits of countercultural politics and anti-establishment behavior."
  concern: Who wrote it (Sinker's introduction to the interview?) and the exact wording and page.
  task: Check against Sinker and fix the attribution and quote.
- id: T05-10
  type: source-text
  priority: medium
  claim: A paragraph on skinheads (few embraced the style without being affected by politics; shock value; anti-socialist inclinations rather than coherent racialist doctrine).
  original_wording: Very few embraced the style without being affected by the politics. For most of these kids it was a shock value factor, also it often reflected youthful anti-socialist inclinations rather than coherent racialist doctrine.
  concern: The second sentence appears to be from an encyclopedia entry, and the generalization is broad.
  task: Find the source. Check the claim and rewrite or credit.
- id: T05-11
  type: claim
  priority: medium
  claim: Minor Threat were really inspired by Ted Nugent, who didn't smoke, drink or do drugs.
  original_wording: Really inspired by Ted Nugent who didn't smoke, drink or do drugs.
  concern: Verify with MacKaye interviews and Azerrad; check the accuracy of the claim about Nugent in the 1970s.
  task: Verify and fix or soften.
- id: T05-12
  type: claim
  priority: medium
  claim: MacKaye met Jeff Nelson when he set off a pipe bomb outside their school.
  original_wording: MacKaye met Jeff Nelson when he set off a pipe bomb outside their school.
  concern: Surprising claim. Who set off the pipe bomb, and is this accurate?
  task: Verify with Azerrad and interviews. If the story is garbled, correct it or cut it and say why.
- id: T05-13
  type: date
  priority: low
  claim: They saw the Cramps in January 1979.
  original_wording: They saw the cramps Jan 1979
  concern: Verify the date and who "they" refers to.
  task: Verify.
- id: T05-14
  type: claim
  priority: low
  claim: White Boy was a local father-and-son band that played proto-punk songs.
  original_wording: White Boy- local father-son band proto-punk songs.
  concern: Unclear what the original means (a band before the Teen Idles? whose?).
  task: Identify the band and its relationship to MacKaye, or cut the sentence.
- id: T05-15
  type: date
  priority: medium
  claim: The Teen Idles' last show was November 6, 1980, at the 9:30 Club; this is where they suggested the X's on their hands.
  original_wording: Last show Nov 6, 1980 at the 930 club. It was at this sow that they first suggested the x's on their hands to show they were underage.
  concern: Verify the date, venue, and the X's origin story, which has several versions.
  task: Verify with Azerrad and other sources and rewrite carefully.
- id: T05-16
  type: claim
  priority: medium
  claim: 'Dischord #1 was the Teen Idles'' Minor Disturbance (January 1981); it was sent to Tesco Vee at Touch and Go; "Get Up and Go" was number one for a few weeks on the Maximum Rocknroll radio show.'
  original_wording: 'Recorded Teen Idles-Minor Disturbance 7'''' EP released in Jan. 81, Dischord #1. Sent it to Tesco Vee at Touch and Go fanzine. Get up and Go, number one for a few weeks on maximumrockandroll radio show'
  concern: Verify catalog numbers, dates and the radio chart claim.
  task: Verify and fix.
- id: T05-17
  type: date
  priority: medium
  claim: Minor Threat's first show was December 17, 1980, opening for Bad Brains; the lineup was Ian, Jeff, Lyle Preslar and Brian Baker; MacKaye's "I was 19..." quote.
  original_wording: 1st show Dec 17th 1980, opening for Bad Brains. MacKaye says – I was 19 and about to leave the ranks of teenagers and I was furious
  concern: Verify date, lineup and quote source (probably Azerrad).
  task: Verify and fix.
- id: T05-18
  type: claim
  priority: medium
  claim: 'Minor Threat debuted as Dischord #3, an untitled 7-inch recorded in May 1981.'
  original_wording: 'Minor Threat debuted Dischord #3 an untitled 7'''' recorded in May 81'
  concern: Verify the catalog number and recording date.
  task: Verify and fix.
- id: T05-19
  type: quote
  priority: medium
  claim: 'MacKaye: "I didn''t know enough about politics..."; "Free choice and independent thinking were the real point of straight edge. FLEX YOUR HEAD!"'
  original_wording: Ian – "I didn't know enough about politics to really sing about them... But I knew enough about MY world to sing about it." "Free choice and Independent thinking were the real point of straight edge. FLEX YOUR HEAD!" Controlling things not having them control you.
  concern: The second quote has no speaker or source in the original (it may be a paraphrase). Verify both.
  task: Find sources and exact wording. Attribute correctly.
- id: T05-20
  type: date
  priority: low
  claim: August 1981 tour with Youth Brigade and the In My Eyes EP; a "final gig" at Christmas 1981 because Preslar was moving away.
  original_wording: Aug. 81 tour with Youth Brigade, also recorded In My Eyes -4 song EP. Christmas 81 final gig as Preslar was moving away. (met steve albini at Northwestern)
  concern: Verify dates. The original also mentions that Preslar met Steve Albini at Northwestern, left out here.
  task: Verify and fix. Decide whether the Albini detail belongs.
- id: T05-21
  type: date
  priority: medium
  claim: Reformed April 1982; Baker second guitarist; Steve Hansgen on bass; Out of Step recorded January 1983; spring 1983 49-day, 33-show tour.
  original_wording: Reformed April 82. Baker becomes second guitarist and Steve Hansgen takes over Bass. Recorded Out Of Step in Jan. 83. Spring 83 49 day, 33 show tour of U.S. and Canada.
  concern: Verify the lineup change, recording dates and tour length.
  task: Verify and fix.
- id: T05-22
  type: claim
  priority: low
  claim: Straight edge sometimes also includes caffeine, vegetarianism, veganism, and abstaining from promiscuity.
  original_wording: Sometimes also includes caffeine, vegetarianism and veganism, and non-sexual promiscuity.
  concern: '"Non-sexual promiscuity" in the original is probably a slip for sexual promiscuity.'
  task: Verify and fix.
- id: T05-23
  type: claim
  priority: medium
  claim: 'Boston: SSD and Al Barile formed the first legitimate hardcore crew; the Boston Crew named on the cover of The Kids Will Have Their Say (1982); the most violent scene; straight edge got its militant edge there.'
  original_wording: Boston- SSD and Al Barile. First formation of legitimate hardcore crew. Al took what was going on in DC to the next step. Called "Boson Crew" on the cover of SSD The Kids Will Have Their Say album 1982... In Boston SXE got its balls, people would knock beers out of peoples hands. It was a closed off, elitist scene.
  concern: Verify the claims; "first" and "most violent" are strong. The original also uses a crude phrase paraphrased here.
  task: Verify and soften where needed. Check the other cities and crew names (Monster Crew, Courage Crew, Chaos Crew).
```

<!-- ===== TOPIC 05 END ===== -->

<!-- ===== TOPIC 06 START ===== -->

# Topic 6: DIY, Indie and the Business of Music

```yaml agent-meta
topic: 6
slug: topic-06
title: DIY, Indie and the Business of Music
syllabus_lessons: 'DIY: what it is and how it works; what is indie; Indie vs. Major, "the Great Debate"; Fugazi; pop culture vs. the underground.'
syllabus_readings: 'Steve Albini and Ian MacKaye in Sinker; Fugazi in Azerrad; Kruse, "Indie vs. Major," pp. 41-50 and 64-69; Stormy Shepherd; Albini, "The Problem with Music." Listening: NPR interview on diyordie.org.'
syllabus_film: (none recorded)
old_links_from_original_notes:
- http://www.stardoom.com/punk_flyers/see_artwork/slayer_pushead.gif
- http://www.warui.com/stefan/winston_smith-boot_face-med.jpg
- http://www.steakmtn.com/work/0305/
- http://www.vbs.tv/player.php?bctid=494769642
- http://www.youtube.com/watch?v=zcaNBK2gw2Y&feature=related
- http://www.lyricsdir.com/fugazi-suggestion-lyrics.html
- http://www.youtube.com/watch?v=RNUxrUtbnzY&mode=related&search
- http://dischord.com/release/45
- http://www.youtube.com/watch?v=B3ty04JdTBA&mode=related&search
```

## Overview

This topic is about the principles of the underground: DIY, the difference between a subculture and a scene, and what it means to be independent. DIY (do it yourself) is one of the main dividers between punk and the underground. For the underground, the point was not to destroy the system but to create your own system by your own rules, and to do it well. Independence is at the core of the great debate of the subculture's growth over the past thirty years: indie versus major.

We close with Fugazi, the quintessential underground band, which lives by the principles of the underground.

## Listen and watch

* The NPR interview on diyordie.org
* The Teen Idles, "Get Up and Go" (as an example of DIY as a sound)
* Dead Legs, track 6 [CONFIRM T06-01]
* Examples of DIY visual art: a Pushead flyer for Slayer, Winston Smith's "Boot Face," and work by Steak Mountain
* Fugazi, "Suggestion," "Repeater," "Styrofoam," "Merchandise," "Turnover" and "And the Same"
* From the listening list: Fugazi, "Suggestion" and "Full Disclosure" [CONFIRM T06-02]

## Films

* *Instrument* (Jem Cohen's film about Fugazi; see Topic 8)

## Readings

* Steve Albini and Ian MacKaye, in Sinker, *We Owe You Nothing*
* Fugazi, in Azerrad, *Our Band Could Be Your Life*
* Holly Kruse, "Indie vs. Major," pp. 41-50 and 64-69
* Stormy Shepherd [CONFIRM T06-03]
* Steve Albini, "The Problem with Music"
* Amy Spencer, *DIY: The Rise of Lo-Fi Culture* [CONFIRM T06-04]

## Discussion questions

**On DIY**

* What is your definition of DIY?
* What does DIY sound like? Can there be a DIY sound?
* What does DIY look like? Can there be DIY art? Is all art DIY?
* What does DIY as a lifestyle entail philosophically? Is it going against the norm for the sake of purity?
* How does the web change DIY? (Art Chantry: "The only venue left for DIY is the computer.")
* DIY artists do not know what else to do, and do not often think of themselves as artists. How does this change the output? Is it art?
* How are the DIY ethic and DIY culture related, or different?

**On subculture and scene**

* What do members of a subculture do? How does it work? How does one get in the club?
* Is a scene different from a subculture? If so, how and why? Is any one of the ways of talking about a scene more authentic than the others?
* What is underground culture? What is indie culture?

**On indie versus major**

* Do we believe that selling out is real and important? Where did the idea come from?
* How do issues of control, artistic and philosophical, affect one's decision to be part of a record label? What does Ian MacKaye say about this?
* In what situations could going major be valuable? Does it change one's identification with "indie"?
* What effect does the decision have on the band, the community, the label and the scene?
* What about money? People who make music for a living need to make money.
* How does this change the idea of being underground? Does becoming part of mass culture take away from the influence a band could have by staying indie? Is influence the primary factor in "indie" music?
* Are there other principles by which the underground works and constructs its identity?

## DIY

### A historic construct in three phases

DIY can be understood as a historic construct with three phases. First is **necessity**: you did it yourself because there was no other way. Second is **statement**, having to do with output: artistic, visual, musical, spoken word. Third is **aesthetic**: a lifestyle of being more authentic than something else.

### What DIY sounds like, looks like, and is

As music: the Teen Idles' "Get Up and Go" is an example. "You keep talking 'bout talent. What do you know? Instead of studying theory, we're gonna get up and go!" As an art form: the flyers, album covers and posters of the underground. As a lifestyle: going against the norm for the sake of purity.

### According to the authors

* Sinker's introduction calls DIY "the foundation that the entire culture is built upon."
* Azerrad (p. 6) calls it necessity more than statement.
* Blush describes "a new definition of musical success: in non economic terms… objective-oriented, community based culture" (p. 275), and self-reliant, anti-corporate individuals becoming entrepreneurs. [CONFIRM T06-05]

### According to the artists

* "DIY was our version of punk." Mike Watt of the Minutemen (Azerrad, p. 77).
* "One aspect of DIY is that you really have to do it yourself. It's work!" Ian MacKaye (Sinker, p. 19).
* "The only venue left for DIY is the computer." Art Chantry (Sinker, p. 189).
* "I was expected to get involved… not all of it was music, a point that is often missed. What the scene really did was inspire and attract talented people of all stripes." Jack Rabid, editor of *The Big Takeover*. [CONFIRM T06-06]

### DIY as an ethic and as a culture

The DIY ethic is the ethic of being self-reliant and doing things yourself, as opposed to paying others to do them. It questions the supposed uniqueness of the expert's skills and promotes the ability of ordinary people to learn to do more than they thought possible. The culture of DIY is different: it is a political movement focused on being responsible for one's surroundings.

The punk DIY ethic also extends to daily life: how groups and individuals avoid contributing to institutions they see as exploitative. That includes converting cars to run on biodiesel or vegetable oil, learning bicycle repair, repairing and modifying clothes, starting gardens and dumpster diving. In a broad sense DIY is an economic model, and skill sharing is central to it. [CONFIRM T06-07]

DIY artists do not know what else to do, and often do not think of themselves as artists. For this subculture, DIY is the currency, the means, the end, your identity, and it provides a sense of authenticity. Truth, purity, authenticity.

## Subculture and scene

Culture, in the textbook sense, is the strategy by which humans adapt to the natural environment: a set of learned, shared behaviors transmitted from one generation to the next by non-biological means. Culture is shared (across sex, gender, age, class and occupation), learned (eating is a biological need; culture dictates how that need is met), based on symbols (the most important cultural symbol is language), and integrated (all aspects of culture tend to function as an interrelated whole).

A subculture is a set of people with a set of behaviors and beliefs, which may be distinct or hidden, that differentiate them from the larger culture to which they belong. If the subculture is characterized by systematic opposition to the dominant culture, it may be described as a counterculture. Subcultural capital is the cultural knowledge and commodities members acquire, which raise their status and help differentiate them from members of other groups. The study of subculture often consists of the study of the symbolism attached to clothing, music and other visible markers, and of how members of the dominant culture interpret those symbols. [CONFIRM T06-08]

A scene may be different from a subculture. It can be talked about as a collective of people, as an ideal, or as a fashion and marketing statement. A scene is made up of bands and music, a sense of community, a venue, a record store, and a zine or label.

## Independent, indie and the great debate

The meaning of "indie" has changed and morphed over time. From film, it means outside the Hollywood mainstream, concerned with art over entertainment, aimed at an audience with "higher" artistic sensibilities than the average consumer. Words associated with it: offbeat, awkward humor, quirky, eccentric, unconventional, experimental, weird. It often deals with the underside of American culture: homosexuality, violence, religion in a different light, complex relationships, unhappy endings. [CONFIRM T06-09]

In plain terms, independent means working outside of some superstructure. In film that is Hollywood. In music it is the music business: corporate art, major labels, pop culture.

### Indie versus major

Music history can almost always be seen as growing out of independent minds. Rock music grew out of blues and jazz, and grassroots movements like folk in the sixties. American labels like Motown, Chess and Atlantic were all once indies (Azerrad, p. 5). Dischord created the model of independent record labels that many others followed. Quite a few bands moved from indies to majors and received a lot of criticism for it, including Sonic Youth, Hüsker Dü, The Replacements and more.

The mainstream plays the role of "the other." The concept of otherness is integral to understanding identities, because people construct roles for themselves in relation to an "other" as part of a fluid process of action and reaction. At stake is the integrity and quality of the music.

Art is a product of its time. Going indie, or "jamming econo," as the Minutemen put it, was a lash against the prosperity of the time. They were not saying they wanted to be poor, but that the excess was unnecessary.

Ian MacKaye and Steve Albini are giants of the underground subculture, and two of the most outspoken about their ideals of being, staying and living independent. The debate between indie and major is at the core of the subculture's growth over the last thirty years. Indie and DIY changed from a lifestyle to a mentality, from a business model to a moral and ethical model, from a philosophy to an ideology.

## Fugazi

Fugazi are the quintessential underground band that lives by the principles of the underground. The members are Ian MacKaye, Guy Picciotto, Joe Lally and Brendan Canty, all born in the early 1960s, which led to their appreciation of the political. [CONFIRM T06-10]

### Roots in Washington, DC

Fugazi formed out of various early-1980s DC bands, including Rites of Spring and Embrace. Revolution Summer in 1985 was the turning point. Rites of Spring's album was recorded in February 1985 by Ian MacKaye, and the band played the Punk Percussion Protest Against Apartheid on June 21 (Azerrad, p. 381). MacKaye founded Embrace that summer with the lineup of the defunct DC band Faith. Picciotto and MacKaye felt that the personal was political. These bands broadened the spectrum of what counted as good music beyond strict hardcore. [CONFIRM T06-11]

Fugazi are tied deeply to the DC scene. Ian MacKaye is half of Dischord Records. On September 24, 1986, Ian, Joe Lally and Colin Sears practiced as a three-piece. Fugazi formed in 1987, with a first show on September 3. They were a three-piece at first, then added Guy Picciotto, a friend who had toured with them, as singer and guitarist. [CONFIRM T06-12] Their musical influences are said to be Ted Nugent, Jimi Hendrix, The Beatles and jazz. Their style is a mix of punk, hardcore, soul and noise, with rhythm sections using reggae and dub.

### Ethics

Fugazi are well known in indie circles for their ethics. Throughout their career they have kept ticket prices at five dollars, played all-ages shows, sold CDs for only ten dollars, and never made any merchandise. They will not give interviews to magazines that advertise cigarettes or alcohol. They are often concerned that such things will overshadow their music. [CONFIRM T06-13]

### The story

In January 1988 they made their first tour, mainly through Michigan, followed by a one-month U.S. tour that spring. They played Olympia, Washington, and founded a cross-national connection with that scene; Dave Grohl moved from the DC band Scream to Nirvana. During this tour they solidified their commitment to the band. [CONFIRM T06-14]

They released their first EP, *Fugazi*, in late 1988, recorded at Inner Ear Studios by Ted Nicely. The song "Suggestion" became one of their best known, about objectification from a female perspective. [CONFIRM T06-15] After that came a three-month European tour, staying in squats. The *Margin Walker* EP was recorded at the end of that tour at Southern Studios in London, in December 1988. They tracked a whole album but, tired from the tour, trimmed it to an EP, released in 1989. The two records were later combined into *13 Songs* in September 1989. "And the Same" is a song condemning force as an instrument of policy. [CONFIRM T06-16]

After this Guy became the second guitar player, and the band began writing as a group, improvising and using new methods like texture, dissonance, feedback and harmonics. *Repeater* was recorded in September 1989 at Inner Ear with Ted Nicely and released in 1990, a classic post-punk album. [CONFIRM T06-17] Songs include "Repeater" and "Styrofoam." It is a mesh of various influences, very clean and organic, with a noticeable call and response taken from hip hop, which was growing at the time. It is practically a concept album about the notion that one can effect social change through what one buys ("Merchandise"). They toured in support of *Repeater* all of 1990.

*Steady Diet of Nothing* (1991) was recorded in January with Don Zientara. After touring extensively, it took them time to work out how to record. It has some non-political songs, about genealogical heritage ("Latin Roots") and the disintegration of friendships ("Long Division"). It was released in the Year Punk Broke and gained Fugazi notoriety. [CONFIRM T06-18]

*In on the Kill Taker* (1993) reached number 153 on the Billboard 200 and has some of the band's most aggressive songs. Rolling Stone voted them best live band. *Red Medicine* (1995) is claimed by many to be their experimental album. On that tour they played worldwide, and by touching down in New Hampshire and Alabama completed all fifty U.S. states. [CONFIRM T06-19] *End Hits* came out in 1998. In 1999 came *Instrument*, a documentary and art film by a good friend, Jem Cohen. A soundtrack was also released that year, containing old demos and unreleased versions of songs, not any of the live material from the film. *The Argument* followed in 2001, with *Furniture* plus two songs released as well. Both albums feature Jerry Busher, who plays second drums and percussion on various songs. [CONFIRM T06-20]

### What they contributed to the underground aesthetic

* **Righteousness and integrity.** They pounded it into the underground: dogmatic in word and deed, all about being fair.
* **Music as community.** They held to the idea that music can be a vital, inspiring part of a community and can change society, with an emphasis on community as outside the mainstream, legitimate and self-supporting.
* **DIY made personal.** They personified DIY for many people, operating entirely outside the music business and often outside the underground as well.
* **A new sound.** Its roots are in hardcore sing-alongs, funk and reggae bass and drums, and American progressive originality.
* **A new relationship with the crowd.** A concert was no longer simple entertainment but an act to be done together. They defied the "laws" of space and created a new environment (Azerrad, p. 393). [CONFIRM T06-21]
* **Local politics.** They connected politically with their own community through the Positive Force group, led by Mark Andersen, author of *Dance of Days*. [CONFIRM T06-22]
* **A simple life.** Vegetarianism, recycling, DIY.
* **Staying indie.** They avoided major labels to keep full control of their output, and spread the wealth by choosing who to tour with and who to support.

## Confirmation queue (Topic 6)

```yaml confirmation-queue
- id: T06-01
  type: name-or-title
  priority: low
  claim: Dead Legs, track 6.
  original_wording: Dead Legs- track 6 (listed with Teen Idles' 'Get Up and Go' as examples of the DIY sound)
  concern: Unclear what "Dead Legs" refers to (band, album or compilation).
  task: Identify the band or release, or ask Micah. Remove if it cannot be identified.
- id: T06-02
  type: claim
  priority: low
  claim: The listening list assigns Fugazi "Suggestion" and "Full Disclosure" to this topic; three more songs (Bad Religion "I Want to Conquer the World" and "Pink Rock Song"; Rancid "Ruby Soho") were tentatively assigned to topics 6 or 4.
  original_wording: listening list rows 15, 18, 32, 34, 60 (likely topic 6?)
  concern: Placement of the Bad Religion and Rancid songs is a guess.
  task: Leave out unless a connection is found. Report in the change log.
- id: T06-03
  type: name-or-title
  priority: low
  claim: A reading called "Stormy Shepherd."
  original_wording: 'Syllabus: "Stormy Shepherd" (listed with the Albini and Kruse readings)'
  concern: Probably a person's name, possibly misspelled; unclear what the reading is.
  task: Identify the reading (author, title) or ask Micah.
- id: T06-04
  type: name-or-title
  priority: low
  claim: 'Amy Spencer, DIY: The Rise of Lo-Fi Culture.'
  original_wording: 'Notes: "Read Amy Spencer pg." and quotes "Amy Spencer - DIY: rise of lo-fi" (Topic 11)'
  concern: The notes give an incomplete reference (no page). The full title and publisher are assumed.
  task: Verify the full citation and decide whether it is a reading for this topic.
- id: T06-05
  type: quote
  priority: medium
  claim: 'Blush: "a new definition of musical success: in non economic terms… objective-oriented, community based culture" (p. 275); self-reliant, anti-corporate individuals becoming entrepreneurs.'
  original_wording: '"a new definition of musical success: in non economic terms… objective-oriented, community based culture." Blush P. 275. Self-reliant, anti-corporate individuals becoming entrepreneurs. Blush'
  concern: Verify the quote and page against Blush (see T03-01).
  task: Verify and correct.
- id: T06-06
  type: quote
  priority: low
  claim: Jack Rabid, editor of The Big Takeover, on the scene inspiring and attracting talented people of all stripes.
  original_wording: '"I was expected to get involved… not all of it was music, a point that is often missed..." Jack Rabid editor of The Big Takeover'
  concern: The source of the quote is not given.
  task: Find the source, check the quote.
- id: T06-07
  type: source-text
  priority: medium
  claim: Descriptions of the DIY ethic, DIY culture and the DIY punk ethic (biodiesel, bicycle repair, gardens, dumpster diving, skill sharing, an economic model).
  original_wording: The DIY ethic (do it yourself ethic) refers to the ethic of being self-reliant... The DIY punk ethic can also extend to how any group or individual applies DIY political stances to daily life... Thus DIY is in a broad sense an economic model. Skill sharing is a central aspect of DIY culture and practice. Wiki
  concern: Pasted from an encyclopedia article (the original is marked "Wiki"). Now paraphrased.
  task: Find the article, check the paraphrase, and rewrite in Micah's voice or credit the source.
- id: T06-08
  type: source-text
  priority: medium
  claim: Definitions of culture, subculture, counterculture and subcultural capital.
  original_wording: 'Culture: textbook- strategy by which humans adapt... Subculture- In sociology, anthropology and cultural studies, a subculture is a set of people with a set of behaviors and beliefs... subcultural capital as the cultural knowledge and commodities acquired by members of a subculture...'
  concern: Pasted from a textbook (culture) and an encyclopedia (subculture); "subcultural capital" is Sarah Thornton's term.
  task: Identify the sources and the concept's originator. Rewrite or credit.
- id: T06-09
  type: source-text
  priority: low
  claim: 'The film sense of indie: outside the Hollywood mainstream, art over entertainment, an audience with "higher" artistic sensibilities.'
  original_wording: From film- outside of the Hollywood mainstream, concerned with art over entertainment, aimed at an audience with "higher" artistic sensibilities than the average consumer.
  concern: May be from an encyclopedia entry.
  task: Check the source.
- id: T06-10
  type: claim
  priority: medium
  claim: Fugazi's members were all born in the early 1960s.
  original_wording: Members- Ian MacKaye, Guy Picciotto, Joe Lally, Brendan Canty. All born in the early 60s which lead to their appreciation of the political.
  concern: Verify birth years. The causal claim ("which led to...") is Micah's.
  task: Verify the birth years and adjust.
- id: T06-11
  type: claim
  priority: medium
  claim: 'Revolution Summer: Rites of Spring''s album recorded February 1985 by Ian MacKaye; Punk Percussion Protest Against Apartheid on June 21 (Azerrad p. 381); MacKaye founded Embrace that summer with the lineup of Faith.'
  original_wording: ROS album recorded Feb 1985 by Ian MacKaye. ROS played the Punk Percussion Protest Against Apartheid on June 21, p.381 Azzerrad. MacKaye founded Embrace that summer with the lineup of defunct DC band Faith
  concern: Verify dates, the page reference and the Embrace lineup.
  task: Verify each.
- id: T06-12
  type: date
  priority: medium
  claim: On September 24, 1986, Ian, Joe Lally and Colin Sears practiced as a three-piece; Fugazi formed in 1987 with a first show on September 3; Guy Picciotto joined as singer and guitarist.
  original_wording: Ian, Joe Lally and Colin Sears Sep 24 1986 practiced as 3 piece. Formed in 1987, first show Sep 3rd. Three piece at first, then added Guy as singer/guitarist.
  concern: Verify the dates and the drummer's identity (Brendan Canty is listed as a member).
  task: Verify and fix.
- id: T06-13
  type: claim
  priority: medium
  claim: 'Fugazi ethics: five-dollar shows, all ages, ten-dollar CDs, no merchandise, no interviews with magazines that advertise cigarettes or alcohol.'
  original_wording: throughout their career they have had $5 prices and played all ages shows, sold CDs for only $10, and never made any merchandise. They will not conduct interviews with magazines that advertise cigarettes or alcohol. Often they are concerned that such things will overshadow their music.
  concern: Verify each claim; "never made any merchandise" is sweeping. The last sentence ("such things") is ambiguous.
  task: Verify and fix, or soften.
- id: T06-14
  type: claim
  priority: medium
  claim: First tour in January 1988 through Michigan; a one-month U.S. tour that spring; Olympia; "Dave Grohl moved from DC band Scream to Nirvana."
  original_wording: Jan. 1988 first tour mainly through Michigan. Followed by a 1 month US tour that spring. Played Olympia WA and founded the cross-national connection with that scene. Dave Grohl moved from DC band Scream to Nirvana
  concern: The link between the Olympia visit and Grohl's move is unclear and may be Micah's shorthand. Verify.
  task: Verify and rewrite the connection, or drop it.
- id: T06-15
  type: claim
  priority: medium
  claim: The first EP, Fugazi, was released in late 1988, recorded at Inner Ear Studios by Ted Nicely; "Suggestion" is about objectification from a female perspective.
  original_wording: Released 1st EP Fugazi in late 1988. The song Suggestion became one of their most well-known, about objectification from a female perspective. recorded at Inner Ear Studios by Ted Nicely
  concern: Verify the release date and the engineer. Check the description of the song with sources. Lyrics must not be reproduced.
  task: Verify and fix.
- id: T06-16
  type: date
  priority: high
  claim: '"And the Same" is a song condemning force as an instrument of policy.'
  original_wording: '"And the Same" – song condemning force as instrument of policy; Bush Desert Storm'
  concern: The original ties the song to Bush and Desert Storm (1990-91), but "And the Same" appeared on a 1989 record. This is likely an anachronism or a looser connection. Also check Margin Walker's dates (recorded December 1988, released 1989) and the 13 Songs compilation (September 1989).
  task: Check the song's release and its subject, and fix. Verify the dates for Margin Walker and 13 Songs.
- id: T06-17
  type: date
  priority: medium
  claim: Repeater was recorded in September 1989 at Inner Ear with Ted Nicely and released in 1990; they toured all of 1990; a call and response taken from hip hop; "practically a concept album" about social change through what one buys.
  original_wording: Repeater- recorded Sep 1989 at Inner Ear with Ted Nicely. classic post-punk album. Released 1990... Noticeable call and response taken from hip hop... Practically a concept album about the notion that one can effect social change by what one buys.
  concern: Verify dates. The hip-hop claim and the concept-album claim are interpretive.
  task: Verify the dates and engineer. Say whether the interpretations are supported in the literature or should be framed as opinion.
- id: T06-18
  type: date
  priority: medium
  claim: Steady Diet of Nothing (1991) was recorded in January with Don Zientara; released in the Year Punk Broke; non-political songs include "Latin Roots" and "Long Division."
  original_wording: 1991 Steady Diet of Nothing Jan recorded with Don Zientara... Released in the Year Punk Broke, gained Fugazi notoriety
  concern: Verify the recording and release dates (the album may have been recorded earlier and released in 1991), and the song descriptions.
  task: Verify and fix.
- id: T06-19
  type: claim
  priority: medium
  claim: In on the Kill Taker (1993) reached number 153 on the Billboard 200; Rolling Stone voted them best live band; Red Medicine (1995); the 1995 tour completed all fifty states.
  original_wording: '1993 In on the kill taker- #153 on Billboard 200... voted best live band by Rolling Stone... 1995 Red Medicine... on this tour they played worldwide and with touching down in New Hampshire and Alabama completed all 50 US states.'
  concern: Verify chart position, the Rolling Stone claim (which year and poll), and the 50-states claim.
  task: Verify each and fix.
- id: T06-20
  type: claim
  priority: low
  claim: Instrument (1999) is a documentary and art film by Jem Cohen with a soundtrack of demos and unreleased versions; The Argument (2001) with Furniture plus two songs; Jerry Busher plays second drums on both.
  original_wording: 1999 Instrument comes out. documentary/art film by a good friend Jem Cohen. a soundtrack was also released that year... 2001 Argument. Furniture + 2 songs, also released. Both albums feature Jerry Busher...
  concern: Verify dates, the Furniture release and Busher's credits.
  task: Verify and fix.
- id: T06-21
  type: quote
  priority: medium
  claim: A concert was an act to be done together; they defied the laws of space (Azerrad, p. 393).
  original_wording: Changed the way the crowd interacts with the band. No longer simple entertainment, it was an act to be done together. P. 393 "people in concert crowds…" Defied "laws" of space and created a new environment
  concern: The original has a truncated quote ("people in concert crowds…").
  task: Find the quote on Azerrad p. 393 and add it, correctly cited, or confirm the paraphrase.
- id: T06-22
  type: name-or-title
  priority: low
  claim: Positive Force, led by Mark Andersen, author of Dance of Days.
  original_wording: Positive Force group led by Mark Anderson (Dance of Days author.)
  concern: Name spelling; Dance of Days has two authors.
  task: Verify and fix, with correct author credits.
```

<!-- ===== TOPIC 06 END ===== -->

<!-- ===== TOPIC 07 START ===== -->

# Topic 7: Metal

```yaml agent-meta
topic: 7
slug: topic-07
title: Metal
syllabus_lessons: underground metal (major genres, bands, musical influences); the Melvins.
syllabus_readings: Deena Weinstein, "Heavy Metal's Proud Pariahs" (in Greenberg); Keith Kahn-Harris, "The Scene and Transgression"; online interviews, reviews and fan sites.
syllabus_film: '*Metal: A Headbanger''s Journey.*'
old_links_from_original_notes:
- http://www.tartareandesire.com/bands/images/anthrax.jpg
- http://www.anus.com/metal/about/history/#metal_history_5b
- http://www.extrememp3s.com/
- http://www.puredeath.org/kcuf/
- http://blogs.guitarworld.com/metalkult/wp-content/uploads/2007/07/possessedgroup.jpg
- http://www.youtube.com/watch?v=Ia7vWGsTBFo&feature=related
- http://www.youtube.com/watch?v=9Z1IGjr2cT0&feature=related
- http://sdyrgas.files.wordpress.com/2007/06/holymountain.jpg
- http://www.youtube.com/watch?v=vtnG6EHh1N4
- http://www.seldonhunt.com/indexx.html
- http://www.themelvins.net/
- http://myspace.com/themelvins
- http://vienna.metblogs.com/archives/images/2007/04/vie_g_melvins.jpg
- http://en.wikipedia.org/wiki/Sonic_Youth
- http://en.wikipedia.org/wiki/Dave_Grohl
- http://en.wikipedia.org/wiki/Scream_%28band%29
- http://en.wikipedia.org/wiki/Krist_Novoselic
- http://cdn.last.fm/coverart/300x300/2447836.jpg
- http://ec1.images-amazon.com/images/I/41TKRH44D4L._AA240_.jpg
- http://ec2.images-amazon.com/images/P/B000001BDX.01._AA300_SCLZZZZZZZ_.jpg
- http://www.youtube.com/watch?v=gqctEypTXkY
- http://www.themelvins.net/wiki/index.php?title=Maximum_Rock_n_Roll_Interview_1988
- http://www.themelvins.net/pics/posters/index.htm
```

## Overview

Between 1983 and 1984, heavy metal went from about an eight percent to about a twenty percent share of all recordings sold in the U.S. Magazines devoted to the genre were launched, including *Kerrang!* in 1981 and *Metal Hammer* in 1984, along with a host of fan journals. In 1985, *Billboard* declared that the metal audience was no longer the exclusive domain of male teenagers: it had become older, younger and more female. [CONFIRM T07-01]

So if metal is so popular, how does it fit our definition of "underground"? Metal was one of the first underground musics to span the mainstream and the underground at the same time. This topic looks at the underground end of the genre, extreme metal and its four subgenres (thrash, death, black and doom), and then at the Melvins, a band that represents underground metal differently from the extreme bands: for them it is a chance to be weird, and sometimes just plain bizarre, for the sake of enjoying the music.

## Listen and watch

* Deicide and Morbid Angel (death metal), played in class
* Possessed, "Death Metal" (1984)
* Sunn O))) (drone doom), a video
* The Melvins, "Ligature" and "Joan of Arc"
* From the listening list: Floor, "Scimitar"; Earth, "An Inquest Concerning Teeth"

## Films

* *Metal: A Headbanger's Journey*

## Readings

* Deena Weinstein, "Heavy Metal's Proud Pariahs," in Greenberg, *Youth Subcultures*
* Keith Kahn-Harris, "The Scene and Transgression"
* Online interviews, reviews and fan sites

## Discussion questions

**Underground metal**

* If metal is so popular, how does it work with our definition of "underground"?
* Why study extreme metal?

**The Melvins**

* How do the Melvins deal with the indie versus major debate?
* How do you think this band is accepted and understood in the underground subculture?
* In what ways do they stretch the mold?
* How do they represent underground metal? Do they?

**After *Metal: A Headbanger's Journey***

* Origins: metal grew out of blues and classical music. How does this fit with the music we have studied so far? What about the claims hardcore musicians made that they were doing the first "non-blues" music? How do these influences transfer across the variety of genres metal offers?
* Culture: Chuck Klosterman says in the film, "The Replacements (college rock) say you are different because you are smart. Metal says you are not different, you are a part of a huge mass of people." How does this work with our model of intellectualism and aggression? Does metal fall entirely on the aggressive side?
* Stereotypes play a huge role in the media's conception of metal. What are they, and were they addressed, challenged or upheld in our discussions?
* Cannibal Corpse album covers are referred to as "art." Do we agree? Can this art be acceptable in a responsible society?
* Gender and sexuality: does metal present a hyper-masculine image? If this music reflects the "underside" or "dark side" of American culture, what does it say about gender roles? How do women in metal challenge or reinforce gender norms?
* Religion: Slayer's album *God Hates Us All*; the singer says, "God doesn't hate. It was a great title." Why the direct interaction with religion? Compare religious themes in pop music, such as "What If God Was One of Us?" Is it the same kind of relationship? What elements of religion work well with metal, and is there a boundary that should not be crossed? Satanism is a common association with metal: is it the devil's music? Think about the historical context it grew up against.

## Why study extreme metal?

The sociologist Keith Kahn-Harris, author of *Extreme Metal: Music and Culture on the Edge*, gives five reasons. [CONFIRM T07-02]

* **It is influential.** "Extreme Metal has provided a crucial if sometimes unacknowledged motor of innovation within metal. It is increasingly becoming a source of inspiration for cutting edge artists in a number of musical fields."
* **It is artistically challenging.** "Extreme metal challenges notions of what music really is. These musicians have pioneered sounds that can be heard nowhere else…"
* **It is globally and culturally diverse.**

## The four subgenres

Metal as a whole is an extremely wide genre: fast to slow, loud to soft, underground to mainstream. It is a worldwide movement. The key elements that make it fit into the underground are the sense of community that comes with being a metalhead, the fashion and aesthetic, and the music. Four subgenres: thrash, death, black and doom. [CONFIRM T07-03]

### Thrash

Thrash features fast tempos, low-register, quick, complex guitar riffs and high-register guitar solos. Palm muting and staccato playing in tightly controlled riffs create a "chugging" sound, and the solos are played at high speed, characterized by shredding. [CONFIRM T07-04]

The first thrash song was Overkill's "The Beast Within" (1981). [CONFIRM T07-05] The "big four" are Anthrax, Megadeth, Metallica and Slayer. In 1984: Anthrax's *Fistful of Metal*, Metallica's *Ride the Lightning* and Slayer's *Haunting the Chapel* EP. In 1985: Megadeth's *Killing Is My Business… and Business Is Good!* The major thrash scenes were the Bay Area, with Testament and Metallica, and New York and New Jersey, with Anthrax and Overkill.

### Death metal

Death metal is often identified by fast, highly distorted and downtuned guitars, with techniques like palm muting and tremolo picking. The percussion is fast and dynamic, with blast beats, double bass and exceedingly fast drum patterns, and the vocals are often grunts, snarls and low gurgles, called death grunts or death growls. [CONFIRM T07-06] The golden years of the genre were 1988 to 1994.

The term's origin: a Florida journalist spoke of the band Death as "Death's metal," and the term was picked up for lyrical content, a fanzine called *Death Metal*, and Possessed's 1984 album. [CONFIRM T07-07] Bands include Deicide, Morbid Angel, Death and Obituary. Seminal albums: Death's *Death by Metal* (1983) and Possessed's *Death Metal* (1984). [CONFIRM T07-08]

**Florida death metal.** Florida has its own brand, concentrated in Tampa, with bands like Assuck, Morbid Angel and Deicide. It is more direct and brutal than other death subgenres. As Natalie Purcell, a sociologist at UC Santa Cruz, writes in *Death Metal Music: The Passion and Politics of a Subculture*: "Often guitars are not downtuned as low, and the guitar work is more tight, precise and clear. Extremely fast, machine gun like blast beats characterize the drumming in Floridian Death Metal." [CONFIRM T07-09] Morrisound Studios in Tampa is where many of these records were made.

**Grindcore.** Grindcore is a close cousin of death metal. It developed in the UK in the mid-1980s with bands like Napalm Death. The name is said to have been introduced by Napalm Death's drummer Mick Harris, who says: "Grindcore came from 'grind', which was the only word I could use to describe Swans after buying their first record in '84. Then with this new hardcore movement that started to really blossom in '85, I thought 'grind' really fit because of the speed so I started to call it grindcore." [CONFIRM T07-10] It is seen as a progression of hardcore punk: fast, short, loud songs, and characterized by microsongs. In 1994 the Book of World Records awarded Brutal Truth the "Shortest Music Video" for their 1994 song "Collateral Damage" (four seconds); in 2007 the record was broken by Napalm Death's "You Suffer" at 1.3 seconds. [CONFIRM T07-11]

Assuck came out of this world, as did power violence, and then emo power violence, like Reversal of Man.

### Doom

Doom is directly related to Black Sabbath and Pentagram. It is very slow, very low and very riff-based, and meant to be very loud. It is the most underground form of metal, barely recognized by metal fans in the 1980s. Bands such as Trouble established the use of Christian imagery and themes in the lyrics of doom metal, which led these bands to be seen as "weird" and unacceptable by some metalheads. Many of the later doom bands were not Christian, but bands such as Candlemass and Saint Vitus still embraced Christian imagery, not as a religious viewpoint but as lyrical symbolism for themes like pain and suffering. [CONFIRM T07-12]

Doom spawned two offshoots:

* **Stoner doom.** Sleep's *Holy Mountain* (1992). Their third album, *Dopesmoker* (1995), was one song more than an hour long, and the record label refused to put it out. They trimmed it to 52 minutes, added lyrics and called it *Jerusalem*, and the label still wouldn't release it. *Jerusalem* came out in 1998 and *Dopesmoker* in 2003. After the breakup, the drummer and bassist went on to form Om, whose music is similar to Tibetan chant. [CONFIRM T07-13]
* **Drone doom.** Noise and ambient music, typically with songs ten to thirty minutes long, sometimes without drums, with an emphasis on volume, texture and physically embracing the music. The major bands are Sunn O))) and Earth. Earth formed in Seattle in 1990 (Slim Moon, Dylan Carlson, Greg Babior), and their album *Hex* was influenced by Neil Young's soundtrack to *Dead Man*. Sunn O))) was formed in 1991 by Stephen O'Malley and Greg Anderson. [CONFIRM T07-14]

There is also a New Wave of American Metal: Baroness, Isis, Pelican and Torche, on the labels Hydra Head and Southern Lord.

## The Melvins

The Melvins are sludge metal, pre-grunge metal, doom, stoner, all of the above. Buzz Osborne is the singer and guitarist and Dale Crover the drummer, with various bassists and second guitarists. Their original bassist, Matt Lukin, went on to Mudhoney.

They formed in 1983 in Montesano and Aberdeen, Washington, and later moved to San Francisco. The name was taken from a grocery store clerk where Buzz worked. [CONFIRM T07-15] They have been called the first post-punk band to really use Black Sabbath as a musical influence. [CONFIRM T07-16]

In 1986 they released *Six Songs* on C/Z Records, and in 1987 Alchemy Records released their first full album, *Gluey Porch Treatments*. In May 1989 they recorded and released *Ozma*, with Lori Black ("Lorax"), Shirley Temple's daughter, on bass. In August 1990, Nirvana was without a drummer, and Crover helped by playing on a brief West Coast tour with Sonic Youth. Osborne gave Dave Grohl, of Scream, the phone number of Nirvana bassist Krist Novoselic, and Grohl later became Nirvana's final full-time drummer. [CONFIRM T07-17] *Bullhead* followed in 1991 on Boner Records ("Ligature" is on it). In 1992 they released "solo" albums by King Buzzo, Dale Crover and Joe Preston, modeled on the solo records KISS released in 1978.

Because of Nirvana's fame, the Melvins were picked up by Atlantic in 1993 and released *Houdini* ("Joan of Arc" is on it). Atlantic dropped them in 1996 after three albums (*Houdini*, *Stoner Witch* and *Stag*). They have worked with Mike Patton's Ipecac Recordings since 1999, which also releases Hella, Isis and The Locust. They have also released albums under different band names, and collaborated with Jello Biafra on a few, as "Jelvins."

In a 1988 interview with *Maximum Rocknroll*, Buzz says, "We sound like Black Sabbath," and Dale says, "We sound like twisted Sabbath." About his lyrics, Buzz says, "We're not set out to be political… the vocals are inspired by the music, I think the lyrics are just as important as the music. They're not a social commentary or anything." And: "We are serious about our music, we are serious about this band, just in normal everyday life we like to have a lot of fun." [CONFIRM T07-18]

There is a lot of mystery around this band. They never really tell the truth and seem to have a lot of fun confusing the interviewer and the audience. Buzz has appeared in videos by Beck, Nine Inch Nails and Primus. [CONFIRM T07-19] Frank Kozik has often done their cover art.

**The point of the Melvins:** they are a good example of how metal spans the mainstream and the underground. They are a notable doom band who influenced bands like Mastodon, Tool and Boris.

## Confirmation queue (Topic 7)

```yaml confirmation-queue
- id: T07-01
  type: source-text
  priority: medium
  claim: Between 1983 and 1984 heavy metal went from 8 to 20 percent of recordings sold in the U.S.; Kerrang! (1981) and Metal Hammer (1984); Billboard 1985 quote about the audience broadening.
  original_wording: Between 1983 and 1984, heavy metal went from an 8 percent to a 20 percent share of all recordings sold in the U.S.[68] ... In 1985, Billboard declared, "Metal has broadened its audience base..." (from wikipedia)
  concern: Pasted from an encyclopedia (the original keeps footnote marker [68]); paraphrased here. Statistics and the Billboard quote need checking against the primary sources.
  task: Find the primary source for the share figures and the Billboard statement. Rewrite or credit.
- id: T07-02
  type: gap
  priority: medium
  claim: Kahn-Harris gives five reasons to study extreme metal.
  original_wording: '"Keith Kahn-Harris... gives 5 reasons:" (only three are listed)'
  concern: Only three reasons appear in the original.
  task: Find Kahn-Harris's other two reasons in the source and add them, or change the text to "three". Verify the quotes.
- id: T07-03
  type: gap
  priority: medium
  claim: The four subgenres include black metal.
  original_wording: '"The 4 Subgenres: Thrash, Death, Black, Doom" (no black metal discussion follows)'
  concern: The original does not cover black metal at all.
  task: Do not invent content. Note whether Micah should add black metal or drop it from the list.
- id: T07-04
  type: source-text
  priority: medium
  claim: A description of thrash guitar (fast tempos, riffs, palm muting, staccato, "chugging," solos).
  original_wording: Thrash- features a number of fast and rapid tempos, low-register, quick, complex guitar riffs, and high-register guitar solos. Palm muting and staccato are used in these tightly controlled riffs to create a 'chugging' sound...
  concern: Pasted from an encyclopedia, now paraphrased.
  task: Identify the source and rewrite in Micah's voice or credit.
- id: T07-05
  type: claim
  priority: low
  claim: The first thrash song was Overkill's "The Beast Within" (1981); the "big four"; albums from 1984 and 1985; Bay Area and NY/NJ scenes.
  original_wording: 'First Thrash song – Overkill''s The Beast Within 1981. The big four: Anthrax, Megadeath, Metallica, Slayer... Major Thrash scenes – Bay Area with Testament, Metallica, NY/NJ with Anthrax and Overkill'
  concern: '"First thrash song" is a contested claim (the song may be from a demo). Verify names and years, including spelling "Megadeth" and the Slayer EP title.'
  task: Verify and rephrase "first" if needed.
- id: T07-06
  type: source-text
  priority: medium
  claim: A description of death metal (downtuned guitars, palm muting, tremolo picking, blast beats, death grunts).
  original_wording: The genre is often identified by fast, highly distorted and downtuned guitars... colloquially called death grunts or death growls. (extrememp3s.com)
  concern: Pasted from a web source, now paraphrased.
  task: Find the source and rewrite or credit.
- id: T07-07
  type: claim
  priority: high
  claim: 'The origin of the term "death metal": a Florida journalist referred to the band Death as "Death''s metal"; lyrical content; the fanzine Death Metal; Possessed''s 1984 album.'
  original_wording: 'origin of the term: from a Florida journalist speaking of the band Death ''Death''s Metal'', lyrical content, fanzine called Death Metal, Possesed album 1984'
  concern: The sentence is a fragment, and the origin story is unclear and contested.
  task: Research the origin of the term and rewrite accurately.
- id: T07-08
  type: claim
  priority: medium
  claim: 'Seminal albums: Death''s Death by Metal (1983) and Possessed''s Death Metal (1984).'
  original_wording: Death- Death by Metal 1983. Possesed- Death Metal 1984
  concern: Both may be demos or early releases and not albums, and the years may be off. Titles may be wrong (Death's debut album is usually dated 1987).
  task: Verify format, year and title for each, and fix.
- id: T07-09
  type: quote
  priority: medium
  claim: 'Natalie Purcell, Death Metal Music: The Passion and Politics of a Subculture, on Floridian death metal guitar and drumming.'
  original_wording: '"Often guitars are not downtuned as low, and the guitar work is more tight, precise and clear. Extremely fast, machine gun like blast beats characterize the drumming in Floridian Death Metal." – Natile Purcell – (Sociology at UC Santa Cruz)'
  concern: Verify the author's name (spelled "Natile" in the original), her affiliation, and the exact quote and page.
  task: Verify and fix.
- id: T07-10
  type: quote
  priority: medium
  claim: Mick Harris of Napalm Death on the origin of the word "grindcore."
  original_wording: Concerning the name, said to be introduced by Napalm Death's drummer Mick Harris, he says, "Grindcore came from 'grind', which was the only word I could use to describe Swans after buying their first record in '84...
  concern: The source of the quote is unknown (probably a Wikipedia entry quoting an interview).
  task: Find the original interview and the exact wording. Check that Harris was the drummer in question.
- id: T07-11
  type: claim
  priority: medium
  claim: Brutal Truth's "Collateral Damage" (1994, four seconds) was awarded the "Shortest Music Video" by the Book of World Records; the record was broken in 2007 by Napalm Death's "You Suffer" at 1.3 seconds.
  original_wording: Book of World Records in 1994 awarded Brutal Truth "Shortest Music video" for 1994 song Collateral Damage (4 seconds). 2007 record was broken by Napalm Death's You Suffer 1.3 seconds
  concern: Which record book, which category (shortest song or shortest video), and the dates. "You Suffer" was released in 1987.
  task: Verify and rewrite accurately.
- id: T07-12
  type: source-text
  priority: medium
  claim: A description of doom metal and Christian imagery (Trouble, Candlemass, Saint Vitus).
  original_wording: bands such as Trouble established the use of Christian imagery and themes in the lyrical side of doom metal which led these bands to be seen as "weird"... (wiki)
  concern: Pasted from an encyclopedia (marked "wiki"), now paraphrased.
  task: Check the claims and rewrite or credit.
- id: T07-13
  type: date
  priority: medium
  claim: 'Sleep: Holy Mountain (1992); Dopesmoker (one song, over an hour); trimmed to 52 minutes and retitled Jerusalem; released 1998 (Jerusalem) and 2003 (Dopesmoker); drummer and bassist went on to Om.'
  original_wording: Sleep 'Holy Mountain' 1992... 3rd album Dopesmoker 1995 – one song more than an hour long... Released in 1998 Jerusalem and 2003 Dopesmoker. After breakup drums and bass went on to form Om.
  concern: Verify the history and dates (the label, the versions and the release years).
  task: Verify and fix.
- id: T07-14
  type: date
  priority: medium
  claim: Earth formed in Seattle in 1990 (Slim Moon, Dylan Carlson, Greg Babior); Hex was influenced by Neil Young's soundtrack to Dead Man; Sunn O))) formed in 1991 by Stephen O'Malley and Greg Anderson.
  original_wording: Earth- Seattle 1990 Slim Moon, Dylan Carlson, Greg Babior. Hex influenced by Neil Young soundtrack to Dead Man. Sunn 0))) – 1991 Stephen O'Malley, Greg Anderson
  concern: Verify the lineup and years. Sunn O))) is usually dated to 1998. Check Slim Moon's membership (see T04-12).
  task: Verify and fix.
- id: T07-15
  type: claim
  priority: low
  claim: The Melvins formed in 1983 in Montesano and Aberdeen, Washington, and later moved to San Francisco; the name came from a grocery store clerk where Buzz worked.
  original_wording: Formed 1983 in Montesano/Aberdeen WA, moved to san fran. Name taken from a grocery store clerk where Buzz worked.
  concern: Verify the location, the move, and the name's origin.
  task: Verify and fix.
- id: T07-16
  type: claim
  priority: medium
  claim: The Melvins have been called the first post-punk band to really use Black Sabbath as a musical influence.
  original_wording: Called the 1st post-punk band to really use Black Sabbath as a musical influence
  concern: Who called them that? Strong claim.
  task: Find the source of this claim. If unsupported, soften it.
- id: T07-17
  type: source-text
  priority: medium
  claim: In August 1990 Crover played on a West Coast tour with Nirvana and Sonic Youth; Osborne gave Dave Grohl Novoselic's phone number.
  original_wording: In August 1990, Nirvana was without a drummer, and Crover helped out by playing on a brief west coast tour with Sonic Youth. Osborne gave Dave Grohl from Scream the phone number of Nirvana bassist Krist Novoselic; Grohl later became Nirvana's final full-time drummer.
  concern: Pasted from an encyclopedia entry (links retained in the original). Verify that Crover played with Nirvana on that tour.
  task: Verify and rewrite or credit.
- id: T07-18
  type: quote
  priority: medium
  claim: Quotes from the 1988 Maximum Rocknroll interview with the Melvins.
  original_wording: Buzz says "We sound like Black Sabbath." Dale says "we sound like twisted Sabbath." About his lyrics buzz says "we're not set out to be political… the vocals are inspired by the music..." "we are serious about our music, we are serious about this band, just in normal everyday life we like to have a lot of fun."
  concern: Verify the quotes against the interview (a copy is on the Melvins fan wiki).
  task: Verify and fix.
- id: T07-19
  type: claim
  priority: low
  claim: Buzz Osborne has appeared in videos by Beck, Nine Inch Nails and Primus.
  original_wording: Beck NIN Primus- Buzz has been in all their videos.
  concern: Verify each.
  task: Verify and fix, or soften.
```

<!-- ===== TOPIC 07 END ===== -->

<!-- ===== TOPIC 08 START ===== -->

# Topic 8: The Transition to the 1990s

```yaml agent-meta
topic: 8
slug: topic-08
title: The Transition to the 1990s
syllabus_lessons: 'new genres and a new socio-cultural context; lo-fi and emocore (Beat Happening, Rites of Spring, Husker Du); Before Nirvana and After Nirvana; the 1990s: music, society and culture; the changing nature of indie; early indie (Guided By Voices, Pavement); 1994 as indie rock''s foundational year.'
syllabus_readings: Duncan Barlow, Bob Mould and Ted Leo in Sinker; Beat Happening, Husker Du and the Epilogue in Azerrad; Greenwald ch. 1; Michael Dennis, "Youth Activism in the 1990s" (in Greenberg).
syllabus_film: '*Instrument.*'
old_links_from_original_notes:
- http://www.bbc.co.uk/music/sevenages/assets/artists/husker-du/gallery/1.jpg
- http://www.spirit-of-metal.com/les%20goupes/H/Husker%20Du/pics/logo.gif
- http://www.metrolyrics.com/broken-home-broken-heart-lyrics-husker-du.html
- http://www.youtube.com/watch?v=q-VhauwyE5k&mode=related&search
- http://www.lyricsondemand.com/r/ritesofspringlyrics/deeperthaninsidelyrics.html
- http://www.lyricsondemand.com/r/ritesofspringlyrics/forwantoflyrics.html
- http://www.lyricsondemand.com/b/blackflaglyrics/inmyheadlyrics.html
- http://www.retrostatic.com/videos/p803_sectionid/4/p803_shownum/15
- http://www.time.com/time/magazine/article/0,9171,970634,00.html
- http://en.wikipedia.org/wiki/Douglas_Coupland
- http://en.wikipedia.org/wiki/Generation_X:_Tales_for_an_Accelerated_Culture
- http://en.wikipedia.org/wiki/1960
- http://en.wikipedia.org/wiki/1965
- http://en.wikipedia.org/wiki/Baby_boom_generation
- http://www.youtube.com/watch?v=a6q3T0gz6SA&feature=related
- http://www.youtube.com/watch?v=CXOl9asxQiY&feature=related
- http://en.wikipedia.org/wiki/Ellen_DeGeneres
- http://www.starpulse.com/Television/Will_And_Grace/
- http://abc.abcnews.go.com/primetime/nypdblue/index.html
- http://www.geocities.com/TelevisionCity/4151/index2.html
- http://www.menbehavingbadly.com/
- http://www.comedycentral.com/tv_shows/southpark/
- http://en.wikipedia.org/wiki/Politically_Incorrect
- http://www.youtube.com/watch?v=W16qzZ7J5YQ&mode=related&search=Budweiser%20wassup%20true%20beer
- http://www.musicoutfitters.com/topsongs/1994.htm
- http://www.cnn.com/2006/SHOWBIZ/Music/09/19/indie.overview/index.html
- http://www.rocklistmusic.co.uk/spinend.htm#94
- http://www.gbv.com/band.html
- http://www.youtube.com/watch?v=6RDmaNPHdDU
- http://lyricwiki.org/Pavement:Cut_Your_Hair
```

## Overview

The move from the 1980s to the 1990s was not only an ideological shift, with the popularity of the underground, but also a musical shift. Ideology is the ideas and manner of thinking characteristic of a group, social class or individual: an organized collection of abstract ideas, a comprehensive vision of a group. The ideology of the underground is wrapped up in its conceptions and definitions of indie and DIY.

To describe the ideological shift: in the first three quarters of the twentieth century it was easy to sort music into a stylistic core (whatever was popular and easily accessible: Tin Pan Alley, jazz, disco) and a periphery (under the radar, different from the norm: blues, folk, heavy metal). The rise of the 1980s underground, and the transitional genres that carried it into the 1990s, complicate that model considerably. There is no longer a center and a periphery, but a hodgepodge of musics influencing and being influenced by one another.

The transitional genres are second-wave punk, metal, and post-hardcore: emocore, lo-fi and indie. This topic follows them through Hüsker Dü and Rites of Spring in the 1980s, the cultural landscape of the 1990s, and 1994, the year indie rock's shape came into view.

## Listen and watch

* Hüsker Dü, "Something I Learned Today," "Broken Home, Broken Heart" and "Hare Krsna" (from *Zen Arcade*)
* Beat Happening, "Bad Seeds" and "Indian Summer"
* Rites of Spring, "Deeper Than Inside" and "For Want Of"
* Black Flag, *In My Head* (for comparison with Rites of Spring) [CONFIRM T08-01]
* Jawbreaker, "Chesterfield King"
* A *120 Minutes* clip of Guided by Voices
* Guided by Voices, "Gold Star for Robot Boy" and "Queen of Cans and Jars"
* Pavement, "Cut Your Hair"
* Trailers for *Mallrats* (1995) and *Dazed and Confused* (1993)
* The Budweiser "Wassup" commercial and other 1990s TV commercials
* The Epitaph Records video

## Films

* *Instrument*

## Readings

* Duncan Barlow, Bob Mould and Ted Leo, in Sinker, *We Owe You Nothing*
* Beat Happening, Hüsker Dü and the Epilogue, in Azerrad, *Our Band Could Be Your Life*
* Greenwald, *Nothing Feels Good*, chapter 1
* Michael Dennis, "Youth Activism in the 1990s," in Greenberg, *Youth Subcultures*

## Discussion questions

**On Hüsker Dü and emocore**

* What makes Rites of Spring more emotional than hardcore bands like Black Flag? Is the proof in the intention or in the influence?
* What issues does this raise about masculinity and femininity?

**On the changing nature of indie** (Azerrad, Barlow, Leo)

* Class issues, a changing business model, the breakdown of the old community (SST), the dilution of DIY, changing modes of identification (fashion): which of these changed most?
* Is there a divorce between the music and the meaning?
* Are class distinctions entering new definitions of underground (working class) and indie (intellectual)?
* Is there a loss of creativity in the face of how easy indie, DIY and underground have become? A loss of principles? A loss of personal connection? What was gained?
* What happened when a flood of fans arrived with no knowledge of history? How did it change the music that came next?
* Is there still an underground? Can there be? Where will the next Seattle be?
* Barlow's key point is that violence pushed many away. Is this a theme for many of the founders? How does it affect a scene?
* Ted Leo: "When you try to epitomize something with a sound, you cheapen it." What does this say about the indie genre? Does the term get cheapened for us?
* How did the community change? What are the new values? Is this true of underground music today?
* Barlow resigned from something. Do we take that resignation seriously? Why does he feel responsible to resign at all? [CONFIRM T08-02]
* Ted Leo's key point is the responsibility of the fan: audiences must become critical consumers, even in the indie sphere. The terminology of "punk" changes its nature. How does the rhetoric of underground culture affect its future?

## Lo-fi and cassette culture

Lo-fi comes from "low fidelity," the quality of the music in its output. It is most often associated with tapes and analog recording methods. As an outgrowth of the underground press and indie label distribution, cassette culture was born, and sharing mixtapes became a way of spreading music across the landscape. K Records and Beat Happening were seminal in this movement.

## Indie as college rock: Hüsker Dü

Hüsker Dü, from Minneapolis, is Norwegian for "Do you remember?" [CONFIRM T08-03] The members were Bob Mould, Grant Hart and Greg Norton. Their logo has a circle for the band, three lines for the members and an intersecting line for the common train of thought.

Azerrad's account, as I read it in class, makes several points:

* They had a huge role in convincing the underground that melody and punk rock were not antithetical (p. 159).
* They became a key link between hardcore and the more melodic, accessible music that would eventually be termed "college rock."
* Their eventual move to a major label sent shock waves through the indie community. R.E.M. and U2 had paved the way, but no one from the community had ever made the leap.
* They, along with a few other bands, created the mainstream market for the commercialization of "college rock."
* Their sound was folk rock played at light speed, with distortion and extreme volume.
* They began to disavow the preachy aspects of hardcore: "We want to pose questions, not answers" (Bob Mould, p. 168). [CONFIRM T08-04]

*Zen Arcade* was released in July 1984 on SST. It is a concept album, the ultimate classic-rock idea, a story about a kid who runs away, deals with drugs and real life, and returns home. "Something I Learned Today" is a simple refutation of hardcore orthodoxy. It is loud and fast, but its use of melody and chord structures is very un-hardcore. The zine *Hard Times* put it this way: the story "encapsulates the wreckage of our era, betrayal, alienation, pain, egotism, emotional suffocation and isolation" (p. 182). It is similar to hardcore in its negative view of the world, but pushed to an extreme limit of emotional connectedness to these issues. [CONFIRM T08-05]

*Zen Arcade* began the trend of opening this music up to a new group of people: college students, interested in the lyrics, reading between the lines. It garnered tons of critical acclaim, many best-of lists, and several of its songs were included in lists of the top 500 songs of the 1980s. It represents the sound of an entire musical movement growing up.

Hüsker Dü was also the first key underground band to make the jump to a major label, releasing *Candy Apple Grey* on Warner Bros. in 1986. [CONFIRM T08-06] They are claimed as an influence on bands from Green Day to the Pixies.

## Emocore: Rites of Spring

Emocore means emotional hardcore. There are numerous theories about where the term came from. Some say it was a derogatory term used at an Embrace show; others say Rites of Spring used it in an interview with *Flipside*. [CONFIRM T08-07]

It was the musical reaction against the violence and close-mindedness of the DC hardcore scene. In DC at this time, the scene was beginning to fracture as hardcore waned, and the core members of the scene had moved out, grown up or become disenchanted with the way things were. Out of these feelings came the idea of Revolution Summer, which we read about in *Dance of Days*.

What did it sound like? It was guitar-oriented, mid-tempo, rock-based music with emotional punk vocals (not posed, soulful crooning like pop music). The central aspect is the guitars: distorted, strummed mostly in duo unison, with occasional catchy riff highlights. This became known as the classic "D.C. sound," along with the octave chords that show up in later "emo" music. Later bands brought in more pop elements: catchy-riff-based songs and pop song structures (Jawbreaker's "Chesterfield King" illustrates this), and smoother, higher-register singing, with less yelling and straining. [CONFIRM T08-08]

## The cultural landscape of the 1990s

If the 1980s was the "Me Generation," the 1990s was the "youth generation." Youth culture, and everything involved in it, was the staple of 1990s cultural history.

**Generation X and the slackers.** In the early 1990s the media portrayed Generation X as flannel-wearing, alienated, overeducated, underachieving slackers with body piercings, who drank franchise-store coffee and worked at McJobs. These ideas had some truth to them but were in many cases stereotypes. The term "Generation X" was popularized by Douglas Coupland's novel *Generation X: Tales for an Accelerated Culture* (1991), which describes the angst of those born roughly between 1960 and 1965, who felt no connection to the cultural icons of the baby boom. In Coupland's usage, the X referred to the namelessness of a generation that was becoming aware of itself as a separate group but felt overshadowed by the boomers. [CONFIRM T08-09]

**Fashion.** Anti-fashion in the first half of the decade, with an emphasis on the individual and personal taste: tattoos and piercings, grunge, hip hop, retro. Films like *Clerks*, *Mallrats* and *Reality Bites* encouraged it.

**Technology.** The technology boom of the 1980s continued. The internet connected the world in new ways. By 1994 three million people were online, and by 1998 it was 100 million. [CONFIRM T08-10] MTV continued as a forerunner of youth culture with *The Real World* in 1992. The X Games were established in 1995, and extreme sports gained popularity.

**Music.** While rock held popular attention for most of the decade (grunge, alternative, nu metal), hip hop culture was also a major force. Many 1990s slang words and phrases were related to hip hop culture ("dawg," "phat," "da bomb"). Tupac and Notorious B.I.G. had a war of words that ended in their deaths in 1996 and 1997. The Fugees, Boyz II Men and TLC were huge throughout the decade. [CONFIRM T08-11]

**Society and politics.** Racial issues were brought into the public eye by the L.A. riots, the O.J. Simpson murder case and the Million Man March, and multiculturalism became a concern of education, politics and global relations. With the collapse of the USSR, the United States was the world's sole superpower. In 1990 Iraq invaded Kuwait, and the U.S. later got involved in Somalia (1993), Haiti (1994), Bosnia (1996) and Yugoslavia (1999). [CONFIRM T08-12] Bill Clinton's two terms brought Democratic concerns back to the White House, and he presided over the longest period of peacetime economic expansion in American history, including a balanced budget and a federal surplus. The decade also saw the World Trade Center bombing (1993), Oklahoma City (1995) and Columbine (1999).

**Entertainment.** Throughout American music history, the margins have been the progressors of music. In the 1990s there was an ironic twist: making the notion of outsider, alternative or marginal music a means of promoting music to a mass audience searching for a sense of authenticity. The tension between commercialism and authenticity can be said to be the main thought process of the underground in this period. The mainstream was Hootie and the Blowfish, Alanis Morissette, Celine Dion, Garth Brooks and the Spice Girls; the movies, *Schindler's List* (1992), *Forrest Gump* (1994) and *Titanic* (1997), with *Pulp Fiction* (1994) as the indie film. [CONFIRM T08-13] Adult-oriented cartoons arrived (*The Simpsons*, *Family Guy*, *Beavis and Butt-Head*), *Seinfeld* and *Friends* had large followings, and TV pushed boundaries on sexual orientation (*Ellen*, *Will and Grace*), nudity, language, crude behavior, violence and political incorrectness.

### What this meant for the underground

In the epilogue to Azerrad's book, he states that Nirvana's *Nevermind* (September 1991) synthesized the music the industry had been ignoring for most of the 1980s, from bands like Black Flag, Hüsker Dü, Dinosaur Jr., the Pixies and the Melvins. "*Nevermind* made the sound palatable to the mainstream with strong melodies and slick production" (p. 494). College radio became a mining ground thanks to the success of R.E.M. and U2. Guy Picciotto: "The conversations changed after 1991. Before people talked about ideas and music. And then after that people talked about money and deals" (p. 495). [CONFIRM T08-14]

Three things mark the change: **visibility**, active interaction with the mainstream; **agency**, the underground's ability to be effective in social, cultural and political America; and **proliferation** of the fan and member base: "everyone was doing it themselves, and a lot of it was mediocre." [CONFIRM T08-15] Indie and underground moved from an idea to a genre.

## 1994

1994 represents the shifts of the 1990s very well. A boiling point was reached, and the output of the underground reflected it. In the 1980s the underground had a semi-unified feel across the board; in the 1990s there was a whole slew of new concerns and new ways of doing DIY. The albums released in 1994 had profound effects, then and now.

* **Green Day, *Dookie*:** released February 1 on Reprise Records. It rose to number 2 on the Billboard chart and raised serious questions in the underground about selling out. It won the Grammy for Best Alternative Album in 1995, and *Time* called it the best rock record of 1994. [CONFIRM T08-16]
* **Weezer, the Blue Album:** released May 10. Several videos directed by Spike Jonze won various awards (MTV VMAs and Billboard). The album is said to have spawned the "pop emo" subgenre. The band calls its influences KISS, Nirvana and the Pixies, showing how 1990s music was beginning to recognize influence from various generations of music. [CONFIRM T08-17]
* Limp Bizkit formed. Kurt Cobain died.

Two subgenres to focus on: second-wave punk and lo-fi. Lo-fi was fully in fruition in 1994. It is associated with earlier bands like Beat Happening, Sebadoh (formerly of Dinosaur Jr.) and cassette culture (K Records). Lo-fi artists often record on old or poor recording equipment, ostensibly out of financial necessity but also because those technologies have a unique association with "authenticity" for listeners, created by years of exposure to demo, bootleg and field recordings and to older pop recordings produced more simply. The growth of lo-fi coincided with the extreme slickness and polish of the multitrack pop recording of the 1980s. [CONFIRM T08-18]

Lo-fi is what some call "true indie rock." The "alternative" genre became commercialized as mainstream success attracted major-label investment and commercially oriented or manufactured acts with a formulaic, conservative approach. The meaning of "alternative" changed away from its original counter-cultural sense to refer to alternative music that achieved mainstream success, and "indie rock" came to refer to the bands and genres that remained underground. [CONFIRM T08-18] Lo-fi was also influenced by The Smiths.

### Guided by Voices

Guided by Voices formed in Dayton, Ohio, in 1983, and their principal songwriter is Robert Pollard. Their influences include psychedelic rock, prog rock, punk and post-punk. They began to capitalize on the success of college radio bands like R.E.M., and in 1993 started to get attention from the press, including *Spin*. In 1994 they released *Bee Thousand* on Scat Records, with distribution through Matador, a major player in 1990s indie circles. They put on a great live show, playing up their chops as a show band after years of experience. [CONFIRM T08-19]

*Bee Thousand* was the culmination of early lo-fi, mixed with early emocore, combined with the melodic structures of pop and the attitude of grunge, transplanted in the Midwest. It also signifies an important shift from the East Coast and West Coast polarization of the scene to the rise of middle America through indie, emo and late-1990s progressive indie emo.

### Pavement

Pavement formed in 1989 in Stockton, California; the primary songwriter is Stephen Malkmus. *Crooked Rain, Crooked Rain* was released on February 2 (1994) on Matador Records. Because of lineup changes and access to a studio, its sound was a jump from the lo-fi of their 1992 release, *Slanted and Enchanted*. The album gained some critical acclaim but did more to expand their cult fan base. It debuted on the U.S. charts at 121, and "Cut Your Hair" became a Top Ten modern rock hit and an MTV hit. [CONFIRM T08-20] On "Cut Your Hair," Malkmus equates the recent popularity of alternative music to a trendy haircut, mocking Nirvana-be's who "dance right down to the practice room / [To] get attention and fame," and reminding them that "songs mean a lot / When songs are bought / And so are you." [CONFIRM T08-21]

Both bands gained some commercial success but were spurred on mostly by the cult following they developed.

## Confirmation queue (Topic 8)

```yaml confirmation-queue
- id: T08-01
  type: name-or-title
  priority: low
  claim: Rites of Spring are compared in class with Black Flag's album "In My Head."
  original_wording: Comparison with Black Flag's In My Head album.
  concern: Verify the album title and year (In My Head, 1985) and confirm it is the comparison Micah intended.
  task: Verify and fix.
- id: T08-02
  type: gap
  priority: low
  claim: Duncan Barlow resigned from something.
  original_wording: Do we take this resignation seriously? Why does he feel responsible to resign at all?
  concern: The original does not say what Barlow resigned from. Presumably the hardcore scene or a band.
  task: Read Barlow's piece in Sinker and fill in the context in a sentence.
- id: T08-03
  type: claim
  priority: low
  claim: Hüsker Dü is Norwegian for "Do you remember?"
  original_wording: Husker Du – Norwegian for "Do you remember?"
  concern: Usually described as Danish/Norwegian (also a board game).
  task: Verify and fix.
- id: T08-04
  type: quote
  priority: medium
  claim: 'Azerrad quotes about Hüsker Dü (pages 159 and 168), including Bob Mould: "We want to pose questions, not answers."'
  original_wording: '"they had a huge role in convincing the underground that melody and punk rock were not antithetical." P 159. "They became a key link between hardcore and the more melodic, accessible music that would eventually be termed ''college rock''." "Their eventual move to a major label sent shock waves through the indie community. REM and U2 had paved the way but no one from the COMMUNITY had ever made the leap." "We want to pose questions, not answers." Bob Mould, p. 168'
  concern: Several of these are quotes or close paraphrases from Azerrad; the prose does not use quotation marks for some of them. Verify wording and pages.
  task: Check each against Azerrad. Mark true quotes with quotation marks and correct page numbers.
- id: T08-05
  type: quote
  priority: medium
  claim: 'The zine Hard Times on Zen Arcade: "encapsulates the wreckage of our era..." (p. 182).'
  original_wording: '"The zine Hard Times put it, ''the story encapsulates the wreckage of our era, betrayal, alienation, pain, egotism, emotional suffocation and isolation.'' P 182.'
  concern: Verify the quote and attribution (Azerrad quoting Hard Times).
  task: Verify and fix. Also verify the release month and label of Zen Arcade.
- id: T08-06
  type: claim
  priority: high
  claim: Hüsker Dü was the first key underground band to make the jump to a major label with Candy Apple Grey (Warner Bros., 1986).
  original_wording: Husker Du was also the first key underground band to make the jump to a major label. They released Candy Apple Grey on Warner Bros in 1986
  concern: Strong "first" claim. Other bands made the jump earlier. Azerrad's wording was "no one from the community." Also Topic 6 says that Sonic Youth and The Replacements moved to majors.
  task: Verify the claim, and fix with a more defensible wording.
- id: T08-07
  type: claim
  priority: medium
  claim: 'Origins of the word "emocore": a derogatory term used at an Embrace show, or used by Rites of Spring in a Flipside interview.'
  original_wording: there are numerous speculations about where the term came from. Some say it was a derogatory term used at an Embrace show, others say that Rites used it in an interview with Flipside.
  concern: Verify the speculation with sources.
  task: Research and tighten.
- id: T08-08
  type: source-text
  priority: medium
  claim: A description of the sound of early emo (guitar-oriented, mid-tempo, emotional punk vocals, duo unison guitars, the D.C. sound, octave chords, later pop elements).
  original_wording: What did it sound like? Guitar-oriented, midtempo rock-based sound with emotional punk vocals... classic "D.C. sound," along with the octave chords... (fourfa.com)
  concern: Pasted from a web page (fourfa.com), now paraphrased.
  task: Find the source. Rewrite in Micah's voice or credit.
- id: T08-09
  type: source-text
  priority: medium
  claim: Generation X paragraph (flannel-wearing slackers; Coupland's 1991 novel; the meaning of "X").
  original_wording: 'During the early 1990s, the media portrayed Generation X as a group of flannel-wearing, alienated, overeducated, underachieving slackers... (wiki). The term, Generation X, was later popularized by novelist Douglas Coupland in Generation X: Tales for an Accelerated Culture (1991)...'
  concern: Both passages are pasted from an encyclopedia article.
  task: Check the claims, rewrite or credit.
- id: T08-10
  type: number-or-stat
  priority: medium
  claim: By 1994 three million people were online, and by 1998 it was 100 million; "birth of AOL 1993."
  original_wording: The internet connects the world in new ways with the birth of AOL 1993 for Microsoft. By 1994 3 million people were online, by 1998 it was 100 million.
  concern: The original sentence about AOL and Microsoft is garbled and is left out of the prose. The figures need sources and a definition (US or worldwide).
  task: Verify and fix. Decide whether to restore an AOL sentence.
- id: T08-11
  type: claim
  priority: low
  claim: Tupac and Notorious B.I.G. had a war of words that ended in their deaths in 1996 and 1997.
  original_wording: Tupac and Notorious B.I.G have a war of words the ends in their deaths. 1996 and 1997
  concern: Contested causal framing; sensitive.
  task: Verify dates and soften the claim to what is documented.
- id: T08-12
  type: date
  priority: low
  claim: U.S. involvement in Somalia (1993), Haiti (1994), Bosnia (1996) and Yugoslavia (1999); the Gulf War began when Iraq invaded Kuwait in 1990.
  original_wording: Gulf War – Iraq invades Kuwait in 1990. World Events The US got involved in– Somolia 1993, Hati 1994, Bosnia 1996, Yugoslovia 1999.
  concern: Verify the years (Bosnia involvement began earlier).
  task: Verify and fix.
- id: T08-13
  type: date
  priority: low
  claim: Schindler's List (1992), Forrest Gump (1994), Titanic (1997), Pulp Fiction (1994); the list of mainstream musicians.
  original_wording: 1992 Schindlers List, 1994 Forrest Gump, Titanic 1997. Indie Films – 1994 Pulp Fiction
  concern: Schindler's List was released in 1993.
  task: Verify and fix.
- id: T08-14
  type: quote
  priority: medium
  claim: 'Azerrad epilogue: Nevermind "made the sound palatable to the mainstream with strong melodies and slick production" (p. 494); Guy Picciotto: "The conversations changed after 1991..." (p. 495).'
  original_wording: '"Nevermind made the sound palatable to the mainstream with strong melodies and slick production." 494. Guy Picciotto "The conversations changed after 1991. Before people talked about ideas and music. And then after that people talked about money and deals." 495'
  concern: Verify the quotes and pages.
  task: Verify and fix.
- id: T08-15
  type: quote
  priority: low
  claim: '"Everyone was doing it themselves, and a lot of it was mediocre."'
  original_wording: 'Proliferation of fan/member base: "everyone was doing it themselves- and a lot of it was mediocre."'
  concern: The speaker and source are not given.
  task: Find the source.
- id: T08-16
  type: claim
  priority: medium
  claim: 'Dookie: released February 1, 1994, on Reprise; reached number 2 on Billboard; won the Grammy for Best Alternative Album in 1995; Time called it the best rock record of 1994.'
  original_wording: 'Feb 1st on Reprise records. Rose to #2 on Billboard chart. Raised serious questions in the underground about selling out. Won a Grammy for best Alternative Album in 1995. Time called in best rock record of 1994.'
  concern: Verify chart peak, award, and the Time claim.
  task: Verify and fix.
- id: T08-17
  type: claim
  priority: medium
  claim: 'Weezer''s Blue Album: released May 10 (1994); videos directed by Spike Jonze won awards; said to have spawned "pop emo"; influences KISS, Nirvana and the Pixies.'
  original_wording: May 10. Several videos directed by Spike Jonze won various awards, MTV VMA, and Billboard. This album is said to have spawned the 'pop emo' sub genre. Call their influences KISS, Nirvana and The Pixies
  concern: Verify the release date and awards. The "pop emo" claim is contested and should be attributed or softened.
  task: Verify and fix.
- id: T08-18
  type: source-text
  priority: medium
  claim: Descriptions of lo-fi and of the difference between "alternative" and "indie rock."
  original_wording: Lo-Fi - Often lo-fi artists will record on old or poor recording equipment... wiki. This genre is what some will call "true indie rock". the alternative genre became commercialized as mainstream success attracted major-label investment... wiki
  concern: Both passages are pasted from an encyclopedia (marked "wiki"). Also check "1994 was the year of lo-fi" and "influenced by The Smiths."
  task: Find the article. Rewrite in Micah's voice or credit it. Check the claims.
- id: T08-19
  type: claim
  priority: medium
  claim: 'Guided by Voices: formed in Dayton, Ohio, in 1983; Robert Pollard; attention from Spin in 1993; Bee Thousand (1994) on Scat Records with Matador distribution.'
  original_wording: formed Dayton OH 1983, principle songwriter Robert Pollard... in 1993 started to get attention from press like Spin magazine. 1994 Released Bee Thousand on Scat Records with Distro through Matador
  concern: Verify founding year and distribution deal.
  task: Verify and fix.
- id: T08-20
  type: number-or-stat
  priority: low
  claim: 'Pavement: formed 1989 in Stockton, CA; Crooked Rain, Crooked Rain released February 2 (1994) on Matador; debuted on the U.S. charts at 121; "Cut Your Hair" a Top Ten modern rock hit.'
  original_wording: Formed in 1989 in Stockton, CA... Crooked Rain, Crooked Rain released Feb 2nd on Matador Records... The album debuted on the U.S. charts at 121 and 'Cut Your Hair' became a Top Ten modern rock hit and MTV hit.
  concern: Verify the dates and chart claims.
  task: Verify and fix.
- id: T08-21
  type: quote
  priority: medium
  claim: A description of "Cut Your Hair" with lyric excerpts, attributed in the original to Rolling Stone.
  original_wording: On "Cut Your Hair," Malkmus equates the recent popularity of alternative music to a trendy haircut, mocking Nirvana-be's who "dance right down to the practice room/[To] get attention and fame," reminding them that "songs mean a lot/When songs are bought/And so are you." (Rolling stone)
  concern: A passage from a Rolling Stone piece with embedded lyric quotes; keep lyric excerpts minimal and credited.
  task: Find the piece. Rewrite in Micah's voice with at most a very short credited lyric quote, or credit the review.
```

<!-- ===== TOPIC 08 END ===== -->

<!-- ===== TOPIC 09 START ===== -->

# Topic 9: Emo

```yaml agent-meta
topic: 9
slug: topic-09
title: Emo
syllabus_lessons: what is emo; a brief history; Sunny Day Real Estate and Jawbreaker; technology and communication (tapes to mp3s, zines to magazines and blogs).
syllabus_readings: Greenwald introduction and chapters 2-5 and 14; Sunny Day Real Estate, Jeremy Enigk, Norman Brannon and Cometbus (course library); Jawbreaker in Sinker; J. Patrick Williams and Emily Lamison in Greenberg (pp. 104, 160).
syllabus_film: (none recorded)
old_links_from_original_notes:
- http://www.bedfordstmartins.com/online/cite7.html
- http://www.libs.uga.edu/ref/turabian.html
- http://www.chicagomanualofstyle.org/tools_citationguide.html
- http://www.youtube.com/watch?v=-6Dmg_4ZA2Y
- http://www.youtube.com/watch?v=Ri6ySOHoDfk
- http://www.last.fm/tag/emo
- http://www.wikihow.com/Be-Emo
- http://topartists.myspace.com/index.cfm?fuseaction=music.topBands
- http://tw.youtube.com/watch?v=GT5LIEUJefM
- http://web.archive.org/web/*/http://www.iuma.com
- http://zinewiki.com/index.php?title=Main_Page
- http://www.underground-library.org/index.php?option=com_frontpage&Itemid=1
- http://givemeback.org/
- http://www.operationphoenixrecords.com/heartattackissue03_1Intro.pdf
- http://www.myspace.com/antimatterbook
- http://www.fotolog.com/bigb0ss/31505798
- http://www.interpunk.com/item.cfm?Item=11655&
- http://www.altpress.com/
- http://www.loosecharm.org/pictures/band/pages/blake.htm
- http://www.loosecharm.org/word/boxcar.html
- http://www.loosecharm.org/word/indict.html
- http://www.youtube.com/watch?v=2J73DX3S98Y
- http://www.sunnydayrealestate.net/images/jeremy1.jpg
- http://www.sunnydayrealestate.net/images/nordstrom.jpg
- http://www.dallasobserver.com/1998-11-12/music/brightness-falls/
- http://www.youtube.com/watch?v=QMkH6xi6-Og
- http://www.sunnydayrealestate.net/lyrics.html
- http://www.sunnydayrealestate.net/jeremyletter.htm
- http://profile.myspace.com/index.cfm?fuseaction=user.viewprofile&friendid=37487352
```

## Overview

What is emo? It can be seen as the culmination of many trends and musical styles from the 1980s and 1990s. The fragmentation of the subculture, due to changing conceptions of what is and isn't acceptable, accounts for the difficulty of explaining and defining emo culture. Over the course of the 1990s, and especially into the 2000s, emo changed hands from one generation to the next, from the underground to the mainstream, and from negative connotations to positive reinforcement.

This topic asks what emo is as a history, a genre and a subculture, then looks at how technology changed the underground, from tapes to CDs and MP3s and from zines to magazines and blogs, and closes with two bands often pointed to as the ones that brought the "down to earth" emotional into emo: Jawbreaker and Sunny Day Real Estate.

## Listen and watch

* Promise Ring, "Red and Blue Jeans"
* Mineral, "Wakingtowinter"
* Dashboard Confessional, "Again I Go Unnoticed"
* Jimmy Eat World, "Sweetness"
* Jawbreaker, "Boxcar" and "Indictment"
* Sunny Day Real Estate, "Seven" and "In Circles"
* From the listening list: Jimmy Eat World, "Thinking, That's All"; Texas Is the Reason, "Johnny on the Spot"; The Get Up Kids, "Coming Clean"; Rainer Maria, "Breakfast of Champions"; Reversal of Man, "Quantis"; American Football, "Never Meant"; Braid, "Please Drive Faster" [CONFIRM T09-01]

## Readings

* Greenwald, *Nothing Feels Good*, the introduction and chapters 2-5 and 14
* Sunny Day Real Estate, Jeremy Enigk, Norman Brannon and Cometbus (course library)
* Jawbreaker, in Sinker, *We Owe You Nothing*
* J. Patrick Williams and Emily Lamison, in Greenberg, *Youth Subcultures* (pp. 104 and 160)

## Discussion questions

**On technology and communication**

* How did technology affect the underground? What changed? How did it affect ideas about indie, underground and DIY?
* With music spread for free, the connection between audience and artist can bypass the industry. Does this change the paradigm of DIY?
* Greenwald asks, "When you take a community-centered music and take it out of the community, what are you left with?" What do the changes look like? Is the artistic value diminished?
* How do music blogs work, compared with zines?

**On Jawbreaker and Sunny Day Real Estate**

* These bands again represent the intellectual versus aggressive nature of the indie underground. Two things came out in the new emo movement: the cult of personality and artistic abstraction. Were they present before, and just easier to see now? Or are they byproducts of the new independent sensibility in relating to the mainstream?
* Is Jawbreaker's "Indictment" a challenge to the connection between audience and artist? How does that become emo? The "cult of Blake"?
* Is Sunny Day Real Estate's music art? Are they trying to say something specific through their music, albums and actions? Is it something different from what we have heard before? Is Sunny Day romantic (Greenwald, p. 30)?

## What is emo?

The Warped Tour began on August 9, 1995. It became the breeding ground for a new culture of bands aimed at a teenage audience. Many of the early tours were headlined by second-wave punk bands, but recently the trend has swung toward "new emo." [CONFIRM T09-02]

### Emo is constantly changing: three waves

* **First wave (1980s): emocore.** Rites of Spring. A reaction against hardcore: melodic but still very raw.
* **Second wave (1990s): indie emo.** Jimmy Eat World, The Get Up Kids, Braid, The Promise Ring, Texas Is the Reason, Mineral. Slowed down, a mix of indie rock's musical sense (it sounded more like music) with personal and sometimes nonsensical lyrics. "Red and Blue Jeans" and "Wakingtowinter" are examples.
* **Third wave (2000s): pop emo.** Thursday, Dashboard Confessional, Jimmy Eat World (*Bleed American*), Taking Back Sunday. "Emo in the arena!" Big sounds, powerful, catchy tunes. Associations with emo are more in the culture than in the history, music or themes. "Again I Go Unnoticed" and "Sweetness" are examples.

### Emo as a genre

Emo is characterized by softer, more aesthetically pleasing sounds than hardcore, more structured than experimental music, and more melodic than grunge. Often the themes are about love, relationships or growing up. As the first and second generations grew up, the music splintered into subgenres, which began to appeal to new audiences through the portal of emo: indie, hardcore (Shai Hulud), screamo (Reversal of Man), neo-folk (Iron and Wine), post-rock (Explosions in the Sky) and metalcore (Zao). The splintering of the scene comes with the invasion of pop culture.

### Emo as a subculture

Emo has all the attributes of a subculture. In the tradition of tongue-in-cheek how-to guides, there is a specific fashion (*Everybody Hurts: An Essential Guide to Emo Culture*), a centralizing ideal (the music), and a connection with youth: Greenwald constantly reminds us in his book that these are kids, teens, adolescents. It interacts with the mainstream culture. This comes out of the tradition that early indie and grunge paved, and the subculture works as an extension of the mainstream culture.

## Technology and communication: tapes to CDs, zines to blogs

Technology changed the subculture in two ways: communication, and the business of music, in both the underground and the mainstream. The music business shifted from album-generated sales to singles, and back. The rise of technology, especially the MP3, revolutionized the music industry, and it is still adapting.

### The MP3

* MP3 files appeared on the internet for the first time in October 1992. [CONFIRM T09-03]
* The Internet Underground Music Archive was created by three people at UC Santa Cruz in 1993, to help unsigned artists release their music and gain a wide audience, circumventing the music industry's model of distribution through a record label. It was a pioneer of internet use for music and popularized independent use of technology to spread music. [CONFIRM T09-04]
* The Fraunhofer Society, a German research group, created the code for compressing audio, called MP3. The first MP3 player, Winplay3, was released on September 9, 1995, allowing people to create their own MP3s. Winamp (1997) and Napster (1999) furthered the rise of the MP3 and the changing face of the music industry. [CONFIRM T09-05]

### The information age and the underground

The teens who grew up alongside 1990s emo, indie and underground music were the world's first fully online generation. The subculture changed in three basic ways. It went from regional to national, because the internet let the Midwest interact with the Northeast in seconds. Its media got an updated look: photocopied zines became glossy magazines. And the way of experiencing the subculture changed.

The online social community is tied inextricably to the growth and popularity of indie culture: Friendster, Makeoutclub, MySpace. This is a move from real community to imagined community. And don't believe the hype: print media is not dead, it is just underground. The technological advances of the mid-1990s changed forever the way the subculture is disseminated, and the exponential speeding up of our culture has changed the landscape. The mixtape, a form of speech particular to the late twentieth century, is being replaced by the playlist.

### From zine to magazine

A zine is a non-commercial, small-circulation publication produced and distributed by its creators. [CONFIRM T09-06]

* ***Cometbus.*** Big in the late 1980s, handwritten by Aaron Cometbus, a crust punk from the East Bay.
* ***No Answers.*** Written by Kent McClard, who later went on to found *HeartattaCk*. Begun in 1983, it was often poetry and photocopied pictures of bands. Its ninth issue was a 7-inch, Downcast (called Ebullition #1), the beginning of a record label that put out records by Ampere, Los Crudos and Reversal of Man. [CONFIRM T09-07]
* ***HeartattaCk.*** 1994 to 2006. It would not review anything with a UPC label. After it ended, several contributors went on to found Give Me Back.
* ***Anti-Matter.*** Published by Norman Brannon in the mid-1990s, a little more professional and intellectual. Brannon went on to play guitar in Texas Is the Reason. [CONFIRM T09-08]
* ***Law of Inertia.*** Ross Siegel, at Cornell. This is seen as one of the major moves from zine to magazine: full-color pages, actual interviews with big bands. [CONFIRM T09-09]
* ***Alternative Press.*** Mike Shea, Cleveland, mid-1980s. Its first headline was "Smiths Tour US." For a few years it was black and white, with interviews with local acts and an occasional large group. It went through a nu metal phase, with covers devoted to Korn, Limp Bizkit and Insane Clown Posse, who was on eight covers. Then it caught on to the early emo bands before it became a buzzword, with Saves the Day, Dashboard Confessional and Thursday all on covers. The magazine grew with the subculture and is now widely read as a kind of "new emo" bible. [CONFIRM T09-10]

## Jawbreaker and Sunny Day Real Estate

An important factor starts to come out of mid-1990s emo bands: they burn out quickly. Why? These two bands are pointed to as the ones that really brought the "down to earth" emotional into emo. The highlight of both, and one that becomes an emo trait, is the connection the audience feels to the band, and burning out quickly because of attention, media and culture. 1994 was the year for both.

### Jawbreaker

Jawbreaker were Blake Schwarzenbach, Chris Bauermeister and Adam Pfahler. They formed at NYU in the 1980s and relocated to San Francisco. In January 1990 they recorded *Unfun*, followed by a short tour and then a hiatus to finish school. *Bivouac* came out in October 1991, and its songs were often lifted right out of Blake's diary. It was slower and gloomier, more complex in structure and instrumentation, with political lyrics replaced by emotional despair, relationship issues and semi-autobiographical episodes. In a sense, the album was a rejection of the fast hardcore of *Unfun*. [CONFIRM T09-11]

In late summer and fall 1992 they went on the "Hell Is on the Way" tour of the Midwest and East Coast, then to Europe for the first time. Over the long tour, Blake's raspy singing caught up with him, and he needed throat surgery in London in early October to remove polyps. [CONFIRM T09-12]

*24 Hour Revenge Therapy* (1994, Tupelo/Communion Records) was, in Rich Egan's words, "just 11 cut and dry little stories about living in the East Bay… straight and to the point." The bulk of it was recorded in Chicago in March with Steve Albini. In the middle they paused to do the "When It Pains, It Roars" tour across the U.S., recorded a few more songs in August 1993 in San Francisco, and in October played a few dates with Nirvana. [CONFIRM T09-13]

"Indictment" is a song Blake introduced as a "Scathing Indictment of the Pop Industry" in some 1992 and 1993 performances. In an early 1992 version he sang different words than on the record, and in some 1996 shows he changed "Will they ever learn?" to "Will we ever learn?" Is this a challenge to the connection between audience and artist? [CONFIRM T09-14]

### Sunny Day Real Estate

Sunny Day Real Estate were Jeremy Enigk, Dan Hoerner, William Goldsmith and Nate Mendel. They were fans of punk, but all accomplished musicians with high ambitions. They existed as a four-piece only briefly before releasing their debut album, and released several 7-inches and EPs before *Diary*. The group was shrouded in mystery from the start: they released only one picture to the press, conducted one interview, and, for some still-unknown reason, never played a show in California with all four members. [CONFIRM T09-15]

*Diary* (1994, Sub Pop) became Sub Pop's best seller behind only Nirvana. It has extremely poetic lyrics, and it was the album that made emo accessible. In September 1994 they played "Seven" on the *Jon Stewart* show, and a few days later recorded several songs for MTV's *120 Minutes*. The sounds they achieved on this album set a specific way of doing emo, and its loud/soft dynamic was reproduced by many groups after them. [CONFIRM T09-16]

After this album Jeremy became a Christian, and the band split up. The rhythm section went on to play with the Foo Fighters. They reunited in 1997 but never achieved the same status.

## Confirmation queue (Topic 9)

```yaml confirmation-queue
- id: T09-01
  type: claim
  priority: low
  claim: The listening list assigns seven songs to this topic with confidence; a few more (Assuck "Alabaster"; Hot Water Music "Southeast First"; At the Drive-In "Pattern Against User"; Twothirtyeight "The Hands of Men") are tentatively assigned to topic 9.
  original_wording: listening list rows marked 9 and 9?
  concern: The "9?" songs are guesses. The original notes mention "Play" cues only for some of the songs listed.
  task: Leave the "9?" songs out unless a connection is found. Note it in the change log.
- id: T09-02
  type: date
  priority: low
  claim: The Warped Tour began on August 9, 1995.
  original_wording: August 9th 1995 Warped Tour begins. This becomes the breeding ground for the new culture of bands aimed at a teenage audience.
  concern: Verify the date and claims about early bands. "Recently" refers to about 2009.
  task: Verify and fix.
- id: T09-03
  type: date
  priority: medium
  claim: MP3 files appeared on the internet for the first time in October 1992.
  original_wording: 1992 oct. mp2 files appeared on the internet for the first time.
  concern: The original says "mp2", probably a slip for mp3 (or MPEG-1 audio layers). Verify.
  task: Verify and fix.
- id: T09-04
  type: claim
  priority: low
  claim: The Internet Underground Music Archive (IUMA) was created by three people at UC Santa Cruz in 1993.
  original_wording: The Internet Underground Music Archive, created by 3 guys at UC, Santa Cruz in 1993.
  concern: Verify founders and year.
  task: Verify and fix.
- id: T09-05
  type: date
  priority: medium
  claim: The Fraunhofer Society created the MP3 code; Winplay3 (first MP3 player) was released September 9, 1995; Winamp 1997; Napster 1999.
  original_wording: The Frounhofer Society, A German research group created the code for compressing audio and called it mp3. Sep. 9th 1995 the first mp3 player, Winplay 3 was released... Winamp 1997, and Napster 1999
  concern: Verify names, dates and the "first" claim.
  task: Verify and fix.
- id: T09-06
  type: source-text
  priority: low
  claim: A zine is a non-commercial, small-circulation publication produced and distributed by its creators.
  original_wording: Zine – non-commercial, small circulation publications which are produced and distributed by their creators.
  concern: Likely from an encyclopedia or glossary.
  task: Check the source. Rewrite or credit.
- id: T09-07
  type: claim
  priority: medium
  claim: 'No Answers: written by Kent McClard (later HeartattaCk); begun in 1983; its ninth issue was the 7-inch Downcast, Ebullition #1; Ebullition released Ampere, Los Crudos and Reversal of Man.'
  original_wording: 'No answers – written by Kent McClard who later went onto found HeartattaCk zine. 1983, often poetry and photocopied pictures of bands. 9th issue was a 7'''' Downcast (called Ebullition #1) beginnings of record label that put out records by Ampere, Los Crudos and Reversal of Man.'
  concern: Verify the claims, year and catalog.
  task: Verify and fix.
- id: T09-08
  type: attribution
  priority: high
  claim: Anti-Matter was published by Norman Brannon, who went on to play guitar in Texas Is the Reason.
  original_wording: 'Anti-matter – Norm Arenas, mid-90s a little more professional and intellectual. Went on to play guitar in Texas is the Reason. (Pasted blurb: "Anti-Matter was conceived and created by Norman Brannon..."). In Topic 12 the notes say "Norm Arenas of Anti-Matter zine and Texas is the Reason."'
  concern: The notes give Norm Arenas as the publisher in one place and the pasted blurb names Norman Brannon. The syllabus reading is "Norman Brannon." Brannon and Arenas are different people (Arenas was in Texas Is the Reason? check). The prose uses Brannon.
  task: Verify who published Anti-Matter and who played in Texas Is the Reason, and fix the text here and in Topic 12.
- id: T09-09
  type: claim
  priority: low
  claim: 'Law of Inertia: Ross Siegel, at Cornell; a major move from zine to magazine.'
  original_wording: Law of Inertia- Ross Seigel at NY Cornell. This is seen as one of the major moves from Zine to magazine.
  concern: Verify the editor's name and school.
  task: Verify and fix.
- id: T09-10
  type: claim
  priority: low
  claim: 'Alternative Press: Mike Shea, Cleveland, mid-1980s; first headline "Smiths Tour US"; nu metal covers (Korn, Limp Bizkit, Insane Clown Posse on eight covers); early emo covers.'
  original_wording: AP – Mike Shea, Cleveland. mid- 80s. First headline "Smiths tour US." ... ICP who was on 8 covers.
  concern: Verify each.
  task: Verify and fix.
- id: T09-11
  type: source-text
  priority: medium
  claim: Jawbreaker background (formed at NYU, Unfun in January 1990, Bivouac in October 1991, a description of Bivouac).
  original_wording: '"the songs were slower and gloomier, but also notably more complex in terms of structure and instrumentation. Gone were any political lyrics..." (pasted from a fan or encyclopedia page)'
  concern: A quoted description appears to be pasted from a web page and is paraphrased here. Verify the dates and "diary" claim.
  task: Find the source. Verify. Rewrite or credit.
- id: T09-12
  type: source-text
  priority: low
  claim: The "Hell Is on the Way" tour and throat surgery in London in October 1992.
  original_wording: '"late summer and fall of 1992, Jawbreaker embarked on the "Hell is on the Way" tour... he required throat surgery in the first week of October in London in order to remove polyps..."'
  concern: Pasted from a web page; paraphrased.
  task: Find the source and verify.
- id: T09-13
  type: claim
  priority: medium
  claim: 24 Hour Revenge Therapy (1994, Tupelo/Communion); Rich Egan's quote; recorded in Chicago in March with Albini; "When It Pains, It Roars" tour; more songs in August 1993; dates with Nirvana in October.
  original_wording: 24 Hour Revenge Therepy, 1994 Tupelo/Communion Records. "24 hour is just 11 cut and dry little stories about living in the East Bay… straight and to the point." Rich Egan. The bulk of the album was recorded in Chicago in March with Steve Albini... Recorded a few more songs in Aug. 1993 in San Fran and in Oct. played a few dates with Nirvana.
  concern: The chronology is confused (a March recording, and an August 1993 recording, for a 1994 release). Verify the quote's author and the dates.
  task: Verify and rewrite the chronology.
- id: T09-14
  type: claim
  priority: low
  claim: Notes on "Indictment" (introduced as a "Scathing Indictment of the Pop Industry" in 1992-93; lyric variants in 1992 and 1996).
  original_wording: Blake introduced the song as "Scathing Indictment of the Pop Industry" in some 1992 and 1993 performances... In some 1996 shows, Blake changes "Will they ever learn?" to "Will we ever learn?"
  concern: Pasted from a fan site. Verify; do not quote more lyrics.
  task: Verify or cut.
- id: T09-15
  type: claim
  priority: medium
  claim: 'Sunny Day Real Estate: lineup; four-piece briefly before the debut; one picture, one interview; never played California with all four.'
  original_wording: 'The group was shrouded in mystery from the get-go: they released only one picture to the press; conducted one interview; and, for some still-unknown reason, never played a show in the state of California with all four members.'
  concern: Appears to be pasted from a web page or review. Verify.
  task: Verify and rewrite or credit.
- id: T09-16
  type: claim
  priority: medium
  claim: 'Diary (1994, Sub Pop): Sub Pop''s best seller behind only Nirvana; in September 1994 played "Seven" on Jon Stewart and recorded for 120 Minutes.'
  original_wording: Became Sub Pop's best seller behind only Nirvana. ... Sep. 1994 played the song Seven on Jon Stewart show, then a few days later recorded several songs for MTV 120 minutes.
  concern: Verify the sales claim and the TV appearances (The Jon Stewart Show).
  task: Verify and fix.
```

<!-- ===== TOPIC 09 END ===== -->

<!-- ===== TOPIC 10 START ===== -->

# Topic 10: New Scenes, Labels, Clubs and Sounds

```yaml agent-meta
topic: 10
slug: topic-10
title: New Scenes, Labels, Clubs and Sounds
syllabus_lessons: 'the mid-1990s labels (Jade Tree, Vagrant, No Idea, Deep Elm); Anatomy of a Scene: Chicago, through the eyes of the Kinsella brothers; Saddle Creek.'
syllabus_readings: 'Vagrant Records (course library); Greenwald chapters 6 and 8. Listening: NPR interview with Mike and Tim Kinsella.'
syllabus_film: '*Spend an Evening with Saddle Creek.*'
old_links_from_original_notes:
- http://www.steakmtn.com/work/0305/
- http://www.deepelm.com/470/
- http://www.joanfrc.com/index.html
- http://www.jadetree.com/images/bands/cap'n_jazz/bio_photo.jpg
- http://www.joanfrc.com/capnjazz.html
- http://artists.letssingit.com/capn-jazz-lyrics-oh-messy-life-7nh1jkc
```

## Overview

This topic covers the mid-to-late 1990s transitions in indie, emo and the underground: the labels that grew up around the music, and the clubs and scenes. The point of looking at a case study like Chicago, and of watching a film about Saddle Creek, is to see how scenes, especially in mid-1990s emo, are incestuous. The mainstream is constantly trying to put everything in one category, while a close look shows that regions still maintained specific sounds.

## Listen and watch

* Cap'n Jazz, "Oh Messy Life" [CONFIRM T10-01]
* American Football, "I'll See You When We're Both Not So Emotional" [CONFIRM T10-01]
* Ghosts and Vodka, "Four Red Brains"
* Owls, "For Nate's Brother Whose Name I Never Knew or Can't Remember"
* Owen, "Skin and Bones"
* Make Believe, "Armscaridica" [CONFIRM T10-01]
* From the listening list: Cursive, "Semantics of Sermon," "A Career in Transcendence" and "The Game of Who Needs Who the Worst"; The Faint, "Victim Convenience"; Bright Eyes, "Sunrise, Sunset"; Tortoise, "Blackjack"
* An NPR interview with Mike and Tim Kinsella, discussed in class

## Films

* *Spend an Evening with Saddle Creek*

## Readings

* Vagrant Records (course library)
* Greenwald, *Nothing Feels Good*, chapters 6 and 8

## Discussion questions

**On labels**

* Vagrant complicates the model of record labels from the 1980s. For many it represents a drastic shift in business practices. Do we agree? Had this shift been coming for a while?
* What was the disagreement between Vagrant and Alkaline Trio? [CONFIRM T10-02]

**On the Kinsella interview**

* The way these brothers think and talk about music is new and different. How?
* What do they say about politics? What is the "collective consciousness" of technology, and how does it affect the masses? Does it undo the Enlightenment?
* They think about music in terms of philosophical ideas and enlightenment of the collective unconscious. What does this represent for the underground? Intellectual versus aggressive. Is this intellectualized approach different from Sonic Youth, Fugazi, Pavement and Guided by Voices?
* How is their inspiration for songs new or different for the underground? Compare the sound of a rock band, which everyone knows, with twisting that sound to make people think outside the norm. Is this artistic abstraction related to Sunny Day Real Estate?
* They talk about the structure of songwriting as split between the members. Is this dichotomy of melodic versus chaotic indicative of the 1990s underground as a whole? Is music a means rather than an end? Emo dynamics of loud/soft equal melodic/chaotic?
* They place emphasis on the process of music as opposed to the product, which continually separates this band, and in a way the new underground, from the mainstream. What about artistic intent? The intentional fallacy and the affective fallacy? [CONFIRM T10-03]
* What about the morality or ethics of being independent? Does it change for these musicians? How does Fugazi's influence show?
* Tim says they are "always conscious of leaving space for the listeners, and the song is not completed until someone hears it." What does he mean? He wants to activate people, to be a conductor, like an electrical circuit: "Not to wake up the masses, but at least to keep myself awake." Compare this with Ted Leo's essay: is there a responsibility for the audience in discriminating about the art you support? How does that work for emo culture? [CONFIRM T10-04]

## The labels

### Jade Tree (Wilmington, Delaware)

Darren Walters and Tim Owen started Jade Tree in August 1991. Both started out with straight edge hardcore labels, and as the genre faded they went in on Jade Tree, specializing at first in post-hardcore and noise rock, then in emo and melodic hardcore. In 1994 they signed Lifetime and put out *Hello Bastards*, an East Coast version of Jawbreaker. In 1996 they released the Promise Ring's *30 Degrees Everywhere*, and in 1997 *Nothing Feels Good*; *30 Degrees* sold 4,000 copies on the road before it was even out. The Promise Ring started as a side project for Davey von Bohlen, singer and guitarist in Cap'n Jazz. Other bands include Jets to Brazil, Pedro the Lion, Texas Is the Reason and The Blood Brothers. [CONFIRM T10-05]

### Vagrant (Santa Monica)

Rich Egan and Jon Cohen founded Vagrant in 1996 out of Egan's management deal with Face to Face. The first release was a compilation called *West by North-South*. Then came the *Before You Were Punk* compilation, featuring pop punk bands playing covers of 1980s new wave hits, which sold 70,000 copies. It caught the attention of The Get Up Kids, from Lawrence, Kansas, whose Doghouse debut, *Four Minute Mile*, was widely popular. Vagrant released *Something to Write Home About* in 1999, caught the new emo buzz, and marketed it to the new fans. Other bands include Alkaline Trio, Dashboard Confessional, Saves the Day and Thrice. [CONFIRM T10-06]

### No Idea (Gainesville, Florida)

Var Thelin founded No Idea as a zine in 1985. With his sixth issue, he put out a 7-inch, the first by the local Gainesville band Doldrums. The bands associated with No Idea span the entire country and various genres: Atom and His Package, Assholeparade, Assuck, I Hate Myself, Planes Mistaken for Stars, Less Than Jake. It is seen as a major contributor to the American punk community and has put out records by more than a few bands labeled "beard punk," most notably Hot Water Music and Against Me. It puts on The Fest every October, which showcases bands from all over. [CONFIRM T10-07]

### PolyVinyl (Illinois)

PolyVinyl began as a fanzine called the *Polyvinyl Press*, which Matt and Darcie Lunsford ran while they were still in high school. They were tight with members of Braid, a quartet from Champaign-Urbana, who convinced them to release their 7-inch single. The roster includes American Football, Rainer Maria, Mates of State and Aloha. [CONFIRM T10-08]

### Doghouse (Toledo, Ohio)

Dirk Hemsath founded Doghouse in 1988, originally to release his own band's material, Majority of One. It is known best as a jumping-off point for other indie labels: The Get Up Kids, Hot Water Music and As Friends Rust all started there. In 2002 it released The All-American Rejects, and in 2004 Warner Music Group bought the label. [CONFIRM T10-09]

### Crank

Jeff Matlow founded Crank in September 1994, in Los Angeles. It is known for putting out records by some early Midwest emo bands: Mineral, Boys Life, The Gloria Record and Cursive (their first record). [CONFIRM T10-10]

### Deep Elm (Charlotte, North Carolina)

John Szuch founded Deep Elm in 1996. It is known mainly for its *Emo Diaries* and *This Is Indie Rock* compilation series, which document emo and introduced more than 135 young bands from around the world, including Jimmy Eat World, Appleseed Cast, Further Seems Forever, Samiam and many more, all with new and unreleased songs. Bands were selected from open submissions, and the label says it has never attempted to define any musical style. It kick-started bands like Appleseed Cast, Benton Falls and The White Octave. [CONFIRM T10-11]

### Saddle Creek

Saddle Creek is covered in the film *Spend an Evening with Saddle Creek*. [CONFIRM T10-12]

## Anatomy of a scene: Chicago

Our case study is the Chicago family of bands: Cap'n Jazz, Joan of Arc, Owls, Make Believe and Owen.

Cap'n Jazz formed in Chicago in 1989 with the brothers Mike and Tim Kinsella, Sam Zurick and Victor Villarreal, and later added Davey von Bohlen. They stayed mainly in the Midwest and released several EPs and songs on compilations. They are known for Tim Kinsella's strange vocal style and lyrics. They put out *Shmap'n Shmazz* in 1995 on Man with Gun. [CONFIRM T10-13]

After that album they went in different directions. Davey went to the Promise Ring. Tim founded Joan of Arc, sometimes including Mike and Sam Zurick. Mike did solo projects, American Football and later Owen. Victor Villarreal played in Ghosts and Vodka. After Joan of Arc broke up in 2001, Tim reassembled the members of Cap'n Jazz, minus Davey, into the band Owls. More recently, Tim, his cousin Nate Kinsella, Sam Zurick and a friend, Bobby Burg, started Make Believe. [CONFIRM T10-14] In 1998 Jade Tree released all of Cap'n Jazz's material in an album called *Analphabetapolothology*. [CONFIRM T10-15]

The band's website describes how they dealt with this exposure. What had been a group of teenage friends playing in a punk band was suddenly being touted by zine culture as a band that had galvanized a genre, "dominating" the Chicago indie scene and helping transform emo from a deeply underground punk subgenre into a more widely accepted subset of indie rock. Those claims were false: their following had been highly regional and by no means dominant, and their influence was probably being distorted by the success of Davey von Bohlen's band, The Promise Ring. And their later band was now tagged with a genre buzzword that didn't fit. [CONFIRM T10-16]

## Confirmation queue (Topic 10)

```yaml confirmation-queue
- id: T10-01
  type: name-or-title
  priority: low
  claim: 'Song titles: Cap''n Jazz "Oh Messy Life"; American Football "I''ll See You When We''re Both Not So Emotional"; Make Believe "Armscaridica."'
  original_wording: 'Cap''n Jazz– This Messy Life; American Football– I''ll see you when we''re both not so emotional; Make Believe- Armscaridica (Play list). Listening list: Cap''n Jazz ''Oh Messy Life''.'
  concern: The notes and the listening list differ, and some titles may be misspelled or incorrect (for example American Football's title, Make Believe's title).
  task: Verify each title and spelling and fix.
- id: T10-02
  type: gap
  priority: low
  claim: There was a disagreement between Vagrant and Alkaline Trio.
  original_wording: Tell me about the disagreement between Vagrant and Alkaline Trio.
  concern: The original poses this as a question to students without describing the disagreement.
  task: Research what happened (dates, nature) and decide whether to add a sentence in the Vagrant section.
- id: T10-03
  type: source-text
  priority: low
  claim: The intentional fallacy and the affective fallacy (literary criticism).
  original_wording: Intentional fallacy, in literary criticism, addresses the assumption that the meaning intended by the author of a literary work is of primary importance... Affective fallacy is a term from literary criticism used to refer to the supposed error of judging or evaluating a text on the basis of its emotional effects on a reader.
  concern: Pasted definitions from an encyclopedia are left out of the prose; only the terms remain.
  task: Decide whether to add a one-sentence definition of each (credit Wimsatt and Beardsley) so the questions make sense to a general reader.
- id: T10-04
  type: quote
  priority: medium
  claim: 'Tim Kinsella: "always conscious of leaving space for the listeners, and the song is not completed until someone hears it"; "Not to wake up the masses, but at least to keep myself awake."'
  original_wording: Tim says they are "always conscious of leaving space for the listeners, and the song is not completed until someone hears it." ... He wants to activate people. Be a conductor, like an electrical circuit. Collective consciousness through mass communication. Everyone filters it in their own way. Not to wake up the masses, but at least to keep myself awake.
  concern: The second quote may be Micah's paraphrase of the interview, not a direct quote. The interview is the NPR interview with Mike and Tim Kinsella.
  task: Find the interview, verify both statements and the speaker, and fix the quotation marks.
- id: T10-05
  type: claim
  priority: medium
  claim: 'Jade Tree: founded August 1991 in Wilmington, Delaware, by Darren Walters and Tim Owen; Lifetime''s Hello Bastards (1994) described as an East Coast version of Jawbreaker; the Promise Ring''s 30 Degrees Everywhere (1996) and Nothing Feels Good (1997); 4,000 copies sold on the road; bands.'
  original_wording: Darren Walters and Tim Owen in August 1991, out of Wilmington, Delaware... In 1994 they signed Lifetime and put out Hello Bastards. It was a east coast version of Jawbreaker. 1996- 30 Degrees Everywhere by Promise Ring, 1997 Nothing Feels Good. 30 Degrees sold 4000 copies on the road before it was out.
  concern: Verify founders, dates, albums and the sales figure. "East Coast version of Jawbreaker" is Micah's comparison.
  task: Verify and fix.
- id: T10-06
  type: claim
  priority: medium
  claim: 'Vagrant: founded 1996 by Rich Egan and Jon Cohen in Santa Monica; West by North-South; Before You Were Punk (70,000 copies); The Get Up Kids'' Four Minute Mile (Doghouse); Something to Write Home About (1999).'
  original_wording: Vagrant – 1996 by Rich Egan and Jon Cohen. Founded in Santa Monica out of Egan's management deal with Face to Face... Then the Before You Were Punk comp... 70,000 copies... Released Something To Write Home About in 1999
  concern: Verify dates, names and figures.
  task: Verify and fix.
- id: T10-07
  type: claim
  priority: low
  claim: 'No Idea: zine in 1985 by Var Thelin in Gainesville; a 7-inch with his sixth issue (Doldrums); "beard punk"; The Fest every October.'
  original_wording: founded as a zine in 1985 by Var Thelin in Gainesville, FL. Put out a 7'' with his 6th issue... puts on The Fest every year in Oct... 2000? First year?
  concern: The year The Fest began is a question in the original and is left out.
  task: Verify and add the first year if confirmed.
- id: T10-08
  type: claim
  priority: medium
  claim: 'PolyVinyl: began as a fanzine run by Matt and Darcie Lunsford in high school; Braid convinced them to release their 7-inch; roster.'
  original_wording: PolyVinyl – founded in Champaign, Il. The label was founded ten years ago by Matt and Darcie Lunsford, in Danville, Illinois...
  concern: The original gives two locations (Champaign and Danville), and "ten years ago" is relative to an unknown date. The description is pasted from a web article.
  task: Verify location and founding date, rewrite in Micah's voice or credit.
- id: T10-09
  type: claim
  priority: medium
  claim: 'Doghouse: founded 1988 in Toledo by Dirk Hemsath for his band Majority of One; a launching pad for The Get Up Kids, Hot Water Music and As Friends Rust; 2002 All-American Rejects; bought by Warner Music Group in 2004.'
  original_wording: founded 1988 in Toledo, OH by Dirk Hemsath. Originally for releasing his bands material Majority of One... 2002 All American Rejects, 2004 label bought by Warner Music Group.
  concern: Verify. The original lists "current bands" as of about 2009 (All American Rejects, Meg and Dia, Say Anything), left out here.
  task: Verify and fix.
- id: T10-10
  type: claim
  priority: medium
  claim: 'Crank: founded September 1994 by Jeff Matlow in Los Angeles.'
  original_wording: Crank – founded Sep. 1994 Jeff Matlow in L.A.?
  concern: The original has a question mark on the location.
  task: Verify and fix.
- id: T10-11
  type: source-text
  priority: medium
  claim: 'Deep Elm: founded 1996 in Charlotte by John Szuch; the Emo Diaries and This Is Indie Rock series; more than 135 bands.'
  original_wording: Over the past ten years, this popular series has been Deep Elm's way of documenting an extraordinary and powerful style of music... "Emo Diaries" has acted as an introduction to over 135 of the best young bands...
  concern: A long quote from the label's website is paraphrased.
  task: Verify and credit or rewrite. Update the 135-band figure if possible.
- id: T10-12
  type: gap
  priority: medium
  claim: Saddle Creek is covered in the film.
  original_wording: 'Saddle Creek – covered in the video on Friday. Don''t Forget to Breathe Jan. 1997. Nowcore: The Punk Rock Evolution.'
  concern: 'The original has two stray items after Saddle Creek ("Don''t Forget to Breathe Jan. 1997" and "Nowcore: The Punk Rock Evolution") that are not explained (possibly releases or compilations).'
  task: Identify them (Saddle Creek, Vagrant or another label) and place or drop. Also add a few sentences on Saddle Creek (founding, bands) if sourced.
- id: T10-13
  type: claim
  priority: medium
  claim: 'Cap''n Jazz: formed in Chicago in 1989 with Mike and Tim Kinsella, Sam Zurick and Victor Villarreal, later adding Davey von Bohlen; Shmap''n Shmazz (1995, Man with Gun).'
  original_wording: Cap'n Jazz was formed 1989 in Chicago with brothers Mike and Tim Kinsella, Sam Zurick, and Victor Villareal. Later added Davey Von Bohlen... Put out Shmap'n Shmazz in 1995 on Man With Gun. This album had an alternate title
  concern: Verify. The original adds that the album had an alternate title (left out); the title and label need checking.
  task: Verify and fix. Add the alternate title if confirmed.
- id: T10-14
  type: claim
  priority: medium
  claim: 'After the album: Davey von Bohlen to the Promise Ring; Tim Kinsella founded Joan of Arc; Mike did American Football and Owen; Victor Villarreal in Ghosts and Vodka; after Joan of Arc broke up in 2001 Tim reassembled Cap''n Jazz minus Davey as Owls; later Make Believe.'
  original_wording: After Joan of Arc's break up in 2001 Tim reassembled the members of Cap'n Jazz minus Davey into the band Owls.
  concern: Joan of Arc did not break up in 2001 as far as I know; the claim probably garbles the timeline. Also verify who played in each band.
  task: Verify the lineup and chronology and fix.
- id: T10-15
  type: claim
  priority: medium
  claim: In 1998 Jade Tree released all of Cap'n Jazz's material in an album called Analphabetapolothology.
  original_wording: 1998 Jade Tree released all of Joan of Arc's material in an album called Analphabetapolothology.
  concern: The original says Joan of Arc, but the album is Cap'n Jazz's anthology. The prose uses Cap'n Jazz.
  task: Verify and fix.
- id: T10-16
  type: source-text
  priority: medium
  claim: A description (from Joan of Arc's website) of how the band dealt with being labeled a genre-defining emo band.
  original_wording: '"What had been a group of teenage friends playing in a punk band was now being touted by zine culture as a band who had galvanized a genre. Suddenly Cap''n Jazz had ''dominated the Chicago indie scene of the early nineties''..."'
  concern: A long quote is paraphrased; the speaker is a band (Joan of Arc). Verify the claims.
  task: Find the original page, and decide whether to quote briefly with credit.
```

<!-- ===== TOPIC 10 END ===== -->

<!-- ===== TOPIC 11 START ===== -->

# Topic 11: Gender in the Underground

```yaml agent-meta
topic: 11
slug: topic-11
title: Gender in the Underground
syllabus_lessons: riot grrrl; queercore; famous women of the underground.
syllabus_readings: Greenwald ch. 9; Kathleen Hanna, Matt Wobensmith, The Gossip, Jody Bleyle and Sleater-Kinney in Sinker; a riot grrrl article (course library); Natalie Porter in Greenberg (p. 121).
syllabus_film: (none recorded)
old_links_from_original_notes:
- http://qzap.org/v5/index.php?option=com_gallery2&Itemid=28&g2_itemId=359
- http://www.youtube.com/watch?v=bLYSWlVKbIE&feature=related
- http://www.youtube.com/watch?v=peFVkDWTdgM&feature=related
```

## Overview

As culture changed and evolved in the 1990s, gender issues peaked in influence. Spurred by the rise of identity politics, mixed with social concerns for freedoms and rights, a new generation of feminists was born, focused on women's rights, gay rights and abortion rights. It happened in mainstream America as well as in the underground, and perhaps more radically and influentially in the underground.

Two major movements came out of punk: riot grrrl and queercore. These gender movements matter because punk and the underground were being taken into cultural movements that were important to the world, and because people outside punk began to realize that DIY and the infrastructure of punk, zines and record labels, were useful for spreading important ideas. The key point: both movements were founded on, and spread mostly through, written media. Zines.

## Listen and watch

* Kathleen Hanna (a video of Bikini Kill, discussed in class)
* Pansy Division (a video, discussed in class)
* From the listening list: Bikini Kill, "Feels Blind"
* The Queer Zine Archive Project (qzap.org), a collection of queer zines

## Readings

* Greenwald, *Nothing Feels Good*, chapter 9
* Kathleen Hanna, Matt Wobensmith, The Gossip, Jody Bleyle and Sleater-Kinney, in Sinker, *We Owe You Nothing*
* A riot grrrl article (course library)
* Natalie Porter, in Greenberg, *Youth Subcultures* (p. 121)

## Discussion questions

* Where did riot grrrl and queercore come from, and what came before them?
* How did zines make these movements possible?
* What happened when the movements met the mainstream press?
* Why did riot grrrl burn out so quickly as a force, and what did it still change?

## Riot grrrl

Riot grrrl did not just happen out of nowhere. The movement was a culmination and continuation of other trends that had been going on before: women in punk, and in the early hardcore and metal scenes. Third-wave feminism was aimed at taking feminism out of intellectualism and academia and making it relevant to real women, and riot grrrl was an offshoot of it, with roots in the music, the DIY ethos and the indie spirit of the underground. As Amy Schroeder of *Venus Zine* put it, "the riot grrrl movement was based on a feminist and DIY philosophy that women can empower themselves by taking action politically and artistically." Amy Spencer, in *DIY: The Rise of Lo-Fi Culture*, writes that the riot grrrls "redefined feminism for the 90s and recognized each other as manufacturers of culture as opposed to participants in a culture they were forced to accept." [CONFIRM T11-01]

The movement was centered on the Pacific Northwest and Washington, DC, and mostly happened in the early 1990s. The major figures include Kathleen Hanna (Bikini Kill, later Le Tigre) and Allison Wolfe (Bratmobile), and the labels Kill Rock Stars (Slim Moon) and K Records in Olympia, Washington, put out many of the bands. It was focused around music, but for many the main concern was spreading the ideals of feminism, through workshops, support groups, festivals and zines. The most popular zines were *Riot Grrrl* and *Revolution Girl Style Now!* (Tobi Vail and Kathleen Hanna). [CONFIRM T11-02]

From August 20 to 25, 1991, K Records put on the International Pop Underground festival, with all-female bands on the first night. [CONFIRM T11-03] In 1992, feeling misrepresented by the mainstream media (including bands like Hole being lumped in with riot grrrl), many of the key players called for a year of non-communication with the press. This created a vacuum that made the media more than interested, to the point of exploitation, and later their slogan "Girl Power" was adopted by the Spice Girls (1996). [CONFIRM T11-04] Riot grrrl burned out quickly as a force but affected change nonetheless, carrying on in bands like Le Tigre (Kathleen Hanna) and Sleater-Kinney (Carrie Brownstein), and in many DIY activist groups since, such as the Radical Cheerleaders.

## Queercore

Queercore is a subgenre of punk music but also a cultural movement for a homosexual voice in the punk community. It, too, did not come out of nowhere: there were gay members of the punk world before queercore. It is a culmination, and a name that grew out of zine culture.

The early queer zines include *JDs*, founded by Bruce LaBruce (gay) and G.B. Jones (lesbian) in Toronto in 1985. They were put out by the gay scene for being punk and on the outskirts of the punk scene for being queer, so they "turned to the traditionally punk medium of the zine to express their views… to reach others with similar attitudes in order to network, share ideas, and develop an alternative culture, which would then blend queer and hardcore identities" (Spencer, p. 41). In February 1989, LaBruce and Jones wrote an article for *Maximum Rocknroll* as a call for queer punks to unite. Other zines included *Homocore* (Tom Jennings, San Francisco), *Holy Titclamps* (Larry Bob, Minneapolis) and *Outpunk* (Matt Wobensmith, San Francisco). [CONFIRM T11-05]

This loosely connected sub-subculture shared ideas through the mail and met for the first time at SPEW, a national queer zine gathering, in May 1991 in Chicago. The bands include Pansy Division, Team Dresch and Fifth Column. Pansy Division opened for Green Day in 1994, took queercore into the mainstream and inspired many to get into the music as well as the subculture. For many, queercore was a political movement more than a musical one. [CONFIRM T11-06]

## Famous women of the underground

* Kim Gordon
* Kathleen Hanna
* Rainer Maria
* Jenny Lewis
* Sleater-Kinney
* Kim Deal (the Pixies, the Breeders)
* Discount [CONFIRM T11-07]

## Confirmation queue (Topic 11)

```yaml confirmation-queue
- id: T11-01
  type: quote
  priority: medium
  claim: 'Amy Schroeder (Venus Zine) and Amy Spencer (DIY: The Rise of Lo-Fi Culture) on riot grrrl.'
  original_wording: '"the riot grrrl movement was based on a feminist and DIY philosophy that women can empower themselves by taking action politically and artistically." Amy Schreoder- Venus Zine. The riot grrrls "redefined feminism for the 90s and recognized each other as manufacturers of culture as opposed to participants in a culture they were forced to accept." Amy Spencer - DIY: rise of lo-fi'
  concern: Verify names, spelling, quotes and sources. "Spencer's book" is also cited at p. 41 below.
  task: Verify both quotes against their sources and fix names and citations.
- id: T11-02
  type: claim
  priority: low
  claim: Riot grrrl was centered on the Pacific Northwest and DC; Hanna, Wolfe; Kill Rock Stars and K; the zines Riot Grrrl and Revolution Girl Style Now! (Tobi Vail and Kathleen Hanna).
  original_wording: Most popular zines – riot grrrl, Revolution Grrrl Style Now! (tobi vail/Kathleen Hanna)
  concern: The original title ("Revolution Grrrl Style Now!") is probably "Revolution Girl Style Now!". Verify who made each zine.
  task: Verify and fix.
- id: T11-03
  type: date
  priority: low
  claim: International Pop Underground festival, August 20-25, 1991, by K Records, with all-female bands on the first night.
  original_wording: Aug. 20-25 1991- International Pop Underground fest put on by K Records. All female bands the first night.
  concern: Verify the dates and the first-night claim.
  task: Verify and fix.
- id: T11-04
  type: claim
  priority: medium
  claim: In 1992 key players called for a year of non-communication with the press; later "Girl Power" was adopted by the Spice Girls (1996).
  original_wording: Media blackout 1992 – feeling misrepresented by mainstream media (including bands like Hole with riot grrrl) many of the key players called for a year of non-communication with the press... Later their slogans "Girl Power" was adopted by Spice Girls (1996)
  concern: Verify the history and the "Girl Power" slogan's origin (Bikini Kill used it).
  task: Verify and fix.
- id: T11-05
  type: claim
  priority: medium
  claim: JDs was founded by Bruce LaBruce and G.B. Jones in Toronto in 1985; they wrote a call for queer punks to MRR in February 1989; the zines Homocore, Holy Titclamps and Outpunk.
  original_wording: JDs- founded by Bruce LaBruce (gay) and GB Jones (Lesbian) in Toronto in 1985... Feb 1989 LaBruce and Jones wrote an article for MRR... Other zines – Homocore- Tom Jennings, San Fran; Holy Titclamps – Larry Bob, Minneapolis; Outpunk- Matt Wobensmith, San Fran
  concern: Verify names, places and dates, and the Spencer quote on p. 41.
  task: Verify and fix.
- id: T11-06
  type: claim
  priority: low
  claim: SPEW, a national queer zine gathering, in May 1991 in Chicago; Pansy Division opened for Green Day in 1994.
  original_wording: met for the first time at SPEW – national queer zine gathering in may 1991. Held in Chicago... Pansy Division opened for Green Day in 1994.
  concern: Verify.
  task: Verify and fix.
- id: T11-07
  type: gap
  priority: medium
  claim: 'The "Famous Women" list has no commentary: Kim Gordon, Kathleen Hanna, Rainer Maria, Jenny Lewis, Sleater-Kinney, Kim Deal, "Discount."'
  original_wording: 'Famous Females: Kim Gordon, Kathleen Hanna, Rainer Maria, Jenny Lewis, Sleater – Kinney, Kim Deal (Pixies Breeders), Discount'
  concern: A bare list. Rainer Maria and Discount are bands, not women. Do not invent commentary.
  task: Note whether to expand with a sentence per entry, using only sourced facts, or drop the list. Verify the names.
```

<!-- ===== TOPIC 11 END ===== -->

<!-- ===== TOPIC 12 START ===== -->

# Topic 12: Religion in the Underground

```yaml agent-meta
topic: 12
slug: topic-12
title: Religion in the Underground
syllabus_lessons: religious themes; Krishnacore; Christian hardcore and Christian underground music; Pedro the Lion.
syllabus_readings: 'Porcell in Sinker; Ray Cappo, Porcell, and Andrew Beaujon''s chapter "The Baffled King" (course library); Robert Wood in Greenberg (p. 223). Listening: NPR interview with Andrew Beaujon.'
syllabus_film: (none recorded)
old_links_from_original_notes:
- http://www.affdoublethink.com/archives/2005/02/15/punk_puritan.php
- http://www.metroland.net/back_issues/vol_27_no38/listen_here.html
- http://www.mp3.com/artist/shelter/summary/
- http://www.punknews.org/review/5557
- http://www.punknews.org/article/22932
- http://www.techgnosis.com/chunkshow-single.php?chunk=chunkfrom-2005-02-15-1437-0.txt
- http://wm05.allmusic.com/cg/amg.dll?p=amg&sql=11:09fexqe5ldje~T1
- http://www.krishnamedia.org/files/teachings/Hare_Krishna_mantra.mp3
- http://www.krishnacore.com/contents.html
- http://www.youtube.com/watch?v=xZ1BSvmPPm8&feature=related
- http://www.youtube.com/watch?v=uy4gr6tCqms&feature=related
- http://www.krishnacore.com/images/pictures/gallery/SHELTER/4.JPG
- http://www.christianrocklyrics.com/unashamed/whostoblame.php
- http://www.indievisionmusic.com/wordpress/2007/04/26/jeff-jacquayunashamed
- http://www.avclub.com/content/node/23015
- http://www.rightrightright.com/index.php?go=6
- http://www.pedro-the-lion.com/
- http://www.hardtofindafriend.blogspot.com/
- http://hardtofindafriend.blogspot.com/2007/11/david-bazan-live-at-grey-eagle-11407.html
- http://www.timmcmahan.com/pedrothelion.htm
- http://www.youtube.com/watch?v=qsnNHd8CwKc&feature=related
- http://www.youtube.com/watch?v=CCobegwdt3o&feature=related
- http://www.onetimesone.com/sound/interviews/pedrothelion.php
```

## Overview

Is the morality and ethics of underground music easily connected to religious ideas? Why is this a theme in a course on underground music? Religion is a part of American culture. Current groups are addressing similar issues. And often the language and ideals of the underground are religious in tone: believe, authenticity, morality, truth, suffering, persecution.

The most obvious link to religious ideas is the connection to straight edge, a moral lifestyle. This topic follows that thread into Krishnacore, then into Christian punk and hardcore, and closes with Pedro the Lion, a band that gives voice to the questions its songwriter has about the Christian upbringing that shaped him.

## Listen and watch

* The Hare Krishna mantra (an audio recording)
* Shelter, videos of live performances
* Strongarm, "Supplication" and "Advent of a Miracle"
* Unashamed, "Who's to Blame" (compared in class with Fugazi's "Suggestion")
* Pedro the Lion, "Letter from a Concerned Follower," and a clip of David Bazan
* A recorded interview with David Bazan
* From the listening list: Shelter, "Civilized Man"; Underoath, "Reinventing Your Exit" [CONFIRM T12-01]

## Readings

* Porcell, in Sinker, *We Owe You Nothing*
* Ray Cappo, Porcell, and Andrew Beaujon's chapter "The Baffled King" (course library)
* Robert Wood, in Greenberg, *Youth Subcultures* (p. 223)
* Listening: an NPR interview with Andrew Beaujon

## Discussion questions

* How is spirituality made a problem for groups that have the label "Christian" attached to them without their permission? (Mutemath, Pedro the Lion.)
* How does Pedro the Lion fit into the underground? Musically and aesthetically it fits our model, but the content is a little different.
* Does spiritual content in lyrics change the authority of a work of art?
* The questions Pedro raises (capitalism, image, anti-authority) fall in line with many other underground artists. Is it important to include the process of belief in discussing this subculture? Why?
* There is a trend in softer folk that is vaguely spiritual. Bands like Iron and Wine use the language and images of religion to tell stories. How much of this storytelling, including religious themes, is part of a new movement in the underground toward abstracting the message and making it more artistic? Can we point to it as a trend?

## Krishnacore

Hare Krishna is a religion in which, by chanting the mantra, you can reach a higher state of life. It is associated with the hippies and the Beatles. As one of its proponents puts it, "Krishna consciousness is not an artificial imposition on the mind; this consciousness is the original energy of the living entity." [CONFIRM T12-02]

Krishna consciousness was introduced to the straight edge subculture by Larry Pugliese in New York City in the early 1980s. He established a house, free food distribution, clothing drives and concerts for punks living on the Lower East Side. Bands like the Cro-Mags and Youth of Today came out of this group, including Ray Cappo and John Porcelly ("Porcell") of Youth of Today and later Shelter, and Harley Flanagan and John Joseph of the Cro-Mags. [CONFIRM T12-03]

Krishnacore describes the portion of the music played by members of the hardcore community connected to the Hare Krishna movement. It had its roots in the early 1980s with bands such as the Cro-Mags and Cause for Alarm (although Krishnacore itself did not exist yet), grew out of straight edge, and established itself as a sect inside hardcore in the early 1990s. [CONFIRM T12-04]

John Joseph of the Cro-Mags met Bad Brains and was inspired by their Rastafarianism, then met some Krishnas in New York. Comparing the Cro-Mags to other Krishna-conscious bands, he says, "It wasn't like we were up on stage in dhotis and chanting. It was all-out assault." In Vedic philosophy there are different kinds of people, he says; not everyone is meant to be a monk, and there were the warriors. He would chant and meditate before going onstage and get into a "mystical-type warrior mentality." [CONFIRM T12-05]

**Youth of Today** (1985-1990) recorded for Positive Force Records and Revelation Records. They were part of the second wave of straight edge, known for positive thinking, melodic hardcore and a New York base. Similar bands: Gorilla Biscuits, Bold and Sick of It All. Ray Cappo is seen as one of the first to move from straight edge to full-on Hare Krishna. In 1989 *Maximum Rocknroll* put him on the cover with the title "Ray Cappo and the Krishnas." The article, written by Tim Yohannon, tried to make the movement look negative, but Ray's responses inspired many to look into it, including Norm Arenas, of the zine *Anti-Matter* and the band Texas Is the Reason. In the early 1990s Cappo went on a trip to India and came back a full priest. [CONFIRM T12-06]

Being accustomed to saying no to many "pleasures of the flesh" made it easier to appreciate and practice the four regulative principles of the Vedas: no meat-eating, no intoxication, no illicit sex and no gambling. Instead of the quantum leap most people are expected to make from materialistic habits, many of these youth found it refreshing to give them up for the greater satisfaction of spiritual practices such as mantra meditation. The major scenes were Brooklyn, Philadelphia and Washington, DC. [CONFIRM T12-07]

**Shelter** (1991-2001) released eleven albums, mostly on Equal Vision and Revelation Records. The members were Porcell and Ray Cappo. Their album *Perfection of Desire* (1992), written by Ray and recorded with friends, helped create the new face of Krishnacore. Norm Arenas played with them to promote their next album. Porcell says, "We don't just do it to put out this positive spiritual message. We do it for our own purification. You can't just shout all these slogans. There's a method to changing your consciousness." He compares Shelter's thunderous growl to the sacred bhajans the devotees sing for hours in the temple: onstage, he is meditating on the lyrics. [CONFIRM T12-08] One writer describes these bands as "not dogmatic robots but thoughtful people negotiating the conflicting demands of traditional religious practice and the chaos of a modern world they do not entirely want to reject." [CONFIRM T12-09]

**Equal Vision Records** was founded by Ray Cappo and Vic DiCara (of the L.A. band Inside Out, which featured Zack de la Rocha) in the Philadelphia temple, to put out Krishnacore records. They sold the label to Steve Reddy in 1992. Bands include Earth Crisis, Shelter and Coheed and Cambria. **Revelation Records** was founded in 1987 by Jordan Cooper and Ray Cappo, originally to put out Warzone's *Lower East Side Crew* 7-inch. It also put out Shai Hulud, and later moved to California. [CONFIRM T12-10]

## Christian punk and hardcore

In Andrew Beaujon's words, the Christian underground "is perched precariously between a subculture that's never been entirely comfortable with what used to be seen as the devil's music and a mainstream that's never been entirely comfortable with what it sees as a recruiting tool for the other side." [CONFIRM T12-11]

The subculture can be pointed to as beginning with Doug Van Pelt's fanzine *Heaven's Metal* in 1985, which combined his three loves: Jesus, hard rock and music journalism. In the 1990s he changed the name to *HM: Hard Music Magazine* and began to include punk, alternative and other new hard genres.

**Tooth and Nail** was founded in 1993 by Brandon Ebel "as a means to give independent artists a forum to creatively express positivity through music." It is an independent label whose artists are often not accepted in the mainstream Christian market. Is this the same split that happens in other genres we have discussed? Is it a subculture within a subculture? Fifty percent of the label's sales are outside the Christian market. [CONFIRM T12-12] MXPX's *Pokinatcha* (1995) was, for many Christian teens who were not allowed to listen to Blink-182 or Green Day, an introduction to the subculture of punk as a whole. They helped create a category that perplexed many (Christian, mainstream, underground), and they said they were Christians in a band, not a Christian band. The album sold a hundred thousand copies. [CONFIRM T12-13]

### Spirit-filled hardcore

This is a brand of hardcore typified by bold, faith-based lyrics, a typical hardcore aesthetic and often a straight edge mentality. It saw its rise and fall in the 1990s.

**Strongarm**, from Pompano Beach, Florida (1993-1998), released two 7-inches and two CDs on Tooth and Nail, and are called the godfathers of Christian hardcore. They traded members with Shai Hulud, and after they broke up most of the members went on to form Further Seems Forever, whose singer, Chris Carrabba, then went on to Dashboard Confessional. They sang blatantly about faith and dealt with the issues of life through their Christianity. Their purpose, as stated at most if not all of their shows, was to be missionaries into the underground. Because the underground was for the most part built on ideas of tolerance and respect, Strongarm was not compartmentalized to Christian audiences, and fan reviews suggest their religious lyrics mattered to fans from all walks of life. [CONFIRM T12-14]

**Unashamed** (1994-1996) built their bold faith-based lyrics around ideas directly lifted from the Bible and conservative morality, instead of the usual punk themes of teen angst, anger and pain. Their music was in the vein of East Coast hardcore and metalcore. "Who's to Blame" is similar in form to Fugazi's "Suggestion."

### Anti-religion

Omega Man and Modest Mouse come at religion from the opposite direction. [CONFIRM T12-15]

## Pedro the Lion

David Bazan, who is Pedro the Lion, was raised Christian, with a father who was a music minister, and was not allowed to listen to secular music until high school. He was inspired by Nirvana and Fugazi: "They're sort of the general-market equivalent of what I loved about Christianity growing up… There was this sense of authenticity and this really strong ethical sense about what they were doing. You felt it in their music, you felt it in everything they were doing." His first band was Coolidge, with Damien Jurado. [CONFIRM T12-16]

Pedro the Lion formed in Seattle in 1995 to emulate slowed-down indie bands like Sebadoh, Bedhead and Low. Bazan calls his style "slow-core." They released an EP, *Whole*, in 1997 on Tooth and Nail, and Bazan played most of the instruments on the first two records, both released on Jade Tree. The lineup changed constantly, and Tim Walsh was the only other semi-regular. They put out four albums and ended their career in 2006; the most notable is *Control* (2002). [CONFIRM T12-17]

The importance of Pedro is that it reflects and gives voice to Bazan's questions about his Christian upbringing, which is generally discouraged in the Christian subculture. At the time he was struggling to define himself outside Christian culture. This is a common theme for many bands that come out of the subgenre: they want to be recognized for their music, not their faith. That happens a lot in the underground, where a high premium is placed on musicality. Of *Whole*, he says, "The band has basically been a document of the tension between living by my own code and being a good Christian." The songs include "Nothing," "Lullaby" and "Secret of the Easy Yoke." [CONFIRM T12-18]

The 1999 EP *The Only Reason I Feel Secure (Is That I Am Validated by My Peers)* includes "Letter from a Concerned Follower." The album *It's Hard to Find a Friend* began to be played on the University of Washington radio station, which allowed Pedro the Lion to play shows outside the church circuit. In reviews he is often called a cynic.

With *Control* (2002), he began to deliberately critique the American system of capitalism and Christian politics. He began to read liberation theology and hard-left literature like Noam Chomsky. Liberation theology "helped me understand my faith. Not what Christianity is but what Jesus talked about. It's very much in line with these things that I am starting to think and feel about politics. About the belief in the unfair nature of corporate America, the political process, and things like that." Here he equates the structure of the American church with a corporation, and the power it holds over those it influences, which is radically different from other bands coming out of the Christian tradition. [CONFIRM T12-19]

Despite his radical stance on America and religion, he is still very popular in the Christian subculture, and he is a divisive figure among his fans. Some swear he is preaching true Christianity, being Christlike, and some cannot get over the fact that he swears and drinks. He always takes questions from the audience. At concerts he is often asked if he is still a Christian, and he usually answers no. Andrew Beaujon asked him why: "I'd rather there just be a misunderstanding because it is not necessary for strangers to know exactly how I feel." He is quite the opposite of the typical Christian model of evangelizing.

## Confirmation queue (Topic 12)

```yaml confirmation-queue
- id: T12-01
  type: claim
  priority: low
  claim: 'Listening-list songs placed in this topic: Shelter "Civilized Man"; Underoath "Reinventing Your Exit" (marked uncertain); Strongarm and Pedro the Lion songs are cued in the notes.'
  original_wording: listening list rows 33, 39, 40, 54, 71 (12, 12?)
  concern: Placement of Underoath is a guess.
  task: Verify or leave out.
- id: T12-02
  type: source-text
  priority: medium
  claim: A quote from a proponent of Hare Krishna about Krishna consciousness and the chanting of the mantra.
  original_wording: '"Krishna consciousness is not an artificial imposition on the mind; this consciousness is the original energy of the living entity. When we hear the transcendental vibration..."'
  concern: The speaker is not named in the original ("one of the proponents of the religion"). It is probably Prabhupada.
  task: Identify the speaker and source. Quote accurately with credit.
- id: T12-03
  type: claim
  priority: medium
  claim: Larry Pugliese introduced Krishna consciousness to straight edge in New York City in the early 1980s; he set up a house, free food distribution, clothing drives and concerts on the Lower East Side; the Cro-Mags and Youth of Today came out of this group; named members.
  original_wording: 'Introduced to the straight edge subculture through Larry Pugliese in NYC in the early 80s... Bands like Cro-Mags, Youth of Today came out of this group. Ray Cappo, John Porcelly (Porcell) of YOT and later Shelter: Harley Flanagan and John Joseph of Cro-Mags.'
  concern: Verify the name, the history and the lineup claims.
  task: Verify and fix.
- id: T12-04
  type: source-text
  priority: medium
  claim: A definition of Krishnacore.
  original_wording: Krishna Core - "A term that describes the portion or the music played by members of the hardcore community connected or adepts to the Hare Krishna movement. Had its roots in the early 80's with bands such as Cro-Mags and Cause For Alarm..."
  concern: A quote from a web page, paraphrased.
  task: Find the source. Rewrite or credit.
- id: T12-05
  type: quote
  priority: medium
  claim: John Joseph of the Cro-Mags on Bad Brains, Rastafarianism, Krishnas, and the warrior mentality.
  original_wording: John Joseph of Cro Mags – met Bad Brains and was inspired by their Rastafarianism. Met some Krishnas in NY and found the Aryan equivalent... "It wasn't like we were up on stage in dhotis and chanting," Joseph says. "It was all-out assault. Even in the Vedic philosophy, there are different kinds of people..."
  concern: The quote is probably from a magazine profile. The original also says he "found the Aryan equivalent," which is sensitive wording and may be a garbled paraphrase; it is left out of the prose.
  task: Find the source (author, date) and verify the quotes. Decide whether anything from the "Aryan equivalent" clause belongs, and reword it carefully if so.
- id: T12-06
  type: claim
  priority: medium
  claim: 'Youth of Today (1985-1990): labels, second-wave straight edge, similar bands; Ray Cappo''s move to Hare Krishna; the 1989 Maximum Rocknroll cover "Ray Cappo and the Krishnas"; the article by Tim Yohannon; Norm Arenas; Cappo''s trip to India and return as a priest.'
  original_wording: Youth of Today – 1985-1990, recorded for Positive Force Records and Revelation Records... 1989 Maximumrockandroll featured him on the cover with the title "Ray Cappo and the Krishnas". The article written by Tim Yohannon tried to make the movement look negative, but Ray's responses inspired many to look into it. Norm Arenas of Anti-Matter zine and Texas is the Reason. In the early 90s he went on a trip to India and came back a full priest.
  concern: Verify the claims. The sentence about Norm Arenas is a fragment. Also see T09-08 about who published Anti-Matter and who was in Texas Is the Reason.
  task: Verify and fix the whole paragraph.
- id: T12-07
  type: source-text
  priority: medium
  claim: The four regulative principles and why straight edge youth found Krishna consciousness a natural step.
  original_wording: Already being accustomed to saying no to many 'pleasures of the flesh' made it easier to appreciate and practice the 4 regulative principles of the Vedas; no meat-eating, no intoxication, no illicit-sex and no gambling...
  concern: Pasted from a web article. Verify "of the Vedas" (these are usually described as principles of the Hare Krishna movement).
  task: Find the source and verify. Rewrite or credit.
- id: T12-08
  type: quote
  priority: medium
  claim: 'Shelter: 1991-2001; eleven albums; Perfection of Desire (1992); Porcell''s quote about purification and bhajans (Spin).'
  original_wording: Shelter – 1991-2001 released 11 albums on mostly Equal Vision and Revelation Records... Perfection of Desire-1992... "We don't just do it to put out this positive spiritual message," adds Porcell... (Spin)
  concern: Verify the claims and the quote and its source (a Spin article).
  task: Verify and fix.
- id: T12-09
  type: quote
  priority: medium
  claim: A quote about "thoughtful people negotiating the conflicting demands of traditional religious practice and the chaos of a modern world."
  original_wording: '"were not dogmatic robots but thoughtful people negotiating the conflicting demands of traditional religious practice and the chaos of a modern world they do not entirely want to reject."'
  concern: No author or source given.
  task: Find the source and credit it, or cut.
- id: T12-10
  type: claim
  priority: medium
  claim: Equal Vision Records was founded by Ray Cappo and Vic DiCara; sold to Steve Reddy in 1992; bands; Revelation Records founded 1987 by Jordan Cooper and Ray Cappo, first for Warzone's Lower East Side Crew 7-inch; later moved to California.
  original_wording: Equal Vision records – founded by Ray Cappo and Vic De Cara (of L.A. band Inside Out featuring Zac De La Rocha). In Philly temple, to put out Krishnacore records. Sold the label to Steve Reddy in 1992... Revelation Records – founded 1987 by Jordan Cooper and Ray Cappo...
  concern: Verify dates, names and the Inside Out connection.
  task: Verify and fix.
- id: T12-11
  type: quote
  priority: medium
  claim: Andrew Beaujon on the Christian underground being "perched precariously" between two subcultures.
  original_wording: '"It is perched precariously between a subculture that''s never been entirely comfortable with what used to be seen as the devils music and a mainstream that''s never been entirely comfortable with what it sees as a recruiting tool for the other side." – Andrew Beaujon'
  concern: Verify the quote and its source (probably Beaujon's book Body Piercing Saved My Life).
  task: Verify and credit with title and year.
- id: T12-12
  type: claim
  priority: medium
  claim: 'Tooth and Nail: founded 1993 by Brandon Ebel; the mission quote; 50 percent of sales outside the Christian market.'
  original_wording: Founded in 1993 by Brandon Ebel. "as a means to give independent artists a forum to creatively express positivity through music."... 50% of the labels sales are outside the Christian market.
  concern: Verify the date, the quote and the 50 percent claim (and date it).
  task: Verify and fix.
- id: T12-13
  type: claim
  priority: low
  claim: MXPX, Pokinatcha (1995); "Christians in a band, not a Christian band"; sold a hundred thousand copies.
  original_wording: MXPX – 1995 Pokinatcha – in a similar vein as Blink182 or Greenday... They said they were Christians in a band, NOT a Christian band. The album sold one hundred thousand copies.
  concern: Verify year, sales and quote.
  task: Verify and fix.
- id: T12-14
  type: claim
  priority: medium
  claim: 'Strongarm: Pompano Beach, Florida; 1993-1998; two 7-inches and two CDs on Tooth and Nail; "godfathers of Christian hardcore"; traded members with Shai Hulud; members formed Further Seems Forever; Chris Carrabba and Dashboard Confessional; "missionaries into the underground."'
  original_wording: Strongarm – From Pompano Beach, FL. 1993-1998. Released 2 7'' and 2 CDs on T&N. called the godfathers of Christian Hardcore... Their purpose, as stated at most if not all of their shows, was as missionaries into the underground.
  concern: Verify the facts and the "godfathers" claim, and the shows statement. A lyric excerpt in the original ("Supplication") is left out.
  task: Verify and fix.
- id: T12-15
  type: gap
  priority: medium
  claim: Omega Man and Modest Mouse are presented as "anti-religion."
  original_wording: 'Anti- Religion: Omega Man; Modest Mouse (link to an AV Club article)'
  concern: The original lists only the names, with no explanation. The prose adds a one-line framing sentence.
  task: Do not invent content. Research and write one or two sentences about each, or cut the subsection.
- id: T12-16
  type: claim
  priority: medium
  claim: 'David Bazan: raised Christian, father a music minister, not allowed secular music until high school; inspired by Nirvana and Fugazi; his first band was Coolidge with Damien Jurado.'
  original_wording: David Bazan, raised Christian, father a music minister. Not allowed to listen to secular music until high school. Inspired by Nirvana, and Fugazi. " They're sort of the general-market equivalent of what I loved about Christianity growing up…" First band was Coolidge with Damien Jurado.
  concern: Verify each claim and the quote source (an interview).
  task: Verify and fix.
- id: T12-17
  type: claim
  priority: medium
  claim: Pedro the Lion formed in Seattle in 1995; Whole EP (1997, Tooth and Nail); first two records on Jade Tree; four albums; ended in 2006; Control (2002).
  original_wording: formed in Seattle in 1995 to emulate slowed down indie bands like Sebadoh, Bedhead, and Low. Calls his style Slow-core. Released an EP Whole in 1997 on Tooth and Nail. Bazan played most of the instruments on the first two records, both released on Jade Tree... Put out 4 albums and ended their career in 2006.
  concern: Verify details and the album count. The label history conflicts (the EP on Tooth and Nail, first two records on Jade Tree).
  task: Verify and fix.
- id: T12-18
  type: claim
  priority: medium
  claim: Bazan was struggling to define himself outside Christian culture when he made Whole; his quote on the tension between his code and being a good Christian; songs "Nothing," "Lullaby," "Secret of the Easy Yoke."
  original_wording: He was 18 at this time and struggling to define himself outside of Christian culture... He says of this record "The band has basically been a document of the tension between living by my own code and being a good Christian."
  concern: The original says he was 18 at this time. The age is left out of the prose because it may not fit the 1997 date of the EP. Lyric excerpts from three songs are left out.
  task: Verify the age and the quote. Add the age only if it is confirmed.
- id: T12-19
  type: quote
  priority: medium
  claim: Bazan on liberation theology and politics, Control (2002), Chomsky; equating the American church with a corporation.
  original_wording: He began to read liberation theology and hard left literature like Noam Chomsky. Liberation theology "helped me understand my faith. Not what Christianity is but what Jesus talked about – it's very much in line with these things..."
  concern: Verify the quote and its source.
  task: Verify and credit.
```

<!-- ===== TOPIC 12 END ===== -->

<!-- ===== TOPIC 13 START ===== -->

# Topic 13: New Weird America and the Folk Re-revival

```yaml agent-meta
topic: 13
slug: topic-13
title: New Weird America and the Folk Re-revival
syllabus_lessons: the folk re-revival; Elliott Smith; new weird America.
syllabus_readings: Elliott Smith (course library); "more readings TBA."
syllabus_film: '*Danielson: A Family Movie.*'
old_links_from_original_notes:
- http://en.wikipedia.org/wiki/Freak_folk
- http://en.wikipedia.org/wiki/New_Weird_America
- http://www.last.fm/group/New++Weird++America
- http://www.bbc.co.uk/dna/collective/A3212740
- http://www.sisterray.co.uk/images/Elliot%20Smith%20From%20A%20basement%20On%20the%20hill.jpg
- http://www.youtube.com/watch?v=0ADiSSNWU90
- http://www.youtube.com/watch?v=8Td2Ce2ZK2M
- http://www.devendrabanhart.com/photospage.html
- http://www.npr.org/templates/story/story.php?storyId=5037501
- http://www.arthurmag.com/player.php?AIDL=1&site=ART
- http://en.wikipedia.org/wiki/The_Golden_Apples_of_the_Sun_%28album%29
- http://www.youtube.com/watch?v=oc_CMLGkBuE&feature=related
- http://entertainment.timesonline.co.uk/tol/arts_and_entertainment/music/article1554704.ece
- http://www.thestranger.com/seattle/Content?oid=74766
- http://www.anus.com/zine/articles/radical_traditionalism/
```

## Overview

Moving from the 1990s into the 2000s, there is again a shift in the underground. It is probably due to the popularization of certain elements (emo, indie) and to technological advances in music production and communication. This topic follows one thread of that shift: the folk re-revival. Elliott Smith is the precursor, a songwriter who took steps toward a folk revival, using songs as stories and approaching music as art. After him comes "New Weird America," the psychedelic folk movement of the early 2000s, which makes direct references and homage to the 1960s.

## Listen and watch

* Elliott Smith, "Needle in the Hay"
* A two-minute NPR story on New Weird America (Devendra Banhart)
* From the listening list: Elliott Smith, "Independence Day"; Iron & Wine, "Promising Light"; Animal Collective, "Leaf House"; Ariel Pink's Haunted Graffiti, "For Kate I Wait"; Devendra Banhart, "It's a Sight to Behold"

## Films

* *Danielson: A Family Movie*

## Readings

* Elliott Smith (course library)
* More readings to be announced [CONFIRM T13-01]

## Discussion questions

* How do Devendra Banhart, Joanna Newsom and Sufjan Stevens compare with The Decemberists and Bright Eyes? Both come out of folk traditions, use similar instruments and are highly acclaimed on college charts, yet Bright Eyes and The Decemberists are also very popular in the mainstream. Why? Is there a difference in the artistic sphere of freak folk? Is it the association with religious themes and language?
* How much of the storytelling in this music, including religious themes, is part of a new movement in the underground toward abstracting the message and making it more artistic?

## Elliott Smith

Elliott Smith died in 2003. He was proficient at many instruments and began his solo career in 1994, and became famous through movies, including *Good Will Hunting* and the films of Wes Anderson. He dealt with depression for many years. The themes of his songs came mainly from philosophy and literature. Musically he was heavily influenced by The Beatles, Bob Dylan and Neil Young, as well as many contemporary artists. [CONFIRM T13-02]

His first two albums were on Kill Rock Stars, and then he moved to Dreamworks. [CONFIRM T13-03] He said of his music: "I like folk songs, but it is a very defined genre, and I think it's not really what I play. For me, the difference between folk and pop is that in folk, there is a clear message in every song and there is usually a moral to the story. That's fine, but it's not how I write. I like more 'impressionistic' things, word pastings. Pop is broader, more things can be in it together." And: "At first, I thought of it as storytelling. It's never seemed confessional to me. I don't need people to understand what it is to be me. It's more like dreams… Pieces are me and pieces are other people and pieces are some character I'm making up." [CONFIRM T13-04]

His influence comes from the steps he took toward a folk revival, using songs as stories and approaching his music as art, and as inspired by art. The direct references and homage to the 1960s are also an important connection, one that gets played up in New Weird America.

## New Weird America

"New Weird America" is the term used to describe the psychedelic folk movement of the early 2000s. It is generally believed to have been coined by David Keenan in the August 2003 issue of *The Wire*, after the Brattleboro Free Folk Festival. It plays on "Old Weird America," a term used by Greil Marcus for the lineage connecting early American folk performers to 1960s folk revivalists like Bob Dylan. [CONFIRM T13-05]

Musically it pulls from the psychedelic folk of the 1960s and 1970s as well as heavy metal, free jazz, electronic music, early American folk and American experimental composers. *Arthur* magazine covered it extensively, put on a festival dedicated to the music, and released a compilation called *The Golden Apples of the Sun* in 2005. It was not a unified movement, and many of the artists do not associate themselves with the label. Of "freak folk," Banhart told the *New York Times*, "it's cool, you have to call it something, but we didn't name it. We've been thinking about what to call it, and we just call it the Family." Ed Droste of Grizzly Bear has said, "Freak-folk comes with an image attached: you have to have a beard and be Jesusy, if you know what I mean. You have to have a really extreme voice, and be really divisive." [CONFIRM T13-06]

The artists associated with New Weird America and freak folk include Akron/Family, Devendra Banhart, Danielson Famile, Espers, Jack Rose, Joanna Newsom, Sufjan Stevens, M. Ward, Iron and Wine, Bonnie "Prince" Billy, Little Wings, Smog, and Wooden Wand and the Vanishing Voice. The music ranges from uber-indie to semi-popular. Many people may have heard of Sufjan Stevens or Iron and Wine, but many more may never hear of Ariel Pink. It goes from weird to aesthetically pleasing.

### Scenes and collectives

The major scene is Northern California (the Bay Area, San Francisco and Oakland), the same area where the Beats in the 1950s and the hippies in the 1960s congregated. Bands there include the Skygreen Leopards, Gris Gris, Thee Oh Sees and Ariel Pink. The music is often associated with new folk collectives: groups of people who play in one another's bands, multi-instrumentalists.

* **Elephant 6** began in Colorado and relocated to Athens, Georgia. Associated bands include The Apples in Stereo, Neutral Milk Hotel and of Montreal. [CONFIRM T13-07]
* **Wooden Wand and the Vanishing Voice** is a collaboration between James Jackson Toth and Jessica Toth (Wooden Wand) and The Vanishing Voice, a Brooklyn band made up of G. Lucas Crane, Heidi Diehl and Steven Jarvis Tavaniere, who met at Purchase College.
* **Animal Collective** is based in New York City, though the members are from Baltimore. They are experimental musicians who met in high school and college and recorded together and separately: Avey Tare (David Portner), Panda Bear (Noah Lennox), Geologist (Brian Weitz) and Deakin (Josh Dibb). They founded Paw Tracks Records.
* **The Skygreen Leopards** began in 2001 as a duo, Glenn Donaldson and Donovan Quinn, in San Francisco; by 2003 they were performing as a band, and have also performed as the Giant Skyflower Band, mixing members from different bands. [CONFIRM T13-08]
* **Ariel Pink** is an avant-garde "hauntology" musician from Los Angeles. He self-produces, often records on a four-track, and has a lo-fi sound. He has been making tapes since 1996, and got some attention by giving a CD-R to Paw Tracks. [CONFIRM T13-09]

### Hauntology and radical traditionalism

Hauntology, as used about this music, orients itself toward ideas and aesthetics thought of as rustic, bizarre or "old-timey": toward the "ghost" of the past. Jim Jupp, who co-founded Ghost Box in 2004 with the graphic designer Julian House, says it is about "delving into the past for inspiration, with the aim of creating an imaginary world, rather than doing exercises in nostalgia." [CONFIRM T13-10]

Radical traditionalism is a view of tradition from within a modern time, and it holds that in order to escape the modern crisis we must first escape the modern mindset. The composer Ralph Shapey called himself a "radical traditionalist": his music combines radical language and romantic sensibility. [CONFIRM T13-11]

## Confirmation queue (Topic 13)

```yaml confirmation-queue
- id: T13-01
  type: gap
  priority: low
  claim: The syllabus lists "more readings TBA" for this topic.
  original_wording: 'Syllabus: "Elliott Smith (course library); more readings TBA"'
  concern: The notes contain links to articles on freak folk, New Weird America, and an NPR piece, but no readings are named.
  task: Identify likely readings from the links in the original notes, or leave this line out.
- id: T13-02
  type: claim
  priority: medium
  claim: 'Elliott Smith: died 2003; began his solo career in 1994; famous through Good Will Hunting and Wes Anderson films; depression; themes of philosophy and literature; influences The Beatles, Bob Dylan and Neil Young.'
  original_wording: Pre-cursor Elliot Smith - died 2003. Proficient at many instruments, began solo career in 1994, became famous through movies. Good Will Hunting, Wes Anderson... Dealt with depression for many years. Themes of his songs came from philosophy, and literature mainly. Musically heavily influenced by The Beatles, Bob Dylan and Neil Young
  concern: Verify the claims, and the framing. Be careful with sensitive details about his death and mental health.
  task: Verify and rephrase sensitively.
- id: T13-03
  type: claim
  priority: medium
  claim: Smith's first two albums were on Kill Rock Stars, then Dreamworks.
  original_wording: First 2 albums on Kill Rock Stars, than moved to Dreamworks.
  concern: His first album (Roman Candle) was on Cavity Search, and Kill Rock Stars released later albums. Check the label history, and also the claim in Topic 4 that KRS released his self-titled album in 1995.
  task: Verify and fix both places.
- id: T13-04
  type: quote
  priority: medium
  claim: Two Elliott Smith quotes about folk, pop and storytelling.
  original_wording: '"I like folk songs, but it is a very defined genre, and I think it''s not really what I play..." "At first, I thought of it as storytelling. It''s never seemed confessional to me..."'
  concern: No source is given for either (probably an interview).
  task: Find the source and verify the exact wording.
- id: T13-05
  type: claim
  priority: medium
  claim: '"New Weird America" was coined by David Keenan in The Wire in August 2003 after the Brattleboro Free Folk Festival; a play on Greil Marcus''s "Old Weird America."'
  original_wording: The term is generally believed to have been coined by David Keenan in the August 2003 issue of The Wire, following the Brattleboro Free Folk Festival. A play of the term Old Weird America, used by Greil Marcus which deals with the lineage connecting early American folk performers with 60s folk revivalists like Bob Dylan.
  concern: Appears to be from an encyclopedia article. Verify the details.
  task: Verify and rewrite or credit.
- id: T13-06
  type: quote
  priority: medium
  claim: Banhart (in the New York Times) and Ed Droste of Grizzly Bear on the term "freak folk"; Arthur magazine's festival and compilation The Golden Apples of the Sun (2005).
  original_wording: Freak-folk - "If you were to ask me how I feel about the term freak-folk," said Banhart to the New York Times... Ed Droste, of Grizzly Bear, has said, "Freak-folk comes with an image attached..." Covered extensively by Arthur Magazine who put on a fest... and released a comp called The Golden Apples of the Sun in 2005.
  concern: The quotes are from an encyclopedia article and need checking against the primary sources.
  task: Verify the quotes and the compilation's year, and credit.
- id: T13-07
  type: claim
  priority: medium
  claim: Elephant 6 began in Colorado and relocated to Athens, Georgia; bands.
  original_wording: Elephant 6 – originally Colorado, relocated to Athens, GA. Bands associated Apples in Stereo, Neutral Milk Hotel, Of Montreal
  concern: Verify the history.
  task: Verify and fix.
- id: T13-08
  type: source-text
  priority: low
  claim: The Skygreen Leopards and Wooden Wand and the Vanishing Voice histories.
  original_wording: The Skygreen Leopards - Brief history. In 2001 (year of the Snake) the Skygreen Leopards began as a duo consisting of Glenn Donaldson and Donovan Quinn in the hobo-Victoria of San Francisco...
  concern: Pasted from the bands' own bios; paraphrased.
  task: Verify and credit or rewrite.
- id: T13-09
  type: claim
  priority: low
  claim: 'Ariel Pink: avant-garde "hauntology" musician from Los Angeles; self-produced, four-track; making tapes since 1996; gave a CD-R to Paw Tracks.'
  original_wording: Ariel Pink – Avant Gaurde/Hauntology musician from LA. Self-produced played recorded often on a 4 track. Lo-fi sound. Making tapes since 1996, got some attention by giving a cd-r to Paw Tracks.
  concern: Verify.
  task: Verify and fix.
- id: T13-10
  type: source-text
  priority: medium
  claim: A definition of hauntology and a quote from Jim Jupp of Ghost Box.
  original_wording: Hauntology - to orient itself towards ideas and aesthetics that are thought of as rustic, bizarre or "old-timey"; that is, towards the "ghost" of the past. "Essentially, we're delving into the past for inspiration, with the aim of creating an imaginary world, rather than doing exercises in nostalgia," says Jim Jupp
  concern: Pasted from a Wikipedia entry and a Times article; a longer quote from the K-Punk blog is left out.
  task: Verify and credit or rewrite. Decide whether the K-Punk passage belongs.
- id: T13-11
  type: source-text
  priority: medium
  claim: A definition of radical traditionalism, and Ralph Shapey as a "radical traditionalist."
  original_wording: Radical Traditionalism is a view of tradition from within a modern time... Ralph Shapey - composer "Radical traditionalist" is what I've been called. My music combines two fundamentally contradictory impulses--radical language and romantic sensibility.
  concern: The definition is pasted from a website (anus.com, a site tied to a radical-traditionalist movement that may not be appropriate to cite). The Shapey quote is from the composer.
  task: Check the sources. Strongly consider dropping the web definition and keeping only the Shapey quote, correctly cited.
```

<!-- ===== TOPIC 13 END ===== -->

<!-- ===== TOPIC 14 START ===== -->

# Topic 14: Visual Art and Authenticity

```yaml agent-meta
topic: 14
slug: topic-14
title: Visual Art and Authenticity
syllabus_lessons: art in the underground; album cover meaning and message; poster art; film and photography; Raymond Pettibon, Winston Smith, Art Chantry, Frank Kozik, Jem Cohen; Scott Sinclair and Hot Water Music's album covers.
syllabus_readings: '"An Artist''s Eye and a Killer''s Touch" and the Kozik, Chantry, Winston Smith and Jem Cohen interviews in Sinker.'
syllabus_film: (none recorded)
old_links_from_original_notes:
- http://www.philipsleingallery.com/view.php?todo=viewone&which=1143662216&rtst=42
- http://www.philipsleingallery.com/view.php?todo=viewone&which=1138474955&rtst=42
- http://www.fkozik.com/
- http://winstonsmith.com/gallery/albums/
- http://winstonsmith.com/gallery/albums/small/greenday.html
- http://jemcohenfilms.com/wp/
- http://jemcohenfilms.com/wp/news-upcoming-screenings/
```

## Overview

The common thought, when discussing punk art, is that it is associated with the working class, a lack of skill, and carelessness about making art. That is not to say it lacks meaning for the people producing it, but viewed from the outside it does not at first come off as high art. The artists in this topic are working against that misconception. They create the visuals that accompany the subculture, sometimes affecting the mainstream culture more than the music or its messages.

This topic is about high art versus low art in the underground: the poster and album cover artists Art Chantry, Frank Kozik and Winston Smith, and the filmmaker Jem Cohen.

## Listen and watch

* Posters and album covers by Art Chantry, Frank Kozik and Winston Smith
* Winston Smith's cover for the Dead Kennedys' *In God We Trust, Inc.*
* Winston Smith's cover for Green Day's *Insomniac*
* Films by Jem Cohen: Fugazi's *Instrument* and Elliott Smith's *Lucky Three*

## Films

* *Instrument* (Jem Cohen's film about Fugazi; see Topics 6 and 8)

## Readings

* "An Artist's Eye and a Killer's Touch," in Sinker, *We Owe You Nothing*
* The Frank Kozik, Art Chantry, Winston Smith and Jem Cohen interviews, in Sinker

## Discussion questions

* Chantry echoes the sentiment that, because DIY is accessible to everyone, we end up with a lot of mediocre art. Is that fair?
* Chantry has "one foot in subculture, one foot in mainstream." Is that dangerous? Is it selling out, or compromising his principles? Chantry seems unconcerned with the commercialization of underground art. Why?
* Is what we are doing in this class something negative? (See Chantry, p. 192.) [CONFIRM T14-01]
* Frank Kozik represents an extremely different voice from what we have heard in the underground: he loves America. How does such an alternate view fit into an underground that is so vehemently leftist and anti-capitalist?
* Winston Smith's work uses the juxtaposition of images to create masterful critiques of suburban culture and capitalist ideologies (Sinker). "You've gotta hit people over the head?" Is that what many graphic artists are doing? The underground as a whole?
* Smith says, "I think that's what happens in a lot of art: people see their own life experience in it." Is this true of the connections between audience and artist, musical or graphic, in the underground? Is the eye of the beholder in this subculture searching for a deeper form of authenticity, and therefore finding it in the art it consumes?

## Art Chantry

Art Chantry is credited with creating the graphic art language of the Seattle grunge scene. He talks a lot about the shift from handmade art to computers, and says computers are the last or newest form of DIY. [CONFIRM T14-02] He also echoes the sentiment that, through the accessibility of DIY to everyone, we end up with a lot of mediocre art. In his words, he has "one foot in subculture, one foot in mainstream." [CONFIRM T14-03]

## Frank Kozik

Frank Kozik has done poster art for everyone from the Beastie Boys to Iggy Pop to the Misfits. He was born in Madrid, Spain, in 1962, moved to the United States at fourteen and settled in Austin, Texas. He is credited with single-handedly reviving the "lost" art of the concert poster. His creative career grew out of his enthusiasm for Austin's growing underground rock scene in the mid-1980s, starting with black-and-white flyers for friends' bands posted on telephone poles. His reputation grew as an artist whose work was graphically compelling and culturally gripping, with hundreds of full-color, limited-edition, silkscreened posters for artists such as Nirvana, Pearl Jam, the Red Hot Chili Peppers and the Beastie Boys. He is associated with the Man's Ruin record label, which primarily put out records, although it branched out into CDs. [CONFIRM T14-04]

## Winston Smith

Winston Smith made the cover of the Dead Kennedys' *In God We Trust, Inc.* In the words of the Sinker collection, he "uses the juxtaposition of images to create masterful critiques of suburban culture and capitalist ideologies." [CONFIRM T14-05] He also made the cover of Green Day's *Insomniac*, which comes with its own story. [CONFIRM T14-06]

## Jem Cohen

Jem Cohen is a filmmaker. His work includes Fugazi's *Instrument* and Elliott Smith's *Lucky Three*. [CONFIRM T14-07]

## Confirmation queue (Topic 14)

```yaml confirmation-queue
- id: T14-01
  type: quote
  priority: medium
  claim: A quote on page 192 of the Chantry interview, asking if what the class is doing is something negative.
  original_wording: Read quote on page 192- is this what we are doing in the class? Something negative?
  concern: The quote on p. 192 is not in the original notes, so the question makes little sense without it.
  task: Find the quote on p. 192 of Sinker's Chantry interview and add it, or drop the question.
- id: T14-02
  type: claim
  priority: low
  claim: Art Chantry is credited with creating the graphic art language of the Seattle grunge scene; he says computers are the last or newest form of DIY.
  original_wording: credited with creating the graphic art language of Seattle grunge scene. Talks a lot about the shift from handmade art to computers. Says computers are the last or newest form of DIY.
  concern: Verify and attribute. The same idea appears in Topic 6 ("The only venue left for DIY is the computer," Sinker, p. 189).
  task: Verify and fix, and check consistency with Topic 6.
- id: T14-03
  type: quote
  priority: low
  claim: 'Chantry: "One foot in subculture, one foot in mainstream."'
  original_wording: '"One foot in subculture, one foot in mainstream." Dangerous, selling out, compromise his principles?'
  concern: Verify the quote and whether it is in quotation marks in Sinker.
  task: Verify.
- id: T14-04
  type: source-text
  priority: medium
  claim: A biography of Frank Kozik (born in Madrid in 1962, Austin, the concert poster revival, famous posters, Man's Ruin).
  original_wording: '"Frank Kozik was born in Madrid, Spain in 1962. At the age of 14, he moved to the United States and settled in Austin Texas. Credited with single handedly reviving the ''lost'' art of the concert poster..." (From his website)'
  concern: A long passage from his website is paraphrased. Verify and credit or rewrite.
  task: Verify against his site and the Sinker interview.
- id: T14-05
  type: quote
  priority: low
  claim: Winston Smith "uses the juxtaposition of images to create masterful critiques of suburban culture and capitalist ideologies" (Sinker).
  original_wording: Uses the juxtaposition of images to create masterful critiques of suburban culture and capitalist ideologies. –Sinker.
  concern: Verify the wording and attribution within Sinker.
  task: Verify.
- id: T14-06
  type: gap
  priority: low
  claim: Winston Smith's Green Day cover "comes with its own story."
  original_wording: Green Day's Insomniac. ... cool story
  concern: The original says only "cool story." The prose is a placeholder.
  task: Find the story (Smith's account of the Insomniac cover) and write one or two sentences, or cut the sentence.
- id: T14-07
  type: gap
  priority: medium
  claim: Jem Cohen is a filmmaker; his work includes Instrument and Lucky Three.
  original_wording: 'Jem Cohen: Fugazi Instrument, Elliot Smith Lucky Three. "facts quote p. 170"'
  concern: The original has almost nothing else, and a note about a quote on p. 170 that is not included. The syllabus also lists the artists Raymond Pettibon and Scott Sinclair and Hot Water Music covers, which the original notes do not cover.
  task: Add a sourced paragraph on Cohen from the Sinker interview (p. 170). Do not invent content for Pettibon or Sinclair; report whether Micah should add them.
```

<!-- ===== TOPIC 14 END ===== -->

<!-- ===== TOPIC 15 START ===== -->

# Topic 15: Is "Underground" Still Possible?

```yaml agent-meta
topic: 15
slug: topic-15
title: Is "Underground" Still Possible?
syllabus_lessons: new meanings of indie; blogs; indie and the future.
syllabus_readings: (none recorded)
syllabus_film: (none recorded)
old_links_from_original_notes:
- http://en.wikipedia.org/wiki/Freak_folk
- http://en.wikipedia.org/wiki/New_Weird_America
- http://www.last.fm/group/New++Weird++America
- http://www.bbc.co.uk/dna/collective/A3212740
```

## Overview

Moving from the 1990s into the 2000s, there is again a shift in the underground, probably due to the popularization of certain elements (emo, indie) and to technological advances in music production and communication. What is the definition of indie now? Does it reflect the history of this subculture? Is "underground" still possible?

The timeline of the underground is now almost long enough to start to see patterns. In cultural movements there is often a movement followed by a counter-movement. Is there a pendulum swinging from one extreme to another in this subculture, from art to action?

## Listen and watch

* From the listening list: Modest Mouse, "Ocean Breathes Salty"; The National, "Looking for Astronauts"; Sufjan Stevens, "The Predatory Wasp of the Palisades Is Out to Get Us!"; Arcade Fire, "No Cars Go"; Bon Iver, "Skinny Love"; Feist, "I Feel It All"; MGMT, "The Youth"

## Readings

None listed for this topic. [CONFIRM T15-01]

## Discussion questions

* What is the definition of indie now? Does it reflect the history of this subculture?
* Is underground still possible?
* Is there a pendulum swinging from one extreme to another in our subculture? Art to action?
* Is it a fair assumption to say that the indie underground is moving more toward artistic and intellectual sensibilities, or toward aggressive ones?
* Where will the next Seattle be?

## Where things stand

By this time in history it can be said that there is a fan culture surrounding this music: a distinct culture, often divorced from its history, yet pulling from it. A lot of the precedents set by the early underground are being reflected in new ways.

For example, DIY was adopted into technology, and now it is coming out of it again, with a return to print zines, 7-inch records, LPs and house shows.

Is it a fair assumption that the indie underground is moving more toward artistic and intellectual sensibilities, or toward aggressive ones? In certain genres, yes. The folk re-revival and New Weird America (Topic 13) are one example of the artistic direction.

## Confirmation queue (Topic 15)

```yaml confirmation-queue
- id: T15-01
  type: gap
  priority: high
  claim: 'This topic is thin: the original notes give only a short set of questions and two observations (fan culture; DIY coming out of technology).'
  original_wording: 'Syllabus lessons: new meanings of indie; blogs; indie and the future. Notes: "Week Fourteen Theme- Is underground still possible? 1. Indie and the Future" followed by about 300 words of questions and observations, then the topic on folk (Topic 13) and visual art (Topic 14).'
  concern: The syllabus lessons on new meanings of indie and blogs have no notes behind them (blogs appear in Topic 9, in the technology section). The listening list assigns seven songs here with no discussion.
  task: Do not invent content. Report whether this topic should be merged into Topic 13 or Topic 9 or expanded by Micah. If the agent can research it, propose a short sourced section for Micah to approve, clearly separated from the rest.
```

<!-- ===== TOPIC 15 END ===== -->

<!-- ===== TOPIC 16 START ===== -->

# Topic 16: Florida's Underground Music Scenes

```yaml agent-meta
topic: 16
slug: topic-16
title: Florida's Underground Music Scenes
syllabus_lessons: a special lecture, and in one version a symposium, on the Florida scenes. The FSView article also mentions an April 2009 symposium on artistry and business in independent music.
syllabus_readings: (none recorded)
syllabus_film: (none recorded)
old_links_from_original_notes: []
```

## Overview

Florida has a distinct personality in the underground. It is a product of several things: geography, demography, and a history of punk that is the same as the national story but that, for some reason, the national story did not acknowledge. This topic walks through that history and the state's three regional scenes, and ends with a shift in the early 2000s from heavy music toward emo.

## Listen and watch

* Florida bands from the course listening list: Floor, "Scimitar"; Hot Water Music, "Southeast First"; Twothirtyeight, "The Hands of Men"; Strongarm, "Supplication" and "Advent of a Miracle"; Assuck, "Alabaster"; Underoath, "Reinventing Your Exit" [CONFIRM T16-01]

## Readings

None listed for this topic. The lecture was a special lecture on the Florida scenes. [CONFIRM T16-02]

## Discussion questions

* Why does Gainesville have such a thriving DIY community? Is it the university?
* How does the influx of people affect the underground? (New ideas, music and movements come in, and a sense of nativism that can mix with underground culture.)
* In a state where scenes are divided by region and not by city, what does "scene" mean?

## Geography and demography

**Geography.** Disconnected from the rest of the country, Florida has historically been left out of certain groupings: it is the southernmost state in the Union and yet not considered part of "the South." It is 361 miles wide and 447 miles long. For the underground, this meant that much of the foundational work done in the 1980s, touring networks most especially, overlooked Florida as a possibility. This changed somewhat through the 1990s, as Gainesville became a punk epicenter and tours started to dip further south. [CONFIRM T16-03]

**Demography.** Florida is typically known for two things, Miami and Disney (the space program may also be included). The ebb and flow of population due to attractions makes Florida a very different state from any other, and the snowbird and tourist market has a profound effect on the state's identity. It is the nation's third-fastest-growing state, and has historically grown by outstanding numbers: between 1950 and 1960, the population grew by 78 percent. It is the fourth most populous state, after California, Texas and New York. [CONFIRM T16-04] Most of the population lives along the coast, so the highway becomes the main thoroughfare for travel, and automobile culture is very different from public transportation culture.

The influx of people has a cause-and-effect relationship with the underground. First, it allows new ideas, music and movements to come in. Second, it creates a sense of nativism, which can and does mix with underground culture: the "Florida cracker." Both factors play into the growth and influences of the underground culture.

## A history of Florida punk

The history of Florida punk is the same as national punk, but for some reason Florida was not acknowledged. The story of the scene's history works in conjunction with the regional divisions. The period between 1994 and 2001 was a sort of Renaissance, with many different trends in music reflected across the state.

* **Early 1990s, punk and ska:** HWM and Less Than Jake. [CONFIRM T16-05]
* **Mid-1990s, emo and indie:** Peterbuilt, Carlisle, Recess Theory, Divine Child (Denison Mars), Twothirtyeight, and Bagwell and The Miracle Youth.
* **Late 1990s and early 2000s, hardcore:** Poison the Well, Floor, Shai Hulud, Red Roses for a Blue Lady and Dragbody.

## The three regional scenes

The major scenes connect with another state-specific trait: while a specific city is often associated with a scene elsewhere, in Florida scenes are divided into regions.

### North Florida

North Florida takes in Pensacola, Tallahassee, Gainesville and Jacksonville. Gainesville has had the most vibrant and centralizing scene, thanks to its inclusion in the touring networks that came to Athens, Georgia, and even Atlanta. It is home to No Idea Records, Fueled by Ramen and Boxcar Records. [CONFIRM T16-06] Gainesville has a thriving DIY community. Why? Is it the university? There is the Wayward Council (a bookstore, music store and DIY venue), the Civic Media Center (an alternative press archive and library), and The Fest, originally called Gainesville Fest.

No Idea is the cornerstone of the Florida underground scene. Its roster includes bands from all over Florida and eventually the U.S. Var Thelin founded it as a zine in 1985. For the sixth issue he decided to put out 7-inch records, the first by a local band called Doldrums and the second a split with Crimpshrine, of Berkeley. The early Gainesville bands mentioned as starting a semblance of a scene are Spoke and Radon, which existed around 1990-1993 and gave rise to the second generation of Gainesville bands. [CONFIRM T16-07] One of them is Hot Water Music: beard punk, gruff vocals, very musically inclined, with an extreme focus on community and making your own way.

### Central Florida

If Gainesville was the head of the Floridian body of music, central Florida was its heart and soul. The melodic strain of Florida music often centralized here. The region includes Melbourne and the beaches, Orlando, Vero Beach and Lakeland. (Tampa and Ocala could fall in here, but their scenes were more aligned with the South Florida hardcore sound.)

Central Florida had a thriving underground Christian music scene for a while, especially in Melbourne: Dear Ephesus and Once Fallen. The Tab was a church that allowed punk shows and was organized by a body of locals who came to be called the Little Reggies, set up very much like 924 Gilman. [CONFIRM T16-08]

Orlando, as the center of central Florida, has long been touted as the center of the underground. The depth and history of the Orlando scene is still being uncovered. In the mid-1990s it was centered on Sapphire Supper Club (The Social) and Park Ave CDs, in Winter Park. As tours started coming to Florida, they would end up at Sapphire or at Club Firestone, in the heart of downtown Orlando on Orange Avenue. Sapphire was *the* place where many cross-state relationships were formed, fostered and continued. There was also a little record store called DIY, near UCF, founded in 1997, which carried a large collection of vinyl and hosted shows in a small area in the back. Jeff Hogan and Anthony Torres put together a compilation of local Orlando bands called *The Spirit of 99*. [CONFIRM T16-09] Famous Orlando bands include Peterbuilt, whose members went on to My Hotel Year, Carlisle, Legends of Rodeo (Lake Worth) and The Miracle Youth.

Lakeland also had an important influence. It supported a smaller scene centered on house shows and The Mad Hatter, and produced a few bands in the screamo genre (Cowboys Become Folk Heroes) and SAGOH 24/7, later Anberlin.

### South Florida

South Florida takes in Pompano Beach, West Palm Beach, Miami and Fort Lauderdale. It is most often associated with South Florida hardcore, and also with New Found Glory and Dashboard Confessional. This is a different brand of hardcore from what we have discussed so far: hardcore concerned with melody, with riffs similar to metal, and very musically technical. Bands of note are Strongarm, Shai Hulud, The Young and the Useless, Poison the Well and Floor. There is no real center of activity; it is a wide genre with an expansive geographic reach.

Respectables Street Café in West Palm Beach has hosted about every major band from Florida and the underground since it opened in 1987. It was founded by Rodney Mayo. [CONFIRM T16-10]

South Florida also represents an important shift in Florida music. When Strongarm broke up, the remaining members formed a band called Further Seems Forever. This band and its style were caught in the midst of the emo craze of the early 2000s. Then its lead singer went on to form Dashboard Confessional, which became for many the face of emo in America. The shift from heavy music to emo-inspired music resonated across the state at around the same time, and Underoath is a perfect example. Some did not make the shift: the Tampa scene is still essentially heavy, and there are scenes that host lots of heavy bands, but for a while it seemed that the emo movement was overtaking Florida.

## Confirmation queue (Topic 16)

```yaml confirmation-queue
- id: T16-01
  type: claim
  priority: low
  claim: The listening-list songs from Florida bands, placed here.
  original_wording: listening list rows 59, 53?, 66?, 39, 40, 49?, 71? (assigned by topic guesses to 7, 9?, 9?, 12, 12, 9?, 12?)
  concern: These are assigned to other topics on the list, and several are uncertain. The notes name no songs for this topic.
  task: Decide whether to keep these here or leave them in their other topics. Verify that each band is from Florida.
- id: T16-02
  type: gap
  priority: medium
  claim: The Florida lecture is a special lecture.
  original_wording: 'Syllabus: "a special lecture, and in one version a symposium, on the Florida scenes." The notes: a section titled "Florida" appears after "Review" at the end.'
  concern: The syllabus mentions a symposium (April 2009, on artistry and business in independent music); the notes do not cover it. No readings are named.
  task: Do not invent content. Note whether Micah should add the symposium or readings.
- id: T16-03
  type: claim
  priority: low
  claim: Florida is the southernmost state and not considered part of "the South"; it is 361 miles wide and 447 miles long; Gainesville became a punk epicenter in the 1990s.
  original_wording: disconnected from the greater US, FL has historically been left out of certain groupings, ie. We are the southern most state in the Union and yet not considered part of the 'South'. FL is 361 miles wide and 447 miles long
  concern: '"Southernmost state" is wrong (Hawaii is farther south) unless "southernmost in the contiguous states." The cultural claim about "the South" is an opinion. Verify the dimensions.'
  task: Verify and fix, with correct wording.
- id: T16-04
  type: number-or-stat
  priority: medium
  claim: Florida is the nation's third-fastest-growing state; 78 percent growth between 1950 and 1960; fourth most populous state, after California, Texas and New York.
  original_wording: FL is the nations 3rd fastest growing state... Between 1950 and 1960 FL grew by 78%. It is the 4th most populated state in the US (following CA, TX and NY).
  concern: Rankings are as of about 2009 and have changed (Florida is now third). Verify the 1950-60 figure.
  task: Verify and date or update. Rewrite the sentences accordingly.
- id: T16-05
  type: name-or-title
  priority: low
  claim: 'Early 1990s punk and ska: HWM and Less Than Jake.'
  original_wording: 'Early 90s- Punk/Ska: HWM, Less Than Jake'
  concern: '"HWM" is ambiguous (Hot Water Music is discussed in Gainesville, but formed in 1994).'
  task: Clarify and fix. Verify the band names in each decade's list (Peterbuilt, Carlisle, Recess Theory, Divine Child, Twothirtyeight, Bagwell, The Miracle Youth, Poison the Well, Floor, Shai Hulud, Red Roses for a Blue Lady, Dragbody).
- id: T16-06
  type: claim
  priority: medium
  claim: Gainesville is home to No Idea Records, Fueled by Ramen and Boxcar Records; it had the most centralizing scene thanks to Athens and Atlanta touring networks; the Wayward Council, the Civic Media Center, The Fest (originally Gainesville Fest).
  original_wording: Home to No Idea Records, Fueled By Ramen records and Boxcar Records... Wayward Council – bookstore, music store, DIY venue. Civic Media Center - Alternative press archive library. The Fest – originally called Gainesville Fest
  concern: Verify each; record labels moved over time.
  task: Verify and fix, and date each statement ("was founded in Gainesville").
- id: T16-07
  type: claim
  priority: medium
  claim: No Idea's history (zine in 1985, sixth issue Doldrums 7-inch, second a split with Crimpshrine); Spoke and Radon around 1990-1993; Hot Water Music.
  original_wording: Was founded in 1985 as a zine by Var Thelin. For the 6th issue he decided to put out 7'' records the first one being a local band called Doldrums, the second being a split with Crimpshrine, of Berkeley, CA. Early g-ville bands... Spoke and Radon. Both existed around 1990-1993
  concern: Verify. This repeats Topic 10's No Idea section; check consistency.
  task: Verify and make the two topics consistent.
- id: T16-08
  type: claim
  priority: low
  claim: The Tab was a church that allowed punk shows, organized by locals called the Little Reggies, set up very similarly to 924 Gilman; Dear Ephesus and Once Fallen in Melbourne.
  original_wording: The Tab was a church that allowed punk shows and was organized by a body of locals who came to be called Little Reggies. Set up very similarly to 924 Gilman.
  concern: Local history likely from personal knowledge. Verify with local sources or ask Micah to confirm.
  task: Research. If not verifiable, mark it as Micah's own account and keep.
- id: T16-09
  type: claim
  priority: low
  claim: 'The Orlando scene: Sapphire Supper Club (The Social), Park Ave CDs, Club Firestone, the record store DIY near UCF (founded 1997), and the compilation The Spirit of 99 by Jeff Hogan and Anthony Torres.'
  original_wording: In the mid-90s it was centered around Sapphire Supper Club (The Social), and Park Ave CDs (Winter Park)... There was also a little record store called DIY, located near UCF. It was founded in 1997... Jeff Hogan and Anthony Torres put together a compilation called The Spirit of 99
  concern: Local history likely from personal knowledge. The venue's name and year may need checking.
  task: Research. If not verifiable, mark as Micah's own account and keep.
- id: T16-10
  type: name-or-title
  priority: low
  claim: Respectables Street Café in West Palm Beach has hosted nearly every major band from Florida and the underground since it opened in 1987; it was founded by Rodney Mayo.
  original_wording: Repectables Street Café in West Palm Beach has hosted about every major band from FL and in the underground since it opened in 1987. Founded by Rodney Mayo.
  concern: Spelling of the venue's name; the date and founder; the sweeping claim.
  task: Verify and fix.
```

<!-- ===== TOPIC 16 END ===== -->
