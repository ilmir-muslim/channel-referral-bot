from sqlalchemy import create_engine, Column, Integer, BigInteger, String, Numeric, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Инициализация базы данных
engine = create_engine("postgresql://july122a:root@localhost/bot_july122a")
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Модель пользователя
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tg_id = Column(BigInteger, unique=True, nullable=False)
    stars = Column(Numeric, default=0)
    referral_link = Column(String, nullable=True)
    subscription_status = Column(Boolean, default=False)

# Создание таблиц
def init_db():
    Base.metadata.create_all(engine)
