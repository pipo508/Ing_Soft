from app.repositories.user_repository import UserRepository 
from app import db

class UserService:

    def __init__(self):
        self.__repo = UserRepository()
    
    def create(self, entity):
        return self.__repo.create(entity)      
    