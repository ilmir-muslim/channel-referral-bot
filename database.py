from models import Session, User

# Создание нового пользователя
def add_user(tg_id, referral_link):
    session = Session()
    user = session.query(User).filter_by(tg_id=tg_id).first()
    if not user:
        new_user = User(tg_id=tg_id, referral_link=referral_link)
        session.add(new_user)
        session.commit()
    session.close()

# Проверка существующего пользователя
def get_user(tg_id):
    session = Session()
    user = session.query(User).filter_by(tg_id=tg_id).first()
    session.close()
    return user

# Обновление статуса подписки
def update_subscription_status(tg_id, status):
    session = Session()
    user = session.query(User).filter_by(tg_id=tg_id).first()
    if user:
        user.subscription_status = status
        session.commit()
    session.close()
