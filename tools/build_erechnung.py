# German landing pages for Halewood E-Rechnung (for Google search). Run: python3 tools/build_erechnung.py
import os, json
R = os.path.join(os.path.dirname(__file__), '..')
SITE = 'https://halewoodsystems.com'
APP = '/rechnung/'
BUY = 'https://halewoodsystems.gumroad.com/l/e-rechnung'

CSS = '''*{box-sizing:border-box}body{margin:0;font:17px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:#0f1b2d;background:#f6f8fb}
a{color:#1f5bff}header{background:#0f1b2d}header .w{display:flex;align-items:center;gap:20px;height:62px}
header a{color:#c9d4e6;text-decoration:none;font-size:15px}header a.logo{color:#fff;font-weight:700;font-size:18px;margin-right:auto}header a.logo span{color:#7fb0ff}
header a.cta{background:#1f5bff;color:#fff;padding:8px 14px;border-radius:9px;font-weight:600}
.w{max-width:960px;margin:0 auto;padding:0 22px}
.hero{background:linear-gradient(160deg,#0f1b2d,#18305e);color:#fff;padding:64px 0 56px}.hero h1{font-size:40px;line-height:1.15;margin:0 0 16px;max-width:760px}
.hero p{font-size:19px;color:#c9d4e6;max-width:700px;margin:0 0 26px}
.btn{display:inline-block;background:#1f5bff;color:#fff;text-decoration:none;font-weight:700;padding:13px 22px;border-radius:11px;margin:0 10px 10px 0}
.btn.g{background:#fff;color:#0f1b2d}.hero .note{font-size:14px;color:#93a3bd;margin-top:6px}
main{padding:46px 0 30px}h2{font-size:27px;margin:44px 0 12px}h3{font-size:19px;margin:26px 0 6px}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:18px}.card{background:#fff;border:1px solid #e2e7ef;border-radius:14px;padding:20px}
.card b{display:block;margin-bottom:4px}.price{background:#fff;border:2px solid #1f5bff;border-radius:16px;padding:26px;max-width:460px}
.price .p{font-size:36px;font-weight:800}.price ul{padding-left:20px}
table{border-collapse:collapse;width:100%;background:#fff;border-radius:12px;overflow:hidden}td,th{border-bottom:1px solid #e2e7ef;padding:11px 12px;text-align:left;vertical-align:top}th{background:#eef2f8}
.faq details{background:#fff;border:1px solid #e2e7ef;border-radius:12px;padding:14px 18px;margin-bottom:10px}.faq summary{font-weight:700;cursor:pointer}
.small{font-size:14px;color:#5b6678}footer{border-top:1px solid #e2e7ef;margin-top:50px;padding:26px 0;font-size:14px;color:#5b6678}footer a{color:#5b6678;margin-right:16px}
@media(max-width:760px){.cards{grid-template-columns:1fr}.hero h1{font-size:30px}header .hide{display:none}}'''

NAV = f'''<header><div class="w"><a class="logo" href="/e-rechnung/">Halewood <span>E-Rechnung</span></a>
<a class="hide" href="/e-rechnung/xrechnung-erstellen/">XRechnung erstellen</a><a class="hide" href="/e-rechnung/xrechnung-oeffnen/">XRechnung öffnen</a>
<a class="hide" href="/e-rechnung/e-rechnungspflicht/">E-Rechnungspflicht</a><a class="cta" href="{APP}">App öffnen</a></div></header>'''

FOOT = '''<footer><div class="w"><a href="/e-rechnung/">Halewood E-Rechnung</a><a href="/support/">Kontakt</a><a href="/legal/privacy/">Datenschutz</a><a href="/legal/terms/">AGB</a>
<p>Halewood E-Rechnung ist ein Produkt von Halewood Systems. Die Inhalte auf dieser Seite sind allgemeine Informationen und keine Steuer- oder Rechtsberatung.
Stand: November 2026.</p></div></footer>'''

