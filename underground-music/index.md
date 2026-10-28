<!--
  Course home page. The list of topics at the bottom builds itself:
  every file named topic-XX.md in this folder shows up automatically,
  in order, using its title and summary.
-->

# Underground Music in America: 1980 – Present

From Minor Threat to Mineral, underground music has moved and changed the youth culture in America over the decades since 1980.

![Course flyer: a crowd surrounds a singer at a hardcore show. Text reads "Underground Music in America, 1980-Present, AMS 3810-01".](/underground-music/images/course-flyer.jpg)

This site is an archive of an undergraduate course I taught at Florida State University while I was in graduate school, for five semesters. It collects my lecture notes, the music and films we listened to and watched, and the readings.

## Course description

Underground Music in America focuses upon the musical heritage that grew from the Punk traditions in the late seventies. Often overlooked as naive ignorance and teenage emotionalism, this music has had lasting effects on the ideals of youth and sub-cultures. For example, The "Do It Yourself" ethos of those who crafted this music has become a cultural phenomenon inspiring many. The underground nature of this scene utilizes the cultural framework of American character, freedom of speech, class mobility, community, and more to develop and challenge established traditions, artistic and social.

## Course objectives

After completing this class, you will be able to:

* clearly identify different stylistic elements of underground music;
* describe the timeline in which this music grew and changed through the last 20 years;
* articulate an argument for the importance of sub-cultural movements, especially in the technological age;
* describe how art can mobilize large groups of disaffected people toward common goals.

## Class format

A combination of lecture and discussion, with media (music, films, slides) to provide realistic examples of the ideas discussed.

## Texts

* Greenwald, Andy. *Nothing Feels Good: Punk Rock, Teenagers, and Emo.* St. Martin's Griffin, 2003. ISBN 0312308639.
* Sinker, Daniel, ed. *We Owe You Nothing: Punk Planet: The Collected Interviews.* Expanded edition. Punk Planet Books/Akashic Books, 2008. ISBN 978-1933354323.
* Azerrad, Michael. *Our Band Could Be Your Life: Scenes from the American Indie Underground 1981-1991.* Back Bay Books, 2001. ISBN 0316787531.
* Greenberg, Arielle. *Youth Subcultures: Exploring Underground America.* Longman, 2007. ISBN 0-321-24194-0.
* Kruse, Holly. *Site and Sound: Understanding Independent Music Scenes.*

Additional readings were shared through the course's online library.

See [Texts and Readings](/underground-music/texts.html) for library links and the other books mentioned in the topics.

## Films

* *American Hardcore*
* *Metal: A Headbanger's Journey*
* *Instrument*
* *Danielson: A Family Movie*
* *Spend an Evening with Saddle Creek*

See [Films](/underground-music/films.html) for directors, years and the topics where each film comes up.

## Listening

The [Listening List](/underground-music/listening.html) has every song on the course list, with a link to a recording of each.

## Themes to emphasize

* Sense of community
* Scene identity vs. sub cultural identity
* Incestual quality
* It all revolves around the music
* Intensity and personal feeling
* Nostalgia
* Politics
* High vs. Low Art
* Regionalism
* Skate Culture
* Technology
* Zines

## Bands to cover

* Sonic Youth
* Fugazi
* Husker Du
* Earth
* Bikini Kill
* Fifteen
* Cap'n Jazz, Joan of Arc, The Owls, Make Believe, Owen, Ghosts and Vodka

## Topics

{%- assign topics = site.pages | where_exp: "p", "p.path contains 'underground-music/topic-'" | sort: "path" %}
{%- for topic in topics %}
* [{{ topic.title }}]({{ topic.url | relative_url }}){% if topic.summary %}: {{ topic.summary }}{% endif %}
{%- endfor %}
