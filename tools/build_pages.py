import re
import os, textwrap
import pathlib; R=str(pathlib.Path(__file__).resolve().parent.parent)
YT='https://www.youtube.com/@HalewoodSystems'
DON='https://buy.stripe.com/14AcMY4rr24U6Pqec0dUY02'
MAIL='support@halewoodsystems.com'
# Gumroad checkout links (fill in when the products exist); empty = "On sale soon"
LIVE=False   # turn on once the Gumroad products are published
G='https://thomasknot.gumroad.com/l/'
BUY={k:(G+v if LIVE else '') for k,v in {'driver':'kyrofix-driver-updater-pro','cleaner':'kyrofix-cleaner-pro','backup':'kyrofix-backup-pro','space':'kyrofix-space-pro','shredder':'kyrofix-shredder-pro','photo':'kyrofix-photo-cleaner-pro'}.items()}
def buybtn(k,label='Buy Pro'):
    return f'<a class="btn p" href="{BUY[k]}" target="_blank" rel="noopener">{label}</a>' if BUY[k] else '<span class="btn p off">On sale soon</span>'
SALEBADGE=lambda k:'<span class="badge live">Pro</span>' if BUY[k] else '<span class="badge soon">Pro</span>'
PRONOTE='<p class="updated" style="text-align:center">One-time payment, no subscription. After buying you get your key at <a href="/activate/">halewoodsystems.com/activate</a>.</p>'
KF_ICO='<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z"/></svg>'
SG_ICO='<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="11" rx="4"/><path d="M7 11v3M5.5 12.5h3M15 12h.01M18 13h.01"/></svg>'
def page(path,title,desc,body):
    html=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://halewoodsystems.com/img/og.jpg">
<meta property="og:type" content="website">
<meta name="theme-color" content="#07090d">
<link rel="icon" href="/favicon-48.png" type="image/png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/site.css?v=8">
</head>
<body>
<header id="nav"></header>
<main>
{body}
</main>
<footer id="foot"></footer>
<script src="/assets/site.js?v=6"></script>
<script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "a11dfd5ee7a843d0b247e834f27c971c"}}'></script>
</body>
</html>
'''
    fp=os.path.join(R,path); os.makedirs(os.path.dirname(fp),exist_ok=True); open(fp,'w').write(html)

CARDS=f'''<div class="grid">
  <a class="card" href="/products/windrova/"><div class="ico"><img src="/img/windrova-icon.png" alt=""></div><span class="badge live">● Live</span><h3>Windrova</h3><p>Live weather map for the whole world, with three forecast models and an activity planner.</p><div class="meta"><span>Web · Free</span><span>Mobile app soon</span></div></a>
  <a class="card" href="/products/kyrofix/"><div class="ico kf">{KF_ICO}</div><span class="badge free">Free download</span><h3>Kyrofix Driver Updater</h3><p>Finds outdated drivers and updates them safely, with an AI assistant that explains every fix.</p><div class="meta"><span>Windows · Free &amp; Pro</span></div></a>
  <a class="card" href="/products/kyrofix-cleaner/"><div class="ico kc"><img src="/img/kyrofix-cleaner/icon.png" alt="" width="34" height="34"></div><span class="badge free">Free download</span><h3>Kyrofix Cleaner</h3><p>Cleans junk files, browser cache and update leftovers, and speeds up Windows startup.</p><div class="meta"><span>Windows · Free &amp; Pro</span></div></a>
  <a class="card" href="/products/kyrofix-backup/"><div class="ico kc"><img src="/img/kyrofix-backup/icon.png" alt="" width="34" height="34"></div><span class="badge free">Free download</span><h3>Kyrofix Backup</h3><p>Backs up your documents and photos to a USB drive or external disk, and gets them back when you need them.</p><div class="meta"><span>Windows · Free &amp; Pro</span></div></a>
  <a class="card" href="/products/kyrofix-space/"><div class="ico kc"><img src="/img/kyrofix-space/icon.png" alt="" width="34" height="34"></div><span class="badge free">New · Free download</span><h3>Kyrofix Space</h3><p>What is filling your disk? See the biggest folders and files in seconds and free up space.</p><div class="meta"><span>Windows · Free &amp; Pro</span></div></a>
  <a class="card" href="/products/kyrofix-shredder/"><div class="ico kc"><img src="/img/kyrofix-shredder/icon.png" alt="" width="34" height="34"></div><span class="badge free">New · Free download</span><h3>Kyrofix Shredder</h3><p>Delete files for good. Shredded files cannot be recovered.</p><div class="meta"><span>Windows · Free &amp; Pro</span></div></a>
  <a class="card" href="/products/kyrofix-photo-cleaner/"><div class="ico kc"><img src="/img/kyrofix-photo-cleaner/icon.png" alt="" width="34" height="34"></div><span class="badge free">New · Free download</span><h3>Kyrofix Photo Cleaner</h3><p>Find duplicate, similar and blurry photos and free up space.</p><div class="meta"><span>Windows · Free &amp; Pro</span></div></a>
  <a class="card" href="/products/potion-sort/"><div class="ico kc"><img src="/img/potion-sort/icon.png" alt="" width="34" height="34"></div><span class="badge live">New · Free to play</span><h3>Potion Sort</h3><p>Pour the potions until every bottle holds one colour. Endless relaxing levels.</p><div class="meta"><span>Phone &amp; browser · Free</span></div></a>
  <a class="card" href="/products/triple-bloom/"><div class="ico kc"><img src="/img/triple-bloom/icon.png" alt="" width="34" height="34"></div><span class="badge live">New · Free to play</span><h3>Triple Bloom</h3><p>Tap tiles and match three of a kind to clear the garden.</p><div class="meta"><span>Phone &amp; browser · Free</span></div></a>
  <a class="card" href="/products/skystack/"><div class="ico kc"><img src="/img/skystack/icon.png" alt="" width="34" height="34"></div><span class="badge live">New · Free to play</span><h3>Skystack</h3><p>Tap to drop the block. Stack as high as you can.</p><div class="meta"><span>Phone &amp; browser · Free</span></div></a>
  <a class="card" href="/products/starfuse/"><div class="ico kc"><img src="/img/starfuse/icon.png" alt="" width="34" height="34"></div><span class="badge live">New · Free to play</span><h3>Starfuse</h3><p>Drop planets, merge matching ones and grow them into stars and black holes. Plays on any phone.</p><div class="meta"><span>Phone &amp; browser · Free</span></div></a>
  <a class="card" href="/products/slipgate/"><div class="ico sg">{SG_ICO}</div><span class="badge free">Free to play</span><h3>Slipgate</h3><p>A tricky puzzle game that starts easy and gets hard fast. Play it free in your browser.</p><div class="meta"><span>Browser · Free</span></div></a>