def page(path, title, desc, hero, body, faq=None):
    ld = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Halewood E-Rechnung",
          "applicationCategory": "BusinessApplication", "operatingSystem": "Web",
          "offers": {"@type": "Offer", "price": "7.00", "priceCurrency": "EUR"}, "inLanguage": "de"}
    extra = ''
    if faq:
        extra = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}, ensure_ascii=False) + '</script>'
        body += '<h2>Häufige Fragen</h2><div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faq) + '</div>'
    html = f'''<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{SITE}{path}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:url" content="{SITE}{path}">
<link rel="icon" href="/favicon-48.png" type="image/png"><style>{CSS}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>{extra}</head><body>
{NAV}<section class="hero"><div class="w">{hero}</div></section><main><div class="w">{body}</div></main>{FOOT}</body></html>'''
    out = os.path.join(R, path.strip('/'), 'index.html'); os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(html)
    return path

CTA = f'<a class="btn" href="{BUY}" target="_blank" rel="noopener">1 Monat kostenlos testen</a><a class="btn g" href="{APP}">App ansehen</a>'
PAGES = []

PAGES.append(page('/e-rechnung/', 'XRechnung einfach erstellen – E-Rechnung für Selbstständige & kleine Firmen | Halewood E-Rechnung',
  'E-Rechnungen im XRechnung-Format online erstellen, empfangene XRechnung und ZUGFeRD lesbar anzeigen. Für Freiberufler und kleine Unternehmen. 1. Monat kostenlos, danach 7 € im Monat.',
  f'''<h1>XRechnung erstellen – einfach, schnell, ohne teure Buchhaltungssoftware</h1>
<p>Ab 2027/2028 müssen Unternehmen in Deutschland E-Rechnungen versenden. Eine normale PDF reicht dann nicht mehr. Mit Halewood E-Rechnung erstellen Sie gültige XRechnung-Dateien in einer Minute – direkt im Browser.</p>{CTA}
<div class="note">Erster Monat kostenlos · danach 7 € pro Monat oder 70 € pro Jahr · jederzeit kündbar</div>''',
  f'''<h2>Was Halewood E-Rechnung kann</h2><div class="cards">
<div class="card"><b>XRechnung erstellen</b>Rechnung ausfüllen, XML herunterladen, per E-Mail senden. Format XRechnung 3.0 nach EN 16931.</div>
<div class="card"><b>E-Rechnungen lesen</b>Empfangene XRechnung- und ZUGFeRD-Dateien als normale Rechnung anzeigen und drucken – kostenlos.</div>
<div class="card"><b>Kunden &amp; Rechnungen</b>Kunden speichern, Rechnungsnummern automatisch, PDF zum Ausdrucken, Datensicherung.</div>
<div class="card"><b>19 %, 7 % oder § 19 UStG</b>Umsatzsteuer wird automatisch berechnet. Auch für Kleinunternehmer ohne Umsatzsteuer.</div>
<div class="card"><b>Geprüft</b>Unsere Testrechnungen bestehen die offiziellen Prüfregeln (EN 16931 und XRechnung-Regeln der KoSIT).</div>
<div class="card"><b>Ihre Daten bleiben bei Ihnen</b>Die Rechnungsdaten werden in Ihrem Browser gespeichert, nicht auf unseren Servern.</div></div>
<h2>So funktioniert es</h2><ol><li>Einmal Ihre Firmendaten und Bankverbindung eintragen.</li><li>Kunde und Positionen eingeben – Summen und Umsatzsteuer rechnet die App.</li>
<li>„XRechnung herunterladen“ klicken und die XML-Datei an Ihren Kunden senden.</li></ol>
<h2>Preis</h2><div class="price"><div class="p">7 € <small style="font-size:16px;font-weight:400">/ Monat</small></div><p>oder 70 € pro Jahr (2 Monate gespart)</p>
<ul><li>Erster Monat kostenlos</li><li>Unbegrenzt viele Rechnungen</li><li>Jederzeit kündbar</li><li>E-Rechnungen ansehen ist immer kostenlos</li></ul>
<a class="btn" href="{BUY}" target="_blank" rel="noopener">1 Monat kostenlos testen</a></div>
<p class="small">Zahlung und Rechnung über Gumroad (inkl. Umsatzsteuer). Nach der Anmeldung erhalten Sie einen Lizenzschlüssel per E-Mail.</p>''',
  [('Ist eine PDF-Rechnung noch erlaubt?', 'Im B2B-Bereich gilt eine PDF ab 2027 bzw. 2028 nicht mehr als E-Rechnung. Eine E-Rechnung muss strukturiert und maschinenlesbar sein, z. B. im Format XRechnung oder ZUGFeRD.'),
   ('Ab wann muss ich E-Rechnungen versenden?', 'Unternehmen mit mehr als 800.000 € Vorjahresumsatz ab 1. Januar 2027, alle anderen ab 1. Januar 2028. Empfangen können müssen alle Unternehmen bereits seit 1. Januar 2025.'),
   ('Brauche ich als Kleinunternehmer eine E-Rechnung?', 'Kleinunternehmer nach § 19 UStG müssen E-Rechnungen empfangen können, sind aber vom Versand ausgenommen. Sie dürfen trotzdem freiwillig E-Rechnungen schicken – Halewood E-Rechnung unterstützt das.'),
   ('Wie verschicke ich die XRechnung?', 'Am einfachsten per E-Mail als XML-Anhang. Eine bestimmte Plattform ist im B2B-Bereich nicht vorgeschrieben.'),
   ('Kann ich jederzeit kündigen?', 'Ja. Das Abo läuft monatlich oder jährlich und ist jederzeit kündbar. Im ersten Monat zahlen Sie nichts.')]))

