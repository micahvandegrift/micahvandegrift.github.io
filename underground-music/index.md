<!--
  Course home page. The list of sessions at the bottom builds itself:
  every file named week-XX.md in this folder shows up automatically,
  in order, using its title and summary.
-->

# Underground Music in America: 1980 – Present

An undergraduate course I taught in graduate school. This site is an archive of the lecture notes, recordings, listening and viewing lists, and readings from each class meeting.

## About the course

*(Course description goes here: what the class was about, where and when it was taught, and how it was organized.)*

## Sessions

{% assign sessions = site.pages | where_exp: "p", "p.path contains 'underground-music/week-'" | sort: "path" %}
{% for session in sessions %}
* [{{ session.title }}]({{ session.url | relative_url }}){% if session.summary %}: {{ session.summary }}{% endif %}
{% endfor %}
