# Builds translated copies of every page into /<lang>/...  Run after build_pages.py.
# Strings: tools/i18n/_en.json (source list) + tools/i18n/<lang>.json ({"index": "translation"}).
import os, sys, json, re, pathlib
sys.path.insert(0, os.path.dirname(__file__))
from i18n_common import *
from bs4 import BeautifulSoup
R = str(pathlib.Path(__file__).resolve().parent.parent); os.chdir(R)
SITE = 'https://halewoodsystems.com'
KEEP = ('/downloads/', '/img/', '/assets/', '/favicon', '/apple-touch')

def url_of(f):  # 'products/kyrofix/index.html' -> '/products/kyrofix/'
    return '/' + f[:-len('index.html')] if f.endswith('index.html') else '/' + f

def extract():
    allu, seen = [], set()
    for f in pages():
        for k, o, t in units(BeautifulSoup(open(f, encoding='utf-8').read(), 'html.parser')):
            if t not in seen: seen.add(t); allu.append(t)
    json.dump(allu, open('tools/i18n/_en.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    return allu

def alternates(soup, u, lang=''):
    head = soup.head
    for l in head.find_all('link', rel='alternate'): l.decompose()
    for l in head.find_all('link', rel='canonical'): l.decompose()
    for code, pre in [('en', '')] + [(x, '/' + x) for x in LANGS]:
        head.append(soup.new_tag('link', rel='alternate', hreflang=code, href=SITE + pre + u))
    head.append(soup.new_tag('link', rel='alternate', hreflang='x-default', href=SITE + u))
    head.append(soup.new_tag('link', rel='canonical', href=SITE + ('/' + lang if lang else '') + u))

def build():
    src = json.load(open('tools/i18n/_en.json', encoding='utf-8'))
    old = {t: i for i, t in enumerate(src)}
    cur = extract()
    new = [t for t in cur if t not in old]
    if new: print('NOT TRANSLATED YET (shown in English):', len(new)); [print('  ', t[:80]) for t in new]
    json.dump(src + new, open('tools/i18n/_en.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    src = src + new; idx = {t: i for i, t in enumerate(src)}
    for f in pages():  # English pages get hreflang links too
        if f == '404.html': continue
        s = BeautifulSoup(open(f, encoding='utf-8').read(), 'html.parser'); alternates(s, url_of(f))
        open(f, 'w', encoding='utf-8').write(str(s))
    urls = []
    for lang in LANGS:
        p = f'tools/i18n/{lang}.json'
        tr = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}
        for f in pages():
            if f == '404.html': continue
            s = BeautifulSoup(open(f, encoding='utf-8').read(), 'html.parser')
            for k, o, t in units(s):
                x = tr.get(str(idx.get(t)))
                if not x: continue
                if k == 'html':
                    o.clear(); o.append(BeautifulSoup(x, 'html.parser'))
                else:
                    el, a = o; el[a] = x
            for a in s.find_all('a', href=True):
                h = a['href']
                if h.startswith('/') and not h.startswith(KEEP) and not re.match(r'^/(%s)/' % '|'.join(LANGS), h):
                    a['href'] = '/' + lang + h
            s.html['lang'] = lang
            u = url_of(f); alternates(s, u, lang)
            out = os.path.join(lang, f); os.makedirs(os.path.dirname(out) or lang, exist_ok=True)
            open(out, 'w', encoding='utf-8').write(str(s)); urls.append('/' + lang + u)
    eng = [url_of(f) for f in pages() if f != '404.html']
    open('sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + ''.join(f'<url><loc>{SITE}{u}</loc></url>\n' for u in eng + urls) + '</urlset>\n')
    print('i18n ok:', len(LANGS), 'languages,', len(urls), 'pages')

if __name__ == '__main__':
    build()

# translated game folders need the same icons, manifest and offline file as the English ones
import shutil, glob
for lang in LANGS:
    for g in glob.glob('games/*/'):
        dst = os.path.join(lang, g)
        if os.path.isdir(dst):
            for f in os.listdir(g):
                if not f.endswith('.html'): shutil.copy(os.path.join(g, f), dst)