PAGES.append(page('/e-rechnung/xrechnung-erstellen/', 'XRechnung erstellen: Anleitung in 3 Schritten (2026) | Halewood E-Rechnung',
  'So erstellen Sie eine XRechnung ohne teure Software: Pflichtangaben, Leitweg-ID, Käuferreferenz und Versand per E-Mail. Mit Online-Tool, 1. Monat kostenlos.',
  f'''<h1>XRechnung erstellen: So geht es in 3 Schritten</h1><p>Eine XRechnung ist eine Rechnung als XML-Datei nach dem deutschen Standard. Hier erfahren Sie, welche Angaben nötig sind und wie Sie sie ohne Buchhaltungssoftware erstellen.</p>{CTA}''',
  '''<h2>Was ist eine XRechnung?</h2><p>Die XRechnung ist das deutsche Format für elektronische Rechnungen nach der europäischen Norm EN 16931. Die Rechnung besteht aus einer XML-Datei, die das Buchhaltungsprogramm Ihres Kunden automatisch lesen kann. Ein Mensch sieht darin zunächst nur Code – deshalb gibt es Programme, die sie als normale Rechnung anzeigen.</p>
<h2>Diese Angaben brauchen Sie</h2><table><tr><th>Angabe</th><th>Hinweis</th></tr>
<tr><td>Ihr Firmenname und Ihre Anschrift</td><td>wie auf jeder Rechnung</td></tr>
<tr><td>USt-IdNr. oder Steuernummer</td><td>mindestens eine davon</td></tr>
<tr><td>Ansprechpartner, Telefon, E-Mail</td><td>in der XRechnung Pflicht</td></tr>
<tr><td>Bankverbindung (IBAN)</td><td>für die Überweisung</td></tr>
<tr><td>Name, Anschrift und E-Mail des Kunden</td><td>die E-Mail dient als elektronische Adresse</td></tr>
<tr><td>Käuferreferenz bzw. Leitweg-ID</td><td>bei Behörden die Leitweg-ID, sonst z. B. Kunden- oder Bestellnummer</td></tr>
<tr><td>Rechnungsnummer, Datum, Leistungsdatum</td><td>fortlaufende Nummer</td></tr>
<tr><td>Positionen, Menge, Preis, Umsatzsteuersatz</td><td>19 %, 7 % oder Kleinunternehmer nach § 19 UStG</td></tr></table>
<h2>In 3 Schritten zur XRechnung</h2><h3>1. Firmendaten einmal eintragen</h3><p>Öffnen Sie <a href="/rechnung/">Halewood E-Rechnung</a> und tragen Sie unter „Mein Unternehmen“ Ihre Daten ein. Sie werden gespeichert.</p>
<h3>2. Rechnung ausfüllen</h3><p>Kunde, Käuferreferenz und Positionen eingeben. Netto, Umsatzsteuer und Gesamtbetrag werden automatisch berechnet.</p>
<h3>3. XML herunterladen und senden</h3><p>Mit „XRechnung herunterladen“ erhalten Sie die fertige Datei. Senden Sie sie per E-Mail – gern zusammen mit einer PDF zum Ansehen.</p>''',
  [('Was ist der Unterschied zwischen XRechnung und ZUGFeRD?', 'Die XRechnung ist eine reine XML-Datei. ZUGFeRD ist eine PDF, in der die XML-Daten eingebettet sind. Beide Formate erfüllen die E-Rechnungspflicht, wenn sie der Norm EN 16931 entsprechen.'),
   ('Brauche ich eine Leitweg-ID?', 'Nur bei Rechnungen an öffentliche Auftraggeber. Bei Firmenkunden tragen Sie stattdessen eine Käuferreferenz ein, zum Beispiel Kunden- oder Bestellnummer.'),
   ('Kann ich eine XRechnung kostenlos erstellen?', 'Sie können Halewood E-Rechnung einen Monat lang kostenlos nutzen. Danach kostet das Abo 7 € im Monat.')]))

