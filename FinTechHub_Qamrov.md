# FinTechHub — HTMLdan TZga qamrov reyestri

Sana: 31.10.2026. [Asosiy TZ](FinTechHub_TZ.md) · [Batafsil ilova](FinTechHub_TZ_Ilova.md).

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

## 1. Sahifa variantlari — SCREENS

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

## 2. Route reyestri

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

## 3. Admin viewlar

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

## 4. Formalar

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

## 5. Amallar

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

## 6. Click/formdan tashqari asosiy triggerlar

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

### Sozlama maydonlari alohida tekshiruvi

| `data-uset` maydoni | TZ / ilova |
|---|---|
| `autoNext` | B3; F2 |
| `digest` | R-DIGEST; G3 |
| `marketing` | G3; F3 |
| `quiet` | R-QUIET; G3; P3 |
| `speed` | B3; F2 |
| `subsDefault` | B3; F2 |

### Handoff va production izohlaridagi qo'shimcha scope

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

## 7. Demo va production izohlarining talqini

- Demo quick login, email/SMS qutisi, demo authenticator, vaqtni surish, card failure va reset productionda yo'q; ular uchun haqiqiy auth/provider/worker oqimi tegishli A/D/G/K bo'limlarda talab qilingan.
- Eski `builder` va `b-*` actionlari yangi `konstruktor` / `bld-*` bilan bir mahsulot imkoniyatini anglatadi; ikkita mustaqil konstruktor talab qilinmaydi.
- UI kit va ekranlar xaritasi staging handoff vositalari; admin credentiallarini public ko'rsatish talab emas.
- Production izohlaridagi resumable media, HLS himoyasi, ichki live, question bank/CSV va Go/C++/SQL B2/B3/B5/G/H hamda D-13 qarorida; iOS/Android/push/offline video P va D-15da qayd qilingan.
- Har elementning bandga bog'lanishi funksiyaning tayyorligi yoki barcha biznes qarorlar tasdiqlanganini anglatmaydi. Ochiq qarorlar ilova Nda.

## 8. Manba triggerlarining statik mosligi

Literal data-action havolalari: 174; literal data-form havolalari: 34. Dinamik satr qurilishi va inline modal callbacklar ushbu sonlarga to'liq kirmasligi mumkin.

Reyestrda topilmagan literal actionlar: yoq. `modal-backdrop` umumiy handlerda alohida bajariladi.

Reyestrda topilmagan literal formalar: yoq.

Bu tekshiruv UI/E2E sinovi o'rnini bosmaydi; xatti-harakat qoidalari ilovadagi oqimlar va QA ssenariylari bilan tekshiriladi.
