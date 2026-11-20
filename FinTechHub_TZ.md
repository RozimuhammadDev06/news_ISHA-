# FinTechHub LMS — frontend va backend uchun texnik topshiriq

Versiya: 2.0 — takroriy to'liq tahlil. Sana: 31.10.2026.
Manba: foydalanuvchi taqdim etgan `fintechhub.html` faylining statik kod tahlili. Brauzerda ishlash va tashqi integratsiyalar sinovdan o'tkazilmadi.

Hujjatlar to'plami:

- Ushbu hujjat — mahsulot, frontend/backend vazifalari, biznes qoidalari va qabul mezonlari.
- [Batafsil funksional va texnik ilova](FinTechHub_TZ_Ilova.md) — oqimlar, maydonlar, holatlar, qo'shimcha API, infratuzilma va kengaytirilgan testlar.
- [Manba bilan qamrov reyestri](FinTechHub_Qamrov.md) — HTMLdagi sahifa, forma, action va sozlama triggerlarini tegishli TZ bandiga bog'lash.

2.0 versiya 1–13-bo'limlarni saqlab, quyidagi tuzatishlar va ilovadagi tafsilotlar bilan to'ldiradi. Birinchi versiyadagi umumiy jumla va yangi aniq qoida farqlansa, 14-bo'lim va ilovadagi aniq qoida ustuvor. “Manba” qaydi kuzatilgan demo xatti-harakatini, “Taklif” qaydi esa production uchun tanlangan loyihaviy yechimni anglatadi. Ochiq tijoriy qarorlar kelishilmaguncha ularni yakuniy tasdiqlangan shart deb talqin qilish mumkin emas.

## 1. Loyiha mazmuni

FinTechHub — dasturlash va kiberxavfsizlikni amaliyot orqali o'rgatadigan onlayn ta'lim platformasi (LMS). Foydalanuvchi kurs tanlaydi, bepul yoziladi yoki to'lov qiladi, darslarni o'qiydi, test va kod mashqlarini bajaradi, mentorga vazifa yuboradi va kurs yakunida tekshiriladigan sertifikat oladi.

Bu nomida fintech bo'lsa-da, taqdim etilgan mahsulot bank yoki pul o'tkazish ilovasi emas. Uning asosiy mahsuloti — IT ta'limi; to'lovlar kurs va obunalarni sotish uchun xizmat qiladi.

Fayldagi yo'nalishlar:

| Yo'nalish | Namuna kurslar |
|---|---|
| Dasturlash | Python, JavaScript/TypeScript, React, Node.js/PostgreSQL, Git/GitHub |
| Kiberxavfsizlik | Linux, Web Pentest/OWASP, kiberxavfsizlikka kirish, SOC/SIEM |

Daromad modeli: alohida kurs xaridi, oylik/yillik Pro obuna, kursni 3 yoki 6 qismga bo'lib to'lash. Qo'shimcha mexanizmlar: promo-kod va referal chegirmasi.

## 2. Manba holati va TZ chegaralari

HTML ichida dizayn, hash orqali sahifa navigatsiyasi, JavaScript biznes qoidalari, demo foydalanuvchilar va kurslar mavjud. Holat `localStorage` orqali saqlanadi. Bu tayyor serverli LMS ekanini anglatmaydi.

To'lovlar, email/SMS/Telegram jo'natish, lab infratuzilmasi, ayrim analitika, integratsiya holatlari va boshqa operatsiyalar demo yoki ishlab chiqarish uchun izohlar sifatida berilgan. Ularni haqiqiy ishlaydigan integratsiya deb qabul qilish mumkin emas.

Ushbu hujjatda:

- **Manbadagi talab** — HTML interfeysi yoki kodida ko'ringan imkoniyat/qoidalar.
- **Ishlab chiqarish talabi** — shu imkoniyatni haqiqiy tizimda ishonchli bajarish uchun qo'shilgan talab.
- **Ochiq qaror** — manbada yetarlicha aniqlanmagan yoki bir-biriga mos kelmaydigan qoida.

