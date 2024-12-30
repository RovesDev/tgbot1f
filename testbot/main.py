from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import nest_asyncio
import asyncio

# Salomlashish funksiyasi
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Bot render serveri orqali yoqildi')

# Botning asosiy funksiyasi
async def main():
    # Botni ishga tushurish
    token = '7981554834:AAE1yMVath0oAJSs-AWba5MR04rFu28Fg2M'  # Tokenni shu yerga joylang
    application = Application.builder().token(token).build()

    # CommandHandler orqali /start komandasini qo'shish
    application.add_handler(CommandHandler("start", start))

    # Botni ishga tushurish va polling qilish
    await application.run_polling()

# Agar tizimingizda event loop muammosi bo'lsa, nest_asyncio yordamida hal qilish
if __name__ == '__main__':
    nest_asyncio.apply()  # Bu usul orqali mavjud voqealar tsiklini yangilab olish mumkin.
    asyncio.run(main())  # Asinxron ishga tushirish
