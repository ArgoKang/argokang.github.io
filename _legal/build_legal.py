"""Convert the legal drafts (*.md here) into the data-lang-block sections of Homepage/pages/*.html.

Lines containing 【...】 are placeholders still to be filled in: they are emitted as HTML comments
so they stay in the page source but do not show up on the site.
"""
import html
import os
import re

SRC = os.path.dirname(os.path.abspath(__file__)) + '/'
SITE = os.path.join(os.path.dirname(SRC.rstrip('/')), 'pages') + '/'
PAGES = {'tos': 'tos.html', 'privacy': 'privacy.html', 'deletion': 'account-deletion.html'}
NAMES = {'en': 'English', 'ko': '한국어', 'pt-BR': 'Português (Brasil)'}


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: '<a href="%s">%s</a>' % (m.group(2).replace('&amp;', '&'), m.group(1)), t)
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)


def convert(md, indent):
    out, stack = [], []

    def close_lists(to=0):
        while len(stack) > to:
            out.append('</li></ul>' if stack.pop() == 'open' else '</ul>')

    for line in md.strip('\n').split('\n'):
        if '【' in line:
            out.append('<!-- TODO 채울 칸: %s -->' % line.strip().lstrip('- ').replace('--', '-'))
            continue
        if line.strip() == ':::box':
            close_lists(); out.append('<div class="box">'); continue
        if line.strip() == ':::':
            close_lists(); out.append('</div>'); continue
        m = re.match(r'^( *)- (.*)$', line)
        if m:
            depth = len(m.group(1)) // 2 + 1
            if depth > len(stack):
                out.append('<ul>'); stack.append('none')
            else:
                while len(stack) > depth:
                    stack.pop(); out.append('</li></ul>')
                if stack[-1] == 'open':
                    out.append('</li>')
            out.append('<li>' + inline(m.group(2))); stack[-1] = 'open'
            continue
        close_lists()
        if not line.strip():
            continue
        if line.startswith('### '):
            out.append('<h3>%s</h3>' % inline(line[4:]))
        elif line.startswith('## '):
            out.append('<h2>%s</h2>' % inline(line[3:]))
        elif line.startswith('# '):
            out.append('<h1>%s</h1>' % inline(line[2:]))
        else:
            out.append('<p>%s</p>' % inline(line))
    close_lists()
    return '\n'.join(indent + l for l in '\n'.join(out).replace('\n</li>', '</li>').split('\n'))


for key, fn in PAGES.items():
    p = SITE + fn
    s = open(p, encoding='utf-8').read()
    a = s.index('<div class="wrap">', s.index('<main class="legal">')) + len('<div class="wrap">')
    b = s.index('</div>\n\t\t</main>')
    blocks = []
    for lang in ['en', 'ko', 'pt-BR']:
        body = convert(open(SRC + '%s.%s.md' % (key, lang), encoding='utf-8').read(), '\t\t\t\t\t')
        blocks.append('\t\t\t\t<!-- %s -->\n\t\t\t\t<div data-lang-block lang="%s"%s>\n%s\n\t\t\t\t</div>'
                      % (NAMES[lang], lang, '' if lang == 'en' else ' hidden', body))
    s = s[:a] + '\n\n' + '\n\n'.join(blocks) + '\n\n\t\t\t' + s[b:]
    open(p, 'w', encoding='utf-8').write(s)
    print('built', fn)
