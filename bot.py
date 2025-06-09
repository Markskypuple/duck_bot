from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from config import Config
from duck_cards import give_random_card, get_user_collection
import os

config = Config()

async def start(update: Update, context):
    await update.message.reply_text("Привіт! Надішли слово 'кря' або 'утка', щоб отримати картку.")

async def handle_message(update: Update, context):
    text = update.message.text.lower()
    user_id = str(update.message.from_user.id)

    if "кря" in text or "утка" in text:
        card = give_random_card(user_id)
        await update.message.reply_photo(photo=open(card["image_path"], "rb"),
                                         caption=f"Ти отримав картку 🦆: {card['name']} (Lv {card['level']})")
    elif "/collection" in text:
        collection = get_user_collection(user_id)
        if collection:
            message = "\n".join([f"{c['name']} (Lv {c['level']})" for c in collection])
            await update.message.reply_text("Твоя колекція:\n" + message)
        else:
            await update.message.reply_text("У тебе ще немає карток.")

def run_bot():
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
