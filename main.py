from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = 7760817892:AAHNgIG2M7QDDKApPy00xFLv42nFEkF_kCY

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("КІТ оновився. Це точно.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

async def run():
    await app.initialize()
    await app.start()
