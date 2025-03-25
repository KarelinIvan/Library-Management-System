# Создание всех таблиц в БД
from config import Base, engine
from models import Book, Reader, BookIssue

Base.metadata.create_all(bind=engine)