Frontend prototipning ko'rinishi va foydalanuvchi oqimlarini asos qilib oladi. Narx, ruxsat, natija, sertifikat, taymer va to'lov bo'yicha yakuniy qarorni backend beradi. Demo boshqaruvlari va demo akkauntlar productionga chiqarilmaydi.

## 3. Rollar va vakolatlar

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

## 4. Frontend texnik topshirig'i

### FE-01. Umumiy interfeys

- Ommaviy sahifalar, shaxsiy kabinet va dars o'qish muhiti uchun alohida layout.
- Desktopda sidebar; mobil qurilmada ochiladigan navigatsiya. Darsda modullar ro'yxati va asosiy kontent.
- O'zbek, rus va ingliz tillari; ochiq, qorong'i va tizim mavzusi. UI tarjimasi va kurs kontenti tili alohida tushuncha.
- Asosiy ko'rinish HTMLdagi ranglar, kartalar, tugmalar, jadvallar va grafiklardan olinadi. Faylda CSS qatlamlari takrorlanganligi sababli yakuniy ko'rinish uchun computed style asos qilib olinadi.
- Loading, bo'sh natija, xato, qayta urinish, offline, 403, 404 va texnik ishlar holatlari.
- Forma xatosi tegishli maydon yonida ko'rsatiladi. Klaviatura navigatsiyasi, fokus, label, kontrast va grafiklarning jadval ko'rinishi ta'minlanadi.
- Shaxsiy ma'lumotlar va tokenlar URLga chiqarilmaydi; `localStorage`da faqat xavfsiz interfeys afzalliklari saqlanishi mumkin.

### FE-02. Ommaviy sahifalar

- Landing: platforma tavsifi, ikki yo'nalish, kurslar, o'qish jarayoni, FAQ, ro'yxatdan o'tish chaqirig'i.
- Katalog: matnli qidiruv, yo'nalish, daraja, bepul/pullik filtri, saralash, sahifalash.
- Kurs kartasi: nom, yo'nalish, daraja, davomiylik, narx, reyting va foydalanuvchiga mos harakat tugmasi.
- Kurs sahifasi: tavsif, o'rganiladigan natijalar, talablar, muallif, modul/dars dasturi, preview, sharhlar va xarid.
- Narxlar: kurs va Pro shartlari; sertifikat tekshirish; yordam; oferta, maxfiylik, qaytarish va cookie sahifalari.
- Ochiq profil faqat foydalanuvchi ruxsat bergan maydonlarni ko'rsatadi.

### FE-03. Autentifikatsiya va onboarding

- Ism, familiya, email, parol, shartlarga rozilik bilan ro'yxatdan o'tish; referal havolani saqlash.
- Email/parol orqali kirish, email OTP tasdiqlash, kodni qayta yuborish taymeri, parolni tiklash.
- 2FA kodi va bir martalik zaxira kodi oynalari.
- SMS orqali kirish, Google/GitHub/Telegram orqali autentifikatsiya va CAPTCHA to'liq mahsulot scope'iga kiradi; provayder credentials va bosqichlash alohida qaror. Ishlamaydigan demo login productionga chiqarilmaydi.
- Noto'g'ri kod, tugagan muddat, bloklangan akkaunt va ortiqcha urinish holatlarini ko'rsatish.

### FE-04. Talaba kabineti

- Bosh panel: oxirgi darsni davom ettirish, kurs progressi, haftalik maqsad, faollik, XP/streak va yaqin muddatlar.
- Kurslarim: davom etayotgan, tugallangan va sevimli kurslar.
- Vazifalar va lablar ro'yxati; darsga o'tish va holat bo'yicha filtrlash.
- Natijalar: haftalik vaqt, kurs/modul progressi, test natijalari va vazifa baholari. Grafik va jadval ko'rinishi.
- Qaydlar: darsga bog'langan yozuvlar va saqlangan darslar.
- Jadval: vazifa muddati, jonli dars, to'lov sanasi; jonli darsga qatnashish belgilashi.
- Yutuqlar: nishonlar, XP tarixi, daraja; reyting: hafta, umumiy va kurs kesimi.