</div>'''


def gcards(hs):
    return '<div class="grid">'+''.join(FULL[h] for h in hs)+'</div>'
FULL={'/products/windrova/': '  <a class="card" href="/products/windrova/"><div class="ico"><img src="/img/windrova-icon.png" alt=""></div><span class="badge live">● Live</span><h3>Windrova</h3><p>Live weather map for the whole world, with three forecast models and an activity planner.</p><div class="meta"><span>Web · Free</span><span>Mobile app soon</span></div></a>\n', '/products/kyrofix/': '  <a class="card" href="/products/kyrofix/"><div class="ico kf">{KF_ICO}</div><span class="badge free">Free download</span><h3>Kyrofix Driver Updater</h3><p>Finds outdated drivers and updates them safely, with an AI assistant that explains every fix.</p><div class="meta"><span>Windows · Free &amp; Pro</span></div></a>\n', '/products/kyrofix-cleaner/': '  <a class="card" href="/products/kyrofix-cleaner/"><div class="ico kc"><img src="/img/kyrofix-cleaner/icon.png" alt="" width="34" height="34"></div><span class="badge free">Free download</span><h3>Kyrofix Cleaner</h3><p>Cleans junk files, browser cache and update leftovers, and speeds up Windows startup.</p><div class="meta"><span>Windows · Free &amp; Pro</span></div></a>\n', '/products/kyrofix-backup/': '  <a class="card" href="/products/kyrofix-backup/"><div class="ico kc"><img src="/img/kyrofix-backup/icon.png" alt="" width="34" height="34"></div><span class="badge free">Free download</span><h3>Kyrofix Backup</h3><p>Backs up your documents and photos to a USB drive or external disk, and gets them back when you need them.</p><div class="meta"><span>Windows · Free &amp; Pro</span></div></a>\n', '/products/kyrofix-space/': '  <a class="card" href="/products/kyrofix-space/"><div class="ico kc"><img src="/img/kyrofix-space/icon.png" alt="" width="34" height="34"></div><span class="badge free">New · Free download</span><h3>Kyrofix Space</h3><p>What is filling your disk? See the biggest folders and files in seconds and free up space.</p><div class="meta"><span>Windows · Free &amp; Pro</span></div></a>\n', '/products/kyrofix-shredder/': '  <a class="card" href="/products/kyrofix-shredder/"><div class="ico kc"><img src="/img/kyrofix-shredder/icon.png" alt="" width="34" height="34"></div><span class="badge free">New · Free download</span><h3>Kyrofix Shredder</h3><p>Delete files for good. Shredded files cannot be recovered.</p><div class="meta"><span>Windows · Free &amp; Pro</span></div></a>\n', '/products/kyrofix-photo-cleaner/': '  <a class="card" href="/products/kyrofix-photo-cleaner/"><div class="ico kc"><img src="/img/kyrofix-photo-cleaner/icon.png" alt="" width="34" height="34"></div><span class="badge free">New · Free download</span><h3>Kyrofix Photo Cleaner</h3><p>Find duplicate, similar and blurry photos and free up space.</p><div class="meta"><span>Windows · Free &amp; Pro</span></div></a>\n', '/products/potion-sort/': '  <a class="card" href="/products/potion-sort/"><div class="ico kc"><img src="/img/potion-sort/icon.png" alt="" width="34" height="34"></div><span class="badge live">New · Free to play</span><h3>Potion Sort</h3><p>Pour the potions until every bottle holds one colour. Endless relaxing levels.</p><div class="meta"><span>Phone &amp; browser · Free</span></div></a>\n', '/products/triple-bloom/': '  <a class="card" href="/products/triple-bloom/"><div class="ico kc"><img src="/img/triple-bloom/icon.png" alt="" width="34" height="34"></div><span class="badge live">New · Free to play</span><h3>Triple Bloom</h3><p>Tap tiles and match three of a kind to clear the garden.</p><div class="meta"><span>Phone &amp; browser · Free</span></div></a>\n', '/products/skystack/': '  <a class="card" href="/products/skystack/"><div class="ico kc"><img src="/img/skystack/icon.png" alt="" width="34" height="34"></div><span class="badge live">New · Free to play</span><h3>Skystack</h3><p>Tap to drop the block. Stack as high as you can.</p><div class="meta"><span>Phone &amp; browser · Free</span></div></a>\n', '/products/starfuse/': '  <a class="card" href="/products/starfuse/"><div class="ico kc"><img src="/img/starfuse/icon.png" alt="" width="34" height="34"></div><span class="badge live">New · Free to play</span><h3>Starfuse</h3><p>Drop planets, merge matching ones and grow them into stars and black holes. Plays on any phone.</p><div class="meta"><span>Phone &amp; browser · Free</span></div></a>\n', '/products/slipgate/': '  <a class="card" href="/products/slipgate/"><div class="ico sg">{SG_ICO}</div><span class="badge free">Free to play</span><h3>Slipgate</h3><p>A tricky puzzle game that starts easy and gets hard fast. Play it free in your browser.</p><div class="meta"><span>Browser · Free</span></div></a>\n'}
FULL={k:v.replace('{KF_ICO}',KF_ICO).replace('{SG_ICO}',SG_ICO) for k,v in FULL.items()}
GAMES=['/products/starfuse/', '/products/potion-sort/', '/products/triple-bloom/', '/products/skystack/', '/products/slipgate/']
GPLAY={'/products/starfuse/':'/games/starfuse/','/products/potion-sort/':'/games/potion-sort/','/products/triple-bloom/':'/games/triple-bloom/','/products/skystack/':'/games/skystack/','/products/slipgate/':'https://halewood-systems.itch.io/slipgate'}
def gameCard(h):
    c=FULL[h];m=re.search(r'<h3>(.*?)</h3><p>(.*?)</p>',c);ico=re.search(r'<img src="([^"]+)"',c)
    icon=f'<img src="{ico.group(1)}" alt="" width="72" height="72" style="border-radius:18px">' if ico else '<div class="ico sg" style="width:72px;height:72px">'+SG_ICO+'</div>'
    ext=' target="_blank" rel="noopener"' if GPLAY[h].startswith('http') else ''
    return f'<div class="card gcard">{icon}<h3 style="margin-top:14px">{m.group(1)}</h3><p>{m.group(2)}</p><div class="cta" style="margin-top:16px"><a class="btn p s" href="{GPLAY[h]}"{ext}>▶ Play free</a><a class="btn g s" href="{h}">Details</a></div></div>'

# ---------- catalogue ----------
KY=lambda slug:f'<img src="/img/{slug}/icon.png" alt="" width="56" height="56">'
CAT={
 'driver':('/products/kyrofix/','Kyrofix Driver Updater','Finds outdated drivers and updates them safely, with an assistant that explains each fix.','Windows 10 / 11','Free','Pro €19.99 / year','/downloads/Kyrofix-Driver-Updater-Setup.exe','Download','<div class="ico kf">'+KF_ICO+'</div>'),
 'cleaner':('/products/kyrofix-cleaner/','Kyrofix Cleaner','Removes junk files, browser cache and update leftovers, and speeds up startup.','Windows 10 / 11','Free','Pro €14.99 / year','/downloads/Kyrofix-Cleaner-Setup.exe','Download',KY('kyrofix-cleaner')),
 'space':('/products/kyrofix-space/','Kyrofix Space','Shows which folders and files fill your disk, so you know what to clear.','Windows 10 / 11','Free','Pro €9.99 / year','/downloads/Kyrofix-Space-Setup.exe','Download',KY('kyrofix-space')),
 'photo':('/products/kyrofix-photo-cleaner/','Kyrofix Photo Cleaner','Finds duplicate, near-identical and blurry photos and keeps the best copy.','Windows 10 / 11','Free','Pro €9.99 / year','/downloads/Kyrofix-Photo-Cleaner-Setup.exe','Download',KY('kyrofix-photo-cleaner')),
 'backup':('/products/kyrofix-backup/','Kyrofix Backup','Copies your documents and photos to a USB drive or external disk, and brings them back.','Windows 10 / 11','Free','Pro €14.99 / year','/downloads/Kyrofix-Backup-Setup.exe','Download',KY('kyrofix-backup')),
 'shredder':('/products/kyrofix-shredder/','Kyrofix Shredder','Overwrites files before deleting them, so they cannot be recovered.','Windows 10 / 11','Free','Pro €9.99 / year','/downloads/Kyrofix-Shredder-Setup.exe','Download',KY('kyrofix-shredder')),
 'starfuse':('/products/starfuse/','Starfuse','Drop planets and merge matching ones until you make a black hole.','Phone and browser','Free','optional ads','/games/starfuse/','Play','<img src="/img/starfuse/icon.png" alt="" width="56" height="56">'),
 'potion':('/products/potion-sort/','Potion Sort','Pour coloured potions until every bottle holds one colour.','Phone and browser','Free','optional ads','/games/potion-sort/','Play','<img src="/img/potion-sort/icon.png" alt="" width="56" height="56">'),
 'bloom':('/products/triple-bloom/','Triple Bloom','Match three garden tiles at a time and clear the board.','Phone and browser','Free','optional ads','/games/triple-bloom/','Play','<img src="/img/triple-bloom/icon.png" alt="" width="56" height="56">'),
 'stack':('/products/skystack/','Skystack','Tap to drop each block and build the tallest tower you can.','Phone and browser','Free','optional ads','/games/skystack/','Play','<img src="/img/skystack/icon.png" alt="" width="56" height="56">'),
 'slipgate':('/products/slipgate/','Slipgate','Slide blocks out through the gates of their colour. 200 levels.','Browser','Free','','https://halewood-systems.itch.io/slipgate','Play','<div class="ico sg">'+SG_ICO+'</div>'),
 'windrova':('/products/windrova/','Windrova','Live wind, rain, waves and three forecast models for every place on Earth.','Web, Android soon','Free','Premium later','https://windrova.com','Open','<img src="/img/windrova-icon.png" alt="" width="56" height="56">'),
}
NEW={'space','photo','shredder','potion','bloom','stack'}
def rows(keys):
    out='<ul class="rows">'
    for k in keys:
        h,n,d,pl,c1,c2,url,lab,ic=CAT[k]
        ext=' target="_blank" rel="noopener"' if url.startswith('http') else (' download' if url.endswith('.exe') else '')
        nw='<span class="new">New</span>' if k in NEW else ''
        bc='g' if lab=='Download' else 'p'
        out+=f'<li><a class="ri" href="{h}" aria-hidden="true" tabindex="-1">{ic}</a><div class="rn"><a href="{h}">{n}</a>{nw}<p>{d}</p></div><div class="rp">{pl}</div><div class="rc"><b>{c1}</b><span>{c2}</span></div><div class="ra"><a class="btn {bc} s" href="{url}"{ext}>{lab}</a></div></li>'
    return out+'</ul>'
def fam(cls,title,desc,keys,more=None):
    m=f'<a href="{more[0]}">{more[1]}</a>' if more else ''
    return f'<div class="fam"><div class="famhead {cls}"><i></i><h2>{title}</h2><p>{desc}</p>{m}</div>{rows(keys)}</div>'
KY_ALL=['driver','cleaner','space','photo','backup','shredder'];GM_ALL=['starfuse','potion','bloom','stack','slipgate']

# ---------- home ----------
page('index.html','Halewood Systems — PC software, games and weather','Halewood Systems makes Kyrofix PC tools for Windows, free games for phone and browser, and the Windrova weather map. Every product has a free version.',f'''
<section class="hero"><div class="wrap hhero">
  <div>
    <h1>Tools for your PC, games for your phone, weather for everywhere.</h1>
    <p class="lead">Halewood Systems is a small software studio in the EU. Everything we make has a free version that does the job, with nothing extra installed.</p>
    <div class="cta"><a class="btn p" href="/software/">Browse PC software</a><a class="btn g" href="/games/">Play a game</a></div>
    <div class="facts"><div><b>Free versions</b>for every product</div><div><b>No bundled extras</b>no toolbars or add-ons</div><div><b>EU company</b>GDPR privacy</div><div><b>14-day refund</b>on Pro</div></div>
  </div>
  <div class="stage" aria-hidden="true">
    <div class="win"><img src="/img/kyrofix-space/s1.jpg" alt="" width="1100" height="740"></div>
    <div class="wx"><img src="/img/windrova/hero.jpg" alt="" width="1440" height="810"><span>Windrova · live wind</span></div>
    <div class="phone"><img src="/img/potion-sort/s1.jpg" alt="" width="390" height="844"></div>
  </div>
</div></section>
<section class="strip"><div class="wrap"><div><b>12</b> products</div><div><b>6</b> Windows tools</div><div><b>5</b> free games</div><div><b>9</b> languages</div><div><b>0</b> bundled extras</div></div></section>
<section><div class="wrap">
  '''+fam('kf','PC software','Kyrofix tools for Windows 10 and 11.',KY_ALL,('/software/','All PC software'))+fam('gm','Games','Free to play on phone and computer, no download.',GM_ALL,('/games/','All games'))+fam('wr','Weather','',['windrova'])+f'''
</div></section>
<section class="alt"><div class="wrap feat">
  <div>
    <h2>Windrova: the whole world's weather, live.</h2>
    <p class="lead">A live weather map for every place on Earth. Open it in any browser, no account needed.</p>
    <ul class="ticks"><li>Live wind, rain, temperature, clouds and sea waves</li><li>ECMWF, GFS and GEM forecast models in one click</li><li>Hurricanes, lightning, earthquakes, fires and live satellite</li><li>Best hours for the beach, sailing, kitesurf and hiking</li></ul>
    <div class="cta"><a class="btn p" href="https://windrova.com" target="_blank" rel="noopener">Open Windrova</a><a class="btn g" href="/products/windrova/">Learn more</a></div>
  </div>
  <div class="shot"><img src="/img/windrova/hero.jpg" alt="Windrova live wind map over Europe" width="1440" height="810"></div>
