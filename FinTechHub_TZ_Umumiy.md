# FinTechHub LMS ? umumiy texnik topshiriq

Versiya: 2.0. Sana: 31.10.2026.

Frontend, backend, iOS/Android, ma'lumotlar bazasi, API, integratsiyalar, infratuzilma va qabul qilish mezonlari bitta hujjatda jamlangan.

## Mundarija

- [1-qism. Asosiy texnik topshiriq](#asosiy-tz)
- [2-qism. Batafsil funksional va texnik talablar](#batafsil-talablar)
- [3-qism. HTML bilan qamrov reyestri](#qamrov)

---

<a id="asosiy-tz"></a>

## 1-qism. Asosiy texnik topshiriq

Versiya: 2.0 — takroriy to'liq tahlil. Sana: 31.10.2026.
Manba: foydalanuvchi taqdim etgan `fintechhub.html` faylining statik kod tahlili. Brauzerda ishlash va tashqi integratsiyalar sinovdan o'tkazilmadi.

Ushbu umumiy fayl asosiy TZ, batafsil talablar va qamrov reyestrini o'z ichiga oladi.

2.0 versiya 1–13-bo'limlarni saqlab, quyidagi tuzatishlar va ilovadagi tafsilotlar bilan to'ldiradi. Birinchi versiyadagi umumiy jumla va yangi aniq qoida farqlansa, 14-bo'lim va ilovadagi aniq qoida ustuvor. “Manba” qaydi kuzatilgan demo xatti-harakatini, “Taklif” qaydi esa production uchun tanlangan loyihaviy yechimni anglatadi. Ochiq tijoriy qarorlar kelishilmaguncha ularni yakuniy tasdiqlangan shart deb talqin qilish mumkin emas.

### 1. Loyiha mazmuni

FinTechHub — dasturlash va kiberxavfsizlikni amaliyot orqali o'rgatadigan onlayn ta'lim platformasi (LMS). Foydalanuvchi kurs tanlaydi, bepul yoziladi yoki to'lov qiladi, darslarni o'qiydi, test va kod mashqlarini bajaradi, mentorga vazifa yuboradi va kurs yakunida tekshiriladigan sertifikat oladi.

Bu nomida fintech bo'lsa-da, taqdim etilgan mahsulot bank yoki pul o'tkazish ilovasi emas. Uning asosiy mahsuloti — IT ta'limi; to'lovlar kurs va obunalarni sotish uchun xizmat qiladi.

Fayldagi yo'nalishlar:

| Yo'nalish | Namuna kurslar |
|---|---|
| Dasturlash | Python, JavaScript/TypeScript, React, Node.js/PostgreSQL, Git/GitHub |
| Kiberxavfsizlik | Linux, Web Pentest/OWASP, kiberxavfsizlikka kirish, SOC/SIEM |

Daromad modeli: alohida kurs xaridi, oylik/yillik Pro obuna, kursni 3 yoki 6 qismga bo'lib to'lash. Qo'shimcha mexanizmlar: promo-kod va referal chegirmasi.

### 2. Manba holati va TZ chegaralari

HTML ichida dizayn, hash orqali sahifa navigatsiyasi, JavaScript biznes qoidalari, demo foydalanuvchilar va kurslar mavjud. Holat `localStorage` orqali saqlanadi. Bu tayyor serverli LMS ekanini anglatmaydi.

To'lovlar, email/SMS/Telegram jo'natish, lab infratuzilmasi, ayrim analitika, integratsiya holatlari va boshqa operatsiyalar demo yoki ishlab chiqarish uchun izohlar sifatida berilgan. Ularni haqiqiy ishlaydigan integratsiya deb qabul qilish mumkin emas.

Ushbu hujjatda:

- **Manbadagi talab** — HTML interfeysi yoki kodida ko'ringan imkoniyat/qoidalar.
- **Ishlab chiqarish talabi** — shu imkoniyatni haqiqiy tizimda ishonchli bajarish uchun qo'shilgan talab.
- **Ochiq qaror** — manbada yetarlicha aniqlanmagan yoki bir-biriga mos kelmaydigan qoida.

Frontend prototipning ko'rinishi va foydalanuvchi oqimlarini asos qilib oladi. Narx, ruxsat, natija, sertifikat, taymer va to'lov bo'yicha yakuniy qarorni backend beradi. Demo boshqaruvlari va demo akkauntlar productionga chiqarilmaydi.

### 3. Rollar va vakolatlar

Bir foydalanuvchida bir nechta rol bo'lishi mumkin. Rol bilan birga obyektga tegishlilik ham tekshiriladi.

| Rol | Vazifalar | Chegara |
|---|---|---|
| Mehmon | Katalog, kurs tavsifi, preview, narxlar, FAQ, ochiq sertifikat tekshiruvi | Pullik kontent va shaxsiy kabinet yopiq |
| Talaba | O'qish, topshirish, xarid, o'z natijalari va sozlamalari | Faqat o'z ma'lumotlari va ruxsat berilgan kurslar |
| Mentor | Vazifa tekshirish, savollarga javob, muddat so'rovlarini ko'rish, guruhlar | Biriktirilgan kurs va guruhlar doirasida |
| Muallif | Kurs yaratish/tahrirlash, moderatsiyaga yuborish, kurs analitikasi | O'z kurslari; mustaqil nashr qilish huquqi yo'q |
| Support | Murojaatlar, cheklangan foydalanuvchi yordami | Moliyaviy qaytarish va rol berish huquqi yo'q |
| Admin | Kurs/sharh moderatsiyasi, foydalanuvchi, to'lov, promo, sertifikat va audit | Superadmin vakolatlari berilmaydi |
| Superadmin | Admin vakolatlari, yuqori rollarni berish, tizim sozlamalari | Barcha muhim amallar audit qilinadi |

Manbada support uchun bloklash va foydalanuvchi ko'rinishiga o'tish huquqi ko'rsatilgan. Buni alohida permission sifatida boshqarish kerak. Foydalanuvchi ko'rinishiga o'tish faqat o'qish rejimida bo'ladi; sessiya boshlanishi/tugashi auditga yoziladi. Xodimlar uchun 2FA majburiy. Admin o'zini va boshqa adminni bloklay olmaydi.

### 4. Frontend texnik topshirig'i

#### FE-01. Umumiy interfeys

- Ommaviy sahifalar, shaxsiy kabinet va dars o'qish muhiti uchun alohida layout.
- Desktopda sidebar; mobil qurilmada ochiladigan navigatsiya. Darsda modullar ro'yxati va asosiy kontent.
- O'zbek, rus va ingliz tillari; ochiq, qorong'i va tizim mavzusi. UI tarjimasi va kurs kontenti tili alohida tushuncha.
- Asosiy ko'rinish HTMLdagi ranglar, kartalar, tugmalar, jadvallar va grafiklardan olinadi. Faylda CSS qatlamlari takrorlanganligi sababli yakuniy ko'rinish uchun computed style asos qilib olinadi.
- Loading, bo'sh natija, xato, qayta urinish, offline, 403, 404 va texnik ishlar holatlari.
- Forma xatosi tegishli maydon yonida ko'rsatiladi. Klaviatura navigatsiyasi, fokus, label, kontrast va grafiklarning jadval ko'rinishi ta'minlanadi.
- Shaxsiy ma'lumotlar va tokenlar URLga chiqarilmaydi; `localStorage`da faqat xavfsiz interfeys afzalliklari saqlanishi mumkin.

#### FE-02. Ommaviy sahifalar

- Landing: platforma tavsifi, ikki yo'nalish, kurslar, o'qish jarayoni, FAQ, ro'yxatdan o'tish chaqirig'i.
- Katalog: matnli qidiruv, yo'nalish, daraja, bepul/pullik filtri, saralash, sahifalash.
- Kurs kartasi: nom, yo'nalish, daraja, davomiylik, narx, reyting va foydalanuvchiga mos harakat tugmasi.
- Kurs sahifasi: tavsif, o'rganiladigan natijalar, talablar, muallif, modul/dars dasturi, preview, sharhlar va xarid.
- Narxlar: kurs va Pro shartlari; sertifikat tekshirish; yordam; oferta, maxfiylik, qaytarish va cookie sahifalari.
- Ochiq profil faqat foydalanuvchi ruxsat bergan maydonlarni ko'rsatadi.

#### FE-03. Autentifikatsiya va onboarding

- Ism, familiya, email, parol, shartlarga rozilik bilan ro'yxatdan o'tish; referal havolani saqlash.
- Email/parol orqali kirish, email OTP tasdiqlash, kodni qayta yuborish taymeri, parolni tiklash.
- 2FA kodi va bir martalik zaxira kodi oynalari.
- SMS orqali kirish, Google/GitHub/Telegram orqali autentifikatsiya va CAPTCHA to'liq mahsulot scope'iga kiradi; provayder credentials va bosqichlash alohida qaror. Ishlamaydigan demo login productionga chiqarilmaydi.
- Noto'g'ri kod, tugagan muddat, bloklangan akkaunt va ortiqcha urinish holatlarini ko'rsatish.

#### FE-04. Talaba kabineti

- Bosh panel: oxirgi darsni davom ettirish, kurs progressi, haftalik maqsad, faollik, XP/streak va yaqin muddatlar.
- Kurslarim: davom etayotgan, tugallangan va sevimli kurslar.
- Vazifalar va lablar ro'yxati; darsga o'tish va holat bo'yicha filtrlash.
- Natijalar: haftalik vaqt, kurs/modul progressi, test natijalari va vazifa baholari. Grafik va jadval ko'rinishi.
- Qaydlar: darsga bog'langan yozuvlar va saqlangan darslar.
- Jadval: vazifa muddati, jonli dars, to'lov sanasi; jonli darsga qatnashish belgilashi.
- Yutuqlar: nishonlar, XP tarixi, daraja; reyting: hafta, umumiy va kurs kesimi.

#### FE-05. Dars muhiti — 6 tur

| Tur | Interfeys va harakat |
|---|---|
| Video | Real player, tezlik, boblar, subtitr/transkript, vaqt belgili qayd, ko'rishni davom ettirish |
| Matn | Formatlangan kontent, kod bloklari, materiallar, tugatish harakati |
| Test | Boshlash, savol/variant, navigator, taymer, yakunlash, ball, ruxsat etilgan tahlil va qayta urinish |
| Kod mashqi | JS/Python muharriri, boshlang'ich kod, run, test natijalari, xato, reset |
| Uyga vazifa | Shart, rubrika, muddat, havola/matn/fayl topshirish, urinishlar tarixi, mentor va kod qatori izohlari |
| CTF lab | Ishga tushirish, tayyorlanish, terminal/ulanish, sessiya taymeri, maslahat, flag topshirish, to'xtatish |

- Dars savol-javobi, javob va bildirishnomaga o'tish.
- Qulflangan modulda sabab va ochilish talabi ko'rsatiladi.
- Frontend testning to'g'ri javobi, yashirin kod testi yoki CTF flagni oldindan olmaydi.
- Offline paytida bajarilmagan server operatsiyasi muvaffaqiyatli deb ko'rsatilmaydi. To'liq offline ta'lim alohida scope hisoblanadi.

#### FE-06. Xarid va to'lovlar

- Kurs yoki Pro tanlash, to'liq/3/6 qism rejasini tanlash, promo qo'llash, narx tafsilotlari va rozilik.
- Payme, Click, Uzum Bank va bank kartasi variantlari manbada ko'rsatilgan; frontend faqat backend qaytargan faol usullarni ko'rsatadi.
- Provider checkoutiga o'tish va qaytgach serverdan holatni olish: kutilmoqda, muvaffaqiyatli, xato, bekor qilingan, muddati tugagan.
- To'lovlar tarixi, chek, obuna, avtomatik yangilanishni o'chirish, tokenlashtirilgan kartalar, bo'lib to'lash jadvali.
- Qaytarish huquqi va rad sababini ko'rsatish; ariza yuborish va holatini kuzatish.
- Karta raqami/CVV ilova backendida saqlanmaydi; karta kiritish providerning himoyalangan oynasida bajariladi.

#### FE-07. Mentor kabineti

- Navbat: eng eski topshiriqlar, holat/kurs/guruh filtrlari va SLA belgisi.
- Topshiriq: matn/havola/fayllar, kod, avtotest natijasi, oldingi urinishlar va plagiat signali mavjud bo'lsa uni ko'rish.
- Har rubrika mezoniga ball, umumiy fikr, kod qatoriga izoh; qabul qilish yoki qayta ishlashga qaytarish.
- Muddat uzaytirish so'rovlarini tasdiqlash/rad qilish; savol-javob navbati.
- Guruhlar: talabalar, progress, kechikishlar va yordam talab qiluvchi talabalar.

#### FE-08. Muallif kabineti

- Kurslar va ularning draft/review/published holati.
- Konstruktor: kurs ma'lumoti, narx/daraja/yo'nalish, modullar va 6 turdagi darslarni yaratish, tartiblash, preview belgilash.
- Kontent turiga mos muharrir, saqlash holati, validatsiya, moderatsiyaga yuborish va rad izohini ko'rish.
- Kurs analitikasi: yozilish, darsni tugatish, chiqib ketish, test o'rtachasi va reyting. Productionda simulyatsiya ishlatilmaydi.

#### FE-09. Admin va support

- Admin dashboard: daromad, xarid voronkasi, refund va SLA ogohlantirishlari; metrika davri ko'rsatiladi.
- Foydalanuvchi qidiruvi, filtrlash, profil kartasi, bloklash, ruxsatga mos rol boshqaruvi.
- Kurs va sharh moderatsiyasi; nashr qilish/yashirish; narxni o'zgartirish.
- Buyurtmalar, to'lovlar, refundlar, promo-kodlar va sertifikatni bekor qilish.
- Murojaat navbati, yozishma, kategoriya, ustuvorlik va holat.
- Superadmin uchun integratsiya sozlamalari, feature flag va texnik ishlar rejimi. Maxfiy kalit qayta ochiq ko'rsatilmaydi.
- Rollar matritsasi va o'zgartirib bo'lmaydigan audit ko'rinishi.

#### FE-10. Profil va sozlamalar

Profil/avatar, email/telefonni qayta tasdiqlash, parol, 2FA, sessiyalarni tugatish, kirish tarixi; kanal bo'yicha bildirishnoma afzalligi; Telegram bog'lash; til/mavzu; ma'lumot eksporti va akkauntni o'chirish so'rovi. Eksport va o'chirish jarayon holati bilan ko'rsatiladi.

### 5. Backend texnik topshirig'i

#### BE-01. Arxitektura va umumiy shartnoma

Boshlang'ich arxitektura: domen modullariga ajratilgan bitta backend, relyatsion DB, fon vazifalari navbati, fayl saqlash va alohida kod/lab ijro muhiti. Framework tanlovi ushbu TZ bilan majburlanmaydi.

- Versiyalangan API: `/api/v1`. OpenAPI shartnomasida maydonlar, permission, validatsiya, xatolar va misollar beriladi.
- Sana-vaqt DBda UTC, interfeysda foydalanuvchi vaqt zonasida; boshlang'ich zona `Asia/Tashkent`.
- Summalar float bilan hisoblanmaydi; valyuta va kichik pul birligi API shartnomasida aniq belgilanadi.
- Ro'yxatlar pagination, ruxsat etilgan filter/sort, limit bilan qaytariladi.
- Xato shakli: `code`, `message`, `field_errors`, `request_id`.
- Bir xil mutatsiya qayta yuborilganda takroriy xarid, XP, submission yoki charge yuzaga kelmasligi uchun idempotency ishlatiladi.

#### BE-02. Hisob va xavfsizlik

- Foydalanuvchi, ko'p rollilik va obyekt darajasidagi permissionlar; bloklangan akkaunt uchun sessiya/ruxsatni bekor qilish.
- Parol uchun maxsus xavfsiz password hasher; demo hash algoritmi ko'chirilmaydi.
- Email/telefon OTP va reset tokeni: amal muddati, urinish limiti, qayta yuborish cheklovi, bir martalik foydalanish; saqlashda himoya.
- Xavfsiz sessiya cookie, HTTPS, CSRF himoyasi, sessiya rotatsiyasi va logout/revoke.
- 2FA siri shifrlanadi, backup kodlari hash qilinadi; xodim roli faollashishidan oldin 2FA tekshiriladi.
- Login, OTP, password reset, flag tekshirish va kod ishga tushirish uchun rate limit.
- Server foydalanuvchi IDsi, rol, kursga kirish va topshiriq egasini har so'rovda tekshiradi.

#### BE-03. Kurslar va kirish huquqi

- Yo'nalish, kurs, modul, tartibli darslar va har turga tegishli kontentni boshqarish.
- Kurs holatlari: draft → review → published; rad etilganda izoh bilan tahrirga qaytish. Nashrni yashirish alohida qayd qilinadi.
- Muallif faqat o'z kursini tahrirlaydi; mentor biriktirish va guruh a'zoligi serverda saqlanadi.
- Bepul yozilish, xarid va Pro orqali kirish manbai alohida saqlanadi. Bitta kirish manbai tugashi boshqa haqiqiy kirishni bekor qilmaydi.
- Preview mehmon uchun ochiq; qolgan kontent autentifikatsiya, entitlement va modul ochilishiga bog'liq.
- Sotib olingan kurs uchun UI 12 oy kirishni ko'rsatadi; backendda boshlanish/tugash muddati tekshirilishi kerak.
- Kurs o'zgarganda eski progress, topshiriq va sertifikat buzilmasligi uchun kontent versiyasi/snapshot siyosati bo'ladi.

#### BE-04. Progress, test va kod mashqlari

- Progress: opened/started/completed, video pozitsiyasi, tugatish dalili va vaqtlar. Har dars turi o'z tugatish qoidasiga ega.
- Test: savol va variant tartibi urinishda saqlanadi; boshlanish/tugash vaqti serverniki; javoblar draft saqlanishi mumkin.
- Ball serverda hisoblanadi. Taymer tugaganidan keyin kech javob qabul qilinmaydi; qayta kirish taymerni yangilamaydi.
- To'g'ri javob/tushuntirish faqat urinish yakuni va kurs siyosatiga muvofiq ko'rsatiladi.
- Kod ishlatish asinxron job: queued/running/passed/failed/timeout. CPU, xotira, disk, jarayon va chiqish hajmi cheklangan; tarmoq yopiq.
- Foydalanuvchi kodi asosiy API server jarayonida bajarilmaydi. Yashirin testlar va tizim sirlari foydalanuvchi kodidan ajratiladi.
- Playground natijasi baholanadigan dars natijasidan ajratiladi.

#### BE-05. Vazifa va mentor tekshiruvi

- Har topshirish alohida immutable urinish: havola, matn, fayl/kod snapshoti va topshirilgan vaqt.
- Holatlar: submitted → review → accepted yoki returned; returned holatidan yangi urinish yaratiladi.
- Mentor navbatni egallaganda parallel ikki tekshiruvning to'qnashuvi oldi olinadi.
- Rubrika mezonlari, maksimal ball, mentor izohi, kod qatori izohlari va review tarixi saqlanadi.
- Ball 50% dan past bo'lsa accepted taqiqlanadi; 50% yoki undan yuqori natija mentor qarorisiz avtomatik qabul qilinmaydi.
- Fayl turi/hajmi, zararli fayl tekshiruvi va yopiq yuklab olish ruxsati; tasodifiy storage nomlari.
- Avtotestlar va plagiat tahlili haqiqiy servis bilan amalga oshiriladi yoki funksiyasi o'chiriladi. Demo foizlar ko'rsatilmaydi; plagiat signali avtomatik ayblov yoki bloklashga teng emas.
- Deadline birinchi ochilishda serverda bir marta belgilanadi; uzaytirish sababi, qarori va yangi sana saqlanadi.

#### BE-06. CTF laboratoriyalar

- Lab shabloni, foydalanuvchiga tegishli sessiya, TTL, ulanish ruxsati, maslahat va flag topshirish.
- Holatlar: requested/provisioning/running/stopping/stopped/expired/failed.
- O'quvchilar muhiti bir-biridan va platforma tarmog'idan ajratiladi. Resurslar limitlanadi; ruxsatsiz tashqi nishonlarga chiqish cheklanadi.
- Flaglar frontendda saqlanmaydi; serverda tekshiriladi. Takroriy yechim XP bermaydi.
- TTL tugaganda yoki stop berilganda resurslar avtomatik tozalanadi. Ishga tushirish xatosida band limit bo'shatiladi.
- Bir paytdagi sessiya soni, navbat va tarifga qarab kvota konfiguratsiya qilinadi.

#### BE-07. Buyurtma va to'lovlar

- Mahsulot/narx snapshoti, chegirma, valyuta, to'lov rejasi va rozilik versiyasi bilan buyurtma yaratish.
- Summani server qayta hisoblaydi; mijoz yuborgan narx qabul qilinmaydi.
- Buyurtma holati payment/refund yozuvlaridan ajratiladi. Tavsiya etilgan holatlar: pending/paid/failed/cancelled/expired; refund alohida requested/processing/succeeded/rejected/failed.
- Provider callback/webhook haqiqiyligi uning protokoliga mos tekshiriladi; tranzaksiya, summa, valyuta va buyurtma solishtiriladi.
- Takroriy yoki tartibsiz webhook, checkoutdan qaytmaslik va timeout uchun reconciliation jarayoni bo'ladi.
- Ruxsat faqat server tasdiqlagan to'lovdan so'ng tranzaksion ravishda ochiladi. Brauzerdagi success parametri to'lov isboti emas.
- Kartadan faqat provider tokeni va maskalangan metadata saqlanadi; recurring consent va token revoke yuritiladi.
- Bo'lib to'lashda oxirgi qism qoldiq summaga teng: barcha qismlar yig'indisi buyurtma yakuniy summasiga aniq teng bo'lishi shart.
- Pro: davr, yangilanish, bekor qilish, failed charge, retry, grace va suspend. Avtoyangilanish o'chirilsa joriy to'langan davr saqlanadi.
- Refund ikki bosqichli tasdiq bilan bajariladi; provider tasdig'idan keyin moliyaviy holat va tegishli kirish huquqi yangilanadi.
- Chek yaratish/yetkazish va kerak bo'lsa fiskal servis integratsiyasi; xatolar qayta ishlash navbatiga tushadi.
- Payme/Click/Uzum/card imkoniyatlari, ayniqsa tokenization va recurring, shartnoma va provider texnik imkoniyatiga ko'ra alohida tasdiqlanadi.

#### BE-08. Promo va referal

Promo: foiz/fiks summa, muddat, scope, umumiy va bir foydalanuvchiga limit, birinchi xarid sharti. Promo va referal chegirmasi qo'shilmaydi, kattasi tanlanadi. Parallel xaridlarda limit tranzaksiya bilan tekshiriladi. Bekor/to'lanmagan buyurtma limitni doimiy band qilib qolmasligi kerak.

Referal: kod egasi, taklif qilingan foydalanuvchi, ro'yxat/xarid holati; o'zini taklif qilish va takroriy mukofot taqiqlanadi. Mukofot berish va refunddan keyingi qaytarish siyosati ochiq qaror.

#### BE-09. Sertifikat va gamifikatsiya

- Barcha majburiy darslar tugaganda, vazifalar qabul qilinganda va yakuniy test talabi bajarilganda sertifikat avtomatik yaratiladi.
- Unikal ID, ism/kurs snapshoti, berilgan sana, natija, PDF, QR va ochiq verify URL.
- Verify javobi: valid/revoked/not_found; bekor qilish sababi va vaqtini saqlash. Ochiq javobda email/telefon chiqarilmaydi.
- XP eventlar jurnali; bir hodisa bir marta mukofotlanadi. Daraja, badge, streak va reyting shu jurnal/dalillardan olinadi.
- Faollik va reytingning hafta chegarasi bitta aniq vaqt zonasi qoidasiga asoslanadi. Sintetik/demo statistika ishlatilmaydi.

#### BE-10. Aloqa, support va fon vazifalari

- In-app, email, SMS, Telegram uchun kanal adapterlari, shablon va til, yuborish holati, retry va deduplication.
- Foydalanuvchi afzalliklari hisobga olinadi; xavfsizlik xabarlari o'chirilmaydi.
- Telegram bog'lash bir martalik tasdiqlanadigan token orqali; faqat username kiritish bog'lash uchun yetarli emas.
- Murojaat va xabarlar, kategoriya/priority/status, biriktirilgan xodim, birinchi javob va SLA hisoblash.
- Scheduler: 30 daqiqalik buyurtma expiry, lab TTL, muddat eslatmasi, jonli dars eslatmasi, obuna/bo'lib to'lov, SLA escalation, eksport va cleanup.
- Vazifalar brauzer ochiq bo'lmasa ham bajariladi; worker qayta ishga tushganda xabar yoki to'lov takrorlanmaydi.

#### BE-11. Analitika va operatsion boshqaruv

Talaba, muallif va admin statistikasi real eventlardan olinadi. Daromad hisoboti tushum, refund va sof natijani ajratadi. Kursni tugatish foizi uchun denominator/kohort va vaqt davri hujjatlashtiriladi; o'qish daqiqasi hisoblangan yoki o'lchangan ekanligi ko'rsatiladi.

Audit append-only: actor, amal, obyekt, vaqt, request ID, IP va zarur oldin/keyin ma'lumot; sirlar yozilmaydi. Monitoring: API xato/kechikish, navbat, webhook, charge, lab resursi, backup va disk holati. Integratsiya panelidagi holatlar haqiqiy health-checkdan olinadi.

### 6. Asosiy ma'lumotlar modeli

| Domen | Asosiy entitylar |
|---|---|
| Hisob | User, Role, Permission, UserRole, Session, VerificationChallenge, TwoFactor, LoginEvent, Consent |
| Ta'lim | Track, Course, CourseVersion, Module, Lesson, LessonContent, MediaAsset, Enrollment, Entitlement |
| Natija | LessonProgress, ActivityEvent, QuizQuestion, QuizAttempt, QuizAnswer, CodeRun |
| Mentorlik | Submission, SubmissionFile, RubricCriterion, Review, LineComment, ExtensionRequest, Group, GroupMember, MentorAssignment |
| Lab | LabTemplate, LabSession, LabSolve, HintUsage |
| Moliya | ProductPrice, Order, OrderItem, Payment, ProviderEvent, Subscription, Installment, PaymentMethodToken, Refund, Receipt |
| O'sish | PromoCode, PromoRedemption, Referral, XPEvent, Badge, UserBadge, Certificate |
| Aloqa | Notification, NotificationPreference, Delivery, Ticket, TicketMessage, LessonQuestion, LessonAnswer, CourseReview |
| Qo'shimcha | Note, Bookmark, Favorite, LiveSession, RSVP, AuditLog, FeatureFlag, ExportRequest, DeletionRequest |

Muhim unique cheklovlar: provider transaction/event ID; user+lesson progress; submission urinish raqami; user+lab solve; XP manba hodisasi; sertifikat kodi. Foreign key, status va vaqt indekslari qo'yiladi. Kontent va moliyaviy tarix oddiy cascade delete bilan yo'qolmaydi.

### 7. API guruhlari — frontend/backend kelishuvi

Quyidagi nomlar loyihaviy shartnoma; HTMLda real API mavjudligi tasdiqlanmagan.

| Guruh | Endpoint namunalari |
|---|---|
| Auth | `POST /auth/register`, `/auth/login`, `/auth/verify`, `/auth/password-reset`, `/auth/2fa/verify`, `/auth/logout` |
| Profil | `GET/PATCH /me`, `GET /me/sessions`, `DELETE /me/sessions/{id}`, `POST /me/export`, `/me/deletion-request` |
| Katalog | `GET /courses`, `/courses/{slug}`, `/courses/{id}/curriculum`, `POST /courses/{id}/enroll` |
| Dars | `GET /lessons/{id}`, `PUT /lessons/{id}/progress`, `POST /lessons/{id}/complete`, `GET /lessons/{id}/playback` |
| Test/kod | `POST /lessons/{id}/quiz-attempts`, `PUT /quiz-attempts/{id}/answers`, `POST /quiz-attempts/{id}/submit`, `POST /code-runs`, `GET /code-runs/{id}` |
| Vazifa | `POST /lessons/{id}/submissions`, `GET /submissions/{id}`, `POST /submissions/{id}/reviews`, `POST /lessons/{id}/extension-requests` |
| Lab | `POST /labs/{id}/sessions`, `GET /lab-sessions/{id}`, `POST /lab-sessions/{id}/stop`, `POST /lab-sessions/{id}/flags` |
| To'lov | `POST /checkout/quote`, `/orders`, `GET /orders/{id}`, `POST /orders/{id}/refund-requests`, `POST /webhooks/payments/{provider}` |
| Obuna | `GET /me/subscription`, `POST /me/subscription/cancel-renewal`, `GET/DELETE /me/payment-methods/{id}` |
| Natija | `GET /me/results`, `/me/certificates`, `/leaderboard`, `/certificates/verify/{code}` |
| Aloqa | `GET /me/notifications`, `POST /tickets`, `POST /tickets/{id}/messages`, `GET /calendar` |
| Xodim | `/mentor/queue`, `/mentor/groups`, `/author/courses`, `/author/courses/{id}/analytics`, `/admin/*` |

Har endpoint uchun actor, ruxsat etilgan holat o'tishi, request/response va HTTP xatolari OpenAPIda yoziladi. Fayllar uchun avtorizatsiyali upload/download; lab va code joblar polling yoki event oqimi bilan kuzatiladi.

### 8. Manbadan olingan biznes qoidalari

| Qoida | HTMLdagi qiymat/mazmun |
|---|---|
| Modul ochilishi | Oldingi modul darslarining kamida 80% tugagan |
| Kurs umumiy progressi | Og'irliklar: video/matn 1, test/kod 2, homework/lab 3 |
| Test | Default 300 soniya, o'tish 70%; dars bo'yicha sozlanadi |
| Sertifikat | Barcha darslar tugashi; mavjud yakuniy testdan kamida 70% |
| Yakuniy test bo'lmasa | Demo barcha darslar tugaganda sertifikat beradi; product qarori kerak |
| Vazifa qabul qilish | Kamida 50% va mentorning accepted qarori |
| Vazifa qayta topshirish | UI: ko'pi bilan 2 marta; taklif: dastlabki + 2 qayta = 3 urinish |
| Mentor SLA | Vazifa 48 soat; savolga javob 24 soat |
| Support SLA | Birinchi javob 24 soat |
| Deadline | Birinchi ochilgan vaqtdan darsdagi kunlar; default 7 kun; uzaytirilishi mumkin |
| Eslatmalar | Vazifa muddatiga 24 soatdan kam, jonli darsga 1 soatdan kam qolganda |
| Buyurtma | Pending buyurtma 30 daqiqa amal qiladi |
| Pro demo narxi | Oyiga 199 000, yiliga 1 990 000 so'm; konfiguratsiyadan olinadi |
| Refund | Faqat to'langan kurs, 14 kundan oshmagan, progress 20% dan yuqori emas, faol sertifikat berilmagan |
| Chegirma | Promo va referaldan kattasi, yig'indisi emas |
| XP | Video/matn 10, test 20, kod 30, homework 50, lab 100; sertifikat 200 |
| Daraja | `floor(XP / 1000) + 1` |

Bu qiymatlar prototipdan olingan boshlang'ich sozlamalardir; tijoriy shartlar tasdiqlangach konfiguratsiyada versiyalanadi.

### 9. Aniqlangan nomuvofiqlik va ochiq qarorlar

1. **12 oylik kirish:** checkout shunday deydi, ammo `hasAccess()` faol enrollment uchun muddatni tekshirmaydi. Ishlab chiqarishda muddati aniq entitlement kerak.
2. **Bo'lib to'lash summasi:** demo har qismni yuqoriga yaxlitlaydi; shu summa barcha oyda olinsa jami narx oshishi mumkin. Oxirgi qism qoldiq bo'yicha hisoblanadi.
3. **Pro davri:** demo 30/365 kun qo'shadi. Kalendar oy/yil yoki shu kunlar modeli tanlanishi kerak; billing anniversary aniq belgilanadi.
4. **Kirish va qarzdorlik:** demo `past_due/grace`ni faol obuna kabi qabul qiladi. Grace davomiyligi, retry jadvali va suspend vaqti tasdiqlanadi.
5. **Support va superadmin:** ko'rsatilgan permission matritsasi bilan route tekshiruvlari yagona mexanizm emas. Backend permissionlar matritsasi yakuniy manba bo'ladi; superadmin huquq merosi ochiq belgilanadi.
6. **Vazifa urinishlari/test retake:** qayta tekshiruvda ikkisi ham jami 3 urinish ekanligi kodda tasdiqlandi. Qo'shimcha urinishni mentor berish jarayoni va cooldown ochiq qolmoqda.
7. **Video tugashi/o'qish vaqti:** qayta tekshiruvda video uchun 90% chegara va ko'rilmagan joyga o'tish cheklovi topildi. Ishonchli o'lchash va o'qish vaqti usuli ilovada aniqlashtirildi; demo belgilangan daqiqani qo'shadi.
8. **Jonli dars:** manba production izohida ichki xona, chat, qo'l ko'tarish, ekran ulashish va yozuvni nazarda tutadi. To'liq scope bularni o'z ichiga oladi; faqat havola/RSVP bilan birinchi reliz qilish scope'ni bosqichlash hisoblanadi.
9. **Integratsiyalar:** qaysi providerlar birinchi relizga kirishi, merchant hisoblar, recurring va fiskal xizmat shartlari.
10. **Kontent tili:** uch tildagi UI barcha kurslarni uch tilga tarjima qilish majburiyati emas. Kurs tarjimasi scope sifatida kelishiladi.
11. **Maxfiylik:** ochiq profil/reyting roziligi, moliyaviy yozuvlarni saqlash, akkaunt o'chirish va sertifikat ochiqligi siyosati yakunlanadi.
12. **Chegara va yuklama:** foydalanuvchi soni, bir vaqtdagi video/kod/lab sessiyasi, saqlash hajmi va hosting budjeti hali berilmagan.

### 10. Nofunksional va sifat talablari

- Moslashuvchan interfeys: 360 px mobil, planshet va desktopda asosiy oqimlar ishlaydi; jadvallar o'z konteynerida scroll qiladi.
- Accessibility uchun WCAG AA darajasidagi klaviatura, label, fokus, kontrast va status e'lonlari qabul mezoni qilinadi.
- Taklif etilgan boshlang'ich maqsad: odatiy API o'qish so'rovlarida p95 ≤ 500 ms, 100 parallel faol foydalanuvchi sinovida; video stream va og'ir joblar bundan alohida. Buyurtmachi bilan yuklama tasdiqlanadi.
- Upload, kod va lablar asinxron; UI foydalanuvchiga holat va qayta urinishni ko'rsatadi.
- Backup avtomatlashtiriladi, qayta tiklash sinovi bajariladi; RPO/RTO ishga tushirishdan oldin kelishiladi.
- Sirlar server secret storage orqali beriladi, log va frontend bundle ichiga kirmaydi.
- Boy matn sanitizatsiya qilinadi; fayl va tashqi havolalar nazorat qilinadi. Uchinchi tomon callbacklari va admin mutatsiyalari tekshiriladi.
- Moliyaviy va ta'lim eventlari kuzatiladigan bo'ladi; audit yozuvini oddiy admin tahrirlay/o'chira olmaydi.

### 11. Qabul qilish ssenariylari

1. Mehmon katalogni filtrlaydi, previewni ko'radi; yopiq kontentga to'g'ridan-to'g'ri API orqali ham kira olmaydi.
2. Ro'yxat → OTP → kirish → bepul kursga yozilish oqimi ishlaydi; noto'g'ri/muddati o'tgan kod rad etiladi.
3. To'lov serverda tasdiqlanmaguncha kurs ochilmaydi; bir webhook 3 marta kelganda bitta payment, bitta entitlement va bitta chek hosil bo'ladi.
4. Kurs/Pro huquqi tugasa pullik kontent yopiladi; progress yo'qolmaydi. Boshqa faol xarid huquqi mavjud bo'lsa kirish saqlanadi.
5. Oldingi modul 80% ga yetmaguncha keyingisi API darajasida ham yopiq.
6. Test refresh yoki qayta kirishda yangi taymer olmaydi; vaqt tugagan javob rad etiladi; ball serverda hisoblanadi.
7. Kod timeouti API serverni to'xtatmaydi; yashirin testlar va server sirlari foydalanuvchiga chiqmaydi.
8. Mentor o'ziga biriktirilmagan topshiriqni tekshira olmaydi; 49% natijani accepted qilish rad etiladi; qaytarish yangi urinishga yo'l ochadi.
9. Lab TTL tugaganda resurs yopiladi; bir flagni qayta topshirish XPni oshirmaydi; boshqa talaba sessiyasiga kirish rad etiladi.
10. Bir darsni qayta tugatish XPni takrorlamaydi; sertifikat shartlari bajarilganda faqat bitta faol sertifikat yaratiladi va QR tekshiruv ishlaydi.
11. Refundda 14 kun, 20% va sertifikat chegaralari tekshiriladi; rad etilgan ariza pul qaytarildi deb ko'rsatilmaydi.
12. Bo'lib to'lov qismlari yig'indisi chegirmali jami summaga teng; parallel worker bitta davr uchun ikki marta charge qilmaydi.
13. Muallif o'z kursini moderatsiyasiz nashr qila olmaydi; superadmin amali auditda ko'rinadi; oddiy talaba admin APIga kira olmaydi.
14. Brauzer yopiq bo'lsa ham eslatma, expiry va SLA joblari ishlaydi; qayta urinishda dublikat xabar yaratilmaydi.
15. O'zbek/rus/ingliz UI va light/dark rejimlarida asosiy oqimlar, mobil navigatsiya va xato holatlari tekshiriladi.

### 12. Bosqichlar va topshiriladigan natijalar

Quyidagi bosqichlash — taklif; barcha funksiyalarni birinchi relizga majburan kiritmaydi.

| Bosqich | Natija |
|---|---|
| 1. Asosiy LMS | Auth, rollar, katalog, video/matn/test, enrollment, progress, sodda muallif/admin, bitta bir martalik payment integratsiyasi, vazifa/mentor, sertifikat |
| 2. Tijoriy va xizmat | Pro, recurring/bo'lib to'lov, qo'shimcha providerlar, promo/referal, refund, support, bildirishnoma kanallari, jadval va haqiqiy analitika |
| 3. Amaliy muhit | Izolyatsiyalangan JS/Python run, CTF infratuzilmasi, avtotest/plagiat integratsiyasi, kengaytirilgan gamifikatsiya |

Birinchi bosqichda keyingi bosqich funksiyalari menyuda ishlaydigan imkoniyat sifatida ko'rsatilmaydi. Agar barcha imkoniyatlar birinchi relizga kerak bo'lsa, to'liq TZ shu hajmda baholanadi.

Topshirish paketi: frontend/backend manba kodi, DB migratsiyalari, OpenAPI, konfiguratsiya namunasi, storage/worker sozlamalari, testlar va hisobot, deploy/rollback yo'riqnomasi, backup/restore yo'riqnomasi, rollar matritsasi, admin qo'llanmasi. Production ma'lumotlaridan ajratilgan demo seed ham beriladi.

### 13. Manbadagi tayanch nuqtalar

- Dars turlari, progress og'irligi, XP va providerlar: `TYPE_LABEL`, `TYPE_WEIGHT`, `TYPE_XP`, `PROVIDERS`.
- Demo va local storage: `seed()`, `load()`, `save()`.
- Kirish/modullar: `hasAccess()`, `lessonAccess()`, `moduleUnlocked()`.
- Sertifikat: `checkCertificate()`.
- Chegirma va xarid: `validatePromo()`, `coDiscount()`, `checkoutItem()`.
- Qaytarish: `refundEligible()`.
- Fon jarayonlari: `runJobs()`.
- Rollar: `ADMIN_VIEWS.roles`; sahifalar xaritasi: `SCREENS`.
- Haqiqiy/simulyatsiya statistikasini ajratish: `courseStats()`, `reviewChart()`.

Ushbu hujjat taqdim etilgan HTML mahsulotining texnik talqinidir. U mavjud workspace backendining auditi yoki tayyor implementatsiya hisoboti emas.

### 14. Takroriy tahlildagi majburiy aniqlashtirishlar

#### 14.1. Tasdiqlangan qo'shimcha qoidalar

| ID | Talab | Dalil / ilova |
|---|---|---|
| R-AUTH | Login 3 xatodan keyin CAPTCHA; 5 xatodan keyin 15 daqiqalik vaqtincha cheklov | Yakuniy `FORMS.login`; ilova A |
| R-OTP | Email kodi 10 daqiqa, resend 60 soniya, kuniga 5 yuborish; SMS 5 daqiqa, 10 daqiqada 3 yuborish; noto'g'ri kod limiti 5 | `startVerify`, sms handlerlar; ilova A |
| R-IDENTITY | OAuth bog'lash/uzish; oxirgi kirish usulini uzish taqiqlanadi; email bir xil bo'lishi akkauntlarni avtomatik birlashtirmaydi | `oauth-pick`, `link-oauth`, `unlink-oauth` |
| R-2FA | 5 daqiqalik pending challenge, 5 xato limiti, 10 backup kod, ishonchli qurilma 30 kun | `FORMS.twofa`, `genBackup`; ilova A |
| R-VIDEO | 90% ko'rilganda complete, 0.5–2x tezlik, auto/360/720/1080 sifat, 5 soniyalik auto-next, subtitr defaults, watermark va qisqa muddatli playback token | `videoView`, `vidTick`; ilova B |
| R-QUIZ | Jami 3 urinish; bir/necha javob; savol va variantlar aralashadi; multi-selectda aynan to'g'ri to'plam; eng yaxshi ball hisobga olinadi | `quizView`, `gradeQuiz`; ilova B |
| R-HW | Dastlabki + 2 qayta urinish; kechikish boshlangan har sutkaga 10%, maksimum 30%; deadline+3 kundan keyin yopiladi | `hwView`, `FORMS.review`; ilova B |
| R-EXT | 1/2/3/5/7 kun uzaytirish; pending so'rovni takrorlash yo'q; sabab va qarorlar tarixi; javob maqsadi 24 soat | `ext-open`, `ext-approve`, `ext-reject` |
| R-LAB | Email verified, qoidalarga rozilik, bir paytda 1 lab, 60/120 daqiqa TTL, bir marta +60 daqiqa, 10 flag/min | `labView`, lab actionlar; ilova C |
| R-XP | Testning birinchi muvaffaqiyatli natijasi ≥90% bo'lsa +10 bonus; birinchi lab yechimiga +50; maslahat −15/−30; barcha o'zgarishlar jurnalga | `FORMS.quiz`, `lab-flag`, `lab-hint` |
| R-FREEZE | Haftasiga bir streak freeze; bugungi kun uchun; faollik daqiqasi va XP sifatida hisoblanmaydi | `freeze`, `streak`; ilova E |
| R-REVIEW | Kursning ≥20% progressi, 1–5 yulduz, kamida 10 belgi, linksiz, bir user/kurs sharhi, moderatsiyadan keyin reytingga qo'shiladi | Kurs formasi va yakuniy review handlerlar |
| R-QA | Savol ≥10 belgi, javob ≥2; ovozni qaytarib olish; o'z savoliga ovoz yo'q; resolved, report va flagni oshkor qilmaslik | QA handlerlar; ilova E |
| R-REF | Do'stning birinchi xaridiga chegirma, taklif egasiga bir martalik 90 kunlik bonus promo; ko'rsatilgan bonus foizi sozlamadan | `settle`, `taklif`; ilova D |
| R-DELETE | 30 kunlik bekor qilish oynasi; auto-renew darhol o'chadi; keyin anonimlashtirish va sessiyalarni revoke | Yakuniy delete handler, `runJobs`; ilova A |
| R-MEDIA | Avatar 2 MB, muqova 5 MB, vazifa 20 MB, ticket 5 MB, video 4 GB; video uzilganda yuklashni davom ettirish | Form va konstruktor matnlari; ilova G |
| R-A11Y | Buyruqlar paneli, klaviatura yorliqlari, modal fokus, copy fallback, grafik-jadval almashinuvi | UI action va eventlar; ilova F |
| R-QUIET | Tinch soatlar 23:00–08:00, push/Telegramni ertalab jamlab yuborish | `settingsNotif`; ilova G3 |
| R-DIGEST | Har dushanba o'tgan hafta progressi va yaqin muddatlar hisoboti; marketing alohida ixtiyoriy | `settingsNotif`; ilova G3 |
| R-MOBILE | Web desktop/mobil bilan birga iOS/Android oqimlari, push, yuklab olingan video/qaydlar va deep link | `ekranlar` sahifasidagi handoff matni; ilova P |

#### 14.2. Qo'shimcha topilgan nomuvofiqliklar

- **Billing urinishlari:** `RETRY_DAYS=[0,1,3,5]` — jami 4 urinish; xabarda “3 ta” deyiladi. Boshlang'ich talab: dastlabki + 3 retry; grace to'lov sanasidan 12 kun. Xabar ham shu qiymatlardan tuziladi.
- **Kechikish jazosi:** demo review paytida joriy deadline bilan qayta hisoblaydi; keyinchalik muddat o'zgarsa oldingi submission bahosi o'zgarishi mumkin. Deadline va jazo siyosati submissionda snapshot qilinadi.
- **20% va 100%:** yaxlitlangan progress biznes qarori uchun ishlatilmaydi. Sharh/refund tekshiruvi aniq nisbat, sertifikat esa barcha majburiy darslarning completion holati bilan tekshiriladi.
- **Jonli dars:** avvalgi TZdagi “havola/RSVP yetarli” faqat cheklangan birinchi reliz varianti edi. To'liq mahsulot uchun ichki jonli dars moduli ilova Hda belgilandi.
- **Qo'shimcha tillar va test banki:** Go/C++/SQL, savollar banki, random tanlash va CSV import faqat production izohlarida uchraydi. Ular yo'qolib qolmasligi uchun alohida kengaytma sifatida reyestrga kiritiladi; JS/Python oqimi bilan teng darajada tayyor demo deb ko'rsatilmaydi.
- **Refund tasdig'i:** manbadagi ikki bosqich UI tasdiqlashni bildiradi; ikki alohida xodim tasdig'i manbada yo'q. Productionda qayta autentifikatsiya + yakuniy tasdiq talab qilinadi; ikki xodim talabi tijoriy qaror.
- **Demo ma'lumotlar:** soxta email qutisi, authenticator, tezkor login, vaqtni oldinga surish, card failure va seed reset faqat demo/staging vositalari. Ularni haqiqiy foydalanuvchi funksiyasi sifatida ishlab chiqish talab qilinmaydi.
- **Offline va'dasi:** HTML banneri aloqa tiklanganda yuborishni va'da qiladi, lekin ishonchli sync navbati yo'q. Ilova Fda progress/qayd/kod drafti uchun chegaralangan sync, moliyaviy va baholash amallari uchun online talabi belgilandi.
- **Mobil scope:** ekranlar xaritasi matnida iOS/Android, push, yuklab olingan video va deep linklar aniq tilga olingan. Bu ishlaydigan mobil kod emas, lekin to'liq loyiha talabida yo'qolmaydi: ilova P. Faqat responsive web bilan cheklash alohida reliz/scope qarori bo'ladi.

### 15. To'liq scope va reliz chegarasi

Ushbu TZ va ilovada ko'rsatilgan barcha asosiy oqimlar to'liq loyiha hisobiga kiradi. 12-bo'limdagi bosqichlar ish tartibi; ular funksiyani o'z-o'zidan scope'dan chiqarish uchun asos bo'lmaydi. Olib tashlanadigan yoki keyinga qoldiriladigan band IDsi, sababi va relizi bilan yozma qayd etiladi.

Manbada yetarli bo'lmagan qoida yashirin taxmin bilan yopilmaydi: ilovadagi qarorlar reyestrida boshlang'ich yechim, kim tasdiqlashi va qaysi ish unga bog'liqligi yoziladi. Ishlab chiqish davomida har talab uchun frontend, backend va QA holati yuritiladi. Qamrov reyestri mavjud implementatsiya tayyorligini emas, HTMLdagi imkoniyatlar hujjatga bog'langanini ko'rsatadi.

---

<a id="batafsil-talablar"></a>

## 2-qism. Batafsil funksional va texnik talablar

Bu ilova frontend, backend, QA va infratuzilma ishini bo'lish uchun yozilgan. “Manba” — HTMLdagi qoida; “Taklif” — productiondagi bo'shliqni to'ldiradigan boshlang'ich yechim; “Qaror” — buyurtmachi tasdig'i kerak bo'lgan masala. Hech bir bo'lim integratsiya allaqachon ishlayotganini bildirmaydi.

### A. Hisob, onboarding va ruxsatlar — R-AUTH, R-OTP, R-IDENTITY, R-2FA, R-DELETE

#### A1. Ro'yxatdan o'tish va birinchi kirish

1. Mehmon kurs/preview yoki ro'yxat sahifasidan keladi; qaytiladigan manzil faqat sayt ichidagi ruxsatli yo'l bo'ladi.
2. Ism, familiya, email, parol/takror, yo'nalish (`dev/sec/both`), referal kodi va shartlar roziligi yuboriladi. Marketing roziligi alohida va ixtiyoriy.
3. Email normalizatsiya qilinadi va unikal bo'ladi; vaqtinchalik pochta cheklovi konfiguratsiyadan boshqariladi. Demo qora ro'yxati to'liq himoya deb qabul qilinmaydi.
4. Shartlarning versiyasi, vaqt va rozilik turi saqlanadi; marketingni rad qilish ro'yxatdan o'tishga to'sqinlik qilmaydi.
5. Tasdiqlash kodi yuboriladi. Tasdiqlangandan keyin yangi foydalanuvchi onboardingga o'tadi: daraja va haftalik maqsad. Keyinroq to'ldirish imkoniyati bor.
6. Dashboard checklist: email tasdiqlash, profil/yo'nalish/maqsad, birinchi kurs va birinchi darsga yo'naltirish; bajarilgan qadamlar haqiqiy holatdan olinadi, checklistni yashirish saqlanadi.

Foydalanuvchi holati: `active`, `blocked`, `deleting`, `deleted`. Email/telefon tasdig'i alohida atribut. Tasdiqlanmagan akkaunt bepul kontentni o'qishi mumkin; to'lov, vazifa yuborish va lab ochish verified email talab qiladi. Barcha holatlar backendda tekshiriladi.

#### A2. Maydonlar va validatsiya

| Obyekt/maydon | Manba qoidasi | Production talabi |
|---|---|---|
| Ism/familiya | 2–50 belgi, harf/apostrof/bo'shliq/defis | Unicode va o'zbek apostroflarini qo'llash, trim; frontend/backend bir qoida |
| Email | Format, band emas, lower-case taqqoslash | DB unique; parallel register/change to'qnashuvini qayta tekshirish |
| Parol | ≥8, katta/kichik harf va raqam; demo weak-list; oxirgi 5 tarix | Tarix hashlar orqali tekshiriladi; password maksimal uzunligi kamida 128 belgini qabul qiladigan limit bilan belgilanadi; kesib saqlanmaydi |
| Telefon | `+998` va 9 raqam; 9 raqam kiritilsa normalizatsiya | Tasdiqlangan telefon userlar orasida unikal; o'zgartirishdan oldin avvalgi raqam tasdiqlangan deb qolmaydi |
| Taxallus | 3–20, `A–Z/a–z/0–9/_`, case-insensitive unique | Ochiq profil yoqish uchun majburiy; rezerv nomlar, rename va eski link siyosati |
| Bio | ≤280 belgi | Server limit va sanitizatsiya |
| GitHub | `github.com/username` ko'rinishi | HTTPS link; havolani avtomatik fetch qilish shart emas |
| Haftalik maqsad | 30–3000 daqiqa; onboarding 120/300/600 | Musbat butun son; profil va tezkor edit bir qiymatni o'zgartiradi |
| Avatar | Rang yoki JPG/PNG, 2 MB, 1:1 crop | EXIF olib tashlash, qayta encode, eski faylni retention bo'yicha tozalash |

Parol qoidasi manbadagi boshlang'ich product talabidir. Kompozitsiya siyosati o'zgarsa UI meter, backend validator va xabarlar birga yangilanadi.

#### A3. Challenge va sessiyalar

| Jarayon | TTL | Urinish/yuborish cheklovi | Yakun |
|---|---|---|---|
| Email tasdiqlash | 10 daqiqa | 5 xato; resend ≥60 s; 5 yuborish/kun | Kod bir marta ishlaydi; eskisi bekor |
| SMS login/telefon tasdiqlash | 5 daqiqa | 5 xato; SMS login 3 yuborish/10 min | Tasdiqlangan telefon egasigagina bog'lanadi |
| Parol tiklash OTP | 15 daqiqa | 5 xato; 3 so'rov/soat | Barcha sessiya va ishonch tokenlari revoke |
| 2FA login challenge | 5 daqiqa | 5 xato | To'liq sessiya faqat 2FA tugagach |
| Yangi email kodi | 15 daqiqa | Taklif: 5 xato va resend ≥60 s | Joriy credential qayta tekshiriladi, yangi email tasdiqlangach almashtiriladi |
| Telegram link tokeni | 10 daqiqa | Bir marta, userga bog'langan | Bot tomonidan tasdiqlangan chat ID saqlanadi |
| Admin yuborgan reset havolasi | Demo: 1 soat | Bir marta; rate limit | Oddiy resetdan alohida maqsadli token |

- Urinishlar brauzer state'ida emas, serverda user/challenge/IP bo'yicha saqlanadi; yangi tab orqali limitni chetlab o'tib bo'lmaydi.
- Login 3 xatodan keyin haqiqiy CAPTCHA tekshiruvini talab qiladi, 5 xatoda 15 daqiqa cheklanadi. Reset/SMS login mavjud akkauntni oshkor qilmaydigan javob beradi.
- Taklif: oddiy sessiya idle 24 soat, absolute 7 kun; “eslab qolish” 30 kun absolute. Xodim idle 30 daqiqa, absolute 12 soat; moliyaviy/rol amallarida 5 daqiqadan eski bo'lmagan qayta tasdiq. Qiymatlar sozlanadi va qabul sinovida yoziladi.
- Joriy va boshqa sessiyalar qurilma, taxminiy IP/lokatsiya va oxirgi faollik bilan ko'rsatiladi. Lokatsiya aniqlanmasa “noma'lum”; demo IP hech qachon hardcode qilinmaydi.
- Bitta yoki boshqa barcha sessiyalarni tugatish real server sessiyasini bekor qiladi. “Current” joriy request sessiyasiga nisbatan aniqlanadi.
- TOTP 6 xonali, 30 soniya period; ±1 interval tolerance; ishlatilgan kod shu intervalda qayta qabul qilinmaydi. 10 backup kod bir martalik; regenerate eskilarni bekor qiladi va qayta autentifikatsiya talab qiladi.
- Trust-device 30 kun kriptografik tasodifiy server tokeniga bog'lanadi; brauzer nomi ishonch isboti emas. Xodimning yangi qurilmasida 2FA majburiy; trust siyosati alohida sozlanadi.
- Xodim 2FAni o'chirib xodim APIlariga kirishni davom ettira olmaydi: rol faol bo'lsa o'chirish rad etiladi yoki xodim vakolati qayta enrollmentgacha to'xtatiladi.

#### A4. OAuth va akkauntni tiklash

Google/GitHub OAuth va Telegram autentifikatsiyasi uchun har bir providerning haqiqiy tasdiqlangan oqimi qo'llanadi; providerlar bir xil protokol deb taxmin qilinmaydi. OAuthda state, mos joyda PKCE/nonce va allowlist callback; Telegramda provider dalili serverda tekshiriladi.

Identity `provider + subject` orqali unikal. Email topilgani uchun avtomatik merge yo'q: mavjud foydalanuvchi avval o'z akkauntiga kirib bog'laydi. Email providerda verified bo'lmasa avtomatik verified qilinmaydi. Oxirgi ishlaydigan kirish usulini uzish taqiqlanadi; passwordless akkaunt parol o'rnatishda yaqindagi autentifikatsiya talab qiladi.

Support 2FA reset qilish uchun qayd etilgan tiklash protsedurasi va alohida permission kerak. Ishda case ID, tekshiruv natijasi va sabab saqlanadi; hujjat tasvirlarini cheksiz saqlash talab etilmaydi. Reset barcha sessiya/trust tokenlarini bekor qiladi va userga xavfsizlik xabari yuboradi. Support hech qachon parol, joriy OTP yoki 2FA secretini ko'rmaydi.

#### A5. Eksport va o'chirish

Eksport: profil, roziliklar, yozilishlar, progress, test/vazifa tarixi, o'z izohlari/qaydlari, murojaatlar, to'lov va sertifikatlar. Parol hash, OTP, TOTP secret, backup/trust/provider tokenlari va boshqa user ma'lumoti kirmaydi. Job holati, yaratilgan sana, checksum va muddati cheklangan yuklab olish linki qaytariladi; emailga attachment o'rniga link yuboriladi. Manba: link 24 soat; taklif: eksport fayli 7 kundan keyin tozalanadi.

O'chirish: aniq yozma tasdiq + yaqindagi autentifikatsiya → `deleting`, 30 kunlik `delete_at`, auto-renew off, faol lab/code joblarni to'xtatish, boshqa sessiyalarni revoke. Kirganda bekor qilish tanlovi chiqadi; loginning o'zi o'chirishni jim bekor qilmaydi. Bekor qilish obunani avtomatik qayta yoqmaydi. Qarzdorlikni yo'q qilish yoki moliyaviy tarixni o'chirish ushbu amalning natijasi emas.

Muddat kelgach profil, fayllar va ommaviy ko'rinish saqlash siyosatiga muvofiq o'chiriladi/anonimlashtiriladi; token va identitylar revoke qilinadi. Moliyaviy/audit saqlash muddatlari buyurtmachi siyosati bilan belgilanadi. Eski backup qayta tiklanganda deletion reyestri qayta qo'llanadi.

### B. Kontent, video, test, kod va vazifalar — R-VIDEO, R-QUIZ, R-HW, R-EXT

#### B1. Kurs va kontent versiyasi

- Course: ID, unikal slug, title/subtitle, yo'nalish/daraja, hours, cover, author, learn[], requirements[], base/old price, language, status, version, created/submitted/published timestamps, rejection reason.
- Module: ID, course version, title, position. Lesson: ID, module, title, type, position, preview, required, completion policy, content version.
- Modul ochilish qoidasi: barcha oldingi modullar ichida completed darslar/umumiy darslar ≥0.8; progress og'irligi bu tekshiruvga qo'llanmaydi.
- Kurs progressi: completed darslar og'irligi / barcha majburiy darslar og'irligi. Og'irlik: 1/1/2/2/3/3. UI foizni yaxlitlaydi; biznes cheklovlar aniq nisbatdan olinadi.
- Nashr etilmagan kontent public API/cache/searchga chiqmaydi. “Yashirish” yangi sotuvni to'xtatadi; avval sotib olganlarning kirishi alohida qarorsiz yopilmaydi.
- Talabalar ishlatgan darsni o'chirish/aralash o'zgartirish yangi versiya yaratadi. Eski attempt/rubric/sertifikat snapshoti qoladi. Dars IDsi tartib raqami bilan almashtirilmaydi.
- Muallif/admin parallel tahririda `version/ETag` orqali 409 conflict qaytariladi; oxirgi saqlovchi oldingi ishni jim yo'qotmaydi.

#### B2. Konstruktorning nashr validatsiyasi

| Maydon/tur | Nashrdan oldin majburiy tekshiruv |
|---|---|
| Kurs | Nom ≥5, subtitle ≥10, manbada unique nom; kamida 1 modul va 1 preview; yo'nalish/daraja ruxsatli enum |
| Narx | 0 yoki 1000 so'mga karrali; oldPrice bo'lsa price'dan katta; ishlatilgan buyurtma snapshoti o'zgarmaydi |
| Modul | Nomi bo'sh emas, kamida 1 dars; position takrorlanmaydi |
| Video | Asset haqiqatan ready, duration>0; fayl nomini yozishning o'zi yetarli emas |
| Matn | Taklif: kamida bitta mazmunli blok; markdown sanitizatsiya; ko'rsatilgan o'qish daqiqasi musbat |
| Test | ≥1 savol, ≥2 bo'sh bo'lmagan variant, ≥1 to'g'ri javob; indekslar to'g'ri; timer>0, pass 1–100 |
| Kod | JS/Python, valid funksiya nomi, shart/boshlang'ich kod, ≥1 parse bo'ladigan test; `[args] => expected` JSON bo'yicha |
| Vazifa | Shart bo'sh emas; rubrika nomlari bor, ballar manfiy emas, yig'indi aynan 100; deadline>0 |
| Lab | Mavjud, yoqilgan va sinovdan o'tgan shablonga havola; talab qilingan resurs/TTL konfiguratsiyasi |

Draft to'liq bo'lmasa saqlanadi, nashr esa bloklanadi; xatolar modul/dars bo'yicha ko'rsatiladi va birinchi xatoga o'tiladi. Dars/modullarni yuqori/pastga hamda qo'shni modulga ko'chirish mumkin. Delete tasdiqlanadi. Saqlanmagan tahrir bilan ketishda ogohlantirish; upload davom etayotgan bo'lsa holat saqlanadi. Muallif reviewga yuboradi; admin tasdiqlaydi/rad etadi; rad izohi ≥10 belgi va userga xabar.

Savol banki, tag/difficulty, bankdan tasodifiy tanlash va CSV import manbada production izohi sifatida bor: to'liq scope uchun boshqariladigan savol entitysi, import dry-run/error report va attemptda tanlangan savollarning snapshoti talab qilinadi. Go/C++/SQL playground kengaytmasi alohida sandbox adapterlari, resurs profili va testlar bilan baholanadi; JS/Python implementatsiyasiga yashirin qo'shib hisoblanmaydi.

#### B3. Video oqimi va completion

Upload → media tekshirish → transkodlash → subtitr/transkript drafti → muallif tekshiruvi → ready. Failed media qayta ishlanadi; ready bo'lmaguncha sotiladigan darsga nashr qilinmaydi. HLS auto va mavjud 360p/720p/1080p variantlar; manba past sifatli bo'lsa mavjud bo'lmagan yuqori sifat va'da qilinmaydi.

Player: play/pause, progress/duration, 10 soniya orqaga/oldinga, bob, 0.5/1/1.25/1.5/2x, sifat, CC, fullscreen, oldingi/keyingi dars. Default tezlik, subtitr va auto-next profildan. Tugagach keyingi ochiq darsga 5 soniyadan keyin o'tish va bekor qilish. Oxirgi darsda sertifikat/natija yo'nalishi.

Manba ko'rilgan maksimal pozitsiya bo'yicha 90% hisoblaydi va ko'rilmagan joyga `max+5s`dan ortiq seekni cheklaydi. Taklif: productionda server qabul qilgan takrorlanmagan ko'rish intervallari birlashmasi ≥90% bo'lsa completion; heartbeat bilan tezlik/vaqtga moslik tekshiriladi. Oldinga seek watch credit bermaydi. Xavfsizlik chegarasi: watermark va seek ekran yozuvini to'liq to'xtatmaydi.

Pozitsiya pause/ketish va periodik ravishda saqlanadi; boshqa qurilmada davom etadi. Eski qurilma kech yuborgan heartbeat yangi pozitsiyani jim orqaga surmaydi. Mehmon previewsi shaxsiy progress/XP yaratmaydi.

Playback URL manbada 5 daqiqa; segment va encryption keylarga ham avtorizatsiya kerak. Tokenni uzaytirish video o'rtasida uzilmasdan bajariladi; entitlement tugasa yangi ruxsat berilmaydi. Taklif: watermarkda to'liq email o'rniga user kodi yoki maskalangan identifikator. Subtitr/transkript vaqt belgisini bosish playerga o'tadi; ruxsat yetmasa izoh ko'rsatiladi.

#### B4. Test hayot sikli

`created/in_progress → submitted|timed_out → graded`; admin asosli bekor qilsa `void`. Bitta user/darsda bitta faol attempt; boshlashda limit band qilinadi. Aloqa uzilishi limitni qaytarmaydi. Void/quota grant faqat sabab va audit bilan.

- Default 3 jami urinish. Mentor qo'shimcha urinish bersa `AttemptAllowance` yozuvi yaratiladi; oldingi natija o'chirilmaydi.
- Har attemptda savol va variantlar aralashtiriladi, tartib serverda saqlanadi; refreshda yangi savol/order/timer yo'q.
- Bir javob radio, ko'p javob checkbox. Ko'p javobda aynan to'g'ri to'plam tanlansa 1 ball; qisman ball yo'q. Javobsiz savol 0.
- `raw_score=correct_count/question_count*100`; UI yaxlitlangan foizni ko'rsatadi. Taklif: o'tish raw_score bilan, display yaxlitlash bilan hal qilinmaydi.
- Taymer tugaganda saqlangan javoblar avtomatik yakunlanadi, brauzer yopiq bo'lsa ham job yakunlaydi. Server cutoffgacha qabul qilingan draftlar baholanadi.
- Javobsiz savollar bo'lsa qo'lda submit oldidan tasdiq; “vaqt tugadi” auto-submitida qo'shimcha modal talab qilinmaydi.
- Eng yaxshi yakunlangan urinish kurs natijasi uchun ishlatiladi. Pastroq retake oldingi passni bekor qilmaydi.
- Natijadan keyin to'g'ri/xato javob va tushuntirish manbadagi xatti-harakat; exam reviewni kechiktirish alohida sozlama.
- Birinchi passda asosiy 20 XP; shu pass ≥90% bo'lsa +10. Keyingi qayta urinishlar uchun takroriy XP yo'q.
- Yakuniy test thresholdi asosiy TZdagi 70% bilan muvofiqlashtiriladi; taklif: course final pass yagona `certificate_min_score` qiymatidan olinadi. Bir kursda bir nechta final bo'lishi qo'llansa barchasining talabi aniqlanadi; boshlang'ich modelda ko'pi bilan bitta final.

#### B5. Kod va repository oqimi

Run va Grade alohida: run ko'rinadigan namuna/konsol uchun, grade barcha majburiy server testlari uchun. Graded exercise barcha testlar o'tganda complete. Draft user+dars versiyasi bo'yicha saqlanadi; reset tasdiq bilan starterga qaytaradi.

Manba: 2 soniya limit, JS worker, Python brauzer runtime. Production baholash uchun server sandbox; runtime versiyasi pin qilinadi. Taklif: boshlang'ich 2s CPU, 5s wall time, 256MB RAM, 64KB stdout/stderr, 64KB source; sozlama o'zgarsa UI shu qiymatni oladi. Worker navbati kutish vaqti execution limitga qo'shilmaydi. Job cancel, timeout, syntax/runtime/test xatolari farqlanadi.

Muharrir: qator raqami, syntax highlight, Tab indent, Ctrl+Enter, konsol va testlar. Til/sample almashtirish saqlanmagan kodni almashtirsa tasdiq chiqadi. Playground hello/fibonacci/collection/timeout namunalari bor; playground success kurs completioni hisoblanmaydi.

Repo tekshirish: GitHub/GitLab HTTPS repository linki, ochiq yoki review integratsiyasiga read ruxsat. Fetch asinxron, commit SHA va fayl snapshotiga bog'lanadi; keyingi push topshirilgan ishni o'zgartirmaydi. Provider credentiallari user fayliga/logga chiqmaydi. Fetch xatosi userga tushunarli ko'rsatiladi; private repo uchun minimal read scope. Arbitrary URL/ichki tarmoq fetch va zip path traversal taqiqlanadi.

#### B6. Vazifa, kechikish va uzaytirish

Topshirish shartlari: verified email, entitlement/modul ruxsati, link yoki ruxsatli fayl, halollik roziligi, oldingi urinish yo'q yoki returned, jami <3, `submitted_at ≤ due_at+3 kun`. Pending/review/acceptedda yangi topshirish yopiq. Frontendda yopish backend tekshiruvini almashtirmaydi.

Kechikish formulasi: `days=max(0,ceil((submitted_at-due_at)/24h))`; `penalty=min(30,10*days)`; `final=round(rubric_sum*(1-penalty/100))`. Vaqtlar UTC bo'yicha hisoblanadi. Aynan deadline'da 0%, 1 soniya keyin 10%, aynan +24 soatda 10%, undan keyin 20%; +72 soatdan keyin topshirish rad etiladi. Jazo, deadline va rubrika versiyasi submissionda saqlanadi; mentor keyin tekshirishi jazo miqdorini oshirmaydi.

Manbadagi default rubrika: ishlashi 40, xatolar 30, kod sifati 20, README/izoh 10. UI raw mezonlar, jazo va final ballni alohida ko'rsatadi. Accept uchun final≥50/100. Return uchun kamida 10 belgilik tuzatish izohi. Mentor avtotest xatosini ko'radi; servis xatosi talabaning noto'g'ri yechimi deb baholanmaydi.

Uzaytirish: 1/2/3/5/7 kun, sabab≥15 belgi, bitta pending so'rov. Mentor tasdiq yoki sabab≥5 bilan rad etadi; userga xabar va yangi deadline. Deadlinega kunlar qo'shiladi, bugundan qayta boshlanmaydi. Qabul qilingan ish uchun extension yo'q. Ko'p marta uzaytirish limiti ochiq qaror; taklif: mentor ruxsat bersa har bir holat tarixda saqlanadi. Oldingi bahoni o'zgartirish kerak bo'lsa alohida audited reassessment, avtomatik qayta hisob yo'q.

Review lock/lease bo'ladi; ikki mentor bir ishni parallel accept/return qilganda faqat bir versiya saqlanadi. Lease tugasa navbatga qaytadi. Mentor ajratilmasa admin navbatiga tushadi; talaba topshirig'i yo'qolmaydi. Plagiat signali dalil va qo'lda review bilan; soxta random foiz yo'q.

### C. CTF laboratoriyalar — R-LAB

- Shablonlar: Linux hidden flag (60 daqiqa), SQL injection va reflected XSS (120 daqiqa). Har biri tasdiqlangan ta'lim muhitida; muallif mavjud shablonni tanlaydi, yangi shablon infratuzilma ish oqimi orqali qo'shiladi.
- Ruxsat: kursga kirish, ochiq modul, verified email, qoidalar versiyasi va qabul vaqti. Halollik/flag tarqatmaslik qoidasi roziligi saqlanadi.
- Bir userga bir active/provisioning sessiya. Start parallel bosilganda ham bitta resurs; TTL faqat running boshlanganda yuradi. Qisqa uzilishda sessiyaga qayta ulanish mumkin.
- Bitta running sessiya bir marta +60 daqiqaga uzayadi; expired/stoppedni uzaytirish yo'q. Stop/TTLdan keyin terminal ephemeral holati tozalanadi, yechim va baho saqlanadi.
- Flag user+lab/shablon versiyasiga bog'lanadi, frontenda hisoblanmaydi. Boshqa user flagi topshirilsa hodisa audit qilinadi; javobda flag egasining kimligi oshkor etilmaydi.
- Rate: user+lab uchun 10 urinish/60 s, 429 va Retry-After. Noto'g'ri format ham limitga kiradi; muvaffaqiyatli duplicate yangi XP bermaydi.
- Maslahatlar: bepul yoki 15/30 XP; tasdiqdan so'ng bir marta ochiladi. XP debit va unlock bitta tranzaksiya; taklif: XP yetmasa rad etish. Demo XPni 0gacha tushiradi — bu farq D-07 qarorida qayd etilgan.
- First blood: shu lab versiyasidagi eng birinchi haqiqiy yechimga +50. Parallel ikki solvega unique/lock bilan faqat bitta bonus. Birinchi dars completionidan allaqachon XP olingan bo'lsa dublikat bermaydi.
- XSS admin bot alohida izolyatsiya, qat'iy target allowlist, hech qanday real admin cookie/sirlarisiz ishlaydi. Bu bot platforma admin sessiyasi emas.
- Terminal autentifikatsiyali WebSocket yoki ekvivalent transportda; qisqa muddatli token, origin/owner tekshiruvi, command tarix chegarasi. Frontenddagi `help/clear/history` ishlaydi, haqiqiy shell capabilitylari image siyosatiga bog'liq.
- Klaster to'lgan/feature o'chgan/provisioning failed holati tushunarli ko'rsatiladi; kutish navbati va retry. Orphan resurslar reconciler orqali topilib yopiladi. Block/delete/revoke paytida faol sessiya tugatiladi.

### D. Savdo, billing, refund, promo va referal — R-REF

#### D1. Narx va access manbalari

Buyurtma bitta mahsulot: course yoki Pro; debt esa mavjud billing obligationga havola. Cart, marketplace muallif payouti va talaba pul hamyoni manbada yo'q, scopega avtomatik kiritilmaydi. Alohida kurs 12 oylik kirish; Pro oylik/yillik barcha ruxsatli kurs/lablarga kirish. Bepul enrollment, manual grant va purchase/subscription entitlementlari ajratiladi.

Taklif: yangi narx faqat yangi quote/orderlarga; pending order 30 daqiqalik snapshotida qoladi, recurring narx oshishi alohida xabarnoma/rozilik siyosatiga bog'liq. Quote muddati tugasa qayta hisob va user tasdig'i; summa jim almashtirilmaydi.

Bo'lib to'lov 3/6 qism, manbada ustamasiz; konstruktor izohida kurs >300 000 so'm bo'lsa taklif qilinishi aytilgan, checkoutda bu threshold tekshirilmagan. D-02da boshlang'ich tanlov berilgan. Karta/token ishlamaydigan providerda installment/subscription usuli yashiriladi yoki sababi bilan disabled.

#### D2. Buyurtma va to'lov ketma-ketligi

1. Backend quote: base price, promo/ref variantlari, qo'llangan chegirma, total, installment schedule, currency, expires.
2. User shartlarni tasdiqlaydi; idempotency key bilan order yaratiladi. Bitta mahsulot uchun mavjud haqiqiy pending order davom ettirilishi mumkin; narx yoki provider o'zgarsa yangi payment attempt yaratiladi.
3. Provider checkout/tokenization ishga tushadi. Backend payment attempt va provider reference saqlaydi.
4. Browser return “tekshirilmoqda” holatini ochadi; to'langanlik server callback/status API bilan tasdiqlanadi.
5. Tasdiqda payment, order, entitlement, promo redemption, referal reward va receipt outbox bir transaction chegarasida bajariladi. Tashqi receipt/email alohida job, ularning xatosi pul qayta yechilishiga olib kelmaydi.
6. Kech kelgan muvaffaqiyatli callback expired/cancelled order uchun ham provider bilan solishtiriladi. Pul olingan bo'lsa “pul yechilmadi” deyish mumkin emas: kirishni tiklash yoki audited reversal holati ishlaydi.

Webhooklar: valid signature/auth, amount/currency/merchant reference, unique provider transaction/event ID, ruxsat etilgan o'tish; raw payload shaxsiy/sir maydonlari maskalanib saqlanadi. `failed`dan oldin/so'ng kelgan success uchun precedence belgilanadi. Reconciliation unresolved paymentlarni provider statusi bilan taqqoslaydi; operator qo'lda paid qilish uchun dalil va alohida permission talab qilinadi.

#### D3. Recurring va qarzdorlik

Manba jadvali: due kunida charge, +1/+3/+5 kun retry — jami 4 urinish. Hammasi failed bo'lsa grace, due+12 kunda suspend. Bu qiymatlar konfiguratsiya va versiyaga ega; bir worker bir necha oy ishga tushmagan bo'lsa eski davrlarni birdaniga cheksiz yechmaydi, reconciliation/operator siyosati ishlaydi.

- Har obligation: subscription/installment ID, period start/end, due, amount, currency, paid amount, attempt count, next retry, grace end, provider reference.
- Charge transport timeout `unknown/processing`; status so'ralmasdan yangi charge yo'q. Job lock va idempotency user+obligation+periodga bog'lanadi.
- Grace/past_due davrida vaqtinchalik access, suspendda faqat shu obligationga bog'liq access yopiladi; progress saqlanadi.
- Manual debt pay va avtomatik retry parallel kelsa bittasi oldin lock oladi; ortiqcha olingan pul reconciliationga tushadi. Qarz yopilishi tegishli obligation va accessni tiklaydi.
- Auto-renew off joriy to'langan davrni bekor qilmaydi, joriy qarzni yo'q qilmaydi. Resume karta/consent tekshiruvi bilan, kerak bo'lsa yangi jadval bilan ishlaydi.
- Kartani default qilish keyingi charge uchun qo'llanadi; faol charge tokeni o'rtada almashtirilmaydi. Oxirgi karta o'chsa auto-renew/qarz uchun oqibat oldindan ko'rsatiladi. Provider token revoke jobining xatosi monitoringga tushadi.
- Bo'lib to'lovda birinchi qism paid bo'lganda kirish ochiladi; barcha qismlar va oxirgi qoldiq oldindan ko'rsatiladi. Chek har bir real charge uchun; umumiy order bilan bog'lanadi.

#### D4. Refund va chek

Eligibility manbasi: paid course, paid_atdan ≤14*24h, weighted progress≤20%, faol sertifikat yo'q. Ariza paytida ham, tasdiq paytida ham tekshirish; manba tarixini saqlash. Bir paymentda bir faol refund, amount≤captured−already_refunded. Qisman refund va installmentning qaysi to'lovlari qaytarilishi D-04 qarori.

User sababi≥10 belgi, admin reject sababi≥5. Arizani ko'rish manbada 3 ish kuni; bankka tushish 1–3 ish kuni deyilgan. Bu provider natijasidan mustaqil kafolat sifatida hardcode qilinmaydi; status matni va muddat konfiguratsiyadan. Ish kunlari uchun dam olish/holiday kalendari kelishiladi.

Admin qayta autentifikatsiya va yakuniy confirmationdan keyin refundni ishga tushiradi. Provider processing/unknown holati bor. Faqat haqiqiy successdan so'ng refunded va kirish manbai bekor; failda paid access saqlanadi. Refund requestning o'zi kursni yopmaydi. Tasdiqdan keyin boshqa Pro/manual entitlement bo'lsa umumiy access qoladi.

Chekda ID, order/payment reference, xizmat snapshoti, amount/currency, discount taqsimoti, vaqt, provider txn, kerak bo'lsa fiskal reference. HTML preview va fayl/download/print; user faqat o'z chekini, moliyaviy xodim permission bilan ko'radi. Admin CSV amaldagi filterga mos, ustunlar: ID, sana, user, xizmat, summa, usul, holat, txn; CSV formula injection va encoding/escaping himoyasi.

Tashkilot rekvizitlari: yuridik nom, STIR/identifikator, manzil, support kontakt, chek rekvizitlari va buxgalter tasdiqlaydigan mahsulot kodi/soliq maydonlari konfiguratsiyadan. Demo fiskal belgi yoki to'qima soliq qiymati haqiqiy chek sifatida chiqarilmaydi. Maydonlarning formatini tanlangan fiskal integratsiya shartnomasi belgilaydi.

#### D5. Promo va referal aniqligi

Promo code 4–16 A–Z/0–9, case-insensitive unique; percent >0≤90 yoki positive fixed; scope all/Pro; validTo kelajak, maxUses 0=limitsiz, perUser≥1, firstOnly, active, owner optional. Ownerli bonus kod boshqa userga berilmaydi. Global va user limitlari atomik; quote tekshiruvi order/payment vaqtida qayta qilinadi. Expiry vaqt zonasi va inkluziv chegarasi qayd qilinadi.

Manbada fiks promo pullik summani kamida 1000 so'm qoldiradi. Taklif: pullik order uchun shu minimal yakuniy summa yagona konfiguratsiya; promo/ref chegirmalari unga mos clamp qilinadi. Chegirmalar qo'shilmaydi, katta variant tanlanadi; teng bo'lsa promo (manbadagi qoida). Qo'llanmagan promo limitdan sarflanmaydi.

Referal link/kod registerga o'tkaziladi; bir userga bitta referrer, keyin yashirin almashtirish yo'q. Birinchi haqiqiy xarid uchun do'stga konfiguratsiyadagi chegirma, referrerga bir martalik foiz promo, 90 kun. Refund keyingi rewardga ta'siri D-05da; refund windowgacha reward pending qilish taklif etiladi. Bir karta/qurilma mosligi shubha signali, avtomatik ayblov emas; self-referral rad etiladi va asosli review mavjud.

### E. Hamjamiyat, profil, gamifikatsiya va analitika — R-XP, R-FREEZE, R-REVIEW, R-QA

#### E1. Qayd, bookmark, savol-javob va sharh

- Note 2–2000 belgi, user+darsga bog'liq; video timestamp ixtiyoriy va duration ichida. Dars va umumiy qaydlar sahifasida ko'rish, matn/kurs bo'yicha qidiruv, vaqtga o'tish va delete. Timestamp linki boshqa darsdan ochilganda tegishli dars+vaqtga olib boradi.
- Bookmark va favorite toggle idempotent unique user+lesson/course. Favorite hali sotib olinmagan published kursda ham mumkin; entitlement bermaydi.
- Qaydlar va draftlar shaxsiy; mentor/support ularni oddiy user kartasidan ko'ra olmaydi.
- QA savoli≥10, javob≥2 belgi. Course accessi bor userlar o'zaro javob berishi mumkin; mentor belgisi server rol/assignmentidan olinadi.
- Ovoz bitta userga bir marta, toggle bilan bekor qilinadi, o'z savoliga ovoz yo'q. Resolvedni savol egasi yoki biriktirilgan mentor/moderator o'zgartiradi.
- Shikoyat faqat audit yozuvi bo'lib qolmaydi: Report entity, sabab, obyekt snapshoti, navbat, qaror va moderator tarixi. Zarur bo'lsa yashirish; userga natija.
- Flag shabloni ochiq matnda tarqatilishi bloklanadi yoki moderationga tushadi; umumiy anti-spam/rate limit va sanitizatsiya qo'llanadi.
- Course review uchun aniq progress≥20%, rating butun 1–5, text≥10, linksiz; user/kurs bo'yicha bitta submission. `pending/approved/rejected` holatlar; faqat approved reytingga kiradi. Re-approve dublikat sanamaydi. Review edit/re-submit siyosati: taklif — rejected tahrirlanib qayta pending, oldingi tarix saqlanadi.
- Rating approved baholarning real o'rtachasi; hisoblagichni ko'p marta yaxlitlangan oldingi o'rtachadan yig'ish yo'q. Seeddagi agregatlar production dalili sifatida import qilinmaydi.

#### E2. XP, streak va 12 nishon

XP ledger: source_type/id, user, amount (+/−), reason, effective time, unique idempotency key. Jami va haftalik reyting ledgerdan olinadi; debit yo'qolib qolmaydi. Sertifikat revoke qilinganda XP reversal bormi — D-07. Barcha userlarda daraja `floor(max(0,XP)/1000)+1`.

Streak: Asia/Tashkent bo'yicha faol kunlar; bugun faollik bo'lmasa hisob kechadan davom etadi. Kun activity bo'lishi uchun haqiqiy ta'lim eventi; sahifani shunchaki ochish yetarli emas. Freeze bugungi kun uchun haftada 1 ta, o'tgan kunga retroaktiv qo'llanmaydi; yangi haftada quota yangilanadi, yig'ilib ketmaydi. Haftalik XP va activity metrikalari freeze tufayli oshmaydi.

| Badge ID | Nom/shart |
|---|---|
| first | Birinchi qadam — 1 dars complete |
| ten | O'nta dars — 10 dars complete |
| streak7 / streak30 | 7 / 30 kunlik streak |
| quiz | Test ustasi — 3 xil testda 100% |
| python | Pythonchi — Python kod mashqi yechilgan; hardcoded demo dars IDsi emas, semantic tag |
| ctf | CTF ovchisi — 3 xil lab solve |
| blood | Birinchi qon — kamida bir first blood |
| clean | Toza kod — accepted vazifada ≥90/100 |
| helper | Yordamchi — QAda 3 javob; spam orqali mukofot olmaslik nazorati |
| cert | Sertifikatli — kamida 1 faol sertifikat |
| secure | Xavfsiz akkaunt — 2FA yoqilgan |

Manbada badge real vaqtda shartdan hisoblanadi. Taklif: achievement earned_at va evidence saqlanadi; streak pasayishi tarixiy badge'ni yo'qotmaydi; revoked certificate va security kabi joriy holat badge'lari faol/nofaol ko'rsatilishi mumkin. Badge mukofoti qo'shimcha XP beradi deb taxmin qilinmaydi.

Reyting: hafta va umumiy kesimda XP bo'yicha; kurs tanlanganda manbada kurs progressi bo'yicha saralanadi va foiz ko'rsatiladi. Kurs XP reytingi deb noto'g'ri nomlanmaydi. Taklif: teng bo'lsa shu qiymatga oldin yetgan, keyin user ID. Bloklangan/deleted va `hideLb` tanlaganlar chiqmaydi. Ochiq profil roziligi leaderboard roziligidan alohida. Profil: ism/bio/nick, GitHub, daraja/XP/streak, tugatilgan kurslar, badge va sertifikatlar; email, telefon, buyurtma va private activity yo'q.

#### E3. Sertifikat hayot sikli

`eligible → issuing → issued → revoked`. Shartlar barcha majburiy darslar, accepted vazifalar va final thresholdi. Course progressining UI “100%”i yakka dalil emas. Yakuniy test bo'lmasa manba sertifikat beradi; course policy `final_required=false` orqali aniq belgilash talab qilinadi.

Sertifikat code, yil (joriy berish yili, hardcoded 2026 emas), ism/kurs/sarlavha/soat/ball snapshoti, issue_at, verify_url, PDF asset va holat. Bir user+course versionda bitta faol sertifikat; retry duplicate qilmaydi. PDF xatosida issuing/failed va retry; XP faqat bitta issuance hodisasiga.

QR public HTTPS verify URL; PDF/print va LinkedIn ulashish. Ochiq tekshiruv valid/revoked/not_found; revoke reason oldindan public-safe matnga ajratiladi, shaxsiy dalillar ochiq berilmaydi. Admin revoke sabab≥5, audit va userga xabar. Ism o'zgarishida eski PDF jim almashtirilmaydi; correction/reissue eski kodga tarixiy bog'lanadi. Reissue uchun alohida audit/permission.

#### E4. Analitika metrikalari

| Hisobot | Hisoblash va filtr |
|---|---|
| Talaba | 11 haftalik study time va goal, 16 haftalik heatmap, oxirgi 4 hafta o'rtacha, kurs/modullar, oxirgi 12 test, graded vazifalar |
| Mentor | 14 kunlik tekshiruv soni, backlog va eng eski ish, real review turnaround, SLA breach, guruh progressi |
| Muallif | 8 haftalik yangi enrollment, dars bo'yicha completion/drop-off, quiz o'rtacha, approved rating, kurs finish rate |
| Admin | Tanlangan davr bo'yicha yangi user, verified, active, paid, refund va net revenue; conversion bosqichlari |

Study time ikki qiymat bilan: measured_active_minutes va estimated_content_minutes; bitta nom bilan aralashtirilmaydi. Parallel video/code/livedagi bir daqiqa faol vaqtga ikki marta kirmaydi. Browser focus/input/heartbeat signallari yordamchi; daqiqa hisobini “tomosha isboti” deb oshirib talqin qilinmaydi.

Quiz statistikasida attempt average va user best average farqi ko'rsatiladi. Drop-off cohort: shu davrda enrolled va haqiqiy accessga ega userlar; numerator/denominator bir xil cohort. Daromad pending/failed/unknown orderlardan olinmaydi; refund sanasi davrga mos hisoblanadi. Bo'sh dataset 0 yoki “ma'lumot yo'q”, sintetik qiymat emas. Har grafikda davr, timezone, metrika ta'rifi va table toggle; export faqat permission bilan.

### F. Frontend UX, qidiruv, tarjima va offline — R-A11Y

#### F1. Navigatsiya va holat matritsasi

Public header/footer, kabinettagi sidebar/topbar, notification bell, profile menu, mobil bottom tabs va dars raili bir navigatsiya xaritasidan boshqariladi. Ko'p rollilikda mos bo'limlar ko'rinadi; faqat `student` borligi adminni yo'qotmaydi. Breadcrumb va browser back/forward/query filter qayta tiklanadi; chuqur link refreshda ishlaydi.

Katalog qidiruvi kurs nomi, subtitle, muallif va learn natijalari bo'yicha; yo'nalish `all/dev/sec`, daraja `all/beg/mid/adv`, narx `all/free/paid`, sort `popular/new/rating/cheap/exp` — ommabop/yangi/reyting/arzon/qimmat. Filter kombinatsiyasi va query URLda; reset. Yo'q natija, filter bo'yicha count va pagination; eski qidiruv javobi yangisini bosib ketmaydi.

Ctrl/Cmd+K command palette: ruxsatli sahifa, published kurs va o'z ruxsatli darslarini qidirish; ↑↓/Enter/Esc, fokus qaytishi, bo'sh natija. Maxfiy draft/dars nomlari search natijasida sizib chiqmaydi. Oddiy topbar search katalogga yo'naltiradi.

Har mutatsiya: idle → submitting → success/error; double-submit blok, timeoutda tekshirish/qayta urinish, idempotency. Optimistic UI server rad etsa rollback. O'chirish va moliyaviy amallarda aniq obyekt/summa tasdiqi; modal focus trap, Esc/backdrop siyosati, yopilganda oldingi fokus. Klaviatura shortcut matn maydonida yozishni buzmaydi; ekran o'quvchi uchun status va xato e'loni.

#### F2. Media va o'qish UX

Video yorliqlari Space, ←→10s, C, F, N; kod Ctrl+Enter va Tab. Copy code/link/backup/CSV clipboard API ishlamasa tanlab nusxalash fallback. Default player speed, subtitles, auto-next profilda saqlanadi. Player va settings tezlik variantlari manbada farq qiladi (settingsda 0.75x ham bor); taklif: yagona 0.5/0.75/1/1.25/1.5/2x enum. System theme OS o'zgarsa moslashadi; explicit light/dark bundan ustun. O'qish fonti/kengligini userga sozlatish manbada alohida forma sifatida yo'q, majburiy qo'shimcha feature emas.

Grafik tooltip mouse va klaviatura fokusda ishlaydi; ma'lumot faqat rang orqali tushuntirilmaydi; jadval muqobili mavjud. Reduced-motion afzalligi hurmat qilinadi. UI kit va sahifalar xaritasi review/staging uchun qolishi mumkin, demo credentials va debug ma'lumotlar public bo'lmaydi.

#### F3. Til, public sahifalar va cookie

UI `uz/ru/en`, matn kalitlari markazlashgan; DOMdagi o'zbek matnini runtime almashtirish production i18n o'rnini bosmaydi. Plural, sana/raqam/pul/vaqt, server xatolari, email/SMS shablonlari tarjima qilinadi. Kontent tili alohida ko'rsatiladi; mavjud bo'lmagan tarjima ochiq fallback bilan.

Public landing/kurs/narx/help/legal/profil/verify sahifalar uchun title/meta, canonical, Open Graph, sitemap va robots. Kabinet/auth/admin search indeksiga kirmaydi. Public kurs URLlari barqaror slug; eski hash yoki ulashish URLlari uchun redirect xaritasi. Huquqiy matnlar kontent sifatida versiyalanadi; ushbu TZ ularning yuridik matnini tasdiqlamaydi.

Cookie: necessary default; analytics faqat rozilikdan keyin yuklanadi. “Faqat zarurlari”, “Hammasi”, sozlamadan qayta o'zgartirish; versiya/vaqt/tanlov saqlanadi. Banner tugmasini bosish real tracker holatini boshqaradi.

#### F4. Chegaralangan offline sync

Taklif qilingan to'liq mahsulot xatti-harakati:

- Oldin ochilgan dars shelli va saqlangan draftni offline ko'rish mumkin; pullik video/lab uchun yangi ruxsat olinmaydi.
- Faqat qayd drafti, kod drafti va progress heartbeat navbatga olinadi; user ID, content version, event ID va yaratish vaqti bilan.
- Quiz answer local draft sifatida saqlanishi mumkin, ammo server cutoffsiz “qabul qilindi” deb ko'rsatilmaydi; qayta ulanganda faqat deadline ichida serverga yetgan javoblar baholanadi.
- To'lov, refund, vazifa final submit, lab start, role va account security amallari online talab qiladi. Navbatga moliyaviy buyruq qo'yilmaydi.
- Aloqa tiklanganda qayta autentifikatsiya, entitlement va version tekshiriladi; conflict userga ko'rsatiladi. Logoutda mahalliy shaxsiy cache tozalanadi, boshqa akkauntga yuborilmaydi.
- Navbatda/bajarilgan/xato aniq; kafolatlangan sync bo'lmasa “hammasi yuboriladi” degan banner qo'yilmaydi.

### G. Media, storage va bildirishnomalar — R-MEDIA

#### G1. Fayl siyosati

| Joy | Manbadagi format/hajm | Qo'shimcha ishlov |
|---|---|---|
| Avatar | JPG/PNG, 2 MB, square crop | MIME/magic tekshirish, resize, metadata tozalash |
| Kurs cover | JPG/PNG/WebP, 5 MB, tavsiya 1600×900 | Crop/preview, responsive variant, alt matn |
| Video | MP4/MOV, 4 GB, resumable | Upload URL/ticket, checksum, malware/codec tekshiruv, transkodlash |
| Vazifa | ZIP/PDF/MD/PY/JS/TXT, 20 MB | ZIP bomb/path traversal, executable/rendering cheklovi, private snapshot |
| Ticket | Image/PDF, 5 MB | Private preview, MIME allowlist, malware scan |

Max hajm server va object storage siyosatida ham tekshiriladi. Taklif: MiB/GiB aniq qiymatlari UI/API metadatasida qaytariladi; server yuklab olishdan oldin quota ajratadi. Upload `created/uploading/uploaded/scanning/processing/ready/failed/cancelled`; resumable sessiyaning egasi va expiry tekshiriladi. Tugallanmagan upload/unused assetlar cleanup qilinadi. Private fayl uchun qisqa muddatli download URL, xavfsiz alohida origin va Content-Disposition; user yuklagan HTML/script asosiy domen originida bajarilmaydi.

#### G2. Bildirishnoma hodisa/kanal matritsasi

| Hodisa | Qabul qiluvchi | Kanal/majburiylik |
|---|---|---|
| Verify/reset/phone/login/2FA/identity/deletion | Tegishli user | Xavfsizlik/OTP kanali, o'chirib bo'lmaydi; sirlar in-app previewda yo'q |
| Yangi vazifa / review natijasi / extension | Biriktirilgan mentor yoki talaba | In-app; email/Telegram afzallikka muvofiq |
| Deadline <24h | Vazifasi bor talaba | In-app/email/Telegram; accepted yoki pending review ishga yuborilmaydi |
| QA javobi / mentor xabari | Savol egasi yoki talaba | Ruxsatli dars deep linki; afzallikka muvofiq |
| Jonli dars 1h oldin / o'zgardi / bekor | RSVP va ruxsatli user | In-app va yoqilgan kanallar |
| Payment/receipt/failed retry/grace/suspend/refund | To'lov egasi | Transactional xabar; kanal siyosati yoziladi |
| Promo/referral reward / yangi kurs | Egasi yoki rozilik bergan auditoriya | Marketing roziligi va event afzalligi |
| Sertifikat issued/revoked | Egasi | In-app va yoqilgan kanallar |
| Ticket create/reply/status | Egasi va biriktirilgan support | In-app/email; actorning o'z xabari qayta yuborilmaydi |
| SLA breach/flag-sharing/media/job xatosi | Tegishli xodim/on-call | Ichki ruxsatli alert, userga ichki dalil chiqmaydi |

Preference event kategoriyalari: homework, deadline, qa, payment, course, security; kanallar app/email/SMS/Telegram; mobil push alohida device opt-in bilan P bo'limida. Mavjud bo'lmagan telefon/chatga jo'natishga urinish yo'q; fallback siyosati aniq. Notification mark-read/all-read, hammasi/o'qilmagan filtri, unread count va chuqur link. Deep link endi mavjud bo'lmasa tushunarli fallback.

Delivery `queued/sending/sent/delivered/failed/suppressed`; sent yetkazildi degani emas. Provider timeout, bounce va Telegram bot blocked alohida; retry backoff va dead-letter. Dedupe kalit event+recipient+channel. Shablon o'zgaruvchilari validatsiya, HTML escaping, locale fallback, staging preview/test send. OTP va sirlar shablon/logda maskalanadi; demo mailbox productionda yo'q.

#### G3. Tinch soatlar, haftalik hisobot va marketing — R-QUIET, R-DIGEST

Manba sozlamalari: quiet default yoqilgan, 23:00–08:00; push va Telegram ertalab jamlanadi. Bu toggle demo schedulerda to'liq bajarilmagan, production job alohida quriladi. Quiet userning vaqt zonasida, boshlang'ich Asia/Tashkent; 23:00dan boshlab noncritical xabar deferred, 08:00da jamlanma. In-app xabar vaqtida saqlanadi, email/SMS uchun tanlangan event siyosati amal qiladi. OTP va zarur xavfsizlik xabarlari quiet bilan kechiktirilmaydi. Jo'natish paytida event hali dolzarbmi, user ruxsati va afzalligi qayta tekshiriladi; bekor qilingan dars/past deadline noto'g'ri eslatilmaydi.

Har dushanba o'tgan haftadagi progress, vaqt, test/vazifa natijasi va yaqin muddatlar hisoboti. Taklif: 08:00 lokal, email va user yoqqan kanalga; `(user,week,locale,channel)` dedupe. Digestni o'chirish OTP/chekni o'chirmaydi. Marketing ixtiyoriy, alohida consent/time va unsubscribe; yangi kurs/aksiya xabari faqat rozilik bo'lsa. Telegram test xabari foydalanuvchining bog'langan chatiga yuboriladi; jo'natildi/yetkazilmadi holati real.

Qo'shimcha joblar: quiet release/digest generation; qo'shimcha delivery status `deferred`, payloadga `not_before`, `digest_group`. Week boundary va quietga yozgi/qishki vaqt ishlatiladigan zonalar tanlansa timezone kutubxonasi qoidasi qo'llanadi; server vaqt zonasi taxmin qilinmaydi.

### H. Jonli darslar va kalendar

Manba kalendar, RSVP va eslatma bilan birga productionda ichki jonli xona, chat, qo'l ko'tarish, ekran ulashish va avtomatik yozuvni nazarda tutadi. Shuning uchun to'liq scope quyidagicha:

- LiveSession: title, description, course/group/audience, host/co-host, starts_at, duration, timezone, capacity, room provider, status, recording va attendance.
- Vakolatli mentor/muallif/admin yaratadi, tahrirlaydi, bekor qiladi. Qaysi kurs/guruh uchun e'lon qilish permission bilan cheklangan; tahrir tarixi va RSVPga xabar.
- RSVP toggle va capacity atomik; taklif: sig'im to'lsa kutish ro'yxati, joy bo'shasa FIFO taklif. Kursdan chiqarilgan user qatnasha olmaydi.
- Join server room tokeni: user/course/room/role va expiry; faqat host xona boshlaydi. Taklif: scheduled startdan 10 daqiqa oldin lobby, boshlangach active xona; tugagach recording sahifasi.
- Learner mic/camera, raise hand, chat; host mute/remove, screen share va moderatsiya; browser permission/device/connection xatolari va reconnect.
- Audio/video masshtablash media provider orqali; asosiy API server media oqimini uzatmaydi. Record uchun oldindan xabarnoma/rozilik siyosati; processing/ready/failed va private playback.
- Recording tugagach tegishli kurs darsi yoki live sessionga biriktiriladi. Transkript/subtitr media oqimiga o'xshash review bilan.
- Attendance join/leave intervaldan olinadi; join tugmasini qayta bosish avtomatik +30 daqiqa bermaydi. Kurs completionga ta'siri alohida policy.
- Kalendar oy/oldingi/keyingi/bugun, kurs filtri, lokal vaqt: homework due, live, installment/subscription due. Har hodisa ruxsatli obyektga olib boradi. To'lov sanasi kun bo'yi event bo'lsa aniq vaqt ham detailsda.
- Boshlang'ich relizda tashqi meeting linki ishlatilsa bu bandlar bekor emas, keyingi reliz deb yoziladi. Yangi ichki chat/livedagi yozuv retentioni D-09 qaroriga bog'liq.

### I. Mentor, guruhlar, support va admin amallari

#### I1. Guruh va mentor ish oqimi

Group: nom, kurs/cohort, mentorlar, a'zolar, boshlanish/yakun sanasi va status; admin create/assign/member change, mentor faqat o'z guruhini ko'radi. Self-enrollment avtomatik qaysi guruhga tushishi D-10. Guruh yo'q bo'lsa kurs bo'yicha navbat ishlaydi.

Xavf signallari uchun taklif: 7 kun haqiqiy activity yo'q; overdue homework; qayta failed test; eng yaqin deadline. Manba UI shunday talabalarni alohida ko'rsatadi, ammo chegaralar yagona server konfiguratsiyasiga o'tkaziladi. Mentor talaba/kurs kesimida in-app/email/Telegram xabari yuborishi mumkin; preview, user afzalligi va rate limit, audit. Bu xabar tashqi chatda istalgan odamga yozish huquqi emas, LMS ichidagi mahsulot funksiyasi.

Navbat: submission date ascending, course/group/status/SLA filtri; extension va QA alohida tab. SLA 48h submissiondan, QA/extension javobi 24h; navbatda avtotest uzoq qolishi SLAni jim qayta boshlamaydi. Chegara yaqin ogohlantirish va breached escalation; reassignment sanani o'zgartirmaydi. Review comment templates editable yoki konfiguratsiyadan; rubric total live hisoblanadi.

#### I2. Support holatlari

Ticket kategoriya account/payment/tech/content/other. Subject 5–120, birinchi message≥15, reply≥2; attachment siyosati G1. Payment kategoriyasi yoki aniqlangan to'lov muammosi high priority; xodim uni qo'lda o'zgartirsa sabab saqlanadi.

`open` — staff javobi kutilmoqda; `waiting` — user javobi kutilmoqda; `resolved` — yechim taklif qilingan; `closed` — yakunlangan. Staff reply `waiting`, user reply `open`, resolveddan user reply `open`, user “hal bo'ldi” desa closed. Closedga to'g'ridan-to'g'ri reply rad; qayta ochish alohida amal, policy bilan. Assignee, status, priority va history ko'rinadi.

Support va admin javoblari haqiqiy permission bilan; manbada ba'zi joylar faqat adminni staff deb tanishi to'liq ro'l modeli sifatida ko'chirilmaydi. Birinchi staff javob 24h; `waiting`da kutish va birinchi javob SLA alohida metrikalar. FAQ qidiruv/kategoriya, yangi ticket va o'z ticketlar tarixi. Ichki staff eslatma qo'shilsa userga jo'natiladigan javobdan alohida entity/visibility bo'ladi.

#### I3. Foydalanuvchi kartasi va operatsion ruxsat

User kartasi: profil/roles/status/verified, enrollment va access expiry, progress, submission, payment, certificate, sessiyalar va audit havolalari. Keraksiz sirlar responsega kirmaydi. Filtrlar role/status/query, pagination.

- Block/unblock: sabab≥3, faol sessiya/trust/lab/code revoke; avtomatik refund deb talqin qilinmaydi. O'zini/admin peerini bloklash rad; superadmin uchun ham oxirgi superadmin himoyasi.
- Rol grant/revoke: kamida bir rol, yuqori rol faqat superadmin; boshqa user IDsi bilan so'rovda ham permission. Rol olinganda tegishli faol sessiya cachelari darhol invalidatsiya qilinadi. Oxirgi superadminni olib tashlash/deletion taqiqlanadi.
- Manual email verify: faqat maxsus permission, dalil/sabab, audit, userga xabar; odatiy verify bilan adashtirilmaydi.
- Reset link, 2FA recovery, barcha sessiyalarni revoke; tiklash ishi case IDga bog'lanadi.
- Kurs grant: sabab≥3, course, accessUntil, actor; source=manual. Revoke faqat tegishli grantni o'chiradi, progress saqlanadi. Purchased entitlementni o'chirish moliyaviy tarixni bekor qilmaydi.
- Impersonation: support/admin permission, actor va target serverda alohida, boshlash/tugatish/expiry audit, banner; barcha write endpointlarda backend guard. Read hisoblangan view ham notification mark-read yoki last-seen kabi yozuvni yashirin bajarmaydi.
- Moliya CSV, certificate revoke, course price/publish va promo enable/disable yuqori permissionlar bilan; har biri obyekt va oldin/keyin qiymatini auditga yozadi.

#### I4. Tizim sozlamalari

Provider enable/disable, labs/live/referral/leaderboard feature flaglari, maintenance, referal foizi 0–50, shablon preview. Setting schema validatsiya, version, actor va time; frontend toggle permission o'rnini bosmaydi.

Feature o'chishi yangi amalni to'xtatadi, mavjud qarz/payment webhook yoki lab cleanupni to'xtatmaydi. Maintenance public/authenticated userga mos ekran va 503/Retry-After; healthcheck, zarur callback, background worker va vakolatli recovery kirishi davom etadi. Admin o'zini butunlay tashqarida qoldirmasligi uchun recovery tartibi bo'ladi.

Integratsiya health paneli email/SMS/bot/video/lab/fiscal holati, oxirgi tekshiruv, real navbat/xato; mavjud bo'lmagan monitoring qiymati “noma'lum”. Kalit almashtirish, webhook rotation va test/sandbox/live muhitlari alohida. Secret qiymati UIga qaytmaydi; preview/test yuborish ham permission va audit bilan.

### J. To'ldirilgan ma'lumotlar va API shartnomasi

#### J1. Entity qo'shimchalari va minimal maydonlar

Asosiy TZ 6-bo'limidagi entitylarga quyidagilar qo'shiladi: `ExternalIdentity`, `TrustedDevice`, `PasswordHistory`, `AttemptAllowance`, `Report`, `ReviewClaim`, `BillingObligation`, `PaymentAttempt`, `OutboxEvent`, `WebhookInbox`, `Attendance`, `RoomParticipant`, `MediaJob`, `PolicyVersion`, `SettingVersion`, `DeletionTombstone`, `QuestionBank`, `ImportJob`.

| Model | Muhim maydonlar/cheklov |
|---|---|
| Base | UUID/ekvivalent taxmin qilib bo'lmaydigan ID, created_at, updated_at, version; soft-delete kerak bo'lgan joyda deleted_at |
| Challenge | User/subject, purpose, digest, expires_at, attempts, resend_at, consumed_at; purpose va owner tekshiruv |
| Entitlement | User, course/scope, source_type/id, status, starts_at, ends_at, revoked_at/reason; bir source bir marta |
| Progress | User, lesson version, opened/completed_at, last_position, watched intervals, evidence; unique user+lesson version |
| Attempt | User, quiz version, ordinal, question/option snapshot, started/deadline/submitted_at, status, raw score, allowance reference |
| Submission | User/course/lesson version, ordinal, files/commit SHA, honesty version, due snapshot, penalty policy, status, timestamps |
| Review | Submission, rubric version/scores, raw/penalty/final, decision, comments, reviewer, version; immutable review history |
| BillingObligation | User, subscription/order, period, due, currency, expected/paid, state, next retry, grace_until; unique billing period |
| PaymentAttempt | Obligation/order, amount/currency, provider ref, idempotency key, state, provider error, timestamps |
| Refund | Captured payment, amount, reason, eligibility snapshot, requester/approver, provider ref/status, processed_at |
| Event | ID/type/version, aggregate ID/version, dedupe key, occurred_at, payload schema; PII minimizatsiyasi |
| Audit | Actor/target/impersonator, permission, action, object, before/after, request ID, timestamp, IP; maxfiy qiymat redaction |

User/role, assignment va entitlement tekshiruvi cache bo'lsa invalidatsiya bilan. Unique cheklovlar DBda: case-insensitive email/nick, provider subject/event/txn, period charge, source XP, user+question vote, user+course review, user+live RSVP, user+hint unlock. Foreign key deletion siyosati moliyaviy/ta'lim snapshotlarini yo'qotmaydi. PII anonimlashtirilganda snapshotdagi public ismni ham retention qaroriga muvofiq boshqarish kerak.

#### J2. Qo'shimcha API operatsiyalari

Barcha pathlar `/api/v1` ostida; endpoint nomi loyihaviy, amal/permission esa talab. `{id}` umumiy obyekt IDsini bildiradi.

| ID | Method va path | Kim / asosiy shart |
|---|---|---|
| API-01 | `POST /auth/email/resend`, `/auth/sms/send`, `/auth/sms/verify` | Challenge egasi, rate limit |
| API-02 | `GET /auth/oauth/{provider}/start`, `GET/POST /auth/oauth/{provider}/callback` | Providerga mos tasdiq, state va callback allowlist |
| API-03 | `POST /me/identities/{provider}/link`, `DELETE /me/identities/{provider}` | Reauth; oxirgi login usulini uzmaslik |
| API-04 | `POST /me/2fa/setup`, `/confirm`, `/disable`, `/backup-codes/regenerate` | Reauth va rol siyosati; secret bir marta |
| API-05 | `DELETE /me/trusted-devices`, `DELETE /me/sessions` | O'z token/sessiyalarini revoke |
| API-06 | `POST /me/email/change`, `/confirm`, `/cancel` | Joriy autentifikatsiya, pending yangi email |
| API-07 | `POST /me/phone/change`, `/confirm`, `/cancel` | SMS challenge owner |
| API-08 | `GET/PATCH /me/preferences`, `POST /me/onboarding` | Enum/range validatsiya |
| API-09 | `DELETE /me/deletion-request`, `GET /me/exports/{id}` | Grace davrida cancel, o'z exporti |
| API-10 | `GET /search?q=`, `GET /profiles/{nick}` | Public/ruxsatli natijalar, PII filtri |
| API-11 | `GET/POST /me/favorites`, `DELETE /me/favorites/{courseId}` | O'z favoritesi, entitlement bermaydi |
| API-12 | `GET/POST /me/bookmarks`, `DELETE /me/bookmarks/{lessonId}` | O'z saved darslari |
| API-13 | `GET/POST /lessons/{id}/notes`, `DELETE /notes/{id}`, `GET /me/notes` | Private owner; timestamp bounds |
| API-14 | `GET/POST /lessons/{id}/questions`, `POST /questions/{id}/answers` | Course access, text/anti-spam |
| API-15 | `PUT/DELETE /questions/{id}/vote`, `PATCH /questions/{id}/resolution` | Ovoz/resolution vakolati |
| API-16 | `POST /reports`, `GET/PATCH /admin/reports/{id}` | Report yaratish/moderator qarori |
| API-17 | `POST /courses/{id}/reviews`, `PATCH /reviews/{id}`, `POST /admin/reviews/{id}/decision` | Progress va owner/moderator |
| API-18 | `POST /mentor/attempt-allowances`, `POST /submissions/{id}/claim`, `/release` | Biriktirilgan mentor, reason/lease |
| API-19 | `POST /submissions/{id}/line-comments`, `DELETE /line-comments/{id}` | Reviewer/own comment, snapshot line bounds |
| API-20 | `POST /extension-requests/{id}/decision`, `POST /mentor/messages` | Assigned mentor, audit va user prefs |
| API-21 | `POST/PATCH /admin/groups`, `PUT /admin/groups/{id}/members`, `/mentors` | Admin group/assignment |
| API-22 | `POST /lab-sessions/{id}/extend`, `POST /labs/{id}/hints/{hintId}/unlock` | Owner, bir extension, atomik XP debit |
| API-23 | `GET /lab-sessions/{id}/connection` | Owner, running, short-lived token |
| API-24 | `POST /uploads`, `GET /uploads/{id}`, `POST /uploads/{id}/complete`, `/cancel` | Quota/MIME/owner; direct upload grant |
| API-25 | `GET /assets/{id}/download`, `GET /media/{id}/status` | Public/private policy |
| API-26 | `POST/PATCH /author/courses/{id}`, `/modules/{id}`, `/lessons/{id}` | Own course, version/ETag |
| API-27 | `PUT /author/courses/{id}/ordering`, `POST /author/courses/{id}/validate`, `/submit` | Stable IDs, publish validation |
| API-28 | `POST /admin/courses/{id}/decision`, `/visibility`, `/price` | Moderator/finance permission, reason |
| API-29 | `GET/POST /author/question-bank`, `POST /author/question-imports` | Own bank, dry-run/report |
| API-30 | `POST /me/payment-methods/setup`, `PATCH /me/payment-methods/{id}/default` | Provider tokenization, consent |
| API-31 | `GET /me/billing-obligations`, `POST /billing-obligations/{id}/pay` | Owner, fixed outstanding amount |
| API-32 | `POST /me/subscription/resume-renewal`, `GET /receipts/{id}` | Consent va owner |
| API-33 | `POST /admin/refunds/{id}/approve`, `/reject`, `POST /admin/payments/{id}/reconcile` | Reauth, state machine, provider proof |
| API-34 | `GET/POST/PATCH /admin/promos`, `GET /me/referrals`, `/me/reward-promos` | Limit, scope, owner |
| API-35 | `GET /certificates/{id}/download`, `POST /admin/certificates/{id}/revoke`, `/reissue` | Owner/public safe verify, reason |
| API-36 | `POST /me/streak-freezes`, `GET /me/xp-events`, `/me/badges` | Haftalik quota, ledger |
| API-37 | `PATCH /me/notifications/{id}/read`, `POST /me/notifications/read-all` | Owner, idempotent |
| API-38 | `POST /me/telegram/link`, `DELETE /me/telegram`, `POST /webhooks/telegram` | Bir martalik token, bot webhook validation |
| API-39 | `POST/PATCH /live-sessions/{id}`, `PUT/DELETE /live-sessions/{id}/rsvp` | Host/admin yoki ruxsatli learner |
| API-40 | `POST /live-sessions/{id}/join`, `/end`, `GET /live-sessions/{id}/recording` | Room role/capacity/access |
| API-41 | `POST /webhooks/media`, `/webhooks/live`, `/webhooks/delivery/{provider}` | Provider auth, dedupe |
| API-42 | `PATCH /tickets/{id}/status`, `/assignment`, `/priority` | Staff scope; user faqat o'z close/reopeni |
| API-43 | `POST /admin/users/{id}/block`, `/unblock`, `/reset-link`, `/2fa-recovery`, `/verify` | Har amalga alohida permission/reason |
| API-44 | `PUT /admin/users/{id}/roles`, `POST /admin/users/{id}/grants`, `DELETE /admin/grants/{id}` | Superadmin/tegishli grant huquqi |
| API-45 | `POST /admin/impersonation`, `DELETE /admin/impersonation/{id}` | Actor+target, read-only guard |
| API-46 | `GET /admin/audit`, `GET /admin/payments/export`, `GET /admin/analytics` | Permission, filter va max output |
| API-47 | `GET/PATCH /admin/settings`, `GET /admin/integrations/health`, `POST /admin/templates/{id}/preview` | Superadmin, schema va secret redaction |

Contract umumiylari: list `{items, next_cursor/total, filters}`; UTC ISO timestamp; pul `{amount_minor,currency}`; domain error `{code,message,field_errors,request_id}`; 401/403/404/409/422/429/503 xatolari. Idempotency bir key+bir bodyga bog'liq, boshqa body bilan qayta ishlatilsa 409; expiry va saqlash muddati hujjatlashtiriladi. Accept/change amount/role kabi amallar generic PATCH bilan permissionni chetlab o'tmaydi.

### K. Fon vazifalari va integratsiya uzilishlari

| Job | Trigger / natija | Takror ishlaganda himoya |
|---|---|---|
| Order expiry/reconciliation | 30 min yoki unresolved provider state | Captured payment bilan solishtirish |
| Quiz timeout | Server deadline | Bitta yakuniy grading |
| Media pipeline | Upload completed/provider event | Asset+pipeline version |
| Code execution | Grade/run job | Job ID, tashqi timeout va cleanup |
| Lab provisioning/TTL/orphan | Start/expiry/reconciler | Active quota/owner lock, destroy retry |
| Billing retry/suspend | Due, +1/+3/+5, +12 | Obligation+period unique charge |
| Homework/live reminders | <24h / <1h, future event | Event schedule version+user+channel |
| SLA escalation | Homework 48h, QA/ext/support 24h | Eskalatsiya bosqichi bir marta |
| Badge/certificate/aggregates | Completion/review/solve | Ledger event va certificate constraint |
| Notifications/receipt | Outbox | Provider event/delivery dedupe |
| Export/delete | Request / delete_at | Job owner/version/tombstone |
| Cleanup | Orphan upload/export/cache | Retention policy, active reference check |

Siyosat: DB commit va tashqi yuborish orasida transaction outbox; worker at-least-once, handler idempotent. Retry exponent backoff/jitter, maksimal urinish va dead-letter; operator replay sabab/audit bilan. Server va worker vaqt sinxronligi, timezone. Xato jobni “success” qilib yashirish taqiqlanadi. Tashqi servis timeoutining userga, navbatga va moliyaga ta'siri runbookda yoziladi.

### L. Infratuzilma, release va ekspluatatsiya

#### L1. Joylashtirish chegaralari

Frontend/public render, API, worker/scheduler, DB, queue/cache, public/private object storage, video/live provider va alohida lab/code klasteri. Boshlang'ich backend modular monolit bo'lishi mumkin; kod/lab izolyatsiyasi bundan mustasno. Framework yoki hosting brandi TZning funksional talabini cheklamaydi.

Dev/staging/production ajratiladi; test merchant/bot/SMTP credentials productionnikiga tegmaydi. CI migration, lint/typecheck va muhim testlarni bajaradi; secret scan/dependency tekshiruv jarayoni konfiguratsiyalanadi. Frontend/back API mos versiya bilan deploy; oldingi client qisqa o'tish davrida ishlay oladi. DB migration backward-compatible, katta o'zgarishda expand/migrate/contract. Rollback moliyaviy/event yozuvini yo'qotmaydi.

TLS, secure cookies, CORS allowlist, CSP, CSRF, sanitizatsiya, upload sandbox, trusted proxy IP sozlamalari. Production debug/error stack va demo superuserlar yo'q. Dependency/assetlar pin va provenance bilan; tashqi CDN ishlamasa asosiy auth/navigation sinmaydi. Secret rotation va access minimal permission bilan.

#### L2. Taklif qilingan xizmat maqsadlari

| Metrika | Boshlang'ich taklif; hosting/yuklama bilan tasdiqlanadi |
|---|---|
| API | 100 parallel faol userda oddiy read p95≤500ms; 5xx<1%; real test dataset va so'rov mixi hisobotda |
| Muhim write | Ichki DB amali p95≤1s, tashqi provider kutishi asinxron holat; timeout userga tushunarli |
| Ommaviy sahifa | Mobil o'rtacha tarmoq profilida LCP≤2.5s, CLS≤0.1 maqsad; o'lchash profili qayd etiladi |
| Mavjudlik | Oyiga 99.5% API/public boshlang'ich maqsad; rejalashtirilgan maintenance hisobi kelishiladi |
| Backup | Taklif RPO≤1h, RTO≤4h; DB+private storage+config restore sinovi bilan |
| Lab | Reprezentativ shablon cold start p95≤120s; queue va kapasitet alohida o'lchanadi |
| Code | Queue wait p95≤10s kelishilgan limitda; CPU vaqt limiti bilan aralashtirilmaydi |

Bu raqamlar buyurtmachining tasdiqlangan hosting va'dasi emas. Noma'lum parallel video/live/CTF soni uchun alohida capacity table: foydalanuvchi, peak concurrence, storage/bandwidth, retention, region va oylik budjet talab qilinadi. Chegaraga yetganda backpressure/rate-limit ishlashi tekshiriladi.

#### L3. Monitoring va runbook

Request ID bilan structured log; user/secret minimizatsiyasi. Alert: payment unknown/duplicate, provider mismatch, billing failures, webhook auth, queue age, failed jobs, API latency/5xx, DB/storage, lab orphan, backup failure. Dashboarddagi ko'rsatkichlar real manbaga bog'langan.

Runbooklar: payment unknown/reconcile, webhook replay, ortiqcha charge/refund, failed recurring, lab klaster to'lishi/orphan, video processing stuck, email/SMS uzilishi, account recovery, DB restore, key rotation, maintenance va rollback. Har birida owner/permission, tekshirish, tuzatish, audit va userga ko'rinadigan holat yoziladi. Production real pul bilan smoke test faqat ajratilgan tasdiqlangan sinov rejasi orqali; stagingda sandbox test yetarli.

### M. Kengaytirilgan qabul testlari va bajarilganlik sharti

Har testda actor, precondition, request/UI harakati, server natijasi, saqlangan ma'lumot va bildirishnoma tekshiriladi. Faqat tugma ishlashi bilan band yopilmaydi.

| ID | Ssenariy va kutilgan natija |
|---|---|
| QA-A01 | Bir xil emailga parallel register → bitta user; terms yo'q bo'lsa reject |
| QA-A02 | 3/5 login xatosi → CAPTCHA/15min; yangi tab/IP limit siyosatini chetlab o'tmaydi |
| QA-A03 | OTP expiry/resend/5 xato/old kod replay → to'g'ri reject; SMS noma'lum raqamni oshkor qilmaydi |
| QA-A04 | 2FA loginning password bosqichi bilan admin API chaqirish → rad; backup ikkinchi marta ishlamaydi |
| QA-A05 | OAuth bir xil email bilan avtomatik merge yo'q; oxirgi login usuli unlink rad |
| QA-A06 | Phone/email parallel tasdiq va uniqueness; eski tasdiq yangi manzilga o'tmaydi |
| QA-A07 | Reset/change/logout-all → sessiya/trust revoke; xodim 2FA disable qilib ishni davom ettira olmaydi |
| QA-A08 | Deletion+cancel+30kun job → auto-renew o'chgan, PII siyosatga mos, saqlanadigan moliya qolgan |
| QA-B01 | 79%/80% modul, 19.99%/20% review/refund, 99.5% UI100 → aniq chegaralar bo'yicha qaror |
| QA-B02 | 89.9%/90% haqiqiy video interval → completion chegarasi; seek credit bermaydi |
| QA-B03 | Playback token 5min tugashi → refresh; access revoke yangi tokenga yo'l bermaydi |
| QA-B04 | Quiz refresh/2 tab/timeout/offline → bitta attempt, o'sha deadline/order; javobsiz 0 |
| QA-B05 | Multi-select ortiqcha variant → xato; yaxlitlash passni o'zgartirmaydi; retake oldingi bestni pasaytirmaydi |
| QA-B06 | 3 attemptdan keyin start rad; allowance audit bilan +1; duplicate submit XPni oshirmaydi |
| QA-B07 | Code loop/output flood/resource/network → izolyatsiya va limit; server API sog'lom |
| QA-B08 | Repo keyingi push → old submission snapshoti o'zgarmaydi; private/fetch xatosi to'g'ri holat |
| QA-B09 | Deadline, +1s, +24h, +24h1s, +72h, +72h1s → 0/10/10/20/30/reject |
| QA-B10 | Mentor kech tekshirishi penaltyni oshirmaydi; extension eski score'ni jim o'zgartirmaydi |
| QA-B11 | 49/50/90 rubric final, ikki mentor parallel qarori, return izohsiz → tegishli limit/lock |
| QA-B12 | Published kurs tahriri/deletion → eski attempt/sertifikat va entitlement saqlanadi |
| QA-C01 | Verified/ethics yo'q, parallel 2 lab start → rad yoki bitta sessiya |
| QA-C02 | +60 bir marta; TTL/stop/revoke/orphan → resurslar tozalanadi va natija qoladi |
| QA-C03 | 11 flag/min, begona flag, duplicate solve, parallel first-blood → limit, maxfiylik, bitta bonus |
| QA-C04 | Hint double-click/XP yetishmasligi → bitta debit va bir unlock; ledger bilan balans mos |
| QA-D01 | Client narx o'zgartirishi, invalid promo/scope/owner → server narxi va reject |
| QA-D02 | Promo global limitga parallel ikki order, referral+promo tengligi → atomik limit va deterministic tanlov |
| QA-D03 | Payment success redirect fake, webhook wrong signature/amount, duplicate/out-of-order → access faqat tasdiqda |
| QA-D04 | Expired orderga kech success, callback yo'q, provider timeout → reconcile, pul holatini noto'g'ri ko'rsatmaslik |
| QA-D05 | 3/6 installment summasi → total bilan aniq teng; default card almashtirish eski charge'ni buzmaydi |
| QA-D06 | Due/+1/+3/+5/+12, worker replay, manual pay+retry parallel → bitta charge va to'g'ri access |
| QA-D07 | Refund ≤14kun/20%, sertifikat bor/yo'q, provider failed/unknown → faqat successda revoke |
| QA-D08 | Refund sababli bitta grant yopilishi faol Pro/manual grantni o'chirmaydi |
| QA-D09 | Narx o'zgarishi eski paid/order snapshotini o'zgartirmaydi; CSV filter/formula xavfsiz |
| QA-E01 | Review rejected/approved/reapproved → reyting approved unique yozuvlardan; linksiz/progress sharti serverda |
| QA-E02 | QA self-vote/report/resolved/flag matni → permission, real moderation queue va xabar |
| QA-E03 | XP/debit/hafta chegara/freeze → ledger va reyting mos; freeze kuniga daqiqa qo'shmaydi |
| QA-E04 | Sertifikat duplicate issuance/PDF fail/revoke/reissue → unikal ID, history va public-safe verify |
| QA-E05 | Private profile/note/export/asset boshqa user IDsi bilan → ma'lumot chiqmaydi |
| QA-F01 | 360px, tablet/desktop, 3 til/2 theme, back/refresh, keyboard/modal/focus → asosiy oqimlar ishlaydi |
| QA-F02 | Offline queue+logout/login boshqa user → draft aralashmaydi; onlinega qaytganda conflict ko'rinadi |
| QA-F03 | Cookie necessary → tracker yuklanmaydi; rozilik qaytarilsa tracking to'xtaydi |
| QA-G01 | Soxta MIME, oversized/zip bomb/path traversal, private asset link → rad va isolation |
| QA-G02 | Interrupted 4GB media upload, transcode failure/duplicate webhook → resumable/retry, bitta asset state |
| QA-G03 | Xabar worker replay/preferences/bot-block/SMTP fail → dedupe, suppression, failed delivery ko'rinadi |
| QA-H01 | Live capacity/room token/begona user/host revoke → to'g'ri role/access; recording private |
| QA-H02 | Live reschedule/cancel/RSVP cancel → eski eslatma ketmaydi; attendance double-count yo'q |
| QA-I01 | Support vs mentor vs author vs admin vs superadmin → positive/negative permission matritsasi |
| QA-I02 | Last superadmin revoke/block, impersonation write via API → rad, actor/target auditi |
| QA-I03 | Closed ticket reply, userga ichki note, assignee change → state/visibility/SLA to'g'ri |
| QA-K01 | Queue/DB/provider restart oralig'ida commit → outboxdan event yo'qolmaydi, duplicate charge yo'q |
| QA-L01 | Backupdan tiklash, migration/rollback, key rotation, maintenance → runbook bo'yicha isbot |
| QA-L02 | Kelishilgan yuklama testi → p95/error/queue/CTF capacity va cheklovlar hisoboti |

Bajarilganlik sharti: talabning FE/BE/QA egasi bor; migratsiya va API hujjati bor; ijobiy/salbiy/chegara holatlari o'tgan; audit va monitoring ishlaydi; stagingda demo emas haqiqiy sandbox integratsiya dalili; muhim regression testlar; accessibility/lokalizatsiya review; deploy/rollback va restore sinovi; ochiq kritik nuqson yo'q. Faqat backend yoki faqat frontend tayyor bo'lsa end-to-end talab yopilmaydi.

### N. Ochiq qarorlar reyestri

Quyidagi boshlang'ich tanlovlar ishni baholashga yetarli. Ular product/providerga bog'liq tasdiqlanmagan joylarni yashirmaydi; tegishli integratsiya yoki reliz oldidan qaror yoziladi.

| ID | Masala | Boshlang'ich tanlov/taklif | Tasdiqlovchi / bog'liq ish |
|---|---|---|---|
| D-01 | Pro oy/yil va kurs 12 oy sanasi | Kalendar oy/yil, oy oxirida oxirgi haqiqiy kun; demo 30/365 farqi qayd qilinsin | Product+finance; recurring |
| D-02 | Installment minimal narxi | Konstruktor matniga mos >300000 so'm base price; jami 3/6 qism; discountdan keyin positive qismlar | Product+provider; quote |
| D-03 | Provider/token/recurring/fiscal | Bir martalik, tokenization va recurring capability matritsasi, sandbox/live contract | Finance+backend; to'lov relizi |
| D-04 | Refund installment/Pro/qisman | Course full refund captured amount doirasida; Pro va partial avtomatik eligibility yo'q; manual policy kerak | Product+finance; refund |
| D-05 | Referal refund va self-referral | Reward refund oynasi tugaguncha pending; allaqachon ishlatilgan reward clawback siyosati alohida | Product; growth |
| D-06 | Final test/retake/cooldown | ≤1 final, default70%, 3 urinish, mentor allowance; default cooldown yo'q | Academic lead; quiz/cert |
| D-07 | XP yetmasligi/badge reversal | Hint yetarli XP bo'lsa; revoke XP compensating event; tarixiy badge saqlansin | Product; gamifikatsiya |
| D-08 | SLA kalendar va chegaralar | Mentor/support24/48h — uzluksiz soat; refund3 ish kuni alohida kalendar | Operations; SLA/escalation |
| D-09 | Privacy/retention/recording | Private by default, minimal public verify; media, audit, moliya retention jadvali tasdiqlanadi | Data owner; deletion/live |
| D-10 | Guruh/enrollment va mentor | Admin course/cohortga mentor biriktiradi; biriktirilmagan ish umumiy admin navbatida | Academic lead; queue |
| D-11 | Stack/hosting/yuklama/budjet | Modular backend, alohida sandbox, L2dagi boshlang'ich SLO | Tech lead+buyurtmachi; infratuzilma |
| D-12 | Tillar va kontent tayyorlash | UI/shablon uz/ru/en; kurs tarjimasi mavjud kontent doirasida | Product+content owner |
| D-13 | Live va qo'shimcha tillar bosqichi | Ichki live to'liq scope; Go/C++/SQL va bank/CSV izohdagi kengaytmalar alohida reliz qatori | Product+tech lead |
| D-14 | Recovery va moliyaviy tasdiq | Reauth+confirmation; 2-person approval bo'lsa alohida permission/state qo'shiladi | Operations+finance |
| D-15 | Mobil client va tarqatish | iOS/Android alohida deliverable; texnologiya, minimal OS, ekran parity matritsasi, push va offline license rejimi kelishiladi | Product+mobile lead; mobil reliz |

### O. Jamoaga topshirish va kuzatish

Har ish elementi format: requirement ID, maqsad, actor/precondition, FE komponent/route, BE endpoint/entity, state transition, audit/notification, QA ID, dependency, reliz va egasi. Bir requirementga ko'p ticket bo'lishi mumkin; barcha bog'liq ishlar o'tmaguncha requirement complete emas.

Frontend topshiradi: design token/componentlar, barcha sahifa va responsive holatlar, typed API client, i18n, error/offline/accessibility, E2E kritik oqimlar. Backend topshiradi: modellar/migratsiyalar, permission, API/OpenAPI, real integration adapterlar, scheduler/outbox, sandbox bog'lanishi, testlar va monitoring. Infratuzilma topshiradi: muhitlar/secrets/storage/queue/worker, izolatsiya, CI/CD, restore/capacity/rollback. Content/operations topshiradi: kurs/media/question bank, shablon/roziliklar, rubrika/mentorlar, tarif/provider va support qoidalari.

Launch checklist aniq dalilga tayanadi: demo triggerlar productionda yo'q; narx va merchantlar tasdiqlangan; legal/consent versiyalari joylangan; bir kurs bo'yicha register→purchase→learn→submit→review→certificate oqimi o'tgan; refund va dunning sandboxda o'tgan; lab/code isolation va cleanup ishlagan; alert va restore tekshirilgan; qamrov reyestridagi har manba elementi talab yoki asosli demo/legacy istisnosiga ega.

### P. iOS va Android clientlar, push va offline video — R-MOBILE

#### P1. Platforma chegarasi va ekranlar mosligi

Manba `ekranlar` sahifasida barcha ekranlarning web desktop/mobil, iOS va Androidda bir xil oqimga ega bo'lishini aytadi; mobil push, offline yuklangan video/qayd va `fintechhub://dars/py/py4` deep link misoli ham bor. HTML native client kodi emas. To'liq loyiha bahosida mobil clientlar alohida frontend ish oqimi bo'ladi; responsive web ularni avtomatik tayyor qilmaydi.

Platforma matritsasi har SCREENS elementi uchun `web/iOS/Android` va rol bilan yuritiladi. Talaba oqimlari: auth/onboarding, katalog/course/preview, barcha darslar, vazifalar/lablar, code playground, notes, jadval/live, natijalar/badge/reyting, sertifikat, checkout/billing, referral, notification, help/ticket va account settings. Xodim ekranlari ham manbadagi rolga mos oqimlar sifatida reyestrda qoladi; native yoki xavfsiz responsive web ko'rinishidan foydalanish har ekran bo'yicha matritsada kelishiladi, jim tushirib qoldirilmaydi.

Mobil bottom navigation va safe area, screen reader/dynamic text, orientatsiya, keyboard/file picker, clipboard/share sheet va permissions xatolari qo'llanadi. Manbada mobil tabbar matni bilan hozirgi kodda Kalendar/Natijalar farqi bor; taklif: asosiy talaba tablari Panel/Kurslar/Vazifalar/Natijalar/Menyu, kalendar menyudan; product tasdiqlaydi. Browserdagi Ctrl+K/keyboard shortcutning telefonda aynan takrorlanishi talab emas, tegishli search/touch amali bo'ladi.

Minimal OS, qurilma matritsasi va ilovalar texnologiyasi D-15; backend umumiy, UI clientlari bilan birga OpenAPI asosida. Build/signing, test distribution, release artifact va privacy metadata topshiriladi; tarqatish kanali/to'lov mexanizmi mobil reliz oldidan tasdiqlanadi. Native xarid bo'lsa purchase verification/restore/renewal adapteri alohida billing scope sifatida yoziladi; web payment callbacki bilan taxminan almashtirilmaydi.

#### P2. Mobil autentifikatsiya va deep link

- Mobil token/sessiya OSning himoyalangan storage'ida, log/analytics/URLda emas. Taklif: mobil uchun rotatsiyali opaque refresh token, qisqa access token va device sessiyasi; webdagi cookie sessiyasi saqlanadi. Revoke/2FA/trust siyosati ikkala clientga bir xil.
- OAuth external user-agent orqali tekshirilgan callback, SMS/OTP autofill mumkin; clipboarddan kod o'qish majburiy emas. Biometrik unlock qo'shilsa server 2FA o'rnini bosmaydi, alohida ixtiyoriy feature.
- Deep linklar course/lesson/time, certificate verify, live, ticket va notification uchun yagona registry; public HTTPS link va mobil app linklar bir obyektga boradi.
- Logout holatida login→2FA→ruxsat tekshiruvi→maqsad sahifa. Begona ticket yoki accessi yopiq dars deep link bilan ochilmaydi. Linkdagi arbitrary external URLga redirect yo'q.
- Ilova o'rnatilmagan bo'lsa HTTPS fallback; obyekt o'chgan/versiyasi eskirgan bo'lsa tushunarli holat. Mobil eski client uchun API compatibility/minimum supported version siyosati.

#### P3. Push va qurilma reyestri

DeviceRegistration: user, installation ID, platform, provider token, locale/timezone, app version, opt-in va last_seen. OS ruxsati user kontekstni tushungach so'raladi; rad etilganda in-app xabarlar ishlaydi. Bir device boshqa userga o'tsa eski ownerdan uziladi. Logout/revoke/delete token bindingni bekor qiladi; invalid token provider javobidan tozalanadi.

Push payload minimal: event ID/type va xavfsiz deep link; OTP, karta yoki vazifa private matni lock screenda default chiqmaydi. Xabar foreground/background/terminated holatlarda mos ochiladi, ikki marta bosilganda mutatsiya dublikat qilinmaydi. Delivered yoki click alohida telemetry, push yuborilishi user o'qidi degani emas. App prefs + OS permission + quiet hours + marketing consent kesishmasi qo'llanadi.

#### P4. Himoyalangan video download va offline sync

- Ruxsatli video uchun sifat/hajm, bo'sh joy, Wi-Fi-only afzalligi, progress/pause/resume/cancel/delete va downloadlar ro'yxati. Subtitr va dars metadata ham qo'shiladi.
- Fayl public gallery/sharega chiqmaydigan private storage'da; media imkoniyatiga mos shifrlash va muddati cheklangan offline license. Har download user/device/course versionga bog'lanadi.
- License muddati D-15da tasdiqlanadi; taklif 7 kun, online tekshiruvdan so'ng entitlement faol bo'lsa yangilanadi. Offline holatda access revoke darhol yetib bormasligi UX va siyosatda aniq: eng kechi license expiryda yopiladi. Mutlaq darhol revoke va to'liq offline ko'rish bir vaqtda va'da qilinmaydi.
- Online bo'lganda obuna/course expiry, block/delete/logout tekshirilib key/token va yuklangan kontent cleanup qilinadi. User almashtirishda oldingi download ochilmaydi; ilova uninstall/cache cleanup holati xato bermaydi.
- Offline playback watch interval, timestamp notes va draftlar event ID bilan lokal navbatga tushadi; qayta ulanganda vaqt/version/entitlement/dedupe qoidalari qo'llanadi. Offline certificate/XP yakuniy deb e'lon qilinmaydi, server syncdan keyin tasdiqlanadi.
- Quiz final submission, graded code, homework final submit, lab va live online talab qiladi. Offline qo'yilgan qayd/kod drafti shu cheklovni chetlab o'tmaydi.
- Offline notes create/delete conflict: taklif optimistic version+tombstone; boshqa qurilmadagi yangilangan yozuv jim o'chirilmaydi. Downloaded eski course versiyasi uchun metadata migration yoki qayta download taklifi.

#### P5. Backend, QA va topshirish qo'shimchasi

Entitylar: `DeviceRegistration`, `MobileSession`, `PushDelivery`, `DownloadGrant`, `OfflineLicense`, `SyncEvent`, `ClientCompatibilityPolicy`.

API: `POST/PATCH/DELETE /me/devices/{id}`, `GET /client-config`, `POST /mobile-sessions/refresh`, `POST /lessons/{id}/download-grants`, `POST /offline-licenses/{id}/renew`, `POST /me/sync-events`, `GET /me/sync?cursor=...`. Har biri owner, version, quota, license/access, replay/rate va retention tekshiruvi bilan. API-48–API-54 sifatida OpenAPIga kiritiladi. Push token ro'yxati public user responsega kirmaydi.

| ID | Mobil qabul ssenariysi |
|---|---|
| QA-P01 | Har kelishilgan ekran iOS/Android/webda actor/oqim bo'yicha mavjud; safe area, katta text va screen reader tekshirilgan |
| QA-P02 | Cold/warm start deep link, app yo'q fallback, login/2FA return va permission rad holatlari |
| QA-P03 | Push ruxsati rad/yoqilgan/token rotate/logout boshqa user → xabar noto'g'ri akkauntga bormaydi |
| QA-P04 | 22:59/23:00/07:59/08:00 quiet, digest dushanba, timezone o'zgarishi → kechiktirish va dedupe to'g'ri |
| QA-P05 | Offline video download pause/resume, kam xotira, license expiry va user switch → xavfsiz/tushunarli holat |
| QA-P06 | Offline progress/note sync bir event 3 marta → bitta natija; eski versiya/conflict ko'rsatiladi |
| QA-P07 | Entitlement revoke/expiry, block/delete/logout → online license yangilanmaydi, local kontent siyosatga mos yopiladi |
| QA-P08 | Eski client/new API compatibility, background/foreground qaytishi va device sessiya revoke ishlaydi |

Mobil release artifact, signing/config yo'riqnomasi, ekran parity matritsasi, push va offline test dalili yakuniy topshirish paketiga qo'shiladi. Mobil ilovalar scope'dan chiqarilsa D-15 qarori va reliz jadvalida aniq yoziladi.

### Q. Vakolat va holat o'tishlari uchun yakuniy matritsa

#### Q1. Role → permission

Belgilar: **O'z** — shaxsiy obyekt, **Birikt.** — biriktirilgan kurs/guruh, **Vakolat** — alohida permission/tekshiruv bilan, **Ha** — rolning asosiy vakolati, **Yo'q** — shu rolning o'zi yetarli emas. Bir userdagi rollar yig'iladi; explicit blok va obyekt cheklovi baribir ustun. Superadmin admin vakolatlarini meros oladi.

| Amal | Talaba | Mentor | Muallif | Support | Admin | Superadmin |
|---|---|---|---|---|---|---|
| Profil/settings/private notes | O'z | O'z | O'z | O'z | O'z | O'z |
| Kurs o'qish | Entitlement | Entitlement / Birikt. preview | Entitlement / O'z preview | Entitlement | Vakolatli preview | Vakolatli preview |
| To'lov qilish | O'z | O'z talaba roli bilan | O'z talaba roli bilan | Yo'q | Yo'q | Yo'q |
| Homework review/line comment | Yo'q | Birikt. | Yo'q | Yo'q | Ha | Ha |
| Mentor sifatida QA javobi | Yo'q | Birikt. | O'z kursi | Yo'q | Ha | Ha |
| Extension/attempt allowance | Yo'q | Birikt. | Yo'q | Yo'q | Ha | Ha |
| Kurs yaratish/tahrirlash | Yo'q | Muallif roli kerak | O'z | Yo'q | Ha | Ha |
| Kurs/sharh publish/moderate | Yo'q | Yo'q | Yo'q | Yo'q | Ha | Ha |
| Ticketga staff javobi | Yo'q | Yo'q | Yo'q | Birikt. | Ha | Ha |
| Talabani block/unblock | Yo'q | Yo'q | Yo'q | Vakolat | Ha, peer admin emas | Vakolat, last-admin himoyasi |
| Refund/promo boshqarish | Yo'q | Yo'q | Yo'q | Yo'q | Vakolat+reauth | Vakolat+reauth |
| Sertifikat revoke/reissue | Yo'q | Yo'q | Yo'q | Yo'q | Vakolat | Vakolat |
| Read-only impersonation | Yo'q | Yo'q | Yo'q | Vakolat | Vakolat | Vakolat |
| Manual grant/revoke | Yo'q | Yo'q | Yo'q | Alohida vakolat bo'lsa | Vakolat | Vakolat |
| 2FA recovery/manual verify | Yo'q | Yo'q | Yo'q | Recovery vakolati bo'lsa | Recovery vakolati bo'lsa | Vakolat |
| Mentor/author/support roli berish | Yo'q | Yo'q | Yo'q | Yo'q | Cheklangan vakolat | Ha |
| Admin/superadmin roli berish | Yo'q | Yo'q | Yo'q | Yo'q | Yo'q | Ha, last-admin himoyasi |
| Platforma settings/secrets | Yo'q | Yo'q | Yo'q | Yo'q | Faqat ruxsatli health o'qish | Ha |
| Audit ko'rish | Yo'q | Yo'q | Yo'q | O'z case doirasida ruxsatli bo'lsa | Ha | Ha |

Bu matritsa manbadagi role jadvalini obyekt scope va production recovery huquqlari bilan aniqlashtiradi. `support` va `superadmin` ayrim route'larda alohida ko'rsatilmaganligi ularning permissionini yo'qotish yoki barcha huquqni berish uchun asos emas. Yakuniy permission seed, admin UI va OpenAPI shu matritsadan olinadi; backend negative testlari har bir taqiqlangan katakni qoplaydi.

#### Q2. State machine va side-effect

| Obyekt | Ruxsatli o'tish | Kim/dalil | Atomik natija |
|---|---|---|---|
| Course | draft/rejected → review → published yoki rejected | Muallif yuboradi, moderator qarori | Version snapshot, audit, xabar; narx/asset validatsiya |
| Course visibility | published → hidden; hidden → published | Admin, nashr talablari | Yangi sotuv/search o'zgaradi; avvalgi entitlement alohida |
| Entitlement | scheduled → active → expired/suspended/revoked; suspended → active | Vaqt/payment/manual reason | Shu access manbai, permission cache va bog'liq sessiya resurslari |
| Quiz | in_progress → submitted/timed_out → graded; zarur bo'lsa void | User/server deadline/admin reason | Answer snapshot, score, best, completion/XP bir marta |
| Submission | submitted → review → accepted/returned | Test job + biriktirilgan reviewer | Rubric/penalty snapshot, completion/XP va notification |
| Extension | pending → approved/rejected | Biriktirilgan mentor/admin | Deadline version yoki rad sababi, audit |
| Lab | requested → provisioning → running → stopping → stopped/expired; failure → failed | Owner/orchestrator/scheduler | Quota, real resource va cleanup holati mos |
| Order | pending → paid/failed/cancelled/expired | Provider dalili; expired success reconciliation bilan | Payment va access; unknown holatni yashirmaslik |
| PaymentAttempt | created → processing → succeeded/failed/unknown; unknown → reconciled natija | Provider status | Charge idempotency, obligation paid amount, receipt outbox |
| Subscription | active → past_due → grace → suspended; paid → active; no-renew → expired | Period va haqiqiy charge | Davr va ruxsat manbai; progress saqlanadi |
| Installment | scheduled → due → processing → paid; fail → past_due/grace/suspended | Obligation/job/provider | Qoldiq, keyingi sana va source access |
| Refund | requested → approved/processing → succeeded/failed/unknown; requested → rejected | Vakolatli xodim+provider | Successdagina refunded amount/access update |
| Review | pending → approved/rejected; rejected edit → pending | User/moderator | Faqat approved agregat rating, audit |
| Ticket | open ↔ waiting; →resolved →closed; reopen policy bilan | User/staffga mos transition | Message visibility, assignee, SLA/audit/xabar |
| Certificate | eligible → issuing → issued → revoked; correction → yangi linked issue | Completion job/admin reason | Unikal code/PDF/XP; public verify real holat |
| Delivery | queued/deferred → sending → sent/delivered/failed/suppressed | Pref/quiet/provider | Dedupe va secret redaction |
| Account | active → blocked/deleting; deleting → active/deleted | Vakolatli actor/grace job | Sessiya/token, auto-renew va anonimlashtirish siyosati |
| Offline download | queued → downloading → ready/failed/paused → expired/deleted | Owner/device/license | Private media va license; sync replaydan mustaqil |

Noqonuniy o'tish 409/domain error; client status nomini yuborib holatni erkin o'zgartira olmaydi. Audit/notification side-effectining xatosi payment yoki bahoni qayta takrorlashga sabab bo'lmaydi; outbox retry ishlaydi.

### R. Ishlar ketma-ketligi va to'liq loyiha chegarasi

| Paket | Old shart | FE/mobile | Backend/infratuzilma | Qabul dalili |
|---|---|---|---|---|
| Foundation | D-11, boshlang'ich dizayn/API qarori | Shell/UI/i18n/auth ekranlari | DB/auth/role/session/log/muhitlar | QA-A va permission negative |
| Content | Foundation | Katalog/course/construktor | Course version/media/entitlement | Publish/preview/access testlari |
| Learning | Content | Video/text/quiz/homework/notes | Progress/attempt/submission/review | QA-B, E1 |
| Commerce | Foundation+provider credentials | Quote/checkout/billing/refund | Provider adapter/billing/outbox/fiscal | QA-D sandbox dalillari |
| Operations | Learning+Commerce | Mentor/support/admin/analytics | SLA/report/moderation/audit/reconciliation | QA-I/K |
| Practice | Foundation+alohida klaster | Code/lab/terminal/playground | Sandbox/provision/TTL/quota | QA-B07/C va capacity |
| Community/live | Content+room provider | QA/review/live/calendar/rewards | Live tokens/recording/notifications | QA-E/G/H |
| Native/offline | API+media policy+D-15 | iOS/Android ekran parity/download | Device/push/license/sync | QA-P, build/signing dalili |
| Release | Barcha tanlangan paketlar | Responsive/a11y/locale/E2E | Backup/restore/monitor/deploy | QA-L va O checklist |

Modullarni parallel bajarish jamoaning ichki rejasida yuqoridagi bog'liqliklar bilan tuziladi. Baholashda har paket uchun FE, BE, mobil, QA, infratuzilma va kontent mehnati alohida yoziladi; muddat va narx jamoa resursi hamda tasdiqlangan scope asosida belgilanadi.

Manbada bo'lmagan va alohida kelishuvsiz scopega kirmaydigan mahsulotlar: bank hisoblari/transfer, mualliflarga marketplace payout, talaba pul hamyoni, e-commerce cart, korporativ multitenancy, SCORM/xAPI integratsiyasi, AI tutor, ishga joylashtirish/job board. Ular LMS nomi yoki kurs mavzusidan taxmin qilinmaydi. HTMLdagi barcha qayd etilgan asosiy imkoniyatlar esa qamrov reyestri va ushbu ilovada qoladi; chiqarib tashlash faqat requirement ID bilan ochiq scope qarori orqali.

---

<a id="qamrov"></a>

## 3-qism. HTML bilan qamrov reyestri

Manba: `fintechhub.html`; SHA-256: `ff09d41a6d9238e62d0e378a9075b644772d3da2e6e43d96df13da5109d9b70d`.

Usul: HTML matn sifatida o'qildi; route, SCREENS, FORMS/ACTIONS reyestrlari va qayta yozilgan handlerlar ajratildi. JavaScript bajarilmadi. Qatorlar asl HTMLga tegishli. Bir nechta ta'rif bo'lsa eng oxirgisi yoki oxirgi wrapper ishlaydi; eski ta'rif alohida yangi feature hisoblanmaydi.

Bu implementatsiya/test o'tdi degan hisobot emas. Har qator manba imkoniyatining TZdagi joyini ko'rsatadi; demo va legacy alohida qayd etilgan. Har yangi relizda FE/BE/QA statusi alohida yuritiladi.

| Element | Soni |
|---|---|
| Unikal route | 44 |
| Admin view | 12 |
| Unikal forma handleri | 35 |
| Unikal action handleri | 173 |
| SCREENSdagi namuna/variant yozuvi | 73 |

### 1. Sahifa variantlari — SCREENS

Bir routega tegishli tab va turli foydalanuvchi variantlari ham ro'yxatda saqlandi. `u1/u6` talaba, `u2` mentor/muallif, `u3` admin, guest/null ommaviy yoki autentifikatsiya konteksti.

| Namuna yo'l | Sahifa/variant | Demo actor | TZ / ilova bandi | Manba qatori |
|---|---|---|---|---|
| `home` | Bosh sahifa (landing) | null | FE-02; F3 | 4957 |
| `kurslar` | Kurslar katalogi: qidiruv, filtr, saralash | null | FE-02; F1 | 4957 |
| `kurs-py` | Kurs sahifasi: dastur, preview, sharhlar | null | FE-02; B1; E1 | 4957 |
| `narxlar` | Narxlar va Pro obuna | null | FE-06; D1 | 4957 |
| `tekshir` | Sertifikatni tekshirish (QR) | null | BE-09; E3 | 4957 |
| `tekshir-FTH-2026-104233` | Tekshirish natijasi — haqiqiy | null | BE-09; E3 | 4957 |
| `tekshir-FTH-2026-099512` | Tekshirish natijasi — bekor qilingan | null | BE-09; E3 | 4957 |
| `yordam` | Yordam markazi (FAQ) | null | FE-02; I2 | 4957 |
| `hujjat-oferta` | Huquqiy sahifalar (oferta, maxfiylik, qaytarish, cookie) | null | FE-02; F3 | 4957 |
| `profil-aziza_sec` | Talabaning ochiq profili | null | FE-10; E2 | 4957 |
| `kirish` | Kirish: email/parol, SMS, OAuth, CAPTCHA, bloklash | guest | FE-03; A3 | 4958 |
| `royxat` | Ro‘yxatdan o‘tish + parol kuchi | guest | FE-03; A1 | 4958 |
| `royxat-AZIZA10` | Taklif havolasi bilan ro‘yxat | guest | FE-03; A1 | 4958 |
| `tasdiqlash` | Email tasdiqlash (OTP) | guest | R-OTP; A3 | 4958 |
| `parol` | Parolni tiklash (3 bosqich) | guest | R-AUTH; A3 | 4958 |
| `ikki` | 2FA tekshiruvi (login → mentor) | guest | R-2FA; A3 | 4958 |
| `panel` | Bosh panel: davom ettirish, checklist, streak, maqsad | u1 | FE-04; E4; I1 | 4959 |
| `kurslarim` | Kurslarim (o‘qilmoqda, tugallangan, sevimlilar) | u1 | FE-04; B1; E1 | 4959 |
| `dars-py-py4` | Video dars: boblar, subtitr, qaydlar, transkript | u1 | FE-05; B; C; E1 | 4959 |
| `dars-py-py6` | Matn darsi + savol-javob | u1 | FE-05; B; C; E1 | 4959 |
| `dars-py-py3` | Test (aralashtirish, taymer, navigator) | u1 | FE-05; B; C; E1 | 4959 |
| `dars-py-py5b` | Kod mashqi — Python (Skulpt) | u1 | FE-05; B; C; E1 | 4959 |
| `dars-py-py5` | Uyga vazifa: tarix, kod izohlari, muddat uzaytirish | u1 | FE-05; B; C; E1 | 4959 |
| `dars-web-web4` | CTF lab: terminal, flag, maslahatlar | u1 | FE-05; B; C; E1 | 4959 |
| `dars-web-web6` | Hisobot turidagi vazifa | u1 | FE-05; B; C; E1 | 4959 |
| `jadval` | Kalendar: muddatlar, jonli darslar, to‘lovlar | u1 | FE-04; H | 4959 |
| `vazifalar` | Uyga vazifalar ro‘yxati | u1 | FE-04; B6 | 4959 |
| `lablar` | Lablar ro‘yxati | u1 | FE-04; C | 4959 |
| `playground` | Kod playground (JS + Python) | u1 | FE-05; B5 | 4959 |
| `qaydlar` | Qaydlar va saqlangan darslar | u1 | FE-04; E1 | 4959 |
| `natijalar` | Natijalarim: grafiklar (vaqt, testlar, kurslar, baholar) | u1 | FE-04; E4 | 4959 |
| `sertifikatlar` | Sertifikatlar | u1 | FE-04; E3 | 4959 |
| `sertifikat-FTH-2026-104233` | Sertifikat (QR, LinkedIn) | u1 | BE-09; E3 | 4959 |
| `yutuqlar` | Yutuqlar: daraja, nishonlar, XP tarixi | u1 | FE-04; E2 | 4959 |
| `reyting` | Reyting (hafta, umumiy, kurs bo‘yicha) | u1 | FE-04; E2 | 4959 |
| `tolov-js` | Checkout: reja, karta, usul, promo | u1 | FE-06; D2 | 4959 |
| `tolovlar` | To‘lovlar: buyurtmalar, cheklar, qaytarish | u1 | FE-06; D | 4959 |
| `tolovlar-obuna` | Pro obuna boshqaruvi | u1 | FE-06; D | 4959 |
| `tolovlar-kartalar` | Saqlangan kartalar | u1 | FE-06; D | 4959 |
| `taklif` | Do‘stlarni taklif qilish | u1 | R-REF; D5 | 4959 |
| `xabarlar` | Bildirishnomalar | u1 | BE-10; G2 | 4959 |
| `murojaat-t1001` | Support murojaati (yozishma) | u1 | FE-09; I2 | 4959 |
| `sozlamalar` | Sozlamalar: profil, telefon, email | u1 | FE-10; A; F; G2 | 4959 |
| `sozlamalar-xavfsizlik` | Xavfsizlik: parol, 2FA (QR), sessiyalar, tarix | u1 | FE-10; A; F; G2 | 4959 |
| `sozlamalar-xabarnoma` | Bildirishnomalar va Telegram | u1 | FE-10; A; F; G2 | 4959 |
| `sozlamalar-interfeys` | Til, mavzu, o‘qish sozlamalari | u1 | FE-10; A; F; G2 | 4959 |
| `sozlamalar-malumot` | Eksport va akkauntni o‘chirish | u1 | FE-10; A; F; G2 | 4959 |
| `tolovlar-bolib` | Bo‘lib to‘lash jadvali (Sardor) | u6 | FE-06; D | 4960 |
| `panel` | Bosh panel — boshqa talaba | u6 | FE-04; E4; I1 | 4960 |
| `panel` | Xodim paneli | u2 | FE-04; E4; I1 | 4961 |
| `mentor` | Tekshirish navbati, muddat so‘rovlari, savollar | u2 | FE-07; I1 | 4961 |
| `tekshirish-s2` | Topshiriqni tekshirish: rubrika, kod qatoriga izoh | u2 | FE-07; B6 | 4961 |
| `tekshirish-s5` | Plagiat shubhasi (81%) | u2 | FE-07; B6 | 4961 |
| `guruhlar` | Guruhlarim: xavf ostidagi talabalar | u2 | FE-07; I1 | 4961 |
| `muallif` | Muallif paneli | u2 | FE-08; B1 | 4961 |
| `konstruktor-py` | Kurs konstruktori (barcha dars turlari) | u2 | FE-08; B2 | 4961 |
| `konstruktor-new` | Yangi kurs yaratish | u2 | FE-08; B2 | 4961 |
| `kursstat-py` | Kurs analitikasi: darslar bo‘yicha o‘tish | u2 | FE-08; E4 | 4961 |
| `admin` | Umumiy ko‘rinish: daromad, voronka, diqqat talab qiladi | u3 | FE-09; I3; I4 | 4962 |
| `admin-users` | Foydalanuvchilar (filtrlar) | u3 | FE-09; I3; I4 | 4962 |
| `admin-user-u4` | Foydalanuvchi kartasi + impersonatsiya | u3 | FE-09; I3; I4 | 4962 |
| `admin-courses` | Kurslar va moderatsiya | u3 | FE-09; I3; I4 | 4962 |
| `admin-payments` | To‘lovlar va qaytarish so‘rovlari | u3 | FE-09; I3; I4 | 4962 |
| `admin-support` | Murojaatlar navbati (SLA) | u3 | FE-09; I3; I4 | 4962 |
| `admin-promo` | Promo-kodlar | u3 | FE-09; I3; I4 | 4962 |
| `admin-certs` | Sertifikatlar va bekor qilish | u3 | FE-09; I3; I4 | 4962 |
| `admin-settings` | Tizim sozlamalari, feature flags, shablonlar | u3 | FE-09; I3; I4 | 4962 |
| `admin-roles` | Rollar va ruxsatlar matritsasi | u3 | FE-09; I3; I4 | 4962 |
| `admin-audit` | Audit jurnali | u3 | FE-09; I3; I4 | 4962 |
| `mavjud-emas` | 404 — sahifa topilmadi | null | FE-01; F1 (404 ssenariysi) | 4963 |
| `admin` | 403 — ruxsat yo‘q (talaba sifatida) | u1 | FE-09; I3; I4 | 4963 |
| `texnik` | Texnik ishlar sahifasi | null | FE-01; I4 | 4963 |
| `dizayn` | Dizayn tizimi (UI kit) | null | F2; O (UI kit) | 4963 |

### 2. Route reyestri

| Element | TZ / ilova bandi | Ta'rif qatorlari (oxirgisi ustuvor) |
|---|---|---|
| `403` | FE-01; A; F1 | 2415 |
| `404` | FE-01; F1 | 2416 |
| `admin` | FE-09; I3; I4 | 2903 |
| `dars` | FE-05; B; C; E1 | 4096 |
| `dizayn` | F2; O (UI kit) | 4972 |
| `ekranlar` | F2; O (staging handoff) | 4965 |
| `guruhlar` | FE-07; I1 | 4656 |
| `home` | FE-02; F3 | 2168 |
| `hujjat` | FE-02; F3 | 4523 |
| `ikki` | R-2FA; A3 | 2404 |
| `jadval` | FE-04; H | 4433 |
| `kirish` | FE-03; A3 | 2325 |
| `konstruktor` | FE-08; B2 | 4812 |
| `kurs` | FE-02; B1; E1 | 2228 |
| `kurslar` | FE-02; F1 | 2204 |
| `kurslarim` | FE-04; B1; E1 | 4084 |
| `kursstat` | FE-08; E4 | 5774 |
| `lablar` | FE-04; C | 2661 |
| `mentor` | FE-07; I1 | 2852, 4594 |
| `muallif` | FE-08; B1 | 4672 |
| `murojaat` | FE-09; I2 | 4505 |
| `narxlar` | FE-06; D1 | 2265 |
| `natijalar` | FE-04; E4 | 5715 |
| `panel` | FE-04; E4; I1 | 4049 |
| `parol` | R-AUTH; A3 | 2384 |
| `playground` | FE-05; B5 | 4316 |
| `profil` | FE-10; E2 | 4454 |
| `qaydlar` | FE-04; E1 | 4410 |
| `reyting` | FE-04; E2 | 4393 |
| `royxat` | FE-03; A1 | 2351 |
| `sertifikat` | BE-09; E3 | 4381 |
| `sertifikatlar` | FE-04; E3 | 2830 |
| `sozlamalar` | FE-10; A; F; G2 | 4584 |
| `taklif` | R-REF; D5 | 4468 |
| `tasdiqlash` | R-OTP; A3 | 2370 |
| `tekshir` | BE-09; E3 | 2278 |
| `tekshirish` | FE-07; B6 | 2871, 4622 |
| `texnik` | FE-01; I4 | 4527 |
| `tolov` | FE-06; D2 | 2702 |
| `tolovlar` | FE-06; D | 4336 |
| `vazifalar` | FE-04; B6 | 2647 |
| `xabarlar` | BE-10; G2 | 2840 |
| `yordam` | FE-02; I2 | 4495 |
| `yutuqlar` | FE-04; E2 | 4445 |

### 3. Admin viewlar

| Element | TZ / ilova bandi | Ta'rif qatorlari (oxirgisi ustuvor) |
|---|---|---|
| `audit` | BE-11; J1 | 2985, 4945 |
| `builder` | B2 (legacy redirect) | 2950, 4864 |
| `certs` | E3 | 2980 |
| `courses` | B2; I3 | 2945, 4902 |
| `overview` | FE-09; E4 | 2905, 4829 |
| `payments` | D2; D4 | 2963 |
| `promo` | D5 | 2974 |
| `roles` | A; I3 | 4938 |
| `settings` | I4 | 4925 |
| `support` | I2 | 4912 |
| `user` | I3 | 4879 |
| `users` | FE-09; I3 | 2932, 4868 |

### 4. Formalar

| Element | TZ / ilova bandi | Ta'rif qatorlari (oxirgisi ustuvor) |
|---|---|---|
| `2fa-enable` | A3 | 3306, 5105 |
| `builder` | B2 (legacy konstruktor) | 3340 |
| `change-pw` | A3 | 3296, 5137 |
| `course-review` | E1 | 3164, 5156 |
| `delete-account` | A5 | 3313, 5147 |
| `email-change` | A3 | 3279 |
| `email-confirm` | A3 | 3289 |
| `ethics` | C | 3201 |
| `forgot-email` | A3 | 3118 |
| `forgot-reset` | A3 | 3130 |
| `homework` | B6 | 3183, 5217 |
| `lab-flag` | C | 3216 |
| `lb-privacy` | E2 | 3263, 5164 |
| `line-comment` | B6 | 5178 |
| `login` | A3 | 3053, 5018 |
| `note` | E1 | 5171 |
| `phone-send` | A3 | 5122 |
| `phone-verify` | A3 | 5131 |
| `profile` | A2 | 3269, 5112 |
| `promo` | D5 | 3256 |
| `promo-create` | D5 | 3360 |
| `qa-ask` | E1 | 3240 |
| `qa-reply` | E1 | 3248 |
| `quiz` | B4 | 3171, 5208 |
| `register` | A1; A2 | 3081, 5046 |
| `review` | B6 | 3322 |
| `sms-send` | A3 | 5080 |
| `sms-verify` | A3 | 5091 |
| `term` | C | 3205 |
| `ticket-new` | I2 | 5184 |
| `ticket-reply` | I2 | 5197 |
| `top-search` | F1 | 3051 |
| `twofa` | A3 | 3150, 5066 |
| `verify-cert` | E3 | 3052 |
| `verify-email` | A3 | 3099 |

### 5. Amallar

| Element | TZ / ilova bandi | Ta'rif qatorlari (oxirgisi ustuvor) |
|---|---|---|
| `2fa-backup` | A3; A4 | 3524 |
| `2fa-cancel` | A3; A4 | 3523 |
| `2fa-disable` | A3; A4 | 3525, 5351 |
| `2fa-setup` | A3; A4 | 3522, 5350 |
| `admin-range` | I3; I4; E4 | 5377 |
| `assign-tab` | B6; F1 | 3494 |
| `b-add-lesson` | B2; I3 | 3551 |
| `b-add-module` | B2; I3 | 3549 |
| `b-del-lesson` | B2; I3 | 3552 |
| `b-del-module` | B2; I3 | 3550 |
| `bld-add-les` | B2; I3 | 5402 |
| `bld-add-mod` | B2; I3 | 5400 |
| `bld-check` | B2; I3 | 5440 |
| `bld-del-les` | B2; I3 | 5403 |
| `bld-del-mod` | B2; I3 | 5401 |
| `bld-move` | B2; I3 | 5404 |
| `bld-opt-add` | B2; I3 | 5436 |
| `bld-opt-del` | B2; I3 | 5437 |
| `bld-publish` | B2; I3 | 5443 |
| `bld-q-add` | B2; I3 | 5434 |
| `bld-q-del` | B2; I3 | 5435 |
| `bld-r-add` | B2; I3 | 5438 |
| `bld-r-del` | B2; I3 | 5439 |
| `bld-save` | B2; I3 | 5441 |
| `bld-sel` | B2; I3 | 5399 |
| `bld-submit` | B2; I3 | 5442 |
| `bld-upload` | B2; I3 | 5417 |
| `bookmark` | E1 | 5301 |
| `cal-move` | H | 5306 |
| `cancel-2fa` | A3 | 3441 |
| `cancel-delete` | A5 | 3418 |
| `card-add` | D | 5329 |
| `card-default` | D | 5348 |
| `card-del` | D | 5349 |
| `cat-reset` | F1 | 3420 |
| `cat-track` | F1 | 3419 |
| `cert-revoke` | E3 | 3562 |
| `checklist-hide` | A1 | 5304 |
| `code-reset` | B5 | 3473 |
| `code-run` | B5 | 3454, 5280 |
| `code-test` | B5 | 3461, 5288 |
| `cookie` | F3 | 5267 |
| `cookie-reset` | F3 | 5268 |
| `copy` | F2 | 3521 |
| `copy-code` | F2; B3 | 5571 |
| `course-price` | B2; I3 | 3548 |
| `course-status` | B2; I3 | 3547 |
| `csv-copy` | D4 | 3561 |
| `drawer-close` | 14.2; F2; O (demo/staging) | 3395 |
| `drawer-open` | 14.2; F2; O (demo/staging) | 3394 |
| `drawer-tab` | 14.2; F2; O (demo/staging) | 3396 |
| `email-cancel` | A3 | 3532 |
| `export-data` | A5 | 3533, 5367 |
| `ext-approve` | B6 | 5324 |
| `ext-open` | B6 | 5314 |
| `ext-reject` | B6 | 5325 |
| `fav` | E1 | 5302 |
| `file-tab` | B6 | 5310 |
| `fill-demo` | 14.2; F2; O (demo/staging) | 3422 |
| `forgot-done` | A3; A4 | 3440 |
| `forgot-restart` | A3; A4 | 3439 |
| `freeze` | E2 | 5305 |
| `goal-edit` | A2; E4 | 3493 |
| `grant-course` | I3 | 5387 |
| `imp-start` | I3 | 5383 |
| `imp-stop` | I3 | 5384 |
| `lab-extend` | C | 3481 |
| `lab-hint` | C | 3482 |
| `lab-start` | C | 3474 |
| `lab-stop` | C | 3480 |
| `lb-tab` | E2 | 3495 |
| `lc-cancel` | B6 | 5312 |
| `lc-del` | B6 | 5313 |
| `lc-open` | B6 | 5311 |
| `link-oauth` | A3; A4 | 5358 |
| `live-join` | H | 5308 |
| `login-tab` | A3; F1 | 5262 |
| `logout` | A3 | 3410 |
| `ltab` | B3; E1 | 5264 |
| `mail-back` | 14.2; F2; O (demo/staging) | 3398 |
| `mail-filter` | 14.2; F2; O (demo/staging) | 5265 |
| `mail-open` | 14.2; F2; O (demo/staging) | 3397 |
| `mentor-filter` | I1 | 3540 |
| `mentor-tab` | I1 | 5326 |
| `menu` | F1 | 5255 |
| `mod-approve` | B2; I3 | 5379 |
| `mod-reject` | B2; I3 | 5380 |
| `modal-btn` | F1; F2 | 3393 |
| `modal-close` | F1; F2 | 3392 |
| `msg-student` | I1 | 5327 |
| `note-del` | E1 | 5303 |
| `notif-all-read` | G2 | 3491 |
| `notif-open` | G2 | 3490 |
| `notif-tab` | G2 | 3492 |
| `oauth` | A4 | 3423 |
| `oauth-pick` | A4 | 3430 |
| `open-mail` | 14.2; F2; O (demo/staging) | 3399 |
| `palette` | F1; F2 | 5256 |
| `palette-close` | F1; F2 | 5257 |
| `palette-go` | F1; F2 | 5258 |
| `pay-debt` | D | 5328 |
| `pay-open` | D | 3504 |
| `pay-start` | D | 3496 |
| `pg-lang` | B5 | 5300 |
| `phone-cancel` | A3 | 5357 |
| `promo-remove` | D | 3505 |
| `pw-toggle` | A2; F2 | 3421 |
| `qa-reply-open` | E1 | 3487 |
| `qa-report` | E1 | 3489 |
| `qa-resolve` | E1 | 3488 |
| `qa-vote` | E1 | 3486 |
| `quick-login` | 14.2; F2; O (demo/staging) | 3400 |
| `quiz-jump` | B4 | 5279 |
| `quiz-start` | B4 | 3453, 5271 |
| `rail-toggle` | F1; F2 | 3443 |
| `receipt` | D4 | 3506 |
| `refund-approve` | D | 3553 |
| `refund-open` | D | 3507 |
| `refund-reject` | D | 3560 |
| `resend-verify` | A3 | 3411 |
| `reset-demo` | 14.2; F2; O (demo/staging) | 3401 |
| `rev-approve` | B2; I3 | 5381 |
| `rev-reject` | B2; I3 | 5382 |
| `revoke-course` | I3 | 5388 |
| `rsvp` | H | 5307 |
| `screen-go` | 14.2; F2; O (demo/staging) | 5389 |
| `sess-revoke` | A3; A4 | 3530 |
| `sess-revoke-all` | A3; A4 | 3531 |
| `set-lang` | F3 | 5261 |
| `set-return` | A1 | 3442 |
| `set-theme` | F2 | 5260 |
| `show-files` | B6 | 5309 |
| `side-close` | F1; F2 | 3409 |
| `side-open` | F1; F2 | 3408 |
| `sim-offline` | 14.2; F2; O (demo/staging) | 5266 |
| `skip` | F1 | 5254 |
| `sms-reset` | A3 | 5263 |
| `sub-cancel` | D | 3519 |
| `sub-resume` | D | 3520 |
| `support-filter` | I2 | 5376 |
| `text-done` | B1; B3 | 3452 |
| `tg-connect` | G2 | 5360 |
| `tg-disconnect` | G2 | 5365 |
| `tg-test` | G2 | 5366 |
| `theme` | F2 | 3402, 5259 |
| `ticket-assign` | I2 | 5374 |
| `ticket-close` | I2 | 5375 |
| `toast-act` | F1; F2 | 3391 |
| `tpl` | I1 | 3541 |
| `tpl-preview` | I3; I4; E4 | 5378 |
| `travel` | 14.2; F2; O (demo/staging) | 5269 |
| `travel-reset` | 14.2; F2; O (demo/staging) | 5270 |
| `trust-clear` | A3 | 5356 |
| `uk-confirm` | 14.2; F2; O (demo/staging) | 5397 |
| `uk-modal` | 14.2; F2; O (demo/staging) | 5396 |
| `uk-toast` | 14.2; F2; O (demo/staging) | 5395 |
| `unlink-oauth` | A3; A4 | 5359 |
| `user-2fa-reset` | I3 | 5386 |
| `user-block` | I3 | 3542 |
| `user-pwreset` | I3 | 5385 |
| `user-role` | I3 | 3544 |
| `user-sessions` | I3 | 3545 |
| `user-unblock` | I3 | 3543 |
| `user-verify` | I3 | 3546 |
| `vid-full` | B3; F2 | 5446 |
| `vid-jump` | B3; F2 | 5445 |
| `vid-next` | B3; F2 | 5447 |
| `vid-next-cancel` | B3; F2 | 5448 |
| `vid-seek` | B3; F2 | 3445 |
| `vid-skip` | B3; F2 | 5444 |
| `vid-subs` | B3; F2 | 3451 |
| `vid-toggle` | B3; F2 | 3444 |
| `vz-table` | E4; F2 | 5695 |

### 6. Click/formdan tashqari asosiy triggerlar

| Trigger | Mazmun | TZ / ilova bandi |
|---|---|---|
| `data-catalog` | Qidiruv, daraja/narx/sort filtrlari | F1 |
| `data-co` | Checkout reja/usul/karta/subscription tanlovi | D1–D3 |
| `data-vid` | Player tezlik/sifat | B3 |
| `data-pg` | Playground namuna | B5 |
| `data-pref` | Event/kanal preference | G2 |
| `data-uset` | O'qish/tinch soat/digest/marketing afzalligi | F2; G3 |
| `data-aset` | Feature/provider/maintenance toggle | I4 |
| `data-aset-num` | Referal foizi | I4; D5 |
| `data-role-toggle` | Rol berish/olish | I3 |
| `data-tk-status` | Ticket holati | I2 |
| `data-promo-toggle` | Promo active | D5 |
| `data-admin-f` | User rol/status filtri | I3 |
| `data-apf` | Payment filtri | D4 |
| `data-admin-q` | User qidiruvi | I3 |
| `data-audit-q` | Audit qidiruvi | J1; I4 |
| `data-help-q` | FAQ qidiruvi | I2 |
| `data-notes-q` | Qayd qidiruvi | E1 |
| `data-palette` | Buyruqlar paneli qidiruvi | F1 |
| `data-lb-course` | Kurs reytingi | E2 |
| `data-group-course` | Guruh kursi | I1 |
| `data-author-all` | Admin barcha muallif kurslari ko'rinishi | B1; I3 |
| `data-lang-select` | Til selector | F3 |
| `data-bf` | Konstruktor nested maydonlari | B2 |
| `data-builder` | Eski konstruktor maydonlari, yangi konstruktorga o'tkaziladi | B2; 14.2 |
| `data-builder-mod` | Legacy modul nomi | B2; 14.2 |
| `data-builder-ltitle` | Legacy dars nomi | B2; 14.2 |
| `data-builder-ltype` | Legacy dars turi | B2; 14.2 |
| `data-demo-cardfail` | Faqat demo payment failure | 14.2; O |
| `data-rubric` | Rubrika total/jazo preview | B6 |
| `data-qi` | Javoblangan savol navigatori | B4 |
| `data-editor` | Kod draft/gutter/shortcut | B5 |
| `data-mask` | Telefon/karta/muddat input format | A2; D3 |
| `data-pw-meter` | Parol kuchi | A2 |
| `data-until` | Server sanasiga taymer/expiry | A3; B4; C; D; K |
| `data-nav-more` | Qo'shimcha navigatsiya ochiq/yopiq afzalligi | F1 |
| `data-chart` | Accessible grafik tooltip | E4; F2 |
| `data-vz-line` | Grafik tooltip/crosshair | E4; F2 |

#### Sozlama maydonlari alohida tekshiruvi

| `data-uset` maydoni | TZ / ilova |
|---|---|
| `autoNext` | B3; F2 |
| `digest` | R-DIGEST; G3 |
| `marketing` | G3; F3 |
| `quiet` | R-QUIET; G3; P3 |
| `speed` | B3; F2 |
| `subsDefault` | B3; F2 |

#### Handoff va production izohlaridagi qo'shimcha scope

| Manba joyi / kalit matn | Talab / ilova |
|---|---|
| Har bir ekran web (desktop + mobil), iOS va Android (qator 4968) | R-MOBILE; P1–P5: platforma parity, push, offline video, deep link |
| Tinch soatlar (23:00–08:00) (qator 4571) | R-QUIET; G3: deferred delivery, 08:00 jamlanma |
| Har dushanba: o‘tgan haftadagi progress (qator 4571) | R-DIGEST; G3: haftalik hisobot |
| Prod’da: WebRTC (qator 5308) | H: xona/chat/raise-hand/screen-share/recording |
| Prod: savollar banki (qator 4796) | B2; J2: question bank, random selection, CSV import |
| Prod’da Go, C++ va SQL (qator 4319) | B2/B5; D-13: qo'shimcha runtime adapterlari |
| MP4/MOV · 4 GB (qator 4787) | R-MEDIA; G1: resumable upload va media pipeline |
| Imzolangan HLS URL (5 daq) (qator 4160) | R-VIDEO; B3: playback token, encryption key, watermark |
| STIR va manzil prod’da (qator 2816) | D4; I4: tashkilot rekvizitlari va fiskal integratsiya |

### 7. Demo va production izohlarining talqini

- Demo quick login, email/SMS qutisi, demo authenticator, vaqtni surish, card failure va reset productionda yo'q; ular uchun haqiqiy auth/provider/worker oqimi tegishli A/D/G/K bo'limlarda talab qilingan.
- Eski `builder` va `b-*` actionlari yangi `konstruktor` / `bld-*` bilan bir mahsulot imkoniyatini anglatadi; ikkita mustaqil konstruktor talab qilinmaydi.
- UI kit va ekranlar xaritasi staging handoff vositalari; admin credentiallarini public ko'rsatish talab emas.
- Production izohlaridagi resumable media, HLS himoyasi, ichki live, question bank/CSV va Go/C++/SQL B2/B3/B5/G/H hamda D-13 qarorida; iOS/Android/push/offline video P va D-15da qayd qilingan.
- Har elementning bandga bog'lanishi funksiyaning tayyorligi yoki barcha biznes qarorlar tasdiqlanganini anglatmaydi. Ochiq qarorlar ilova Nda.

### 8. Manba triggerlarining statik mosligi

Literal data-action havolalari: 174; literal data-form havolalari: 34. Dinamik satr qurilishi va inline modal callbacklar ushbu sonlarga to'liq kirmasligi mumkin.

Reyestrda topilmagan literal actionlar: yoq. `modal-backdrop` umumiy handlerda alohida bajariladi.

Reyestrda topilmagan literal formalar: yoq.

Bu tekshiruv UI/E2E sinovi o'rnini bosmaydi; xatti-harakat qoidalari ilovadagi oqimlar va QA ssenariylari bilan tekshiriladi.