### FE-05. Dars muhiti — 6 tur

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

### FE-06. Xarid va to'lovlar

- Kurs yoki Pro tanlash, to'liq/3/6 qism rejasini tanlash, promo qo'llash, narx tafsilotlari va rozilik.
- Payme, Click, Uzum Bank va bank kartasi variantlari manbada ko'rsatilgan; frontend faqat backend qaytargan faol usullarni ko'rsatadi.
- Provider checkoutiga o'tish va qaytgach serverdan holatni olish: kutilmoqda, muvaffaqiyatli, xato, bekor qilingan, muddati tugagan.
- To'lovlar tarixi, chek, obuna, avtomatik yangilanishni o'chirish, tokenlashtirilgan kartalar, bo'lib to'lash jadvali.
- Qaytarish huquqi va rad sababini ko'rsatish; ariza yuborish va holatini kuzatish.
- Karta raqami/CVV ilova backendida saqlanmaydi; karta kiritish providerning himoyalangan oynasida bajariladi.

### FE-07. Mentor kabineti

- Navbat: eng eski topshiriqlar, holat/kurs/guruh filtrlari va SLA belgisi.
- Topshiriq: matn/havola/fayllar, kod, avtotest natijasi, oldingi urinishlar va plagiat signali mavjud bo'lsa uni ko'rish.
- Har rubrika mezoniga ball, umumiy fikr, kod qatoriga izoh; qabul qilish yoki qayta ishlashga qaytarish.
- Muddat uzaytirish so'rovlarini tasdiqlash/rad qilish; savol-javob navbati.
- Guruhlar: talabalar, progress, kechikishlar va yordam talab qiluvchi talabalar.

### FE-08. Muallif kabineti

- Kurslar va ularning draft/review/published holati.
- Konstruktor: kurs ma'lumoti, narx/daraja/yo'nalish, modullar va 6 turdagi darslarni yaratish, tartiblash, preview belgilash.
- Kontent turiga mos muharrir, saqlash holati, validatsiya, moderatsiyaga yuborish va rad izohini ko'rish.
- Kurs analitikasi: yozilish, darsni tugatish, chiqib ketish, test o'rtachasi va reyting. Productionda simulyatsiya ishlatilmaydi.

### FE-09. Admin va support

- Admin dashboard: daromad, xarid voronkasi, refund va SLA ogohlantirishlari; metrika davri ko'rsatiladi.
- Foydalanuvchi qidiruvi, filtrlash, profil kartasi, bloklash, ruxsatga mos rol boshqaruvi.
- Kurs va sharh moderatsiyasi; nashr qilish/yashirish; narxni o'zgartirish.
- Buyurtmalar, to'lovlar, refundlar, promo-kodlar va sertifikatni bekor qilish.
- Murojaat navbati, yozishma, kategoriya, ustuvorlik va holat.
- Superadmin uchun integratsiya sozlamalari, feature flag va texnik ishlar rejimi. Maxfiy kalit qayta ochiq ko'rsatilmaydi.
- Rollar matritsasi va o'zgartirib bo'lmaydigan audit ko'rinishi.

### FE-10. Profil va sozlamalar

Profil/avatar, email/telefonni qayta tasdiqlash, parol, 2FA, sessiyalarni tugatish, kirish tarixi; kanal bo'yicha bildirishnoma afzalligi; Telegram bog'lash; til/mavzu; ma'lumot eksporti va akkauntni o'chirish so'rovi. Eksport va o'chirish jarayon holati bilan ko'rsatiladi.

## 5. Backend texnik topshirig'i

### BE-01. Arxitektura va umumiy shartnoma

Boshlang'ich arxitektura: domen modullariga ajratilgan bitta backend, relyatsion DB, fon vazifalari navbati, fayl saqlash va alohida kod/lab ijro muhiti. Framework tanlovi ushbu TZ bilan majburlanmaydi.

