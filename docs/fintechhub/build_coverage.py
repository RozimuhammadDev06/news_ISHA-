"""Read HTML as text only; build a source-to-spec inventory, without running JS."""
from pathlib import Path
import collections
import hashlib
import json
import re
import sys

source = Path(sys.argv[1])
root = Path(__file__).resolve().parents[2]
raw = source.read_text(encoding="utf-8-sig")

def line_at(offset):
    return raw.count("\n", 0, offset) + 1

def groups_for(kind, name):
    if kind == "route":
        maps = {
            "home": "FE-02; F3", "kurslar": "FE-02; F1", "kurs": "FE-02; B1; E1",
            "narxlar": "FE-06; D1", "tekshir": "BE-09; E3", "kirish": "FE-03; A3",
            "royxat": "FE-03; A1", "tasdiqlash": "R-OTP; A3", "parol": "R-AUTH; A3",
            "ikki": "R-2FA; A3", "403": "FE-01; A; F1", "404": "FE-01; F1",
            "panel": "FE-04; E4; I1", "kurslarim": "FE-04; B1; E1", "dars": "FE-05; B; C; E1",
            "vazifalar": "FE-04; B6", "lablar": "FE-04; C", "tolov": "FE-06; D2",
            "sertifikatlar": "FE-04; E3", "sertifikat": "BE-09; E3", "reyting": "FE-04; E2",
            "xabarlar": "BE-10; G2", "admin": "FE-09; I3; I4", "playground": "FE-05; B5",
            "tolovlar": "FE-06; D", "qaydlar": "FE-04; E1", "jadval": "FE-04; H",
            "yutuqlar": "FE-04; E2", "profil": "FE-10; E2", "taklif": "R-REF; D5",
            "yordam": "FE-02; I2", "murojaat": "FE-09; I2", "hujjat": "FE-02; F3",
            "texnik": "FE-01; I4", "sozlamalar": "FE-10; A; F; G2",
            "mentor": "FE-07; I1", "tekshirish": "FE-07; B6", "guruhlar": "FE-07; I1",
            "muallif": "FE-08; B1", "konstruktor": "FE-08; B2", "natijalar": "FE-04; E4",
            "kursstat": "FE-08; E4", "ekranlar": "F2; O (staging handoff)", "dizayn": "F2; O (UI kit)",
        }
        return maps.get(name)
    if kind == "admin_view":
        maps = {"overview": "FE-09; E4", "users": "FE-09; I3", "user": "I3",
                "courses": "B2; I3", "payments": "D2; D4", "promo": "D5", "certs": "E3",
                "settings": "I4", "roles": "A; I3", "audit": "BE-11; J1", "support": "I2",
                "builder": "B2 (legacy redirect)"}
        return maps.get(name)
    if kind == "form":
        maps = {
            "top-search": "F1", "verify-cert": "E3", "login": "A3", "register": "A1; A2",
            "verify": "A3", "verify-email": "A3", "forgot-email": "A3", "forgot-reset": "A3", "twofa": "A3",
            "course-review": "E1", "quiz": "B4", "homework": "B6", "ethics": "C",
            "term": "C", "lab-flag": "C", "qa-ask": "E1", "qa-reply": "E1", "promo": "D5",
            "lb-privacy": "E2", "profile": "A2", "email-change": "A3", "email-confirm": "A3",
            "change-pw": "A3", "2fa-enable": "A3", "delete-account": "A5", "review": "B6",
            "builder": "B2 (legacy konstruktor)", "promo-create": "D5", "sms-send": "A3",
            "sms-verify": "A3", "phone-send": "A3", "phone-verify": "A3", "note": "E1",
            "line-comment": "B6", "ticket-new": "I2", "ticket-reply": "I2",
        }
        return maps.get(name)
    exact = {
        "skip": "F1", "menu": "F1", "theme": "F2", "set-theme": "F2", "set-lang": "F3",
        "logout": "A3", "resend-verify": "A3", "cancel-delete": "A5", "oauth": "A4",
        "oauth-pick": "A4", "set-return": "A1", "ltab": "B3; E1", "bookmark": "E1",
        "fav": "E1", "freeze": "E2", "rsvp": "H", "receipt": "D4", "copy": "F2",
        "goal-edit": "A2; E4", "tpl": "I1", "csv-copy": "D4", "grant-course": "I3",
        "revoke-course": "I3", "export-data": "A5", "cookie": "F3", "cookie-reset": "F3",
        "trust-clear": "A3", "text-done": "B1; B3", "show-files": "B6",
        "file-tab": "B6", "cancel-2fa": "A3", "sms-reset": "A3", "phone-cancel": "A3",
        "email-cancel": "A3", "checklist-hide": "A1", "pw-toggle": "A2; F2", "login-tab": "A3; F1",
        "copy-code": "F2; B3", "vz-table": "E4; F2",
    }
    if name in exact:
        return exact[name]
    demo = {"quick-login", "reset-demo", "fill-demo", "open-mail", "travel", "travel-reset",
            "sim-offline", "screen-go"}
    if name in demo or name.startswith(("drawer-", "mail-", "uk-")):
        return "14.2; F2; O (demo/staging)"
    prefixes = [
        (("toast-", "modal-", "side-", "rail-", "palette"), "F1; F2"),
        (("forgot-", "2fa-", "sess-", "link-oauth", "unlink-oauth"), "A3; A4"),
        (("cat-",), "F1"), (("vid-",), "B3; F2"), (("quiz-",), "B4"),
        (("code-", "pg-"), "B5"), (("lab-",), "C"), (("qa-",), "E1"),
        (("notif-",), "G2"), (("assign-",), "B6; F1"), (("lb-",), "E2"),
        (("pay-", "promo-", "refund-", "sub-", "card-"), "D"),
        (("mentor-", "msg-student"), "I1"), (("ext-", "lc-"), "B6"),
        (("note-",), "E1"), (("cal-", "live-"), "H"), (("tg-",), "G2"),
        (("ticket-", "support-"), "I2"), (("user-", "imp-"), "I3"),
        (("course-", "mod-", "rev-", "bld-", "b-"), "B2; I3"),
        (("cert-",), "E3"), (("admin-", "tpl-"), "I3; I4; E4"),
    ]
    for prefixes_, spec in prefixes:
        if name.startswith(prefixes_):
            return spec
    return None

