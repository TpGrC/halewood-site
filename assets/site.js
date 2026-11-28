{
  const LANGS = {en:'English',el:'Ελληνικά',de:'Deutsch',es:'Español',fr:'Français',it:'Italiano',pl:'Polski',pt:'Português',ru:'Русский'};
  const m0 = location.pathname.match(/^\/(el|de|es|fr|it|pl|pt|ru)(\/|$)/);
  const L = m0 ? m0[1] : 'en', P = L === 'en' ? '' : '/' + L;
  const bare = m0 ? location.pathname.slice(3) || '/' : location.pathname;
  const SVC = /^\/(services|ypiresies)\/?$/, to = c => SVC.test(bare) ? (c === 'el' ? '/el/ypiresies/' : '/services/') : (c === 'en' ? '' : '/' + c) + bare;
  try { // first visit: open the site in the visitor's language
    const saved = localStorage.getItem('hw-lang'), nav0 = (navigator.language || 'en').slice(0, 2);
    if (!saved && L === 'en' && LANGS[nav0] && nav0 !== 'en') { localStorage.setItem('hw-lang', nav0); location.replace(to(nav0) + location.search + location.hash); }
    else if (!saved) localStorage.setItem('hw-lang', L);
  } catch (e) {}
  const W = {
    en:['Products','Pricing','Support','About','Try Windrova','Open menu','Fast, simple software. Free to start, no clutter.','Company','Support &amp; contact','Legal','Terms of use','Privacy policy','Refunds &amp; withdrawal','Cookies','Legal notice','All rights reserved.','Made in the EU','Language','PC Software','Games'],
    el:['Προϊόντα','Τιμές','Υποστήριξη','Σχετικά','Δοκίμασε το Windrova','Άνοιγμα μενού','Γρήγορο, απλό λογισμικό. Δωρεάν για αρχή, χωρίς περιττά.','Εταιρεία','Υποστήριξη &amp; επικοινωνία','Νομικά','Όροι χρήσης','Πολιτική απορρήτου','Επιστροφές &amp; υπαναχώρηση','Cookies','Νομική σημείωση','Με επιφύλαξη παντός δικαιώματος.','Φτιαγμένο στην ΕΕ','Γλώσσα','Λογισμικό','Παιχνίδια'],
    de:['Produkte','Preise','Support','Über uns','Windrova testen','Menü öffnen','Schnelle, einfache Software. Kostenlos starten, ohne Ballast.','Unternehmen','Support &amp; Kontakt','Rechtliches','Nutzungsbedingungen','Datenschutz','Erstattung &amp; Widerruf','Cookies','Impressum','Alle Rechte vorbehalten.','Made in the EU','Sprache','PC-Software','Spiele'],
    es:['Productos','Precios','Soporte','Nosotros','Prueba Windrova','Abrir menú','Software rápido y sencillo. Gratis para empezar, sin relleno.','Empresa','Soporte y contacto','Legal','Condiciones de uso','Política de privacidad','Reembolsos y desistimiento','Cookies','Aviso legal','Todos los derechos reservados.','Hecho en la UE','Idioma','Software','Juegos'],
    fr:['Produits','Tarifs','Support','À propos','Essayer Windrova','Ouvrir le menu','Des logiciels rapides et simples. Gratuits pour commencer, sans superflu.','Entreprise','Support &amp; contact','Mentions','Conditions d’utilisation','Politique de confidentialité','Remboursements &amp; rétractation','Cookies','Mentions légales','Tous droits réservés.','Fabriqué dans l’UE','Langue','Logiciels','Jeux'],
    it:['Prodotti','Prezzi','Supporto','Chi siamo','Prova Windrova','Apri il menu','Software veloce e semplice. Gratis per iniziare, senza fronzoli.','Azienda','Supporto e contatti','Note legali','Termini d’uso','Informativa privacy','Rimborsi e recesso','Cookie','Note legali','Tutti i diritti riservati.','Fatto nell’UE','Lingua','Software','Giochi'],
    pl:['Produkty','Cennik','Pomoc','O nas','Wypróbuj Windrova','Otwórz menu','Szybkie, proste oprogramowanie. Za darmo na start, bez zbędnych dodatków.','Firma','Pomoc i kontakt','Informacje prawne','Warunki korzystania','Polityka prywatności','Zwroty i odstąpienie','Cookies','Nota prawna','Wszelkie prawa zastrzeżone.','Stworzone w UE','Język','Oprogramowanie','Gry'],
    pt:['Produtos','Preços','Suporte','Sobre','Experimente o Windrova','Abrir menu','Software rápido e simples. Grátis para começar, sem excessos.','Empresa','Suporte e contacto','Legal','Termos de utilização','Política de privacidade','Reembolsos e livre resolução','Cookies','Aviso legal','Todos os direitos reservados.','Feito na UE','Idioma','Software','Jogos'],
    ru:['Продукты','Цены','Поддержка','О нас','Попробовать Windrova','Открыть меню','Быстрые и простые программы. Бесплатно для начала, ничего лишнего.','Компания','Поддержка и контакты','Правовая информация','Условия использования','Политика конфиденциальности','Возврат и отказ','Cookies','Правовая информация','Все права защищены.','Сделано в ЕС','Язык','Программы','Игры'],
    tr:['Ürünler','Fiyatlar','Destek','Hakkımızda','Windrova’yı dene','Menüyü aç','Hızlı, basit yazılım. Başlamak ücretsiz, gereksiz hiçbir şey yok.','Şirket','Destek ve iletişim','Yasal','Kullanım koşulları','Gizlilik politikası','İade ve cayma','Çerezler','Yasal bildirim','Tüm hakları saklıdır.','AB’de yapıldı','Dil','Yazılım','Oyunlar']
  }[L];
  const W2 = {en:['News','Help','Downloads'],el:['Νέα','Βοήθεια','Λήψεις'],de:['News','Hilfe','Downloads'],es:['Noticias','Ayuda','Descargas'],fr:['Actualités','Aide','Téléchargements'],it:['Novità','Aiuto','Download'],pl:['Aktualności','Pomoc','Pobieranie'],pt:['Notícias','Ajuda','Transferências'],ru:['Новости','Помощь','Загрузки'],tr:['Haberler','Yardım','İndirmeler']}[L];
  const pick = `<select class="langpick" aria-label="${W[17]}">${Object.entries(LANGS).map(([c, n]) => `<option value="${c}"${c === L ? ' selected' : ''}>${n}</option>`).join('')}</select>`;
  const here0 = bare.replace(/index\.html$/, ''), here = /^\/products\/kyrofix|^\/activate/.test(here0) ? '/software/' : /^\/products\/(starfuse|potion-sort|triple-bloom|skystack|slipgate)/.test(here0) ? '/games/' : here0;
  const KF = [['/products/kyrofix/', 'Driver Updater'], ['/products/kyrofix-cleaner/', 'Cleaner'], ['/products/kyrofix-space/', 'Space'], ['/products/kyrofix-photo-cleaner/', 'Photo Cleaner'], ['/products/kyrofix-backup/', 'Backup'], ['/products/kyrofix-shredder/', 'Shredder']];
  const GM = [['/products/starfuse/', 'Starfuse'], ['/products/potion-sort/', 'Potion Sort'], ['/products/triple-bloom/', 'Triple Bloom'], ['/products/skystack/', 'Skystack'], ['/products/slipgate/', 'Slipgate']];
  const links = [['/products/windrova/', 'Windrova'], ['/games/', W[W.length-1], GM], ['/software/', 'Kyrofix', KF], ...(L === 'el' ? [['/ypiresies/', 'Υπηρεσίες']] : L === 'en' ? [['/services/', 'Services']] : []), ['/support/', W[2]]];
  const nav = document.getElementById('nav');
  if (nav) {
    nav.className = 'nav';
    nav.innerHTML = `<div class="wrap">
      <a class="brand" href="${P}/" aria-label="Halewood Systems home"><img src="/img/logo-mark-96.png" alt="" width="52" height="32" style="width:auto;height:32px"><span><b>HALEWOOD</b><small>SYSTEMS</small></span></a>
      <ul class="menu" id="menu">${links.map(([h, t, sub]) => `<li${sub ? ' class="dd"' : ''}><a href="${h.startsWith('/e-rechnung') ? '' : P}${h}"${here.startsWith(h) ? ' class="on" aria-current="page"' : ''}>${t}${sub ? ' <i aria-hidden="true">▾</i>' : ''}</a>${sub ? `<ul class="sub">${sub.map(([sh, st]) => `<li><a href="${P}${sh}"${here0 === sh ? ' class="on"' : ''}>${h === '/software/' ? '<small>Kyrofix</small> ' : ''}${st}</a></li>`).join('')}</ul>` : ''}</li>`).join('')}</ul>
      ${pick}
      <button class="burger" aria-label="${W[5]}" aria-expanded="false" aria-controls="menu">☰</button>
    </div>`;
    nav.querySelector('.langpick').addEventListener('change', e => { const c = e.target.value; try { localStorage.setItem('hw-lang', c); } catch (x) {} location.href = to(c); });
    const b = nav.querySelector('.burger'), m = nav.querySelector('.menu');
    b.addEventListener('click', () => { const o = m.classList.toggle('open'); b.setAttribute('aria-expanded', o); b.textContent = o ? '✕' : '☰'; });
  }
  const foot = document.getElementById('foot');
  if (foot) {
    foot.className = 'foot';
    foot.innerHTML = `<div class="wrap">
      <div class="cols">
        <div><a class="brand" href="${P}/"><img src="/img/logo-mark-96.png" alt="" width="45" height="28" style="width:auto;height:28px"><span><b style="font-size:16px">HALEWOOD</b><small>SYSTEMS</small></span></a>
          <p style="margin-top:14px;max-width:260px">${W[6]}</p><p style="margin-top:10px"><a href="mailto:halewoodsystems@gmail.com" style="color:#7fb0ff;font-weight:600">✉ halewoodsystems@gmail.com</a></p></div>
        <div><h4>${W[0]}</h4><ul><li><a href="${P}/products/windrova/">Windrova</a></li><li><a href="${P}/games/">${W[W.length-1]}</a></li><li><a href="${P}/software/">Kyrofix</a></li><li><a href="${P}/activate/">Kyrofix Pro key</a></li></ul></div>
        <div><h4>${W[7]}</h4><ul><li><a href="${P}/about/">${W[3]}</a></li><li><a href="${P}/news/">${W2[0]}</a></li><li><a href="${P}/help/">${W2[1]}</a></li><li><a href="${P}/support/">${W[8]}</a></li><li><a href="https://www.youtube.com/@HalewoodSystems" target="_blank" rel="noopener">YouTube</a></li><li><a href="https://halewood-systems.itch.io" target="_blank" rel="noopener">itch.io</a></li></ul></div>
        <div><h4>${W[9]}</h4><ul><li><a href="${P}/legal/terms/">${W[10]}</a></li><li><a href="${P}/legal/privacy/">${W[11]}</a></li><li><a href="${P}/legal/refunds/">${W[12]}</a></li><li><a href="${P}/legal/cookies/">${W[13]}</a></li><li><a href="${P}/legal/notice/">${W[14]}</a></li></ul></div>
      </div>
      <div class="base"><span>© ${new Date().getFullYear()} Halewood Systems. ${W[15]}</span><span>${W[16]} 🇪🇺</span></div>
    </div>`;
  }
}