- Versiyalangan API: `/api/v1`. OpenAPI shartnomasida maydonlar, permission, validatsiya, xatolar va misollar beriladi.
- Sana-vaqt DBda UTC, interfeysda foydalanuvchi vaqt zonasida; boshlang'ich zona `Asia/Tashkent`.
- Summalar float bilan hisoblanmaydi; valyuta va kichik pul birligi API shartnomasida aniq belgilanadi.
- Ro'yxatlar pagination, ruxsat etilgan filter/sort, limit bilan qaytariladi.
- Xato shakli: `code`, `message`, `field_errors`, `request_id`.
- Bir xil mutatsiya qayta yuborilganda takroriy xarid, XP, submission yoki charge yuzaga kelmasligi uchun idempotency ishlatiladi.

### BE-02. Hisob va xavfsizlik

- Foydalanuvchi, ko'p rollilik va obyekt darajasidagi permissionlar; bloklangan akkaunt uchun sessiya/ruxsatni bekor qilish.
- Parol uchun maxsus xavfsiz password hasher; demo hash algoritmi ko'chirilmaydi.
- Email/telefon OTP va reset tokeni: amal muddati, urinish limiti, qayta yuborish cheklovi, bir martalik foydalanish; saqlashda himoya.
- Xavfsiz sessiya cookie, HTTPS, CSRF himoyasi, sessiya rotatsiyasi va logout/revoke.
- 2FA siri shifrlanadi, backup kodlari hash qilinadi; xodim roli faollashishidan oldin 2FA tekshiriladi.
- Login, OTP, password reset, flag tekshirish va kod ishga tushirish uchun rate limit.
- Server foydalanuvchi IDsi, rol, kursga kirish va topshiriq egasini har so'rovda tekshiradi.

### BE-03. Kurslar va kirish huquqi

- Yo'nalish, kurs, modul, tartibli darslar va har turga tegishli kontentni boshqarish.
- Kurs holatlari: draft → review → published; rad etilganda izoh bilan tahrirga qaytish. Nashrni yashirish alohida qayd qilinadi.
- Muallif faqat o'z kursini tahrirlaydi; mentor biriktirish va guruh a'zoligi serverda saqlanadi.
- Bepul yozilish, xarid va Pro orqali kirish manbai alohida saqlanadi. Bitta kirish manbai tugashi boshqa haqiqiy kirishni bekor qilmaydi.
- Preview mehmon uchun ochiq; qolgan kontent autentifikatsiya, entitlement va modul ochilishiga bog'liq.
- Sotib olingan kurs uchun UI 12 oy kirishni ko'rsatadi; backendda boshlanish/tugash muddati tekshirilishi kerak.
- Kurs o'zgarganda eski progress, topshiriq va sertifikat buzilmasligi uchun kontent versiyasi/snapshot siyosati bo'ladi.

### BE-04. Progress, test va kod mashqlari

- Progress: opened/started/completed, video pozitsiyasi, tugatish dalili va vaqtlar. Har dars turi o'z tugatish qoidasiga ega.
- Test: savol va variant tartibi urinishda saqlanadi; boshlanish/tugash vaqti serverniki; javoblar draft saqlanishi mumkin.
- Ball serverda hisoblanadi. Taymer tugaganidan keyin kech javob qabul qilinmaydi; qayta kirish taymerni yangilamaydi.
- To'g'ri javob/tushuntirish faqat urinish yakuni va kurs siyosatiga muvofiq ko'rsatiladi.
- Kod ishlatish asinxron job: queued/running/passed/failed/timeout. CPU, xotira, disk, jarayon va chiqish hajmi cheklangan; tarmoq yopiq.
- Foydalanuvchi kodi asosiy API server jarayonida bajarilmaydi. Yashirin testlar va tizim sirlari foydalanuvchi kodidan ajratiladi.
- Playground natijasi baholanadigan dars natijasidan ajratiladi.

### BE-05. Vazifa va mentor tekshiruvi

