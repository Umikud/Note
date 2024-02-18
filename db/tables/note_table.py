from sqlalchemy import Column, Integer, String
from db.database import Base


class Note(Base):
    __tablename__ = 'note'
    id = Column(Integer, primary_key=True)
    header = Column(String(70), nullable=False)
    desc = Column(String, nullable=False)
