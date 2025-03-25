from sqlalchemy import Column, Integer, String, Date
from config import Base


class Book(Base):
    __tablename__ = 'books'
    """ Модель данных """
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    published_date = Column(Date)
    isbn = Column(String, unique=True, index=True)
    pages = Column(Integer)