- Har topshirish alohida immutable urinish: havola, matn, fayl/kod snapshoti va topshirilgan vaqt.
- Holatlar: submitted → review → accepted yoki returned; returned holatidan yangi urinish yaratiladi.
- Mentor navbatni egallaganda parallel ikki tekshiruvning to'qnashuvi oldi olinadi.
- Rubrika mezonlari, maksimal ball, mentor izohi, kod qatori izohlari va review tarixi saqlanadi.
- Ball 50% dan past bo'lsa accepted taqiqlanadi; 50% yoki undan yuqori natija mentor qarorisiz avtomatik qabul qilinmaydi.
- Fayl turi/hajmi, zararli fayl tekshiruvi va yopiq yuklab olish ruxsati; tasodifiy storage nomlari.
- Avtotestlar va plagiat tahlili haqiqiy servis bilan amalga oshiriladi yoki funksiyasi o'chiriladi. Demo foizlar ko'rsatilmaydi; plagiat signali avtomatik ayblov yoki bloklashga teng emas.
- Deadline birinchi ochilishda serverda bir marta belgilanadi; uzaytirish sababi, qarori va yangi sana saqlanadi.

### BE-06. CTF laboratoriyalar

- Lab shabloni, foydalanuvchiga tegishli sessiya, TTL, ulanish ruxsati, maslahat va flag topshirish.
- Holatlar: requested/provisioning/running/stopping/stopped/expired/failed.
- O'quvchilar muhiti bir-biridan va platforma tarmog'idan ajratiladi. Resurslar limitlanadi; ruxsatsiz tashqi nishonlarga chiqish cheklanadi.
- Flaglar frontendda saqlanmaydi; serverda tekshiriladi. Takroriy yechim XP bermaydi.
- TTL tugaganda yoki stop berilganda resurslar avtomatik tozalanadi. Ishga tushirish xatosida band limit bo'shatiladi.
- Bir paytdagi sessiya soni, navbat va tarifga qarab kvota konfiguratsiya qilinadi.

### BE-07. Buyurtma va to'lovlar

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

### BE-08. Promo va referal

Promo: foiz/fiks summa, muddat, scope, umumiy va bir foydalanuvchiga limit, birinchi xarid sharti. Promo va referal chegirmasi qo'shilmaydi, kattasi tanlanadi. Parallel xaridlarda limit tranzaksiya bilan tekshiriladi. Bekor/to'lanmagan buyurtma limitni doimiy band qilib qolmasligi kerak.

Referal: kod egasi, taklif qilingan foydalanuvchi, ro'yxat/xarid holati; o'zini taklif qilish va takroriy mukofot taqiqlanadi. Mukofot berish va refunddan keyingi qaytarish siyosati ochiq qaror.

### BE-09. Sertifikat va gamifikatsiya

- Barcha majburiy darslar tugaganda, vazifalar qabul qilinganda va yakuniy test talabi bajarilganda sertifikat avtomatik yaratiladi.
- Unikal ID, ism/kurs snapshoti, berilgan sana, natija, PDF, QR va ochiq verify URL.
- Verify javobi: valid/revoked/not_found; bekor qilish sababi va vaqtini saqlash. Ochiq javobda email/telefon chiqarilmaydi.
- XP eventlar jurnali; bir hodisa bir marta mukofotlanadi. Daraja, badge, streak va reyting shu jurnal/dalillardan olinadi.
- Faollik va reytingning hafta chegarasi bitta aniq vaqt zonasi qoidasiga asoslanadi. Sintetik/demo statistika ishlatilmaydi.

### BE-10. Aloqa, support va fon vazifalari

- In-app, email, SMS, Telegram uchun kanal adapterlari, shablon va til, yuborish holati, retry va deduplication.
- Foydalanuvchi afzalliklari hisobga olinadi; xavfsizlik xabarlari o'chirilmaydi.
- Telegram bog'lash bir martalik tasdiqlanadigan token orqali; faqat username kiritish bog'lash uchun yetarli emas.
- Murojaat va xabarlar, kategoriya/priority/status, biriktirilgan xodim, birinchi javob va SLA hisoblash.
- Scheduler: 30 daqiqalik buyurtma expiry, lab TTL, muddat eslatmasi, jonli dars eslatmasi, obuna/bo'lib to'lov, SLA escalation, eksport va cleanup.
- Vazifalar brauzer ochiq bo'lmasa ham bajariladi; worker qayta ishga tushganda xabar yoki to'lov takrorlanmaydi.

