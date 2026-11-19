import os, textwrap
import pathlib; R=str(pathlib.Path(__file__).resolve().parent.parent)
YT='https://www.youtube.com/@HalewoodSystems'
DON='https://buy.stripe.com/14AcMY4rr24U6Pqec0dUY02'
MAIL='support@halewoodsystems.com'
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
<link rel="stylesheet" href="/assets/site.css?v=4">
</head>
<body>
<header id="nav"></header>
<main>
{body}
</main>
<footer id="foot"></footer>
<script src="/assets/site.js?v=4"></script>
<script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "a11dfd5ee7a843d0b247e834f27c971c"}}'></script>
</body>
</html>
'''
    fp=os.path.join(R,path); os.makedirs(os.path.dirname(fp),exist_ok=True); open(fp,'w').write(html)

CARDS=f'''<div class="grid">
  <a class="card" href="/products/windrova/"><div class="ico"><img src="/img/windrova-icon.png" alt=""></div><span class="badge live">● Live</span><h3>Windrova</h3><p>Live weather map for the whole world, with three forecast models and an activity planner.</p><div class="meta"><span>Web · Free</span><span>Mobile app soon</span></div></a>
  <a class="card" href="/products/kyrofix/"><div class="ico kf">{KF_ICO}</div><span class="badge free">Free download</span><h3>Kyrofix Driver Updater</h3><p>Finds outdated drivers and updates them safely, with an AI assistant that explains every fix.</p><div class="meta"><span>Windows · Free &amp; Pro</span></div></a>
  <a class="card" href="/products/kyrofix-cleaner/"><div class="ico kc"><img src="/img/kyrofix-cleaner/icon.png" alt="" width="34" height="34"></div><span class="badge free">Free download</span><h3>Kyrofix Cleaner</h3><p>Cleans junk files, browser cache and update leftovers, and speeds up Windows startup.</p><div class="meta"><span>Windows · Free &amp; Pro</span></div></a>
  <a class="card" href="/products/slipgate/"><div class="ico sg">{SG_ICO}</div><span class="badge free">Free to play</span><h3>Slipgate</h3><p>A tricky puzzle game that starts easy and gets hard fast. Play it free in your browser.</p><div class="meta"><span>Browser · Free</span></div></a>
</div>'''

# ---------- home ----------
page('index.html','Halewood Systems — Software that just works','Halewood Systems makes fast, simple software: Windrova live weather map, Kyrofix PC tools and games. Free to start.',f'''
<section class="hero center"><div class="wrap">
  <span class="badge free" style="margin-bottom:24px">Independent software studio · EU</span>
  <h1 style="max-width:900px">Software that <span>just works.</span></h1>
  <p class="lead" style="max-width:620px">Halewood Systems builds fast, simple tools for everyday life, from live weather to PC care and games. Free to start, no clutter.</p>
  <div class="cta"><a class="btn p" href="/products/">Explore products</a><a class="btn g" href="{YT}" target="_blank" rel="noopener">Watch on YouTube</a></div>
</div></section>
<section style="padding-top:20px"><div class="wrap feat">
  <div>
    <span class="badge live">● Live now</span>
    <h2 style="margin-top:16px">Windrova. The whole world's weather, live.</h2>
    <p class="lead">A live weather map for every place on Earth. Open it in any browser, no account needed.</p>
    <ul class="ticks"><li>Live wind, rain, temperature, clouds and sea waves</li><li>ECMWF, GFS and GEM forecast models in one click</li><li>Hurricanes, lightning, earthquakes, fires and live satellite</li><li>Best hours for the beach, sailing, kitesurf and hiking</li></ul>
    <div class="cta"><a class="btn p" href="https://windrova.com" target="_blank" rel="noopener">Open Windrova, free →</a><a class="btn g" href="/products/windrova/">Learn more</a></div>
  </div>
  <div class="shot"><img src="/img/windrova/hero.jpg" alt="Windrova live wind map over Europe" width="1440" height="810"></div>
</div></section>
<section class="alt"><div class="wrap"><h2>Our products</h2><p class="lead">Everything we make, in one place. Every product has a free version.</p>{CARDS}</div></section>
<section><div class="wrap"><h2>Why Halewood</h2>
  <div class="grid">
    <div class="card"><h3>Free to start</h3><p>Every product has a free version that's actually useful, not a demo.</p></div>
    <div class="card"><h3>No clutter</h3><p>No bundled extras, no pop-ups, no tricks. Just the tool you came for.</p></div>
    <div class="card"><h3>Privacy first</h3><p>No ads and no tracking cookies. We follow EU privacy law (GDPR).</p></div>
  </div></div></section>
