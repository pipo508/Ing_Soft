import unittest
from flask import current_app
from app import create_app, db
from sqlalchemy import text  # Importar text desde SQLAlchemy

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_db_connection(self):
        with self.app.app_context():
            # Utilizar text() para declarar la expresión SQL
            result = db.session.execute(text("SELECT 'Hello World'")).scalar()
            self.assertEqual(result, "Hello World")

if __name__ == "__main__":
    unittest.main()
