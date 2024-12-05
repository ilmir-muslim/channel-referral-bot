from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from database import add_user, get_user, update_subscription_status
from utils import generate_referral_link, check_channel_subscription

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_id = update.effective_user.id
    user = get_user(tg_id)

    if not user:
        referral_link = generate_referral_link(tg_id)
        add_user(tg_id, referral_link)

    # Создание инлайн-кнопок
    keyboard = [
        [InlineKeyboardButton("Подписаться", url="https://t.me/+1j_otPem-9Q4OWYy")],
        [InlineKeyboardButton("✅ Я подписался", callback_data="check_subscription")]
    ]
    markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "✨ Добро пожаловать! Подпишитесь на канал, чтобы продолжить.",
        reply_markup=markup
    )

async def check_subscription_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    tg_id = query.from_user.id

    # Проверка подписки
    is_subscribed = await check_channel_subscription(tg_id, context.bot)
    if is_subscribed:
        update_subscription_status(tg_id, True)
        user = get_user(tg_id)
        await query.message.edit_text(
            f"✨ Добро пожаловать! Ваша ссылка: {user.referral_link}"
        )
    else:
        await query.answer("❌ Вы ещё не подписаны. Подпишитесь на канал!", show_alert=True)