### BE-11. Analitika va operatsion boshqaruv

Talaba, muallif va admin statistikasi real eventlardan olinadi. Daromad hisoboti tushum, refund va sof natijani ajratadi. Kursni tugatish foizi uchun denominator/kohort va vaqt davri hujjatlashtiriladi; o'qish daqiqasi hisoblangan yoki o'lchangan ekanligi ko'rsatiladi.

Audit append-only: actor, amal, obyekt, vaqt, request ID, IP va zarur oldin/keyin ma'lumot; sirlar yozilmaydi. Monitoring: API xato/kechikish, navbat, webhook, charge, lab resursi, backup va disk holati. Integratsiya panelidagi holatlar haqiqiy health-checkdan olinadi.

## 6. Asosiy ma'lumotlar modeli

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

## 7. API guruhlari — frontend/backend kelishuvi

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

## 8. Manbadan olingan biznes qoidalari

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

## 9. Aniqlangan nomuvofiqlik va ochiq qarorlar

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

## 10. Nofunksional va sifat talablari

- Moslashuvchan interfeys: 360 px mobil, planshet va desktopda asosiy oqimlar ishlaydi; jadvallar o'z konteynerida scroll qiladi.
- Accessibility uchun WCAG AA darajasidagi klaviatura, label, fokus, kontrast va status e'lonlari qabul mezoni qilinadi.
- Taklif etilgan boshlang'ich maqsad: odatiy API o'qish so'rovlarida p95 ≤ 500 ms, 100 parallel faol foydalanuvchi sinovida; video stream va og'ir joblar bundan alohida. Buyurtmachi bilan yuklama tasdiqlanadi.
- Upload, kod va lablar asinxron; UI foydalanuvchiga holat va qayta urinishni ko'rsatadi.
- Backup avtomatlashtiriladi, qayta tiklash sinovi bajariladi; RPO/RTO ishga tushirishdan oldin kelishiladi.
- Sirlar server secret storage orqali beriladi, log va frontend bundle ichiga kirmaydi.
- Boy matn sanitizatsiya qilinadi; fayl va tashqi havolalar nazorat qilinadi. Uchinchi tomon callbacklari va admin mutatsiyalari tekshiriladi.
- Moliyaviy va ta'lim eventlari kuzatiladigan bo'ladi; audit yozuvini oddiy admin tahrirlay/o'chira olmaydi.

## 11. Qabul qilish ssenariylari

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

## 12. Bosqichlar va topshiriladigan natijalar

Quyidagi bosqichlash — taklif; barcha funksiyalarni birinchi relizga majburan kiritmaydi.

| Bosqich | Natija |
|---|---|
| 1. Asosiy LMS | Auth, rollar, katalog, video/matn/test, enrollment, progress, sodda muallif/admin, bitta bir martalik payment integratsiyasi, vazifa/mentor, sertifikat |
| 2. Tijoriy va xizmat | Pro, recurring/bo'lib to'lov, qo'shimcha providerlar, promo/referal, refund, support, bildirishnoma kanallari, jadval va haqiqiy analitika |
| 3. Amaliy muhit | Izolyatsiyalangan JS/Python run, CTF infratuzilmasi, avtotest/plagiat integratsiyasi, kengaytirilgan gamifikatsiya |

Birinchi bosqichda keyingi bosqich funksiyalari menyuda ishlaydigan imkoniyat sifatida ko'rsatilmaydi. Agar barcha imkoniyatlar birinchi relizga kerak bo'lsa, to'liq TZ shu hajmda baholanadi.

Topshirish paketi: frontend/backend manba kodi, DB migratsiyalari, OpenAPI, konfiguratsiya namunasi, storage/worker sozlamalari, testlar va hisobot, deploy/rollback yo'riqnomasi, backup/restore yo'riqnomasi, rollar matritsasi, admin qo'llanmasi. Production ma'lumotlaridan ajratilgan demo seed ham beriladi.