records = collections.defaultdict(list)
for m in re.finditer(r'\broute\("([^"\n]+)"', raw):
    records[("route", m[1])].append(line_at(m.start()))
for m in re.finditer(r'^ADMIN_VIEWS\.([A-Za-z_]+)\s*=', raw, re.M):
    records[("admin_view", m[1])].append(line_at(m.start()))

for obj, kind in (("FORMS", "form"), ("ACTIONS", "action")):
    starts = list(re.finditer(rf'^(?:const {obj} = \{{|Object\.assign\({obj}, \{{)', raw, re.M))
    for start in starts:
        end = re.search(r'^\}(?:;|\);)', raw[start.end():], re.M)
        if not end:
            raise ValueError(f"Unclosed registry {obj}")
        body = raw[start.end():start.end() + end.start()]
        for m in re.finditer(r'^  (?:"([^"\n]+)"|([A-Za-z_][\w-]*))\s*(?=:|\()', body, re.M):
            name = m[1] or m[2]
            records[(kind, name)].append(line_at(start.end() + m.start()))
    # Wrappers declared after Object.assign are the last effective handlers.
    for m in re.finditer(rf'^{obj}\.([A-Za-z_][\w-]*)\s*=', raw, re.M):
        records[(kind, m[1])].append(line_at(m.start()))
    for m in re.finditer(rf'^{obj}\["([^"\n]+)"\]\s*=', raw, re.M):
        records[(kind, m[1])].append(line_at(m.start()))

screen_start = raw.index("const SCREENS = [")
screen_end = raw.index('\n];', screen_start)
screen_body = raw[screen_start:screen_end]
screens = []
for m in re.finditer(r'\["([^"\n]+)",\s*"([^"\n]+)",\s*(null|"[^"\n]+")\]', screen_body):
    name, title, actor = m.groups()
    screens.append((name, title, actor.strip('"'), line_at(screen_start + m.start())))

unknown = [(kind, name) for kind, name in records if groups_for(kind, name) is None]
if unknown:
    print(json.dumps({"unmapped": unknown}, ensure_ascii=False))
    raise SystemExit(2)