</div></section>
<div class="band"><h2>Questions about a product or a purchase?</h2><p class="lead">We answer every email, usually within a day.</p><div class="cta"><a class="btn p" href="/support/">Contact support</a><a class="btn g" href="{DON}" target="_blank" rel="noopener">Support the studio</a></div></div>
''')

# ---------- products ----------
page('products/index.html','All products — Halewood Systems','Every Halewood Systems product: Kyrofix PC software for Windows, free games and the Windrova weather map.',f'''
<section class="hero"><div class="wrap"><h1>All products</h1><p class="lead">Every product has a free version. Kyrofix Pro adds extra features and works on up to 3 PCs.</p></div></section>
<section><div class="wrap">'''+fam('kf','PC software','Kyrofix tools for Windows 10 and 11.',KY_ALL,('/software/','More about Kyrofix'))+fam('gm','Games','Free to play on phone and computer.',GM_ALL,('/games/','All games'))+fam('wr','Weather','',['windrova'])+'''</div></section>''')

page('software/index.html','Kyrofix PC software for Windows — Halewood Systems','Kyrofix: free Windows tools to update drivers, clean junk, free up space, back up and shred files. Pro from €9.99 a year.',f'''
<section class="hero"><div class="wrap hhero">
  <div><h1>Kyrofix PC tools</h1>
  <p class="lead">Six small Windows programs that keep your PC fast, tidy and safe. Each one is a free download and tells you what it will do before it does it.</p>
  <div class="facts"><div><b>Windows 10 and 11</b>64-bit</div><div><b>No admin needed</b>for most tools</div><div><b>Pro on 3 PCs</b>per licence</div></div></div>
  <div class="shot"><img src="/img/kyrofix-photo-cleaner/s2.jpg" alt="Kyrofix Photo Cleaner showing duplicate photos" width="1100" height="740"></div>
</div></section>
<section><div class="wrap">'''+fam('kf','Fix and speed up','Keep Windows quick and drivers up to date.',['driver','cleaner'])+fam('kf','Free up space','Find what fills your disk and clear it.',['space','photo'])+fam('kf','Protect your files','Keep copies safe, and make deleted files really gone.',['backup','shredder'])+f'''</div></section>
<section class="alt"><div class="wrap"><h2>How Pro works</h2><div class="grid">
  <div class="card"><h3>One payment</h3><p>Pay once for a year, or once for good. Nothing renews by itself.</p></div>
  <div class="card"><h3>Your key</h3><p>After buying, you get the key for that program at <a href="/activate/" style="color:var(--acc)">halewoodsystems.com/activate</a>.</p></div>
  <div class="card"><h3>Up to 3 PCs</h3><p>Use the same key on three of your own PCs. Refund within 14 days if it is not for you.</p></div>
</div></div></section>''')

page('games/index.html','Free games — Halewood Systems','Free puzzle and arcade games by Halewood Systems. Play instantly on your phone or computer, no download.',f'''
<section class="hero"><div class="wrap"><h1>Games</h1><p class="lead">Quick to learn and hard to put down. Every game runs in your browser on phone or computer. Add one to your home screen and it works offline.</p></div></section>
<section><div class="wrap">'''+fam('gm','Puzzle','',['starfuse','potion','bloom','slipgate'])+fam('gm','Arcade','',['stack'])+'''</div></section>''')

# Windrova
page('products/windrova/index.html','Windrova — Live weather map for the whole world','Windrova: free live weather map with wind, rain, waves, satellite, hurricanes and ECMWF, GFS and GEM models. 23 languages.',f'''
<section class="hero"><div class="wrap feat">
  <div>
    <p class="crumb"><a href="/products/">Products</a> / Windrova</p>
    <span class="badge live">● Live · Free</span>
    <h1 style="font-size:clamp(38px,5vw,60px);margin-top:16px">Windrova</h1>
    <p class="lead">The whole world's weather, live. Wind, rain, waves and storms for any place on Earth, right in your browser.</p>
    <div class="cta"><a class="btn p" href="https://windrova.com" target="_blank" rel="noopener">Open Windrova, free →</a><span class="btn g off">📱 Mobile app coming soon</span></div>
    <div class="meta" style="margin-top:22px"><span>Web (any browser)</span><span>23 languages</span><span>No account needed</span></div>
  </div>
  <div class="shot"><img src="/img/windrova/hero.jpg" alt="Windrova wind map" width="1440" height="810"></div>
</div></section>
<section class="alt"><div class="wrap"><h2>Everything you need to read the weather</h2>
  <div class="gallery">
    <figure><img src="/img/windrova/models.jpg" alt="Forecast models" loading="lazy"><figcaption>ECMWF, GFS and GEM models in one click</figcaption></figure>
    <figure><img src="/img/windrova/storm.jpg" alt="Hurricane tracking" loading="lazy"><figcaption>Track hurricanes and storms live</figcaption></figure>
    <figure><img src="/img/windrova/waves.jpg" alt="Waves" loading="lazy"><figcaption>Waves and swell for sailors and surfers</figcaption></figure>
    <figure><img src="/img/windrova/satellite.jpg" alt="Satellite" loading="lazy"><figcaption>Live satellite of the whole planet</figcaption></figure>
    <figure><img src="/img/windrova/wind.jpg" alt="Wind animation" loading="lazy"><figcaption>Animated wind at the surface and at altitude</figcaption></figure>
    <figure><img src="/img/windrova/planner.jpg" alt="Activity planner" loading="lazy"><figcaption>Best hours for beach, sailing and kitesurf</figcaption></figure>
  </div></div></section>
<section><div class="wrap"><h2>Features</h2>
  <div class="grid two">
    <div><ul class="ticks"><li>Wind, gusts, temperature, rain, clouds, pressure, humidity</li><li>Sea waves and wave period</li><li>Thunderstorms, snow depth and isobars</li><li>Live satellite and satellite rain</li></ul></div>
    <div><ul class="ticks"><li>Hurricanes, lightning, earthquakes and wildfires</li><li>10-day forecast and 48-hour chart for any place</li><li>"Best time for" planner: beach, sailing, kitesurf, hiking</li><li>Search any city in the world, in 23 languages</li></ul></div>
  </div>
  <p class="updated">Weather data: MET Norway, ECMWF, NOAA, Environment Canada, EUMETSAT, NASA and others, under their open licences.</p>
</div></section>
<section class="alt"><div class="wrap"><h2>Pricing</h2>
  <div class="plans">
    <div class="plan hl"><span class="badge live">Available now</span><h3 style="margin-top:12px">Windrova Free</h3><div class="price">€0</div><div class="note">Forever free</div><ul><li>All weather maps and models</li><li>10-day forecast for any place</li><li>Storms, lightning, earthquakes, fires</li><li>No account, no ads</li></ul><a class="btn p" href="https://windrova.com" target="_blank" rel="noopener">Open free</a></div>
    <div class="plan"><span class="badge soon">Coming soon</span><h3 style="margin-top:12px">Windrova Premium</h3><div class="price">€2.49 <small>/ month</small></div><div class="note">or €19.99 / year</div><ul><li>Everything in Free</li><li>Extra features for power users</li><li>Mobile app extras</li><li>Supports development</li></ul><span class="btn g off">Coming soon</span></div>
  </div></div></section>
<div class="band"><h2>Open Windrova now.</h2><p class="lead">It's free and runs in any browser.</p><div class="cta"><a class="btn p" href="https://windrova.com" target="_blank" rel="noopener">Open Windrova</a></div></div>''')

# Kyrofix
page('products/kyrofix/index.html','Kyrofix Driver Updater — Free driver updater for Windows','Kyrofix Driver Updater for Windows 10 and 11: official drivers from Windows Update, NVIDIA, AMD and Intel, a restore point before every install, and a private AI that explains fixes. Free download.',f'''
<section class="hero"><div class="wrap">
  <p class="crumb"><a href="/products/">Products</a> / Kyrofix Driver Updater</p>
  <div class="ico kf" style="width:72px;height:72px">{KF_ICO}</div>
  <span class="badge free">Free download · Windows 10 / 11</span>
  <h1 style="font-size:clamp(36px,5vw,60px);margin-top:16px;max-width:820px">Kyrofix Driver Updater</h1>
  <p class="lead">Keep your PC's drivers up to date without hunting through websites. Official drivers only, a restore point before every change, and an AI that explains what's wrong in plain words.</p>
  <div class="cta"><a class="btn p" href="/downloads/Kyrofix-Driver-Updater-Setup.exe" download>Download free (11 MB)</a><a class="btn g" href="#plans">Free vs Pro</a></div>
  <div class="meta" style="margin-top:22px"><span>Version 1.2.0</span><span>Windows 10 / 11, 64-bit</span><span>10 languages</span></div>
  <div class="shot" style="margin-top:34px"><img src="/img/kyrofix/scan.jpg" alt="Kyrofix scan screen" width="1440" height="936"></div>
</div></section>
<section class="alt"><div class="wrap"><h2>What it does</h2>
  <div class="grid">
    <div class="card"><h3>Official drivers</h3><p>Drivers come from Windows Update and straight from NVIDIA, AMD and Intel. Never from random download sites.</p></div>
    <div class="card"><h3>Safe by default</h3><p>Kyrofix makes a Windows restore point before it installs anything, so you can always go back.</p></div>
    <div class="card"><h3>Crash explanations</h3><p>Had a blue screen? Kyrofix reads it and tells you what caused it and how to fix it.</p></div>
    <div class="card"><h3>Sound &amp; network fixes</h3><p>One-click repairs for no sound, no Wi-Fi and other common Windows problems.</p></div>
    <div class="card"><h3>Private AI assistant</h3><p>Ask anything about your PC. The AI runs on your computer, so nothing leaves it.</p></div>
    <div class="card"><h3>10 languages</h3><p>English, Ελληνικά, Deutsch, Español, Français, Italiano, Polski, Português, Русский and Türkçe.</p></div>
  </div></div></section>
<section><div class="wrap"><h2>See it in action</h2>
  <div class="gallery">
    <figure><img src="/img/kyrofix/results.jpg" alt="Scan results" loading="lazy"><figcaption>Clear scan results</figcaption></figure>
    <figure><img src="/img/kyrofix/drivers.jpg" alt="Driver list" loading="lazy"><figcaption>Every driver, with its source</figcaption></figure>
    <figure><img src="/img/kyrofix/ai.jpg" alt="AI assistant" loading="lazy"><figcaption>A private AI that explains fixes</figcaption></figure>
    <figure><img src="/img/kyrofix/tools.jpg" alt="Repair tools" loading="lazy"><figcaption>Sound, network and crash tools</figcaption></figure>
    <figure><img src="/img/kyrofix/boost.jpg" alt="Game Boost" loading="lazy"><figcaption>Game Boost (Pro)</figcaption></figure>
  </div></div></section>
<section class="alt" id="plans"><div class="wrap"><h2>Free vs Pro</h2><p class="lead">The free version is the full driver updater. Pro adds automation and extras.</p>
  <div class="plans">
    <div class="plan"><span class="badge free">Free</span><h3 style="margin-top:12px">Kyrofix Free</h3><div class="price">€0</div><div class="note">Free forever, no time limit</div><ul><li>Scan and update drivers</li><li>Official sources only</li><li>Restore point before installs</li><li>Blue screen explanations</li><li>Sound &amp; network fixes</li><li>AI assistant (daily limit)</li><li class="x">Automatic updates</li><li class="x">Game Boost</li></ul><a class="btn g" href="/downloads/Kyrofix-Driver-Updater-Setup.exe" download>Download free</a></div>
    <div class="plan hl">{SALEBADGE("driver")}<h3 style="margin-top:12px">Kyrofix Pro</h3><div class="price">€19.99<small style="font-size:16px;color:var(--mut)"> / year</small></div><div class="note">Up to 3 PCs · or €49.99 one-time, forever</div><ul><li>Everything in Free</li><li>Automatic updates and weekly checks</li><li>Game Boost</li><li>Missing DLL fixer</li><li>Driver backup &amp; restore</li><li>Unlimited AI</li><li>Priority support</li></ul>{buybtn("driver")}</div>
  </div>
  <p class="updated">Pro is not on sale yet. Prices include VAT and may change at launch.</p>
</div></section>
<section><div class="wrap"><h2>System requirements</h2>
  <div class="grid">
    <div class="card"><h3>System</h3><p>Windows 10 or 11, 64-bit. Administrator rights to install drivers.</p></div>
    <div class="card"><h3>Memory</h3><p>4 GB RAM. 8 GB recommended for the AI assistant.</p></div>
    <div class="card"><h3>Internet</h3><p>Needed to download drivers. Everything else works offline.</p></div>
  </div>
  <p class="updated">Installer SHA-256: <code style="word-break:break-all">88b6a2f6010c21476dd9adbda0cb236febe92c79fc685879237375ba74c442b9</code>. Windows may show a SmartScreen warning for new apps: click "More info" then "Run anyway".</p>
</div></section>
<div class="band"><h2>Fix your drivers in minutes.</h2><p class="lead">Free download for Windows 10 and 11.</p><div class="cta"><a class="btn p" href="/downloads/Kyrofix-Driver-Updater-Setup.exe" download>Download Kyrofix free</a></div></div>''')

