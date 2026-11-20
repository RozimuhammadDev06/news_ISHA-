import  logging
from  datetime import  datetime 
import os
import sys

import django
from asgiref.sync import sync_to_async

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")
django.setup()

from core.models import Category


from  telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext  import(
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

TOKEN = '8975909210:AAHN7BV1-g90QX_CIv2T7EkQ_6CKXtMOVAA'
##   Terminalda bot nima qilyotgani korish uchun 
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

#  Yordamichi  Funksiyallar: Asosiy menyu (pastdagi tugmalar)

def  asosiy_menyu() -> ReplyKeyboardMarkup:
    """"""
    tugmalar =  [
        ["Salom","Vaqt"],
        ["Inline tugmalar"],
    ]

    return ReplyKeyboardMarkup(tugmalar,resize_keyboard=True)





async def start(update:  Update, context: ContextTypes.DEFAULT_TYPE):
    ism =  update.effective_user.first_name

    await update.message.reply_text(
        f"Assalomu  alaykum, {ism}! 👍",
        reply_markup=asosiy_menyu()
    )
async def yordam(update:  Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "yordam"
    )

def get_categories_text():
    categories = Category.objects.all()
    if not categories.exists():
        return "Categoryalar hali yo'q"
    return "\n".join(category.cat_name for category in categories)

async def haqida(update:  Update, context: ContextTypes.DEFAULT_TYPE):
    ctg = await sync_to_async(get_categories_text)()
    await update.message.reply_text(
        f"{ctg}\nbarcha categoryalar"
    )



####################################################################################

async def inline_korsat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tugmalar = [
        [
            InlineKeyboardButton("Yoqdi", callback_data="yoqdi"),
            InlineKeyboardButton("Yoqmadi", callback_data="yoqmadi"),
        ],
        [
            InlineKeyboardButton("Vaqt", callback_data="vaqt"),
        ],
    ]

    await update.message.reply_text(
        "Inline tugmalardan birini tanlang:",
        reply_markup=InlineKeyboardMarkup(tugmalar),
    )


async def inline_javob(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "yoqdi":
        await query.message.reply_text("Rahmat, sizga yoqqanidan xursandman!")
    elif query.data == "yoqmadi":
        await query.message.reply_text("Tushunarli, keyingi safar yaxshiroq qilaman.")
    elif query.data == "vaqt":
        hozir = datetime.now().strftime("%H:%M")
        await query.message.reply_text(f"Hozirgi vaqt: {hozir}")


async def matn_javob(update:  Update, context: ContextTypes.DEFAULT_TYPE):
    matn =  update.message.text.lower().strip()


    logger.info("Xabar keldi: %s (user: %s)", matn, update.effective_user.id)

    if matn == "salom":
        await update.message.reply_text("Salom Qaleysiz?")
    elif matn == "vaqt":
        hozir = datetime.now().strftime("%H:%M")
        await update.message.reply_text(f"Hozirgi vaqt: {hozir}")
    elif matn == "inline tugmalar":
        await inline_korsat(update, context)



async def xato(update:  Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error("xattolik yuz berdi:  %s",  context.error)




def main():
    # Botni token bilan quramiz
    app = ApplicationBuilder().token(TOKEN).build()

    # --- Handlerlarni ro'yxatdan o'tkazamiz ---
    # TARTIB MUHIM: Telegram yuqoridan pastga qarab tekshiradi.

    # Buyruqlar
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", yordam))
    app.add_handler(CommandHandler("about", haqida))
    app.add_handler(CallbackQueryHandler(inline_javob))




    # Oddiy matn (buyruq emas) kelganda
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, matn_javob))

    # Xatolarni ushlovchi
    app.add_error_handler(xato)

    print("Bot ishga tushdi... (to'xtatish: Ctrl + C)")

    # Telegramdan yangi xabarlarni doimiy tekshirib turadi
    app.run_polling()


# Fayl to'g'ridan-to'g'ri ishga tushirilganda main() chaqiriladi
if __name__ == "__main__":
    main()