counts = collections.Counter(kind for kind, name in records)
action_refs = set(re.findall(r'data-action=\\?"([A-Za-z0-9_-]+)\\?"', raw))
form_refs = set(re.findall(r'data-form=\\?"([A-Za-z0-9_-]+)\\?"', raw))
unhandled_actions = sorted(action_refs - {name for kind, name in records if kind == "action"} - {"modal-backdrop"})
unhandled_forms = sorted(form_refs - {name for kind, name in records if kind == "form"})
sha = hashlib.sha256(source.read_bytes()).hexdigest()
out = [
    "# FinTechHub — HTMLdan TZga qamrov reyestri", "",
    "Sana: 31.10.2026. [Asosiy TZ](FinTechHub_TZ.md) · [Batafsil ilova](FinTechHub_TZ_Ilova.md).", "",
    f"Manba: `{source.name}`; SHA-256: `{sha}`.", "",
    "Usul: HTML matn sifatida o'qildi; route, SCREENS, FORMS/ACTIONS reyestrlari va qayta yozilgan handlerlar ajratildi. JavaScript bajarilmadi. Qatorlar asl HTMLga tegishli. Bir nechta ta'rif bo'lsa eng oxirgisi yoki oxirgi wrapper ishlaydi; eski ta'rif alohida yangi feature hisoblanmaydi.", "",
    "Bu implementatsiya/test o'tdi degan hisobot emas. Har qator manba imkoniyatining TZdagi joyini ko'rsatadi; demo va legacy alohida qayd etilgan. Har yangi relizda FE/BE/QA statusi alohida yuritiladi.", "",
    "| Element | Soni |", "|---|---|",
]
for kind, label in (("route", "Unikal route"), ("admin_view", "Admin view"), ("form", "Unikal forma handleri"), ("action", "Unikal action handleri")):
    out.append(f"| {label} | {counts[kind]} |")
out += [f"| SCREENSdagi namuna/variant yozuvi | {len(screens)} |", "",
        "## 1. Sahifa variantlari — SCREENS", "",
        "Bir routega tegishli tab va turli foydalanuvchi variantlari ham ro'yxatda saqlandi. `u1/u6` talaba, `u2` mentor/muallif, `u3` admin, guest/null ommaviy yoki autentifikatsiya konteksti.", "",
        "| Namuna yo'l | Sahifa/variant | Demo actor | TZ / ilova bandi | Manba qatori |", "|---|---|---|---|---|"]
for name, title, actor, line in screens:
    route_name = name.split("-", 1)[0]
    spec = groups_for("route", route_name) or ("FE-01; F1 (404 ssenariysi)" if route_name == "mavjud" else None)
    if not spec:
        raise ValueError(f"Screen not mapped: {name}")
    out.append(f"| `{name}` | {title} | {actor} | {spec} | {line} |")

for index, (kind, title) in enumerate((("route", "Route reyestri"), ("admin_view", "Admin viewlar"), ("form", "Formalar"), ("action", "Amallar")), 2):
    out += ["", f"## {index}. {title}", "",
            "| Element | TZ / ilova bandi | Ta'rif qatorlari (oxirgisi ustuvor) |", "|---|---|---|"]
    for (kind_, name), lines in sorted(records.items()):
        if kind_ == kind:
            out.append(f"| `{name}` | {groups_for(kind, name)} | {', '.join(map(str, lines))} |")