# Kyrofix Cleaner
page('products/kyrofix-cleaner/index.html','Kyrofix Cleaner — Free PC cleaner for Windows','Kyrofix Cleaner for Windows 10 and 11: remove junk files, browser cache and Windows Update leftovers, turn off slow startup apps and find big files. Free download.',f'''
<section class="hero"><div class="wrap">
  <p class="crumb"><a href="/products/">Products</a> / Kyrofix Cleaner</p>
  <div class="ico kc" style="width:72px;height:72px"><img src="/img/kyrofix-cleaner/icon.png" alt="" width="56" height="56"></div>
  <span class="badge free">Free download · Windows 10 / 11</span>
  <h1 style="font-size:clamp(36px,5vw,60px);margin-top:16px;max-width:820px">Kyrofix Cleaner</h1>
  <p class="lead">Free up gigabytes in one click. Kyrofix Cleaner removes junk and leftovers, never your personal files, and shows you everything before it deletes.</p>
  <div class="cta"><a class="btn p" href="/downloads/Kyrofix-Cleaner-Setup.exe" download>Download free</a><a class="btn g" href="#plans">Free vs Pro</a></div>
  <div class="meta" style="margin-top:22px"><span>Version 1.1.0</span><span>Windows 10 / 11, 64-bit</span><span>No ads, no bundled extras</span></div>
  <div class="shot" style="margin-top:34px"><img src="/img/kyrofix-cleaner/results.jpg" alt="Kyrofix Cleaner scan results" width="1440" height="960"></div>
  {PRONOTE}
</div></section>
<section class="alt"><div class="wrap"><h2>What it cleans</h2>
  <div class="grid">
    <div class="card"><h3>Junk &amp; temp files</h3><p>Leftover files from Windows and apps that only take up space.</p></div>
    <div class="card"><h3>Windows Update leftovers</h3><p>Old update files and the Delivery Optimization cache.</p></div>
    <div class="card"><h3>Browser cache</h3><p>Chrome, Edge, Firefox, Brave and Opera. Your logins, passwords and history stay.</p></div>
    <div class="card"><h3>Faster startup</h3><p>Turn off apps that start with Windows. Turn them back on anytime.</p></div>
    <div class="card"><h3>Big file finder</h3><p>Find the biggest files hiding in your folders. Deleted files go to the Recycle Bin.</p></div>
    <div class="card"><h3>Safe by design</h3><p>Only caches and leftovers. Files in use are skipped, and you see everything before cleaning.</p></div>
  </div></div></section>
<section><div class="wrap"><h2>See it in action</h2>
  <div class="gallery">
    <figure><img src="/img/kyrofix-cleaner/scan.jpg" alt="Scan screen" loading="lazy"><figcaption>One click to scan</figcaption></figure>
    <figure><img src="/img/kyrofix-cleaner/startup.jpg" alt="Startup apps" loading="lazy"><figcaption>Startup apps on or off</figcaption></figure>
    <figure><img src="/img/kyrofix-cleaner/big.jpg" alt="Big files" loading="lazy"><figcaption>Find big files</figcaption></figure>
    <figure><img src="/img/kyrofix-cleaner/uninstall.jpg" alt="Uninstaller" loading="lazy"><figcaption>Uninstaller with leftover removal (Pro)</figcaption></figure>
    <figure><img src="/img/kyrofix-cleaner/dupes.jpg" alt="Duplicate files" loading="lazy"><figcaption>Duplicate file finder (Pro)</figcaption></figure>
  </div></div></section>
<section class="alt" id="plans"><div class="wrap"><h2>Free vs Pro</h2><p class="lead">The free version is a full cleaner. Pro adds automation and deep tools.</p>
  <div class="plans">
    <div class="plan"><span class="badge free">Free</span><h3 style="margin-top:12px">Cleaner Free</h3><div class="price">€0</div><div class="note">Free forever, no time limit</div><ul><li>Junk &amp; temp file cleaning</li><li>Windows Update leftovers</li><li>Browser cache (logins kept)</li><li>Startup manager</li><li>Big file finder</li><li class="x">Automatic cleaning</li><li class="x">Privacy cleaning</li></ul><a class="btn g" href="/downloads/Kyrofix-Cleaner-Setup.exe" download>Download free</a></div>
    <div class="plan hl">{SALEBADGE("cleaner")}<h3 style="margin-top:12px">Cleaner Pro</h3><div class="price">€14.99<small style="font-size:16px;color:var(--mut)"> / year</small></div><div class="note">Up to 3 PCs · or €39.99 one-time, forever</div><ul><li>Everything in Free</li><li>Automatic weekly cleaning</li><li>Privacy cleaning (history, cookies)</li><li>Uninstaller with leftover removal</li><li>Duplicate file finder</li><li>Priority support</li></ul>{buybtn("cleaner")}</div>
  </div>
  {PRONOTE}
</div></section>
<section><div class="wrap"><h2>System requirements</h2>
  <div class="grid">
    <div class="card"><h3>System</h3><p>Windows 10 or 11, 64-bit. Administrator rights to clean system folders.</p></div>
    <div class="card"><h3>Memory</h3><p>2 GB RAM.</p></div>
    <div class="card"><h3>Internet</h3><p>Not needed. Everything works offline.</p></div>
  </div>
  <p class="updated">Windows may show a SmartScreen warning for new apps: click "More info" then "Run anyway".</p>
</div></section>
<div class="band"><h2>Free up space in minutes.</h2><p class="lead">Free download for Windows 10 and 11.</p><div class="cta"><a class="btn p" href="/downloads/Kyrofix-Cleaner-Setup.exe" download>Download Kyrofix Cleaner</a></div></div>''')


