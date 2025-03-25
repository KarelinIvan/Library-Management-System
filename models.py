from imaplib import Int2AP

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from config import Base


class Book(Base):
    __tablename__ = 'books'
    """ Модель данных книги"""
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    published_date = Column(Date)
    isbn = Column(String, unique=True, index=True)
    pages = Column(Integer)


class Reader(Base):
    __tablename__ = 'readers'
    """ Модель данных читателя """
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


class BookIssue(Base):
    __tablename__ = 'book_issues'
    """ Модель для учёта выдачи книг """
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    reader_id = Column(Integer, ForeignKey('readers.id'))
    issue_data = Column(Date)
    return_date = Column(Date, nullable=True)

    book = relationship("Book")
    reader = relationship("Reader")