<div class="band"><h2>Try Windrova today.</h2><p class="lead">Free, live, and ready in your browser.</p><div class="cta"><a class="btn p" href="https://windrova.com" target="_blank" rel="noopener">Open Windrova</a><a class="btn g" href="{DON}" target="_blank" rel="noopener">❤ Support us</a></div></div>
''')

# ---------- products ----------
page('products/index.html','Products — Halewood Systems','All Halewood Systems products: Windrova weather map, Kyrofix Driver Updater and Slipgate.',f'''
<section class="hero"><div class="wrap"><h1>Products</h1><p class="lead">Software for weather, PC care and play. See what's free to download and what comes with Pro.</p></div></section>
<section style="padding-top:0"><div class="wrap">{CARDS.replace('<div class="grid">','<div class="grid" style="margin-top:0">')}
  <div class="tablewrap"><table>
    <thead><tr><th>Product</th><th>Platform</th><th>Status</th><th>Free version</th><th>Paid version</th></tr></thead>
    <tbody>
      <tr><td><a href="/products/windrova/"><b>Windrova</b></a></td><td>Web · Android soon</td><td><span class="badge live">Live</span></td><td class="y">✓ Free</td><td>Premium, coming soon</td></tr>
      <tr><td><a href="/products/kyrofix/"><b>Kyrofix Driver Updater</b></a></td><td>Windows 10 / 11</td><td><span class="badge free">Available</span></td><td class="y">✓ Free</td><td>Pro, coming soon</td></tr>
      <tr><td><a href="/products/kyrofix-cleaner/"><b>Kyrofix Cleaner</b></a></td><td>Windows 10 / 11</td><td><span class="badge free">Available</span></td><td class="y">✓ Free</td><td>Pro, coming soon</td></tr>
      <tr><td><a href="/products/slipgate/"><b>Slipgate</b></a></td><td>Browser</td><td><span class="badge live">Live</span></td><td class="y">✓ Free</td><td class="n">—</td></tr>
    </tbody></table></div>