# Kyrofix Backup
page('products/kyrofix-backup/index.html','Kyrofix Backup — Free file backup for Windows','Kyrofix Backup for Windows 10 and 11: back up your documents, desktop and photos to a USB drive, external disk or OneDrive folder. Restore in one click. Free download.',f'''
<section class="hero"><div class="wrap">
  <p class="crumb"><a href="/products/">Products</a> / Kyrofix Backup</p>
  <div class="ico kc" style="width:72px;height:72px"><img src="/img/kyrofix-backup/icon.png" alt="" width="56" height="56"></div>
  <span class="badge free">Free download · Windows 10 / 11</span>
  <h1 style="font-size:clamp(36px,5vw,60px);margin-top:16px;max-width:820px">Kyrofix Backup</h1>
  <p class="lead">Drives fail. Laptops get lost. Kyrofix Backup keeps a copy of your documents and photos on a USB drive or external disk, and gets them back in one click.</p>
  <div class="cta"><a class="btn p" href="/downloads/Kyrofix-Backup-Setup.exe" download>Download free</a><a class="btn g" href="#plans">Free vs Pro</a></div>
  <div class="meta" style="margin-top:22px"><span>Version 1.0.0</span><span>Windows 10 / 11, 64-bit</span><span>No admin rights needed</span></div>
  <div class="shot" style="margin-top:34px"><img src="/img/kyrofix-backup/home.jpg" alt="Kyrofix Backup main screen" width="1440" height="960"></div>
</div></section>
<section class="alt"><div class="wrap"><h2>Simple, safe backups</h2>
  <div class="grid">
    <div class="card"><h3>Your important folders</h3><p>Documents, Desktop and Pictures are picked for you. Add any other folder.</p></div>
    <div class="card"><h3>Any drive</h3><p>USB stick, external disk, second drive or a OneDrive folder.</p></div>
    <div class="card"><h3>Fast</h3><p>Only new and changed files are copied, so later backups take seconds.</p></div>
    <div class="card"><h3>Plain files</h3><p>Backups are normal folders. Open them in Explorer, even without Kyrofix.</p></div>
    <div class="card"><h3>Never deletes</h3><p>Deleting a file on your PC never removes it from the backup.</p></div>
    <div class="card"><h3>One-click restore</h3><p>Put back every missing file, without overwriting anything on your PC.</p></div>
  </div></div></section>
<section><div class="wrap"><h2>See it in action</h2>
  <div class="gallery">
    <figure><img src="/img/kyrofix-backup/restore.jpg" alt="Restore screen" loading="lazy"><figcaption>Restore missing files</figcaption></figure>
    <figure><img src="/img/kyrofix-backup/versions.jpg" alt="Version history" loading="lazy"><figcaption>Get back older versions (Pro)</figcaption></figure>
    <figure><img src="/img/kyrofix-backup/sched.jpg" alt="Automatic backups" loading="lazy"><figcaption>Automatic backups (Pro)</figcaption></figure>
  </div></div></section>
<section class="alt" id="plans"><div class="wrap"><h2>Free vs Pro</h2><p class="lead">The free version backs up and restores. Pro makes it automatic and keeps older versions.</p>
  <div class="plans">
    <div class="plan"><span class="badge free">Free</span><h3 style="margin-top:12px">Backup Free</h3><div class="price">€0</div><div class="note">Free forever, no time limit</div><ul><li>Back up any folders</li><li>USB, external disk or OneDrive folder</li><li>Only changed files are copied</li><li>Restore missing files</li><li class="x">Automatic backups</li><li class="x">Version history</li></ul><a class="btn g" href="/downloads/Kyrofix-Backup-Setup.exe" download>Download free</a></div>
    <div class="plan hl">{SALEBADGE("backup")}<h3 style="margin-top:12px">Backup Pro</h3><div class="price">€14.99<small style="font-size:16px;color:var(--mut)"> / year</small></div><div class="note">Up to 3 PCs · or €39.99 one-time, forever</div><ul><li>Everything in Free</li><li>Automatic daily or weekly backups</li><li>Version history (older copies)</li><li>Reminder when the drive is missing</li><li>Priority support</li></ul>{buybtn("backup")}</div>
  </div>
  {PRONOTE}
</div></section>
<section><div class="wrap"><h2>System requirements</h2>
  <div class="grid">
    <div class="card"><h3>System</h3><p>Windows 10 or 11, 64-bit. No administrator rights needed.</p></div>
    <div class="card"><h3>Storage</h3><p>A USB drive, external disk or any folder with enough free space.</p></div>
    <div class="card"><h3>Internet</h3><p>Not needed. Your files never leave your PC.</p></div>
  </div>
  <p class="updated">Windows may show a SmartScreen warning for new apps: click "More info" then "Run anyway".</p>
</div></section>
<div class="band"><h2>Don't lose your files.</h2><p class="lead">Free download for Windows 10 and 11.</p><div class="cta"><a class="btn p" href="/downloads/Kyrofix-Backup-Setup.exe" download>Download Kyrofix Backup</a></div></div>''')

# Kyrofix utilities
page('products/kyrofix-space/index.html','Kyrofix Space — Free for Windows','Kyrofix Space for Windows 10 and 11: What is filling your disk? See the biggest folders and files in seconds and free up space. Free download.',f'''
<section class="hero"><div class="wrap">
  <p class="crumb"><a href="/products/">Products</a> / Kyrofix Space</p>
  <div class="ico kc" style="width:72px;height:72px"><img src="/img/kyrofix-space/icon.png" alt="" width="56" height="56"></div>
  <span class="badge free">Free download · Windows 10 / 11</span>
  <h1 style="font-size:clamp(36px,5vw,60px);margin-top:16px;max-width:820px">Kyrofix Space</h1>
  <p class="lead">Your disk is full and you don’t know why. Kyrofix Space scans a drive in seconds and shows you exactly which folders and files take the space.</p>
  <div class="cta"><a class="btn p" href="/downloads/Kyrofix-Space-Setup.exe" download>Download free</a><a class="btn g" href="#plans">Free vs Pro</a></div>
  <div class="meta" style="margin-top:22px"><span>Version 1.0.0</span><span>Windows 10 / 11, 64-bit</span><span>No admin rights needed</span></div>
  <div class="shot" style="margin-top:34px"><img src="/img/kyrofix-space/s1.jpg" alt="Kyrofix Space" width="1100" height="740"></div>
</div></section>
<section class="alt"><div class="wrap"><h2>What it does</h2><div class="grid"><div class="card"><h3>Disk map</h3><p>See every folder sorted by size and drill down.</p></div><div class="card"><h3>Free up space</h3><p>Move what you don’t need to the Recycle Bin, safely.</p></div><div class="card"><h3>Protected</h3><p>Windows and program folders can’t be touched.</p></div><div class="card"><h3>Biggest files (Pro)</h3><p>The 100 largest files on your PC.</p></div><div class="card"><h3>File types (Pro)</h3><p>How much space videos, games and photos use.</p></div><div class="card"><h3>Old files (Pro)</h3><p>Big files you haven’t opened in over a year.</p></div></div></div></section>
<section class="alt" id="plans"><div class="wrap"><h2>Free vs Pro</h2>
  <div class="plans">
    <div class="plan"><span class="badge free">Free</span><h3 style="margin-top:12px">Free</h3><div class="price">€0</div><div class="note">Free forever</div><ul><li>Scan any drive or folder</li><li>Biggest folders, drill down</li><li>Move to Recycle Bin</li></ul><a class="btn g" href="/downloads/Kyrofix-Space-Setup.exe" download>Download free</a></div>
    <div class="plan hl">{SALEBADGE("space")}<h3 style="margin-top:12px">Pro</h3><div class="price">€9.99<small style="font-size:16px;color:var(--mut)"> / year</small></div><div class="note">Up to 3 PCs · or €24.99 one-time, forever</div><ul><li>Everything in Free</li><li>Biggest 100 files</li><li>File types breakdown</li><li>Old big files finder</li><li>Export report (CSV)</li></ul>{buybtn("space")}</div>
  </div>
  {PRONOTE}
</div></section>
<section><div class="wrap"><p class="updated">Windows may show a SmartScreen warning for new apps: click "More info" then "Run anyway".</p></div></section>
<div class="band"><h2>Try Kyrofix Space free.</h2><div class="cta"><a class="btn p" href="/downloads/Kyrofix-Space-Setup.exe" download>Download Kyrofix Space</a></div></div>''')

page('products/kyrofix-shredder/index.html','Kyrofix Shredder — Free for Windows','Kyrofix Shredder for Windows 10 and 11: Delete files for good. Shredded files cannot be recovered. Free download.',f'''
<section class="hero"><div class="wrap">
  <p class="crumb"><a href="/products/">Products</a> / Kyrofix Shredder</p>
  <div class="ico kc" style="width:72px;height:72px"><img src="/img/kyrofix-shredder/icon.png" alt="" width="56" height="56"></div>
  <span class="badge free">Free download · Windows 10 / 11</span>
  <h1 style="font-size:clamp(36px,5vw,60px);margin-top:16px;max-width:820px">Kyrofix Shredder</h1>
  <p class="lead">When you delete a file, it can often be brought back with recovery tools. Kyrofix Shredder overwrites the file first, so it is gone for good. Ideal before selling or giving away a PC.</p>
  <div class="cta"><a class="btn p" href="/downloads/Kyrofix-Shredder-Setup.exe" download>Download free</a><a class="btn g" href="#plans">Free vs Pro</a></div>
  <div class="meta" style="margin-top:22px"><span>Version 1.0.0</span><span>Windows 10 / 11, 64-bit</span><span>No admin rights needed</span></div>
  <div class="shot" style="margin-top:34px"><img src="/img/kyrofix-shredder/s1.jpg" alt="Kyrofix Shredder" width="1100" height="740"></div>
</div></section>
<section class="alt"><div class="wrap"><h2>What it does</h2><div class="grid"><div class="card"><h3>Shred files & folders</h3><p>Add anything and shred it in one click.</p></div><div class="card"><h3>Safe by design</h3><p>Windows, program folders and your main folders are protected.</p></div><div class="card"><h3>3 & 7 passes (Pro)</h3><p>Overwrite several times for maximum security.</p></div><div class="card"><h3>Recycle Bin (Pro)</h3><p>Shred everything you already deleted.</p></div><div class="card"><h3>Wipe free space (Pro)</h3><p>Make old deleted files unrecoverable.</p></div><div class="card"><h3>Right-click menu (Pro)</h3><p>"Shred with Kyrofix" in Explorer.</p></div></div></div></section>
<section class="alt" id="plans"><div class="wrap"><h2>Free vs Pro</h2>
  <div class="plans">
    <div class="plan"><span class="badge free">Free</span><h3 style="margin-top:12px">Free</h3><div class="price">€0</div><div class="note">Free forever</div><ul><li>Shred any files and folders</li><li>Quick 1-pass shredding</li><li>System folders protected</li></ul><a class="btn g" href="/downloads/Kyrofix-Shredder-Setup.exe" download>Download free</a></div>
    <div class="plan hl">{SALEBADGE("shredder")}<h3 style="margin-top:12px">Pro</h3><div class="price">€9.99<small style="font-size:16px;color:var(--mut)"> / year</small></div><div class="note">Up to 3 PCs · or €24.99 one-time, forever</div><ul><li>Everything in Free</li><li>3 and 7-pass shredding</li><li>Shred the Recycle Bin</li><li>Wipe free space</li><li>Right-click menu</li></ul>{buybtn("shredder")}</div>
  </div>
  {PRONOTE}
</div></section>
<section><div class="wrap"><p class="updated">Windows may show a SmartScreen warning for new apps: click "More info" then "Run anyway".</p></div></section>
<div class="band"><h2>Try Kyrofix Shredder free.</h2><div class="cta"><a class="btn p" href="/downloads/Kyrofix-Shredder-Setup.exe" download>Download Kyrofix Shredder</a></div></div>''')