PAGES.append(page('/e-rechnung/xrechnung-oeffnen/', 'XRechnung öffnen und lesen – kostenlos online anzeigen | Halewood E-Rechnung',
  'XRechnung oder ZUGFeRD-XML bekommen und können sie nicht lesen? Datei kostenlos im Browser öffnen, als Rechnung anzeigen und drucken. Ohne Upload.',
  f'''<h1>XRechnung öffnen: kostenlos lesen und drucken</h1><p>Sie haben eine E-Rechnung als XML-Datei bekommen und sehen nur Code? Öffnen Sie sie hier als normale Rechnung – kostenlos, ohne Anmeldung, die Datei wird nicht hochgeladen.</p>
<a class="btn" href="{APP}#view">XRechnung jetzt öffnen</a>''',
  '''<h2>So öffnen Sie eine XRechnung</h2><ol><li>Klicken Sie auf „XRechnung jetzt öffnen“.</li><li>Wählen Sie den Bereich „E-Rechnung ansehen“.</li><li>Ziehen Sie die XML-Datei in das Feld oder klicken Sie, um sie auszuwählen.</li></ol>
<p>Die Rechnung erscheint mit Verkäufer, Käufer, Positionen, Umsatzsteuer und Bankverbindung. Mit „Drucken“ können Sie sie als PDF speichern.</p>
<h2>Welche Formate werden unterstützt?</h2><p>XRechnung im UBL-Format sowie ZUGFeRD/Factur-X und XRechnung im CII-Format (die XML-Datei). Bei ZUGFeRD-PDFs ist die XML-Datei in der PDF eingebettet; die PDF selbst können Sie wie gewohnt öffnen.</p>
<h2>Warum muss ich E-Rechnungen öffnen können?</h2><p>Seit 1. Januar 2025 müssen alle Unternehmen in Deutschland E-Rechnungen empfangen können – auch Kleinunternehmer. Wer Rechnungen nur mit einem PDF-Programm öffnet, sieht bei einer XRechnung nur Code.</p>''',
  [('Wird meine Rechnung hochgeladen?', 'Nein. Die Datei wird nur in Ihrem Browser gelesen und nicht an einen Server gesendet.'),
   ('Ist das Anzeigen wirklich kostenlos?', 'Ja, das Anzeigen von E-Rechnungen ist dauerhaft kostenlos. Nur das Erstellen eigener E-Rechnungen ist Teil des Abos.')]))

