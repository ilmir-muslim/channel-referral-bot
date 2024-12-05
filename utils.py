from telegram import Bot
from config import CHANNEL_ID

# Генерация реферальной ссылки
def generate_referral_link(user_id):
    return f"https://t.me/testing_apps_ilmir_bot?start={user_id}"

# Проверка подписки пользователя на канал
async def check_channel_subscription(user_id, bot: Bot):
    member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
    return member.status in ["member", "administrator", "creator"]
