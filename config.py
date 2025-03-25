from sqlalchemy import create_engine, MetaData
from databases import Database
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql+asyncpg://username:password@localhost/library_db"

# Движок для синхронного использования
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Движок для асинхронного использования
database = Database(DATABASE_URL)

# Создание базового класса
Base = declarative_base()

# Создание фабрики сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
