from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate


# Создаем соединение с базой данных
engine = create_engine('sqlite:///../users_leo.db')

# Создаем базовый класс для объявления моделей
Base = declarative_base()


# Определяем модель данных
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    caption = Column(String(4096))


# Создаем таблицу в базе данных
Base.metadata.create_all(engine)

# Создаем сессию для взаимодействия с базой данных
Session = sessionmaker(bind=engine)
session = Session()


def print_users():
    users = session.query(Users).all()
    user_data = [(user.id, user.caption) for user in users]
    headers = ["User ID", "Caption"]
    print(tabulate(user_data, headers=headers, tablefmt="pretty"))