## 13. Manbadagi tayanch nuqtalar

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

## 14. Takroriy tahlildagi majburiy aniqlashtirishlar

### 14.1. Tasdiqlangan qo'shimcha qoidalar

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

### 14.2. Qo'shimcha topilgan nomuvofiqliklar

- **Billing urinishlari:** `RETRY_DAYS=[0,1,3,5]` — jami 4 urinish; xabarda “3 ta” deyiladi. Boshlang'ich talab: dastlabki + 3 retry; grace to'lov sanasidan 12 kun. Xabar ham shu qiymatlardan tuziladi.
- **Kechikish jazosi:** demo review paytida joriy deadline bilan qayta hisoblaydi; keyinchalik muddat o'zgarsa oldingi submission bahosi o'zgarishi mumkin. Deadline va jazo siyosati submissionda snapshot qilinadi.
- **20% va 100%:** yaxlitlangan progress biznes qarori uchun ishlatilmaydi. Sharh/refund tekshiruvi aniq nisbat, sertifikat esa barcha majburiy darslarning completion holati bilan tekshiriladi.
- **Jonli dars:** avvalgi TZdagi “havola/RSVP yetarli” faqat cheklangan birinchi reliz varianti edi. To'liq mahsulot uchun ichki jonli dars moduli ilova Hda belgilandi.
- **Qo'shimcha tillar va test banki:** Go/C++/SQL, savollar banki, random tanlash va CSV import faqat production izohlarida uchraydi. Ular yo'qolib qolmasligi uchun alohida kengaytma sifatida reyestrga kiritiladi; JS/Python oqimi bilan teng darajada tayyor demo deb ko'rsatilmaydi.
- **Refund tasdig'i:** manbadagi ikki bosqich UI tasdiqlashni bildiradi; ikki alohida xodim tasdig'i manbada yo'q. Productionda qayta autentifikatsiya + yakuniy tasdiq talab qilinadi; ikki xodim talabi tijoriy qaror.
- **Demo ma'lumotlar:** soxta email qutisi, authenticator, tezkor login, vaqtni oldinga surish, card failure va seed reset faqat demo/staging vositalari. Ularni haqiqiy foydalanuvchi funksiyasi sifatida ishlab chiqish talab qilinmaydi.
- **Offline va'dasi:** HTML banneri aloqa tiklanganda yuborishni va'da qiladi, lekin ishonchli sync navbati yo'q. Ilova Fda progress/qayd/kod drafti uchun chegaralangan sync, moliyaviy va baholash amallari uchun online talabi belgilandi.
- **Mobil scope:** ekranlar xaritasi matnida iOS/Android, push, yuklab olingan video va deep linklar aniq tilga olingan. Bu ishlaydigan mobil kod emas, lekin to'liq loyiha talabida yo'qolmaydi: ilova P. Faqat responsive web bilan cheklash alohida reliz/scope qarori bo'ladi.

## 15. To'liq scope va reliz chegarasi

Ushbu TZ va ilovada ko'rsatilgan barcha asosiy oqimlar to'liq loyiha hisobiga kiradi. 12-bo'limdagi bosqichlar ish tartibi; ular funksiyani o'z-o'zidan scope'dan chiqarish uchun asos bo'lmaydi. Olib tashlanadigan yoki keyinga qoldiriladigan band IDsi, sababi va relizi bilan yozma qayd etiladi.

Manbada yetarli bo'lmagan qoida yashirin taxmin bilan yopilmaydi: ilovadagi qarorlar reyestrida boshlang'ich yechim, kim tasdiqlashi va qaysi ish unga bog'liqligi yoziladi. Ishlab chiqish davomida har talab uchun frontend, backend va QA holati yuritiladi. Qamrov reyestri mavjud implementatsiya tayyorligini emas, HTMLdagi imkoniyatlar hujjatga bog'langanini ko'rsatadi.
