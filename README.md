# Telegram Bot

Bot Telegram sederhana menggunakan Python dan library `python-telegram-bot`.

## Cara Setup dan Menjalankan Bot

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Konfigurasi Token

Salin file `.env.example` menjadi `.env` dan isi dengan token bot Anda:

```bash
cp .env.example .env
```

Edit file `.env` dan ganti `your_token_here` dengan token yang didapat dari [@BotFather](https://t.me/BotFather) di Telegram.

```
TELEGRAM_BOT_TOKEN=token_bot_anda_disini
```

### 3. Jalankan Bot

```bash
python bot.py
```

## Perintah yang Tersedia

- `/start` - Memulai bot dan menampilkan pesan selamat datang
- `/help` - Menampilkan daftar perintah yang tersedia