</div></section>''')

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
    <div class="plan hl"><span class="badge soon">Pro</span><h3 style="margin-top:12px">Kyrofix Pro</h3><div class="price">€19.99<small style="font-size:16px;color:var(--mut)"> / year</small></div><div class="note">Up to 3 PCs · or €39.99 lifetime</div><ul><li>Everything in Free</li><li>Automatic updates and weekly checks</li><li>Game Boost</li><li>Missing DLL fixer</li><li>Driver backup &amp; restore</li><li>Unlimited AI</li><li>Priority support</li></ul><span class="btn p off">Coming soon</span></div>
  </div>
  <p class="updated">Pro is not on sale yet. Prices include VAT and may change at launch.</p>
</div></section>
<section><div class="wrap"><h2>System requirements</h2>
  <div class="grid">
    <div class="card"><h3>System</h3><p>Windows 10 or 11, 64-bit. Administrator rights to install drivers.</p></div>
    <div class="card"><h3>Memory</h3><p>4 GB RAM. 8 GB recommended for the AI assistant.</p></div>
    <div class="card"><h3>Internet</h3><p>Needed to download drivers. Everything else works offline.</p></div>
  </div>
  <p class="updated">Installer SHA-256: <code style="word-break:break-all">2aebcef80682d8c584741ce505daa14cb5472bceaa1bc087ed7d3a06e9338f04</code>. Windows may show a SmartScreen warning for new apps: click "More info" then "Run anyway".</p>
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
  <div class="meta" style="margin-top:22px"><span>Version 1.0.0</span><span>Windows 10 / 11, 64-bit</span><span>No ads, no bundled extras</span></div>
  <div class="shot" style="margin-top:34px"><img src="/img/kyrofix-cleaner/results.jpg" alt="Kyrofix Cleaner scan results" width="1440" height="960"></div>
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
  </div></div></section>
<section class="alt" id="plans"><div class="wrap"><h2>Free vs Pro</h2><p class="lead">The free version is a full cleaner. Pro adds automation and deep tools.</p>
  <div class="plans">
    <div class="plan"><span class="badge free">Free</span><h3 style="margin-top:12px">Cleaner Free</h3><div class="price">€0</div><div class="note">Free forever, no time limit</div><ul><li>Junk &amp; temp file cleaning</li><li>Windows Update leftovers</li><li>Browser cache (logins kept)</li><li>Startup manager</li><li>Big file finder</li><li class="x">Automatic cleaning</li><li class="x">Privacy cleaning</li></ul><a class="btn g" href="/downloads/Kyrofix-Cleaner-Setup.exe" download>Download free</a></div>
    <div class="plan hl"><span class="badge soon">Pro</span><h3 style="margin-top:12px">Cleaner Pro</h3><div class="price">Soon</div><div class="note">Price announced at launch</div><ul><li>Everything in Free</li><li>Automatic weekly cleaning</li><li>Privacy cleaning (history, cookies)</li><li>Uninstaller with leftover removal</li><li>Duplicate file finder</li><li>Priority support</li></ul><span class="btn p off">Coming soon</span></div>
  </div>
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
      <tr><td><b>Kyrofix Driver Updater</b><br><small style="color:var(--mut)">Windows</small></td><td class="y">€0</td><td>Pro: €19.99/year or €39.99 lifetime (soon)</td><td><span class="badge free">Free available</span></td></tr>
      <tr><td><b>Kyrofix Cleaner</b><br><small style="color:var(--mut)">Windows</small></td><td class="y">€0</td><td>Pro: price at launch</td><td><span class="badge free">Free available</span></td></tr>
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
  <p>Our first product, <a href="/products/windrova/">Windrova</a>, brings professional weather models to everyone, free. Then came <a href="/products/kyrofix/">Kyrofix</a>, PC care software that explains what it does. We also make games, like <a href="/products/slipgate/">Slipgate</a>.</p>
  <p>Want to follow along? Watch us build on <a href="{YT}" target="_blank" rel="noopener">YouTube</a>.</p>
</div></section>''')

# ---------- legal ----------
UPD='<p class="updated">Last updated: 19 November 2026</p>'
def legal(slug,title,desc,content):
    page(f'legal/{slug}/index.html',f'{title} — Halewood Systems',desc,f'<section class="hero" style="padding-bottom:30px"><div class="wrap doc"><p class="crumb">Legal</p><h1 style="font-size:clamp(34px,5vw,52px)">{title}</h1>{UPD}</div></section><section style="padding-top:0"><div class="wrap doc">{content}</div></section>')

legal('notice','Legal notice','Legal notice and provider information for Halewood Systems.',f'''
<h2>Provider</h2><p>Halewood Systems is an independent software project operated in Greece, European Union.</p>
<p>Email: <b>{MAIL}</b><br>Website: halewoodsystems.com</p>
<div class="box">Paid sales are not open yet. Before any paid product goes on sale, the full registered business details (legal name, address and VAT number) will be published on this page, as EU law requires.</div>
<h2>Responsibility for content</h2><p>We take care to keep the information on this site accurate, but it may change without notice. Links to other websites are provided for convenience; we are not responsible for their content.</p>
<h2>Weather information</h2><p>Windrova shows forecasts from public weather services. Forecasts can be wrong. Do not rely on them alone for safety decisions at sea, in the mountains or in the air; always check official warnings.</p>
<h2>Copyright</h2><p>All content on this site, including text, design and logos, belongs to Halewood Systems unless stated otherwise. Third-party data and trademarks belong to their owners.</p>''')

