import asyncio
from telegram import Bot

API_TOKEN = "7974627539:AAH6NPm6tor1UGpFjSqeGfgUACEJgnsZP6I"  # Замените на ваш токен бота

async def get_chat_id():
    '''
    Функция для получения ID чата
    '''
    bot = Bot(token=API_TOKEN)
    updates = await bot.get_updates()
    for update in updates:
        print(update)

asyncio.run(get_chat_id())
