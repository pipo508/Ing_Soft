from app import db
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass
@dataclass
class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(50), nullable=False)
    dni: str = Column(String(50), nullable=False)
    
    
