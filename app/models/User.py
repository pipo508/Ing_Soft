from dataclasses import dataclass
from app import db 
from sqlalchemy import Column, Integer, String

@dataclass
class User:
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    def __init__ (self, username):
            self.id = id
            self.username = username
            