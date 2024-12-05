from telegram import ReplyKeyboardMarkup

def main_menu():
    return ReplyKeyboardMarkup(
        [["⭐ Заработать звезды", "💸 Вывести звезды"],
         ["Мой баланс", "💰 Задания"]],
        resize_keyboard=True
    )
