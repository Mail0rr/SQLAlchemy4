from sqlalchemy import (
    create_engine,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker,
)

#Создание двигателя для подключения к БД
DB = "sqlite:///app.db"

engine = create_engine(DB, echo=True)

Session = sessionmaker(bind=engine)
#sessionmaker использует патерн проэктирование фабрика и возвращает
#класс Session который умеет работать с указаными над ним диалектами

class Base(DeclarativeBase):
    ...

def create_db():
    Base.metadata.create_all(engine)


def dorp_db():
    Base.metadata.drop_all(engine)

