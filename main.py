from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import json
SAVED_DATA = "data.json"

TOKEN: Final = "6742206212:AAGd67HKPYH9OuQFngMg5zgpK8xSB5R-WXA"
BOT_USERNAME = "@MayaZigBot"

# commands


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, i am your new Diet Keeper Helper! what is the type of meal you're having?"
                                    "(breakfast, lunch..) 🍌🥑🌸")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("please type in what kind of meal you are having?"
                                    "(breakfast, lunch, ect... 🍝🍣")


async def handle_responses(text: str) -> str:
    text = text.lower()
    with open(SAVED_DATA, "r") as f:
        meal_plan = json.load(f)
    if any(word in text for word in ['hello', 'hey', 'hi']):
        return 'hi there!'
    if any(word in text for word in ['how are you?', 'whats up?']):
        return 'fine, thanks'
    if 'breakfast' in text:
        return meal_plan['breakfast']
    if 'lunch' in text:
        return meal_plan['lunch']
    if 'snack' in text:
        return meal_plan['snack']
    if 'dinner' in text:
        return meal_plan['dinner']
    else:
        return "didn't get that 😓..please try again"


async def handle_massage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    massage_type = update.message.chat.type
    text = update.message.text

    if massage_type == 'group':
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, '').strip()
            response = handle_responses(new_text)
        else:
            return
    else:
        response = handle_responses(text)
    await update.message.reply_text(response)

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

# commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

# massages
    app.add_handler(MessageHandler(filters.TEXT, handle_massage))

    app.run_polling(poll_interval=3)