PAGES.append(page('/e-rechnung/e-rechnungspflicht/', 'E-Rechnungspflicht 2025, 2027, 2028: Was gilt für kleine Unternehmen? | Halewood E-Rechnung',
  'E-Rechnungspflicht in Deutschland einfach erklärt: Empfang seit 2025, Versand ab 2027 (über 800.000 € Umsatz) bzw. 2028. Ausnahmen für Kleinunternehmer und Kleinbetragsrechnungen.',
  f'''<h1>E-Rechnungspflicht: Was gilt wann – und was müssen kleine Unternehmen tun?</h1><p>Seit 2025 wird die elektronische Rechnung zwischen Unternehmen in Deutschland Schritt für Schritt Pflicht. Hier die wichtigsten Termine einfach erklärt.</p>{CTA}''',
  '''<h2>Die Termine im Überblick</h2><table><tr><th>Ab</th><th>Was gilt</th></tr>
<tr><td>1. Januar 2025</td><td>Alle Unternehmen müssen E-Rechnungen <b>empfangen</b> können.</td></tr>
<tr><td>1. Januar 2027</td><td>Unternehmen mit mehr als 800.000 € Vorjahresumsatz müssen E-Rechnungen <b>versenden</b>.</td></tr>
<tr><td>1. Januar 2028</td><td>Alle Unternehmen müssen im B2B-Bereich E-Rechnungen versenden.</td></tr></table>
<h2>Was ist eine E-Rechnung – und was nicht?</h2><p>Eine E-Rechnung ist eine Rechnung in einem strukturierten, maschinenlesbaren Format nach der Norm EN 16931, zum Beispiel <b>XRechnung</b> oder <b>ZUGFeRD</b>. Eine normale PDF, ein Foto oder ein Scan ist <b>keine</b> E-Rechnung.</p>
<h2>Ausnahmen</h2><ul><li><b>Kleinunternehmer</b> nach § 19 UStG müssen keine E-Rechnungen versenden, aber empfangen können.</li>
<li><b>Kleinbetragsrechnungen</b> bis 250 € sind vom Versand ausgenommen.</li><li>Rechnungen an <b>Privatkunden</b> (B2C) sind nicht betroffen.</li></ul>
<h2>Was sollten kleine Unternehmen jetzt tun?</h2><ol><li>Sicherstellen, dass Sie E-Rechnungen öffnen können (z. B. mit unserem <a href="/e-rechnung/xrechnung-oeffnen/">kostenlosen XRechnung-Viewer</a>).</li>
<li>Ein Werkzeug wählen, mit dem Sie selbst E-Rechnungen erstellen können.</li><li>Frühzeitig umstellen – viele Kunden möchten E-Rechnungen schon vor der Pflicht.</li></ol>
<p class="small">Hinweis: Diese Seite gibt einen allgemeinen Überblick und ersetzt keine Steuerberatung. Für Ihren Einzelfall fragen Sie bitte Ihre Steuerberaterin oder Ihren Steuerberater.</p>''',
  [('Muss ich als Kleinunternehmer E-Rechnungen schreiben?', 'Nein, Kleinunternehmer nach § 19 UStG sind vom Versand ausgenommen. Empfangen können müssen Sie E-Rechnungen aber seit 2025.'),
   ('Reicht eine PDF per E-Mail noch?', 'Nach Ablauf der Übergangsfristen (2027 bzw. 2028) nicht mehr für Rechnungen an andere Unternehmen. Dann ist ein Format wie XRechnung oder ZUGFeRD nötig.'),
   ('Wie verschicke ich E-Rechnungen?', 'Ein bestimmter Übertragungsweg ist nicht vorgeschrieben. Der Versand per E-Mail ist zulässig.')]))

if __name__ == '__main__':
    print('e-rechnung pages:', len(PAGES))