page('products/kyrofix-photo-cleaner/index.html','Kyrofix Photo Cleaner — Free for Windows','Kyrofix Photo Cleaner for Windows 10 and 11: Find duplicate, similar and blurry photos and free up space. Free download.',f'''
<section class="hero"><div class="wrap">
  <p class="crumb"><a href="/products/">Products</a> / Kyrofix Photo Cleaner</p>
  <div class="ico kc" style="width:72px;height:72px"><img src="/img/kyrofix-photo-cleaner/icon.png" alt="" width="56" height="56"></div>
  <span class="badge free">Free download · Windows 10 / 11</span>
  <h1 style="font-size:clamp(36px,5vw,60px);margin-top:16px;max-width:820px">Kyrofix Photo Cleaner</h1>
  <p class="lead">Thousands of photos, the same picture saved three times, ten shots of the same sunset. Kyrofix Photo Cleaner finds them, keeps the best one and clears the rest.</p>
  <div class="cta"><a class="btn p" href="/downloads/Kyrofix-Photo-Cleaner-Setup.exe" download>Download free</a><a class="btn g" href="#plans">Free vs Pro</a></div>
  <div class="meta" style="margin-top:22px"><span>Version 1.0.0</span><span>Windows 10 / 11, 64-bit</span><span>No admin rights needed</span></div>
  <div class="shot" style="margin-top:34px"><img src="/img/kyrofix-photo-cleaner/s1.jpg" alt="Kyrofix Photo Cleaner" width="1100" height="740"></div>
</div></section>
<section class="alt"><div class="wrap"><h2>What it does</h2><div class="grid"><div class="card"><h3>Exact duplicates</h3><p>Finds copies of the same photo anywhere you choose.</p></div><div class="card"><h3>Keeps the best</h3><p>Picks the highest quality copy automatically.</p></div><div class="card"><h3>Nothing lost</h3><p>Everything goes to the Recycle Bin.</p></div><div class="card"><h3>Similar shots (Pro)</h3><p>Bursts and near-identical photos.</p></div><div class="card"><h3>Blurry photos (Pro)</h3><p>Out-of-focus and shaken pictures.</p></div><div class="card"><h3>Private</h3><p>Your photos never leave your PC.</p></div></div></div></section>
<section class="alt" id="plans"><div class="wrap"><h2>Free vs Pro</h2>
  <div class="plans">
    <div class="plan"><span class="badge free">Free</span><h3 style="margin-top:12px">Free</h3><div class="price">€0</div><div class="note">Free forever</div><ul><li>Find exact duplicate photos</li><li>Keeps the best copy</li><li>Everything to the Recycle Bin</li></ul><a class="btn g" href="/downloads/Kyrofix-Photo-Cleaner-Setup.exe" download>Download free</a></div>
    <div class="plan hl">{SALEBADGE("photo")}<h3 style="margin-top:12px">Pro</h3><div class="price">€9.99<small style="font-size:16px;color:var(--mut)"> / year</small></div><div class="note">Up to 3 PCs · or €24.99 one-time, forever</div><ul><li>Everything in Free</li><li>Similar photos (bursts, re-saves)</li><li>Blurry photo finder</li><li>Auto-picks the best shot</li></ul>{buybtn("photo")}</div>
  </div>
  {PRONOTE}
</div></section>
<section><div class="wrap"><p class="updated">Windows may show a SmartScreen warning for new apps: click "More info" then "Run anyway".</p></div></section>
<div class="band"><h2>Try Kyrofix Photo Cleaner free.</h2><div class="cta"><a class="btn p" href="/downloads/Kyrofix-Photo-Cleaner-Setup.exe" download>Download Kyrofix Photo Cleaner</a></div></div>''')

# Activate: exchange a Gumroad licence key for a Kyrofix key
page('activate/index.html','Get your Kyrofix key — Halewood Systems','Bought Kyrofix Pro? Paste the licence key from your Gumroad receipt to get your Kyrofix key.',f'''
<section class="hero"><div class="wrap" style="max-width:720px">
  <h1>Get your Kyrofix key</h1>
  <p class="lead">Thanks for buying Kyrofix Pro! Paste the <b>licence key from your Gumroad receipt</b> below.</p>
  <div class="card" style="margin-top:24px;padding:22px">
    <label for="lic"><b>Gumroad licence key</b></label>
    <input id="lic" placeholder="XXXXXXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX" spellcheck="false" autocomplete="off" style="width:100%;margin:10px 0 14px;padding:12px 14px;border-radius:10px;border:1px solid var(--line,#2a3140);background:transparent;color:inherit;font:inherit">
    <button class="btn p" id="go" type="button">Get my key</button>
    <p id="msg" class="updated" style="margin-top:12px"></p>
    <div id="out" style="display:none;margin-top:8px">
      <p><b id="pn"></b> <span id="pe"></span></p>
      <code id="key" style="display:block;padding:14px;border-radius:10px;background:rgba(127,127,127,.12);word-break:break-all;font-size:15px"></code>
      <button class="btn g" id="cp" type="button" style="margin-top:12px">Copy key</button>
      <ol style="margin-top:18px;line-height:1.8"><li>Open the Kyrofix app and go to <b>Pro</b>.</li><li>Paste the key and click <b>Activate</b>.</li><li>Use the same key on up to 3 of your PCs.</li></ol>
      <p class="updated">Keep this key. You can come back to this page anytime and paste the same Gumroad key to see it again.</p>
    </div>
  </div>
  <p class="updated" style="margin-top:18px">Problems? Email <b>{MAIL}</b> with your Gumroad receipt.</p>
</div></section>
<script>
const $=s=>document.querySelector(s);
$('#go').onclick=async()=>{{const l=$('#lic').value.trim();if(!l)return;$('#go').disabled=true;$('#msg').textContent='Checking your purchase…';$('#out').style.display='none';
 try{{const r=await(await fetch('https://windrova-api.thomaslipknot1.workers.dev/kyro/redeem',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{license:l}})}})).json();
  if(r.ok){{$('#msg').textContent='';$('#pn').textContent=r.name;$('#pe').textContent=r.lifetime?'· forever':'· valid until '+r.expires;$('#key').textContent=r.key;$('#out').style.display='block';}}
  else $('#msg').textContent={{bad:'We could not find this licence key. Copy it exactly from your Gumroad receipt.',refunded:'This purchase was refunded, so the key no longer works.',empty:'Your purchase is fine, but we need a moment to prepare your key. Please email us and we will send it today.',net:'Could not check right now. Please try again in a minute.'}}[r.reason]||'Something went wrong. Please email us.';}}
 catch(e){{$('#msg').textContent='Could not connect. Check your internet and try again.';}}
 $('#go').disabled=false;}};
$('#lic').onkeydown=e=>{{if(e.key==='Enter')$('#go').click();}};
$('#cp').onclick=()=>{{navigator.clipboard.writeText($('#key').textContent);$('#cp').textContent='Copied';}};
</script>''')

# New games
page('products/potion-sort/index.html','Potion Sort — Free game for phones','Potion Sort: Pour the potions until every bottle holds one colour. Endless relaxing levels. Free to play on any phone or computer, no download needed.',f'''
<section class="hero"><div class="wrap">
  <p class="crumb"><a href="/products/">Products</a> / Potion Sort</p>
  <div class="ico kc" style="width:72px;height:72px"><img src="/img/potion-sort/icon.png" alt="" width="64" height="64"></div>
  <span class="badge live">Free to play · Phone &amp; browser</span>
  <h1 style="font-size:clamp(36px,5vw,60px);margin-top:16px">Potion Sort</h1>
  <p class="lead">A colour-sorting puzzle with endless levels. Tap a bottle, tap another, and pour. Every level can be solved.</p>
  <div class="cta"><a class="btn p" href="/games/potion-sort/">Play free now</a></div>
  <div class="meta" style="margin-top:22px"><span>No download</span><span>Works offline after first play</span><span>Add to your home screen</span></div>
</div></section>
<section class="alt"><div class="wrap"><h2>Screenshots</h2><div class="gallery">
  <figure><img src="/img/potion-sort/s0.jpg" alt="Potion Sort menu" loading="lazy"></figure><figure><img src="/img/potion-sort/s1.jpg" alt="Potion Sort gameplay" loading="lazy"></figure>
</div></div></section>
<section><div class="wrap"><h2>How to play</h2><div class="grid"><div class="card"><h3>1</h3><p>Tap a bottle to pick it up, tap another to pour.</p></div><div class="card"><h3>2</h3><p>You can only pour onto the same colour or into an empty bottle.</p></div><div class="card"><h3>3</h3><p>Finish when every bottle holds one colour.</p></div></div>
  <p class="updated">On iPhone: open the game in Safari, tap Share, then "Add to Home Screen". On Android: Chrome menu, then "Install app".</p></div></section>
<div class="band"><h2>Ready to play?</h2><div class="cta"><a class="btn p" href="/games/potion-sort/">Play Potion Sort free</a></div></div>''')

page('products/triple-bloom/index.html','Triple Bloom — Free game for phones','Triple Bloom: Tap tiles and match three of a kind to clear the garden. Free to play on any phone or computer, no download needed.',f'''
<section class="hero"><div class="wrap">
  <p class="crumb"><a href="/products/">Products</a> / Triple Bloom</p>
  <div class="ico kc" style="width:72px;height:72px"><img src="/img/triple-bloom/icon.png" alt="" width="64" height="64"></div>
  <span class="badge live">Free to play · Phone &amp; browser</span>
  <h1 style="font-size:clamp(36px,5vw,60px);margin-top:16px">Triple Bloom</h1>
  <p class="lead">A tile-matching puzzle in a garden. Tap a free tile to put it in your tray; three of the same disappear. Clear the board before the tray fills up.</p>
  <div class="cta"><a class="btn p" href="/games/triple-bloom/">Play free now</a></div>
  <div class="meta" style="margin-top:22px"><span>No download</span><span>Works offline after first play</span><span>Add to your home screen</span></div>
</div></section>
<section class="alt"><div class="wrap"><h2>Screenshots</h2><div class="gallery">
  <figure><img src="/img/triple-bloom/s0.jpg" alt="Triple Bloom menu" loading="lazy"></figure><figure><img src="/img/triple-bloom/s1.jpg" alt="Triple Bloom gameplay" loading="lazy"></figure>
</div></div></section>
<section><div class="wrap"><h2>How to play</h2><div class="grid"><div class="card"><h3>1</h3><p>Tap any tile that is not covered.</p></div><div class="card"><h3>2</h3><p>Three of the same in the tray disappear.</p></div><div class="card"><h3>3</h3><p>Clear every tile before your 7-slot tray is full.</p></div></div>
  <p class="updated">On iPhone: open the game in Safari, tap Share, then "Add to Home Screen". On Android: Chrome menu, then "Install app".</p></div></section>
<div class="band"><h2>Ready to play?</h2><div class="cta"><a class="btn p" href="/games/triple-bloom/">Play Triple Bloom free</a></div></div>''')

