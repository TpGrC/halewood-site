import glob,re
from bs4 import BeautifulSoup
LANGS=['el','de','es','fr','it','pl','pt','ru']
BLOCK={'p','li','h1','h2','h3','h4','td','th','summary','figcaption','dt','dd','button','label','small'}
INLINE_STANDALONE={'a','span','div'}
def pages():
    return [f for f in sorted(glob.glob('**/*.html',recursive=True)) if f.split('/')[0] not in LANGS+['tools','downloads','rechnung'] and 'http-equiv="refresh"' not in open(f,encoding='utf-8').read(600)]
def has_text(s): return bool(re.search(r'[A-Za-zΑ-Ω]{2}',s))
def units(soup):
    """yield (kind, obj, text). kind: 'html' element innerHTML, 'attr' (el,attr)"""
    out=[]
    t=soup.find('title')
    if t: out.append(('html',t,t.decode_contents()))
    for m in soup.find_all('meta'):
        if m.get('name')=='description' or m.get('property') in('og:title','og:description') or m.get('name') in ('twitter:title','twitter:description'):
            out.append(('attr',(m,'content'),m['content']))
    for el in soup.find_all(['img']):
        if el.get('alt') and has_text(el['alt']): out.append(('attr',(el,'alt'),el['alt']))
    for el in soup.find_all(attrs={'aria-label':True}):
        if has_text(el['aria-label']): out.append(('attr',(el,'aria-label'),el['aria-label']))
    from bs4 import NavigableString
    cap=set()
    STRUCT={'div','section','ul','ol','table','figure','img','header','footer','main','nav','form','details','tr','tbody','thead'}
    for el in soup.body.find_all(True):
        if el.name in('script','style','code','svg') or el.find_parent(['script','style','svg']): continue
        if any(id(x) in cap for x in el.parents): continue
        own=any(isinstance(c,NavigableString) and has_text(str(c)) for c in el.children)
        if not own: continue
        if el.find(list(STRUCT|BLOCK)) and el.name not in BLOCK: continue
        h=el.decode_contents().strip()
        cap.add(id(el)); out.append(('html',el,h))
    return out
