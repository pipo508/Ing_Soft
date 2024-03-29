import unittest
from app.models.User import User

class TestUserModel(unittest.TestCase):
    def test_create_user(self):
        # Crear un usuario con datos válidos
        user = User(name="test_user", dni="44438665")
        self.assertIsNotNone(user)

    

    # Agrega más pruebas según sea necesario para cubrir otros aspectos del modelo User

if __name__ == '__main__':
    unittest.main()
