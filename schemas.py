from datetime import date
from typing import Optional

from pydantic import BaseModel


class ReaderBase(BaseModel):
    name: str
    email: str

class ReaderCreate(ReaderBase):
    pass

class ReaderUpdate(ReaderBase):
    pass

class ReaderOut(ReaderBase):
    id: int

    class Config:
        orm_mode = True

class BookIssueBase(BaseModel):
    book_id: int
    reader_id: int
    issue_date: date
    return_date: Optional[date] = None

class BookIssueCreate(BookIssueBase):
    pass

class BookIssueUpdate(BookIssueBase):
    pass

class BookIssueOut(BookIssueBase):
    id: int

    class Config:
        orm_mode = True