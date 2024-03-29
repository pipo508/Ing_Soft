from app.models import User
from app.repositories.repository_base import Create
from app import db


class UserRepository(Create):
        
        def __init__(self):
                self.__model = User


        #Create Section
        def create(self, entity):
                db.session.add(entity)
                db.session.commit()
                return entity