legal('terms','Terms of use','Terms of use for Halewood Systems websites and software.',f'''
<p>These terms apply when you use halewoodsystems.com and our products (Windrova, Kyrofix, Slipgate and others). By using them you agree to these terms. If you are a consumer, nothing here limits your rights under the law of your country of residence in the EU.</p>
<h2>1. Our products</h2><p>We offer free versions of our products, and in the future paid plans (for example Windrova Premium and Kyrofix Pro). The features of each plan are described on its product page at the time you get it.</p>
<h2>2. Licence</h2><p>We give you a personal, non-exclusive, non-transferable licence to use our software for your own purposes. You may not resell it, copy it for distribution, remove notices, or try to break its protections, except where the law allows.</p>
<h2>3. Paid plans (when available)</h2><ul><li>Prices are shown in euros and include VAT where it applies.</li><li>Payments are processed by Stripe. We never see your full card details.</li><li>Subscriptions renew automatically until you cancel. You can cancel at any time and keep access until the end of the paid period.</li><li>Your right of withdrawal is explained in <a href="/legal/refunds/">Refunds &amp; withdrawal</a>.</li></ul>
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
<h3>Payments and donations</h3><p>Payments and donations are handled by Stripe. Stripe processes your payment details under its own <a href="https://stripe.com/privacy" target="_blank" rel="noopener">privacy policy</a>. We receive only what we need for our records, such as the amount and date.</p>
<h2>Legal bases</h2><ul><li>Providing a service you asked for (Art. 6(1)(b) GDPR)</li><li>Our legitimate interest in running secure, working websites (Art. 6(1)(f))</li><li>Legal obligations, such as keeping invoices (Art. 6(1)(c))</li></ul>
<h2>Transfers outside the EU</h2><p>Some providers (for example GitHub, Cloudflare and Stripe) may process data outside the EU. They use safeguards approved by the European Commission, such as Standard Contractual Clauses or the EU–US Data Privacy Framework.</p>
<h2>How long we keep data</h2><p>Only as long as needed for the purpose, or as long as the law requires (for example, tax records).</p>
<h2>Your rights</h2><p>You can ask to access, correct or delete your data, to restrict or object to processing, and to receive your data in a portable format. Email {MAIL}. You can also complain to a data protection authority; in Greece this is the Hellenic Data Protection Authority (<a href="https://www.dpa.gr" target="_blank" rel="noopener">dpa.gr</a>).</p>
<h2>Children</h2><p>Our services are not aimed at children under 16, and we do not knowingly collect their data.</p>''')

legal('refunds','Refunds & withdrawal','Your 14-day right of withdrawal and refunds for Halewood Systems products, under EU law.',f'''
<p>All our products currently have free versions. This page explains your rights when paid plans become available.</p>
<h2>14-day right of withdrawal</h2><p>If you are a consumer in the EU, you can withdraw from a purchase within 14 days without giving a reason (Directive 2011/83/EU). The 14 days start on the day you buy.</p>
<h2>Digital content you start using right away</h2><p>For software and digital content delivered immediately, the law allows the right of withdrawal to end once delivery starts, but only if you agreed to this at checkout and confirmed you understand you lose the right. We will always ask you clearly before that happens.</p>
<h2>Subscriptions</h2><p>You can cancel a subscription at any time. It stops at the end of the current paid period. If you withdraw within 14 days of your first payment, before you start using paid features, we refund you in full.</p>
<h2>If something doesn't work</h2><p>If a product does not work as described, you are entitled to have it fixed, or to a price reduction or refund, under EU law on digital content (Directive (EU) 2019/770). This applies regardless of the 14-day period.</p>
<h2>How to ask</h2><p>Email <b>{MAIL}</b> with the email address you used and the date of purchase. You can also use this sentence: "I hereby give notice that I withdraw from my contract for the following product: …". We refund within 14 days, to the same payment method, at no cost to you.</p>
<h2>Donations</h2><p>Donations are voluntary gifts and are not purchases. If you donated by mistake, contact us within 14 days and we will refund it.</p>''')

legal('cookies','Cookies','Cookie information for Halewood Systems websites.',f'''
<h2>Short version</h2><p>We do not use advertising or tracking cookies, so we don't show a cookie banner.</p>
<h2>What we store</h2><ul><li><b>halewoodsystems.com:</b> no cookies.</li><li><b>Windrova:</b> your settings (language, units, favourite places, last map view) are saved in your browser's local storage so the map remembers them. They never leave your device and you can clear them in your browser settings.</li></ul>
<h2>Third parties</h2><p>When you pay or donate, Stripe may set cookies needed for secure payment and fraud prevention, on its own pages. See Stripe's policy.</p>
<h2>Changes</h2><p>If we ever add cookies that need your consent, we will ask you first.</p>''')

# 404
page('404.html','Page not found — Halewood Systems','Page not found.','<section class="hero center"><div class="wrap"><h1>Page not found</h1><p class="lead">The page you were looking for doesn\'t exist.</p><div class="cta"><a class="btn p" href="/">Go home</a><a class="btn g" href="/products/">See products</a></div></div></section>')
print('ok')
