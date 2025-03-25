from sqlalchemy.orm import Session

from models import Reader
from schemas import ReaderCreate, ReaderUpdate


# Операции Crud для читателей
async def create_reader(db: Session, reader: ReaderCreate):
    db_reader = Reader(**reader.model_dump())
    db.add(db_reader)
    db.commit()
    db.refresh(db_reader)
    return db_reader

async def get_reader(db: Session, reader_id: int):
    return db.query(Reader).filter(Reader.id == reader_id).first()

async def get_readers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Reader).offset(skip).limit(limit).all()

async def update_reader(db: Session, reader_id: int, reader: ReaderUpdate):
    db_reader = db.query(Reader).filter(Reader.id == reader_id).first()
    for var, value in vars(reader).items():
        setattr(db_reader, var, value) if value else None
    db.commit()
    db.refresh(db_reader)
    return db_reader