page('products/skystack/index.html','Skystack — Free game for phones','Skystack: Tap to drop the block. Stack as high as you can. Free to play on any phone or computer, no download needed.',f'''
<section class="hero"><div class="wrap">
  <p class="crumb"><a href="/products/">Products</a> / Skystack</p>
  <div class="ico kc" style="width:72px;height:72px"><img src="/img/skystack/icon.png" alt="" width="64" height="64"></div>
  <span class="badge live">Free to play · Phone &amp; browser</span>
  <h1 style="font-size:clamp(36px,5vw,60px);margin-top:16px">Skystack</h1>
  <p class="lead">A one-tap tower game. Drop each sliding block onto the tower. What hangs over gets cut off. Hit perfect drops in a row and your tower grows back.</p>
  <div class="cta"><a class="btn p" href="/games/skystack/">Play free now</a></div>
  <div class="meta" style="margin-top:22px"><span>No download</span><span>Works offline after first play</span><span>Add to your home screen</span></div>
</div></section>
<section class="alt"><div class="wrap"><h2>Screenshots</h2><div class="gallery">
  <figure><img src="/img/skystack/s0.jpg" alt="Skystack menu" loading="lazy"></figure><figure><img src="/img/skystack/s1.jpg" alt="Skystack gameplay" loading="lazy"></figure>
</div></div></section>
<section><div class="wrap"><h2>How to play</h2><div class="grid"><div class="card"><h3>1</h3><p>Tap anywhere to drop the sliding block.</p></div><div class="card"><h3>2</h3><p>Anything hanging over the edge falls off.</p></div><div class="card"><h3>3</h3><p>Six perfect drops in a row make the tower bigger again.</p></div></div>
  <p class="updated">On iPhone: open the game in Safari, tap Share, then "Add to Home Screen". On Android: Chrome menu, then "Install app".</p></div></section>
<div class="band"><h2>Ready to play?</h2><div class="cta"><a class="btn p" href="/games/skystack/">Play Skystack free</a></div></div>''')

# Starfuse
page('products/starfuse/index.html','Starfuse — Free space merge game for phones','Starfuse: drop planets, merge matching ones and grow them into stars and black holes. Free to play on any phone or computer, no download needed.',f'''
<section class="hero"><div class="wrap">
  <p class="crumb"><a href="/products/">Products</a> / Starfuse</p>
  <div class="ico kc" style="width:72px;height:72px"><img src="/img/starfuse/icon.png" alt="" width="64" height="64"></div>
  <span class="badge live">Free to play · Phone &amp; browser</span>
  <h1 style="font-size:clamp(36px,5vw,60px);margin-top:16px">Starfuse</h1>
  <p class="lead">Drop planets. Merge two of the same into a bigger one. Moons become planets, planets become stars, and two blue stars make a black hole. How far can you grow your cosmos?</p>
  <div class="cta"><a class="btn p" href="/games/starfuse/">Play free now</a></div>
  <div class="meta" style="margin-top:22px"><span>No download</span><span>Works offline after first play</span><span>Add to your home screen</span></div>
</div></section>
<section class="alt"><div class="wrap"><h2>Screenshots</h2>
  <div class="gallery">
    <figure><img src="/img/starfuse/menu.jpg" alt="Starfuse menu" loading="lazy"><figcaption>12 planets to discover</figcaption></figure>
    <figure><img src="/img/starfuse/play.jpg" alt="Starfuse gameplay" loading="lazy"><figcaption>Merge and chain combos</figcaption></figure>
    <figure><img src="/img/starfuse/over.jpg" alt="Starfuse black hole" loading="lazy"><figcaption>Make a black hole</figcaption></figure>
  </div></div></section>
<section><div class="wrap"><h2>How to play</h2>
  <div class="grid">
    <div class="card"><h3>Drop</h3><p>Slide your finger to aim, let go to drop the planet.</p></div>
    <div class="card"><h3>Merge</h3><p>Two of the same touch and fuse into the next, bigger planet. Chain merges for combos.</p></div>
    <div class="card"><h3>Don't overflow</h3><p>If planets stay above the line too long, your cosmos is full. Shake, Pop and Swap help you out.</p></div>
  </div>
  <p class="updated">On iPhone: open the game in Safari, tap Share, then "Add to Home Screen". On Android: Chrome menu, then "Install app".</p>
</div></section>
<div class="band"><h2>Ready to make a black hole?</h2><div class="cta"><a class="btn p" href="/games/starfuse/">Play Starfuse free</a></div></div>''')

# Slipgate
page('products/slipgate/index.html','Slipgate — Free puzzle game | Halewood Systems','Slipgate: a free puzzle game that starts easy and gets hard fast. Play in your browser.',f'''
<section class="hero"><div class="wrap">
  <p class="crumb"><a href="/products/">Products</a> / Slipgate</p>
  <div class="ico sg" style="width:72px;height:72px">{SG_ICO}</div>
  <span class="badge free">Free to play · Browser</span>
  <h1 style="font-size:clamp(36px,5vw,60px);margin-top:16px">Slipgate</h1>
  <p class="lead">A tricky puzzle game that starts easy and gets hard fast. No download, no sign-up. Just play.</p>
  <div class="cta"><a class="btn p" href="https://halewood-systems.itch.io/slipgate" target="_blank" rel="noopener">Play free on itch.io →</a></div>
  <div class="meta" style="margin-top:22px"><span>Browser</span><span>Free</span><span>Desktop &amp; mobile</span></div>
</div></section>''')

# Pricing
page('pricing/index.html','Pricing — Halewood Systems','Prices for Windrova and Kyrofix. Every product has a free version. Prices include VAT where applicable.',f'''
<section class="hero"><div class="wrap"><h1>Pricing</h1><p class="lead">Every product has a free version. Paid plans are coming soon.</p></div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="tablewrap" style="margin-top:0"><table>
    <thead><tr><th>Product</th><th>Free</th><th>Paid</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td><b>Windrova</b><br><small style="color:var(--mut)">Weather map</small></td><td class="y">€0</td><td>Premium: €2.49 / month or €19.99 / year</td><td><span class="badge soon">Paid plan soon</span></td></tr>
      <tr><td><b>Kyrofix Driver Updater</b><br><small style="color:var(--mut)">Windows</small></td><td class="y">€0</td><td>Pro: €19.99 / year or €49.99 forever</td><td>{'<span class="badge live">On sale</span>' if BUY['driver'] else '<span class="badge free">Free available</span>'}</td></tr>
      <tr><td><b>Kyrofix Cleaner</b><br><small style="color:var(--mut)">Windows</small></td><td class="y">€0</td><td>Pro: €14.99 / year or €39.99 forever</td><td>{'<span class="badge live">On sale</span>' if BUY['cleaner'] else '<span class="badge free">Free available</span>'}</td></tr>
      <tr><td><b>Kyrofix Backup</b><br><small style="color:var(--mut)">Windows</small></td><td class="y">€0</td><td>Pro: €14.99 / year or €39.99 forever</td><td>{'<span class="badge live">On sale</span>' if BUY['backup'] else '<span class="badge free">Free available</span>'}</td></tr>
      <tr><td><b>Kyrofix Space</b><br><small style="color:var(--mut)">Windows</small></td><td class="y">€0</td><td>Pro: €9.99 / year or €24.99 forever</td><td>{'<span class="badge live">On sale</span>' if BUY['space'] else '<span class="badge free">Free available</span>'}</td></tr>
      <tr><td><b>Kyrofix Shredder</b><br><small style="color:var(--mut)">Windows</small></td><td class="y">€0</td><td>Pro: €9.99 / year or €24.99 forever</td><td>{'<span class="badge live">On sale</span>' if BUY['shredder'] else '<span class="badge free">Free available</span>'}</td></tr>
      <tr><td><b>Kyrofix Photo Cleaner</b><br><small style="color:var(--mut)">Windows</small></td><td class="y">€0</td><td>Pro: €9.99 / year or €24.99 forever</td><td>{'<span class="badge live">On sale</span>' if BUY['photo'] else '<span class="badge free">Free available</span>'}</td></tr>
      <tr><td><b>Slipgate</b><br><small style="color:var(--mut)">Game</small></td><td class="y">€0</td><td class="n">—</td><td><span class="badge live">Free</span></td></tr>
    </tbody></table></div>
  <h2 style="margin-top:64px;font-size:28px">Questions</h2>
  <details><summary>When can I buy a paid plan?</summary><p>Paid plans open soon. Until then, every product is free to use. Follow us on <a href="{YT}" style="color:#7fb0ff">YouTube</a> to hear first.</p></details>
  <details><summary>Do prices include VAT?</summary><p>Yes. For customers in the EU, prices shown include VAT where it applies.</p></details>
  <details><summary>Can I get a refund?</summary><p>Yes, under EU consumer law. See <a href="/legal/refunds/" style="color:#7fb0ff">Refunds &amp; withdrawal</a>.</p></details>
  <details><summary>Can I cancel a subscription?</summary><p>Yes, at any time. You keep access until the end of the period you paid for.</p></details>
</div></section>''')

# Support
page('support/index.html','Support & contact — Halewood Systems','Get help with Halewood Systems products, or contact us.',f'''
<section class="hero"><div class="wrap"><h1>Support</h1><p class="lead">Questions, bugs or ideas? We read every message.</p>
  <div class="cta"><a class="btn p" href="mailto:{MAIL}">Email us</a><a class="btn g" href="{YT}" target="_blank" rel="noopener">YouTube</a></div>
  <p class="updated" style="margin-top:16px">Email: <b style="color:var(--txt)">{MAIL}</b> · We usually reply within 2 working days.</p>
</div></section>
<section style="padding-top:0"><div class="wrap" style="max-width:820px;margin:0 auto">
  <h2 style="font-size:28px">Frequently asked</h2>
  <details><summary>Is Windrova really free?</summary><p>Yes. All weather maps, models and the 10-day forecast are free, with no account and no ads.</p></details>
  <details><summary>When is the Windrova mobile app coming?</summary><p>Soon. Until then, open windrova.com on your phone and use "Add to home screen". It works like an app.</p></details>
  <details><summary>Is Kyrofix free?</summary><p>Yes. The free version updates your drivers with no time limit. Pro, with automatic updates and extras, is coming soon.</p></details>
  <details><summary>Something isn't working. What do I send?</summary><p>Tell us which product, what you did, and what happened. A screenshot helps a lot.</p></details>
  <details><summary>How do I delete my data?</summary><p>We keep almost no data. If you emailed us, ask and we'll delete your messages. See our <a href="/legal/privacy/" style="color:#7fb0ff">Privacy policy</a>.</p></details>
</div></section>''')

