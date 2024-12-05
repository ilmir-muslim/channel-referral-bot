from telegram.ext import Application, CommandHandler, CallbackQueryHandler 
from handlers import start, check_subscription_callback
from models import init_db
from config import TOKEN

# Инициализация базы данных
init_db()

# Инициализация бота
app = Application.builder().token(TOKEN).build()

# Регистрация хендлеров
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(check_subscription_callback))

if __name__ == "__main__":
    print("Bot is running...")
    app.run_polling()
