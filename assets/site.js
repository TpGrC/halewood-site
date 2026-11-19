{
  const LANGS = {en:'English',el:'Ελληνικά',de:'Deutsch',es:'Español',fr:'Français',it:'Italiano',pl:'Polski',pt:'Português',ru:'Русский'};
  const m0 = location.pathname.match(/^\/(el|de|es|fr|it|pl|pt|ru)(\/|$)/);
  const L = m0 ? m0[1] : 'en', P = L === 'en' ? '' : '/' + L;
  const bare = m0 ? location.pathname.slice(3) || '/' : location.pathname;
  try { // first visit: open the site in the visitor's language
    const saved = localStorage.getItem('hw-lang'), nav0 = (navigator.language || 'en').slice(0, 2);
    if (!saved && L === 'en' && LANGS[nav0] && nav0 !== 'en') { localStorage.setItem('hw-lang', nav0); location.replace('/' + nav0 + bare + location.search + location.hash); }
    else if (!saved) localStorage.setItem('hw-lang', L);
  } catch (e) {}
  const W = {
    en:['Products','Pricing','Support','About','Try Windrova','Open menu','Fast, simple software. Free to start, no clutter.','Company','Support &amp; contact','Legal','Terms of use','Privacy policy','Refunds &amp; withdrawal','Cookies','Legal notice','All rights reserved.','Made in the EU','Language'],
    el:['Προϊόντα','Τιμές','Υποστήριξη','Σχετικά','Δοκίμασε το Windrova','Άνοιγμα μενού','Γρήγορο, απλό λογισμικό. Δωρεάν για αρχή, χωρίς περιττά.','Εταιρεία','Υποστήριξη &amp; επικοινωνία','Νομικά','Όροι χρήσης','Πολιτική απορρήτου','Επιστροφές &amp; υπαναχώρηση','Cookies','Νομική σημείωση','Με επιφύλαξη παντός δικαιώματος.','Φτιαγμένο στην ΕΕ','Γλώσσα'],
    de:['Produkte','Preise','Support','Über uns','Windrova testen','Menü öffnen','Schnelle, einfache Software. Kostenlos starten, ohne Ballast.','Unternehmen','Support &amp; Kontakt','Rechtliches','Nutzungsbedingungen','Datenschutz','Erstattung &amp; Widerruf','Cookies','Impressum','Alle Rechte vorbehalten.','Made in the EU','Sprache'],
    es:['Productos','Precios','Soporte','Nosotros','Prueba Windrova','Abrir menú','Software rápido y sencillo. Gratis para empezar, sin relleno.','Empresa','Soporte y contacto','Legal','Condiciones de uso','Política de privacidad','Reembolsos y desistimiento','Cookies','Aviso legal','Todos los derechos reservados.','Hecho en la UE','Idioma'],
    fr:['Produits','Tarifs','Support','À propos','Essayer Windrova','Ouvrir le menu','Des logiciels rapides et simples. Gratuits pour commencer, sans superflu.','Entreprise','Support &amp; contact','Mentions','Conditions d’utilisation','Politique de confidentialité','Remboursements &amp; rétractation','Cookies','Mentions légales','Tous droits réservés.','Fabriqué dans l’UE','Langue'],
    it:['Prodotti','Prezzi','Supporto','Chi siamo','Prova Windrova','Apri il menu','Software veloce e semplice. Gratis per iniziare, senza fronzoli.','Azienda','Supporto e contatti','Note legali','Termini d’uso','Informativa privacy','Rimborsi e recesso','Cookie','Note legali','Tutti i diritti riservati.','Fatto nell’UE','Lingua'],
    pl:['Produkty','Cennik','Pomoc','O nas','Wypróbuj Windrova','Otwórz menu','Szybkie, proste oprogramowanie. Za darmo na start, bez zbędnych dodatków.','Firma','Pomoc i kontakt','Informacje prawne','Warunki korzystania','Polityka prywatności','Zwroty i odstąpienie','Cookies','Nota prawna','Wszelkie prawa zastrzeżone.','Stworzone w UE','Język'],
    pt:['Produtos','Preços','Suporte','Sobre','Experimente o Windrova','Abrir menu','Software rápido e simples. Grátis para começar, sem excessos.','Empresa','Suporte e contacto','Legal','Termos de utilização','Política de privacidade','Reembolsos e livre resolução','Cookies','Aviso legal','Todos os direitos reservados.','Feito na UE','Idioma'],
    ru:['Продукты','Цены','Поддержка','О нас','Попробовать Windrova','Открыть меню','Быстрые и простые программы. Бесплатно для начала, ничего лишнего.','Компания','Поддержка и контакты','Правовая информация','Условия использования','Политика конфиденциальности','Возврат и отказ','Cookies','Правовая информация','Все права защищены.','Сделано в ЕС','Язык'],
    tr:['Ürünler','Fiyatlar','Destek','Hakkımızda','Windrova’yı dene','Menüyü aç','Hızlı, basit yazılım. Başlamak ücretsiz, gereksiz hiçbir şey yok.','Şirket','Destek ve iletişim','Yasal','Kullanım koşulları','Gizlilik politikası','İade ve cayma','Çerezler','Yasal bildirim','Tüm hakları saklıdır.','AB’de yapıldı','Dil']
  }[L];
  const pick = `<select class="langpick" aria-label="${W[17]}">${Object.entries(LANGS).map(([c, n]) => `<option value="${c}"${c === L ? ' selected' : ''}>${n}</option>`).join('')}</select>`;
  const here = bare.replace(/index\.html$/, '');
  const links = [['/products/', W[0]], ['/pricing/', W[1]], ['/support/', W[2]], ['/about/', W[3]]];
  const nav = document.getElementById('nav');
  if (nav) {
    nav.className = 'nav';
    nav.innerHTML = `<div class="wrap">
      <a class="brand" href="${P}/" aria-label="Halewood Systems home"><img src="/img/logo-mark-96.png" alt="" width="52" height="32" style="width:auto;height:32px"><span><b>HALEWOOD</b><small>SYSTEMS</small></span></a>
      <ul class="menu" id="menu">${links.map(([h, t]) => `<li><a href="${P}${h}"${here.startsWith(h) ? ' class="on" aria-current="page"' : ''}>${t}</a></li>`).join('')}</ul>
      <a class="btn p s navcta" href="https://windrova.com" target="_blank" rel="noopener">${W[4]}</a>${pick}
      <button class="burger" aria-label="${W[5]}" aria-expanded="false" aria-controls="menu">☰</button>
    </div>`;
    nav.querySelector('.langpick').addEventListener('change', e => { const c = e.target.value; try { localStorage.setItem('hw-lang', c); } catch (x) {} location.href = (c === 'en' ? '' : '/' + c) + bare; });
    const b = nav.querySelector('.burger'), m = nav.querySelector('.menu');
    b.addEventListener('click', () => { const o = m.classList.toggle('open'); b.setAttribute('aria-expanded', o); b.textContent = o ? '✕' : '☰'; });
  }
  const foot = document.getElementById('foot');
  if (foot) {
    foot.className = 'foot';
    foot.innerHTML = `<div class="wrap">
      <div class="cols">
        <div><a class="brand" href="${P}/"><img src="/img/logo-mark-96.png" alt="" width="45" height="28" style="width:auto;height:28px"><span><b style="font-size:16px">HALEWOOD</b><small>SYSTEMS</small></span></a>
          <p style="margin-top:14px;max-width:260px">${W[6]}</p></div>
        <div><h4>${W[0]}</h4><ul><li><a href="${P}/products/windrova/">Windrova</a></li><li><a href="${P}/products/kyrofix/">Kyrofix Driver Updater</a></li><li><a href="${P}/products/kyrofix-cleaner/">Kyrofix Cleaner</a></li><li><a href="${P}/products/slipgate/">Slipgate</a></li><li><a href="${P}/pricing/">${W[1]}</a></li></ul></div>
        <div><h4>${W[7]}</h4><ul><li><a href="${P}/about/">${W[3]}</a></li><li><a href="${P}/support/">${W[8]}</a></li><li><a href="https://www.youtube.com/@HalewoodSystems" target="_blank" rel="noopener">YouTube</a></li><li><a href="https://halewood-systems.itch.io" target="_blank" rel="noopener">itch.io</a></li></ul></div>
        <div><h4>${W[9]}</h4><ul><li><a href="${P}/legal/terms/">${W[10]}</a></li><li><a href="${P}/legal/privacy/">${W[11]}</a></li><li><a href="${P}/legal/refunds/">${W[12]}</a></li><li><a href="${P}/legal/cookies/">${W[13]}</a></li><li><a href="${P}/legal/notice/">${W[14]}</a></li></ul></div>
      </div>
      <div class="base"><span>© ${new Date().getFullYear()} Halewood Systems. ${W[15]}</span><span>${W[16]} 🇪🇺</span></div>
    </div>`;
  }
}
