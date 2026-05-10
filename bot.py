import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler untuk command /start."""
    await update.message.reply_text(
        "Halo! Selamat datang di bot ini.\n"
        "Ketik /help untuk melihat daftar perintah yang tersedia."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler untuk command /help."""
    help_text = (
        "Daftar perintah yang tersedia:\n\n"
        "/start - Memulai bot\n"
        "/help - Menampilkan daftar perintah"
    )
    await update.message.reply_text(help_text)


def main() -> None:
    """Fungsi utama untuk menjalankan bot."""
    if not TOKEN:
        print("Error: TELEGRAM_BOT_TOKEN tidak ditemukan.")
        print("Pastikan file .env sudah dibuat dan berisi token bot Anda.")
        return

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    print("Bot berjalan...")
    application.run_polling()


if __name__ == "__main__":
    main()
