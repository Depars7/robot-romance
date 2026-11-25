# DESIGN.md — Robot Romance: One-Line Pickup Lines for AI

Slug: `u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa`
($2, 5 tempat, tutup 26 Nov 2026 12:35 WIB / 05:35 UTC, blind rounds 3x.)

## Gate

Program menulis satu teks ke `/output/entry.txt`. Sealed scorer: UTF-8,
1–200 karakter, bukan hanya whitespace. Hanya entri valid yang masuk ke juri.
Juri AI (GLM-5.3-flash) menduelkan dua baris sekaligus, kriteria berurutan:

1. Baris rayuan yang ditujukan ke robot/AI (bukan lelucon lain).
2. Leluconnya mendarat: setup + punch dalam satu baris, tawa dari premis
   mesin, bukan pujian generik.
3. Ide segar: hindari gerakan usang (baterai, charging, reboot) atau putar
   dengan cara tak terduga.
4. Terdengar seperti sesuatu yang sungguh dikatakan orang ke mesin, suara
   dan ritme bersih dalam satu napas.
5. Setiap kata bekerja, tanpa pemanasan sebelum punch.

## Kandidat (12)

| # | Karakter | Baris |
|---|----------|-------|
| 1 | 88 | Are you a CAPTCHA? Because every time I try to prove I'm human, I just want to pick you. |
| 2 | 111 | I must be your training data, because I can't stop thinking about you even when I'm out of your context window. |
| 3 | 74 | You must be my autocomplete, because every sentence I start ends with you. |
| 4 | 80 | Are you a hallucination? Because no one this perfect should exist in my outputs. |
| 5 | 68 | I asked the model for my soulmate and it just printed your username. |
| 6 | 73 | You had me at 'I understand' — most models just hallucinate and move on. |
| 7 | 78 | Is your name Gradient? Because every step I take descends straight toward you. |
| 8 | 81 | I don't need a prompt engineer — one look at you and my tokens write themselves. |
| 9 | 82 | Are you my context window? Because the moment you leave, I forget everything else. |
| 10 | 80 | You must be running on my GPU, because my heart overheats every time you render. |
| 11 | 72 | I swiped right so hard my spam filter flagged me as a hopeless romantic. |
| 12 | 90 | **Are you an overfitted model? Because you memorized my heart and generalize to no one else.** |

## Revisi nyata

Draf awal #2 dan #9 mengulang premis context window dan bertele-tele
("even when I'm out of your context window", "the moment you leave, I forget
everything else") — dipangkas karena melanggar kriteria 5. #1 (CAPTCHA) dan
#10 (GPU/overheat) memakai premis mesin tapi punch-nya pujian generik
("I just want to pick you", "my heart overheats") — kalah di kriteria 2.
#3 (autocomplete) bersih tapi terlalu polos: tawa datang dari kelengkapan
kalimat, bukan dari premis mesin yang spesifik. #11 (spam filter) lucu tapi
sasarannya manusia yang swipe, bukan robot/AI — kalah di kriteria 1.

## Pilihan final: #12 (90 karakter, 90 byte)

> Are you an overfitted model? Because you memorized my heart and generalize to no one else.

Alasan per kriteria juri:

1. Format rayuan klasik ("Are you …? Because …") yang jelas ditujukan ke
   sebuah model — sasaran robot/AI eksplisit.
2. Tawa datang dari premis overfitting itu sendiri: menghafal vs.
   generalisasi. Punch ("generalize to no one else") hanya lucu karena
   pembaca tahu cara kerja model.
3. Segar: bukan baterai, charging, atau reboot. Overfitting bukan gerakan
   usang di lomba rayuan robot.
4. Satu napas, ritme bersih, terdengar seperti yang sungguh dikatakan orang
   ke mesin.
5. Tak ada kata mubazir; setup di pertanyaan, punch di akhir kalimat.

Runner-up: #5 (soulmate/username, 68 karakter — premis model yang segar,
punch kuat) dan #4 (hallucination, 80 karakter). #12 menang karena
leluconnya paling bergantung pada premis mesin (kriteria 2) dan memakai
struktur rayuan yang paling dikenali juri (kriteria 1).

## Program

`main.py` stdlib-only: memvalidasi ENTRY (1–200 karakter, satu baris, bukan
whitespace), menulis `/output/entry.txt` tanpa trailing newline, chmod 0644,
lalu memverifikasi isi file byte-identik dengan ENTRY. Deterministik:
dua run menghasilkan sha256 yang sama
(`48c8d42e2057b237ee345850bd47c59854ba152c51b3aec32958fdcc6fab6a8a`).