# About
page('about/index.html','About — Halewood Systems','Halewood Systems is an independent software studio in the EU.',f'''
<section class="hero"><div class="wrap doc"><h1>About</h1>
  <p class="lead">Halewood Systems is an independent software studio based in the European Union.</p>
  <p style="margin-top:28px">We make tools we want to use ourselves: fast, simple and honest. No bundled extras, no dark patterns, no selling your data.</p>
  <p>Our first product, <a href="/products/windrova/">Windrova</a>, brings professional weather models to everyone, free. Then came <a href="/products/kyrofix/">Kyrofix</a>, PC care software that explains what it does. We also make games, like <a href="/products/starfuse/">Starfuse</a>, <a href="/products/potion-sort/">Potion Sort</a>, <a href="/products/triple-bloom/">Triple Bloom</a>, <a href="/products/skystack/">Skystack</a> and <a href="/products/slipgate/">Slipgate</a>.</p>
  <p>Want to follow along? Watch us build on <a href="{YT}" target="_blank" rel="noopener">YouTube</a>.</p>
</div></section>''')

# ---------- legal ----------
UPD='<p class="updated">Last updated: 19 November 2026</p>'
def legal(slug,title,desc,content):
    page(f'legal/{slug}/index.html',f'{title} — Halewood Systems',desc,f'<section class="hero" style="padding-bottom:30px"><div class="wrap doc"><p class="crumb">Legal</p><h1 style="font-size:clamp(34px,5vw,52px)">{title}</h1>{UPD}</div></section><section style="padding-top:0"><div class="wrap doc">{content}</div></section>')

legal('notice','Legal notice','Legal notice and provider information for Halewood Systems.',f'''
<h2>Provider</h2><p>Halewood Systems is an independent software project operated in Greece, European Union.</p>
<p>Email: <b>{MAIL}</b><br>Website: halewoodsystems.com</p>
<div class="box">Kyrofix Pro licences are sold through our online reseller Gumroad, Inc., which is the merchant of record: it processes the payment, issues the receipt and handles VAT. Questions about a purchase: <b>{MAIL}</b>.</div>
<h2>Responsibility for content</h2><p>We take care to keep the information on this site accurate, but it may change without notice. Links to other websites are provided for convenience; we are not responsible for their content.</p>
<h2>Weather information</h2><p>Windrova shows forecasts from public weather services. Forecasts can be wrong. Do not rely on them alone for safety decisions at sea, in the mountains or in the air; always check official warnings.</p>
<h2>Copyright</h2><p>All content on this site, including text, design and logos, belongs to Halewood Systems unless stated otherwise. Third-party data and trademarks belong to their owners.</p>''')

legal('terms','Terms of use','Terms of use for Halewood Systems websites and software.',f'''
<p>These terms apply when you use halewoodsystems.com and our products (Windrova, Kyrofix, Slipgate and others). By using them you agree to these terms. If you are a consumer, nothing here limits your rights under the law of your country of residence in the EU.</p>
<h2>1. Our products</h2><p>We offer free versions of our products, and in the future paid plans (for example Windrova Premium and Kyrofix Pro). The features of each plan are described on its product page at the time you get it.</p>
<h2>2. Licence</h2><p>We give you a personal, non-exclusive, non-transferable licence to use our software for your own purposes. You may not resell it, copy it for distribution, remove notices, or try to break its protections, except where the law allows.</p>
<h2>3. Paid plans</h2><ul><li>Kyrofix Pro is sold as a one-time payment: a licence for 1 year, or a licence forever. Nothing renews automatically.</li><li>Payments are processed by our reseller Gumroad, which is the seller of record and handles VAT. We never see your card details.</li><li>Each licence key works on up to 3 of your own PCs. A licence for 1 year stops unlocking Pro 365 days after purchase; the free version keeps working.</li><li>Keys that were refunded or charged back stop working.</li><li>Your right of withdrawal is explained in <a href="/legal/refunds/">Refunds &amp; withdrawal</a>.</li></ul>
<h2>4. Acceptable use</h2><p>Do not use our services to break the law, to attack or overload our systems, or to copy our data in bulk with automated tools.</p>
<h2>5. Weather and system information</h2><p>Windrova forecasts come from public weather services and can be wrong. Kyrofix changes system drivers; it creates a restore point first, but you use it at your own judgement. Keep backups of important files.</p>
<h2>6. Legal guarantee</h2><p>If a product does not work as described, you have the rights given by EU law for digital content and services (Directive (EU) 2019/770), including repair, a price reduction or a refund.</p>
<h2>7. Liability</h2><p>We are fully liable for damage caused intentionally or through gross negligence, and for injury to life, body or health. Otherwise, to the extent the law allows, we are not liable for indirect or unforeseeable damage. Free products are provided as they are.</p>
<h2>8. Changes</h2><p>We may update these terms. If a change affects a paid plan you have, we will tell you in advance, and you may cancel.</p>
<h2>9. Law and disputes</h2><p>Greek law applies, without removing the protection of the law of your country of residence if you are a consumer. If something goes wrong, please contact us first at {MAIL}. You can also contact your national consumer authority; in Greece, the Hellenic Consumer Ombudsman (<a href="https://www.synigoroskatanaloti.gr" target="_blank" rel="noopener">synigoroskatanaloti.gr</a>).</p>''')

legal('privacy','Privacy policy','How Halewood Systems handles personal data, under the EU GDPR.',f'''
<p>We collect as little personal data as possible. This policy explains what we process, why, and your rights under the EU General Data Protection Regulation (GDPR).</p>
<h2>Who is responsible</h2><p>Halewood Systems, Greece, EU. Contact: <b>{MAIL}</b>.</p>
<h2>What we process</h2>
<h3>Visiting our websites</h3><p>Our sites are hosted on GitHub Pages and use Cloudflare for some services. These providers process technical data such as your IP address and browser type to deliver the pages and keep them secure. We do not use advertising or tracking cookies. We count visits with Cloudflare Web Analytics, which uses no cookies and does not identify you.</p>
<h3>Windrova</h3><p>When you look up a forecast, the map position is sent to our weather relay and to public weather services (such as MET Norway) to get the data. Your settings (language, units, favourite places) are stored only in your own browser. Place search uses the Photon service.</p>
<h3>Emails</h3><p>If you email us, we use your email address and message only to answer you, and delete them when they are no longer needed.</p>
<h3>Purchases</h3><p>Kyrofix Pro purchases are handled by Gumroad, Inc. as merchant of record, under its own <a href="https://gumroad.com/privacy" target="_blank" rel="noopener">privacy policy</a>. Gumroad shares with us your email address and the licence key, which we use to deliver and check your Kyrofix key, and to answer support questions. Keys are checked online when you activate Pro; we store the key number and an anonymous ID of each PC.</p><h3>Donations</h3><p>Donations are handled by Stripe. Stripe processes your payment details under its own <a href="https://stripe.com/privacy" target="_blank" rel="noopener">privacy policy</a>. We receive only what we need for our records, such as the amount and date.</p>
<h2>Legal bases</h2><ul><li>Providing a service you asked for (Art. 6(1)(b) GDPR)</li><li>Our legitimate interest in running secure, working websites (Art. 6(1)(f))</li><li>Legal obligations, such as keeping invoices (Art. 6(1)(c))</li></ul>
<h2>Transfers outside the EU</h2><p>Some providers (for example GitHub, Cloudflare, Gumroad and Stripe) may process data outside the EU. They use safeguards approved by the European Commission, such as Standard Contractual Clauses or the EU–US Data Privacy Framework.</p>
<h2>How long we keep data</h2><p>Only as long as needed for the purpose, or as long as the law requires (for example, tax records).</p>
<h2>Your rights</h2><p>You can ask to access, correct or delete your data, to restrict or object to processing, and to receive your data in a portable format. Email {MAIL}. You can also complain to a data protection authority; in Greece this is the Hellenic Data Protection Authority (<a href="https://www.dpa.gr" target="_blank" rel="noopener">dpa.gr</a>).</p>
<h2>Children</h2><p>Our services are not aimed at children under 16, and we do not knowingly collect their data.</p>''')

legal('refunds','Refunds & withdrawal','Your 14-day right of withdrawal and refunds for Halewood Systems products, under EU law.',f'''
<p>Every product has a free version, so you can try it fully before you pay. Kyrofix Pro licences are sold through Gumroad, which processes payments and refunds.</p>
<h2>14-day right of withdrawal</h2><p>If you are a consumer in the EU, you can withdraw from a purchase within 14 days without giving a reason (Directive 2011/83/EU). The 14 days start on the day you buy.</p>
<h2>Digital content you start using right away</h2><p>For software and digital content delivered immediately, the law allows the right of withdrawal to end once delivery starts, but only if you agreed to this at checkout and confirmed you understand you lose the right. We will always ask you clearly before that happens.</p>
<h2>Kyrofix Pro</h2><p>Pro is a one-time payment, not a subscription. If you ask within 14 days of buying, we refund you in full, even if you already activated the key; the key then stops working.</p>
<h2>If something doesn't work</h2><p>If a product does not work as described, you are entitled to have it fixed, or to a price reduction or refund, under EU law on digital content (Directive (EU) 2019/770). This applies regardless of the 14-day period.</p>
<h2>How to ask</h2><p>Email <b>{MAIL}</b> with the email address you used and the date of purchase. You can also use this sentence: "I hereby give notice that I withdraw from my contract for the following product: …". We refund within 14 days, to the same payment method, at no cost to you.</p>
<h2>Donations</h2><p>Donations are voluntary gifts and are not purchases. If you donated by mistake, contact us within 14 days and we will refund it.</p>''')

legal('cookies','Cookies','Cookie information for Halewood Systems websites.',f'''
<h2>Short version</h2><p>We do not use advertising or tracking cookies, so we don't show a cookie banner.</p>
<h2>What we store</h2><ul><li><b>halewoodsystems.com:</b> no cookies.</li><li><b>Windrova:</b> your settings (language, units, favourite places, last map view) are saved in your browser's local storage so the map remembers them. They never leave your device and you can clear them in your browser settings.</li></ul>
<h2>Third parties</h2><p>When you buy, Gumroad may set cookies needed for checkout, on its own pages. When you donate, Stripe may set cookies needed for secure payment and fraud prevention, on its own pages. See Stripe's policy.</p>
<h2>Changes</h2><p>If we ever add cookies that need your consent, we will ask you first.</p>''')

# 404
page('404.html','Page not found — Halewood Systems','Page not found.','<section class="hero center"><div class="wrap"><h1>Page not found</h1><p class="lead">The page you were looking for doesn\'t exist.</p><div class="cta"><a class="btn p" href="/">Go home</a><a class="btn g" href="/products/">See products</a></div></div></section>')
print('ok')