triggers = {
    "data-catalog": ("F1", "Qidiruv, daraja/narx/sort filtrlari"),
    "data-co": ("D1–D3", "Checkout reja/usul/karta/subscription tanlovi"),
    "data-vid": ("B3", "Player tezlik/sifat"), "data-pg": ("B5", "Playground namuna"),
    "data-pref": ("G2", "Event/kanal preference"), "data-uset": ("F2; G3", "O'qish/tinch soat/digest/marketing afzalligi"),
    "data-aset": ("I4", "Feature/provider/maintenance toggle"),
    "data-aset-num": ("I4; D5", "Referal foizi"), "data-role-toggle": ("I3", "Rol berish/olish"),
    "data-tk-status": ("I2", "Ticket holati"), "data-promo-toggle": ("D5", "Promo active"),
    "data-admin-f": ("I3", "User rol/status filtri"), "data-apf": ("D4", "Payment filtri"),
    "data-admin-q": ("I3", "User qidiruvi"), "data-audit-q": ("J1; I4", "Audit qidiruvi"),
    "data-help-q": ("I2", "FAQ qidiruvi"), "data-notes-q": ("E1", "Qayd qidiruvi"),
    "data-palette": ("F1", "Buyruqlar paneli qidiruvi"), "data-lb-course": ("E2", "Kurs reytingi"),
    "data-group-course": ("I1", "Guruh kursi"), "data-author-all": ("B1; I3", "Admin barcha muallif kurslari ko'rinishi"),
    "data-lang-select": ("F3", "Til selector"), "data-bf": ("B2", "Konstruktor nested maydonlari"),
    "data-builder": ("B2; 14.2", "Eski konstruktor maydonlari, yangi konstruktorga o'tkaziladi"),
    "data-builder-mod": ("B2; 14.2", "Legacy modul nomi"),
    "data-builder-ltitle": ("B2; 14.2", "Legacy dars nomi"),
    "data-builder-ltype": ("B2; 14.2", "Legacy dars turi"),
    "data-demo-cardfail": ("14.2; O", "Faqat demo payment failure"),
    "data-rubric": ("B6", "Rubrika total/jazo preview"), "data-qi": ("B4", "Javoblangan savol navigatori"),
    "data-editor": ("B5", "Kod draft/gutter/shortcut"), "data-mask": ("A2; D3", "Telefon/karta/muddat input format"),
    "data-pw-meter": ("A2", "Parol kuchi"), "data-until": ("A3; B4; C; D; K", "Server sanasiga taymer/expiry"),
    "data-nav-more": ("F1", "Qo'shimcha navigatsiya ochiq/yopiq afzalligi"),
    "data-chart": ("E4; F2", "Accessible grafik tooltip"), "data-vz-line": ("E4; F2", "Grafik tooltip/crosshair"),
}
out += ["", "## 6. Click/formdan tashqari asosiy triggerlar", "",
        "| Trigger | Mazmun | TZ / ilova bandi |", "|---|---|---|"]
for name, (spec, desc) in triggers.items():
    if name in raw:
        out.append(f"| `{name}` | {desc} | {spec} |")

pref_values = sorted(set(re.findall(r'data-uset=\\?"([^"\\]+)', raw)))
pref_map = {"autoNext": "B3; F2", "subsDefault": "B3; F2", "speed": "B3; F2",
            "quiet": "R-QUIET; G3; P3", "digest": "R-DIGEST; G3", "marketing": "G3; F3"}
out += ["", "### Sozlama maydonlari alohida tekshiruvi", "",
        "| `data-uset` maydoni | TZ / ilova |", "|---|---|"]
for pref in pref_values:
    if pref not in pref_map:
        raise ValueError(f"Preference not mapped: {pref}")
    out.append(f"| `{pref}` | {pref_map[pref]} |")

out += ["", "### Handoff va production izohlaridagi qo'shimcha scope", "",
        "| Manba joyi / kalit matn | Talab / ilova |", "|---|---|"]
markers = [
    ("Har bir ekran web (desktop + mobil), iOS va Android", "R-MOBILE; P1–P5: platforma parity, push, offline video, deep link"),
    ("Tinch soatlar (23:00–08:00)", "R-QUIET; G3: deferred delivery, 08:00 jamlanma"),
    ("Har dushanba: o‘tgan haftadagi progress", "R-DIGEST; G3: haftalik hisobot"),
    ("Prod’da: WebRTC", "H: xona/chat/raise-hand/screen-share/recording"),
    ("Prod: savollar banki", "B2; J2: question bank, random selection, CSV import"),
    ("Prod’da Go, C++ va SQL", "B2/B5; D-13: qo'shimcha runtime adapterlari"),
    ("MP4/MOV · 4 GB", "R-MEDIA; G1: resumable upload va media pipeline"),
    ("Imzolangan HLS URL (5 daq)", "R-VIDEO; B3: playback token, encryption key, watermark"),
    ("STIR va manzil prod’da", "D4; I4: tashkilot rekvizitlari va fiskal integratsiya"),
]
for marker, spec in markers:
    pos = raw.find(marker)
    if pos < 0:
        raise ValueError(f"Expected source marker missing: {marker}")
    out.append(f"| {marker} (qator {line_at(pos)}) | {spec} |")

