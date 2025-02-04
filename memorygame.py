from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
import json
import os
from datetime import datetime

BOT_TOKEN = '7754206023:AAE1CfD8_jtlccYPsCa0Wa3d2x8aOPAoaSI'
WEBAPP_URL = 'https://naomicodedev.github.io/Find-a-Mate/'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message with a button that opens the web app."""
    await update.message.reply_text(
        "game of memory:",
        reply_markup={
            "inline_keyboard": [[{
                "text": "just click",
                "web_app": {"url": WEBAPP_URL}
            }]]
        }
    )

async def web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle data received from the web app"""
    data = json.loads(update.effective_message.web_app_data.data)
    moves = data.get('moves', 0)
    pairs = data.get('pairs', 0)
    completed = data.get('completed', False)
    
    if completed:
        message = f"🎮 End!!\n📊 Stats:\n- Steps: {moves}\n- Pairs found: {pairs}"
        await update.message.reply_text(message)
    else:
        await update.message.reply_text("saved!")

def main():
    """Start the bot."""
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data))
    application.run_polling()

if __name__ == '__main__':
    main()
