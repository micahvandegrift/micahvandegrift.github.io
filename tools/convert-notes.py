"""Turn a slice of converted lecture notes into clean site Markdown.

This is a helper for Claude, not part of the website (it is excluded from
the published site in _config.yml). Steps used for the Underground Music notes:

  1. soffice --headless --convert-to docx --outdir OUT notes.doc
  2. pandoc -f docx -t gfm --wrap=none OUT/notes.docx -o OUT/notes.md
  3. python3 -I tools/convert-notes.py OUT/notes.md START END > draft.md
     (START and END are line numbers in notes.md; END is not included)

What it does to the slice:
- drops empty bullets and pandoc's <!-- --> separators
- turns every web address into a visible, non-clickable "old link" tag
- turns top-level "- 1. Heading" bullets into ### headings
- keeps bullet lists tight (no blank line between bullets)
The output is a first draft; read it and fix by hand before publishing.
"""
import re, sys

def marker(url):
    url = url.rstrip('.,;')
    return f'<span class="old-link">[old link: {url}]</span>'

LINK = re.compile(r'\[([^\]]+)\]\((https?://[^)]+)\)|<(https?://[^>]+)>|(https?://[^\s<>)\]]+)')

def links(line):
    def sub(m):
        if m.group(2):
            return f'{m.group(1)} {marker(m.group(2))}'
        return marker(m.group(3) or m.group(4))
    return LINK.sub(sub, line)

def main(path, start, end):
    lines = open(path, encoding='utf-8').read().split('\n')[start - 1:end - 1]
    out, in_heading = [], False
    for line in lines:
        if re.fullmatch(r'\s*-?\s*', line) and line.strip():  # "- " empty bullet
            continue
        if line.strip() == '<!-- -->':
            continue
        line = links(line)
        m = re.match(r'^- (\d+)\\\. (.*)$', line)
        if m:
            out += ['', f'### {m.group(1)}. {m.group(2)}', '']
            in_heading = True
            continue
        if line.startswith('- ') or (line and not line.startswith(' ')):
            in_heading = False
        if in_heading and line.startswith('  '):
            line = line[2:]
        out.append(line)
    text = '\n'.join(out)
    text = re.sub(r'\n{3,}', '\n\n', text)
    # keep bullet lists tight: drop a blank line when bullets sit on both sides of it
    rows = text.split('\n')
    tight = []
    for i, row in enumerate(rows):
        if not row.strip() and tight and i + 1 < len(rows):
            if re.match(r'\s*- ', tight[-1]) and re.match(r'\s*- ', rows[i + 1]):
                continue
        tight.append(row)
    text = '\n'.join(tight)
    print(text.strip())

main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
