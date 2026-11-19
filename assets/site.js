{
  const here = location.pathname.replace(/index\.html$/, '');
  const links = [['/products/', 'Products'], ['/pricing/', 'Pricing'], ['/support/', 'Support'], ['/about/', 'About']];
  const nav = document.getElementById('nav');
  if (nav) {
    nav.className = 'nav';
    nav.innerHTML = `<div class="wrap">
      <a class="brand" href="/" aria-label="Halewood Systems home"><img src="/img/logo-mark-96.png" alt="" width="52" height="32" style="width:auto;height:32px"><span><b>HALEWOOD</b><small>SYSTEMS</small></span></a>
      <ul class="menu" id="menu">${links.map(([h, t]) => `<li><a href="${h}"${here.startsWith(h) ? ' class="on" aria-current="page"' : ''}>${t}</a></li>`).join('')}</ul>
      <a class="btn p s navcta" href="https://windrova.com" target="_blank" rel="noopener">Try Windrova</a>
      <button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="menu">☰</button>
    </div>`;
    const b = nav.querySelector('.burger'), m = nav.querySelector('.menu');
    b.addEventListener('click', () => { const o = m.classList.toggle('open'); b.setAttribute('aria-expanded', o); b.textContent = o ? '✕' : '☰'; });
  }
  const foot = document.getElementById('foot');
  if (foot) {
    foot.className = 'foot';
    foot.innerHTML = `<div class="wrap">
      <div class="cols">
        <div><a class="brand" href="/"><img src="/img/logo-mark-96.png" alt="" width="45" height="28" style="width:auto;height:28px"><span><b style="font-size:16px">HALEWOOD</b><small>SYSTEMS</small></span></a>
          <p style="margin-top:14px;max-width:260px">Fast, simple software. Free to start, no clutter.</p></div>
        <div><h4>Products</h4><ul><li><a href="/products/windrova/">Windrova</a></li><li><a href="/products/kyrofix/">Kyrofix Driver Updater</a></li><li><a href="/products/slipgate/">Slipgate</a></li><li><a href="/pricing/">Pricing</a></li></ul></div>
        <div><h4>Company</h4><ul><li><a href="/about/">About</a></li><li><a href="/support/">Support &amp; contact</a></li><li><a href="https://www.youtube.com/@HalewoodSystems" target="_blank" rel="noopener">YouTube</a></li><li><a href="https://halewood-systems.itch.io" target="_blank" rel="noopener">itch.io</a></li></ul></div>
        <div><h4>Legal</h4><ul><li><a href="/legal/terms/">Terms of use</a></li><li><a href="/legal/privacy/">Privacy policy</a></li><li><a href="/legal/refunds/">Refunds &amp; withdrawal</a></li><li><a href="/legal/cookies/">Cookies</a></li><li><a href="/legal/notice/">Legal notice</a></li></ul></div>
      </div>
      <div class="base"><span>© ${new Date().getFullYear()} Halewood Systems. All rights reserved.</span><span>Made in the EU 🇪🇺</span></div>
    </div>`;
  }
}