out += ["", "## 7. Demo va production izohlarining talqini", "",
        "- Demo quick login, email/SMS qutisi, demo authenticator, vaqtni surish, card failure va reset productionda yo'q; ular uchun haqiqiy auth/provider/worker oqimi tegishli A/D/G/K bo'limlarda talab qilingan.",
        "- Eski `builder` va `b-*` actionlari yangi `konstruktor` / `bld-*` bilan bir mahsulot imkoniyatini anglatadi; ikkita mustaqil konstruktor talab qilinmaydi.",
        "- UI kit va ekranlar xaritasi staging handoff vositalari; admin credentiallarini public ko'rsatish talab emas.",
        "- Production izohlaridagi resumable media, HLS himoyasi, ichki live, question bank/CSV va Go/C++/SQL B2/B3/B5/G/H hamda D-13 qarorida; iOS/Android/push/offline video P va D-15da qayd qilingan.",
        "- Har elementning bandga bog'lanishi funksiyaning tayyorligi yoki barcha biznes qarorlar tasdiqlanganini anglatmaydi. Ochiq qarorlar ilova Nda.", ""]
out += ["## 8. Manba triggerlarining statik mosligi", "",
        f"Literal data-action havolalari: {len(action_refs)}; literal data-form havolalari: {len(form_refs)}. Dinamik satr qurilishi va inline modal callbacklar ushbu sonlarga to'liq kirmasligi mumkin.", "",
        f"Reyestrda topilmagan literal actionlar: {', '.join(unhandled_actions) or 'yoq'}. `modal-backdrop` umumiy handlerda alohida bajariladi.", "",
        f"Reyestrda topilmagan literal formalar: {', '.join(unhandled_forms) or 'yoq'}.", "",
        "Bu tekshiruv UI/E2E sinovi o'rnini bosmaydi; xatti-harakat qoidalari ilovadagi oqimlar va QA ssenariylari bilan tekshiriladi.", ""]

target = root / "FinTechHub_Qamrov.md"
target.write_text("\n".join(out), encoding="utf-8")
doc_names = ("FinTechHub_TZ.md", "FinTechHub_TZ_Ilova.md", "FinTechHub_Qamrov.md")
doc_summary = {}
errors = []
for doc_name in doc_names:
    doc = root / doc_name
    content = doc.read_text(encoding="utf-8")
    for link in re.findall(r'\]\(([^)]+)\)', content):
        if "://" in link or link.startswith("#"):
            continue
        local = link.split("#", 1)[0]
        if not (doc.parent / local).exists():
            errors.append(f"Broken document link: {doc_name}: {link}")
    width = None
    for number, row in enumerate(content.splitlines(), 1):
        if row.startswith("|") and row.endswith("|"):
            cols = len(re.split(r'(?<!\\)\|', row)) - 2
            if width is None:
                width = cols
            elif cols != width:
                errors.append(f"Table columns: {doc_name}:{number}: {cols} vs {width}")
        else:
            width = None
    doc_summary[doc_name] = {"lines": len(content.splitlines()), "bytes": doc.stat().st_size}
annex = (root / "FinTechHub_TZ_Ilova.md").read_text(encoding="utf-8")
qa_ids = re.findall(r'^\| (QA-[A-Z]\d+) \|', annex, re.M)
if len(qa_ids) != len(set(qa_ids)):
    errors.append("Duplicate QA IDs")
if errors:
    print(json.dumps({"errors": errors}, ensure_ascii=False))
    raise SystemExit(3)
print(json.dumps({"file": str(target), "source_lines": len(raw.splitlines()), "screens": len(screens), "counts": dict(counts), "unmapped": 0, "preferences": pref_values, "unhandled_actions": unhandled_actions, "unhandled_forms": unhandled_forms, "qa_scenarios": len(qa_ids), "documents": doc_summary, "broken_links": 0, "table_errors": 0}, ensure_ascii=False))
