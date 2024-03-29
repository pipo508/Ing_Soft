import unittest
from sqlalchemy import text
from app import create_app, db

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.db = db

    def tearDown(self):
        with self.app.app_context():
            self.db.session.remove()
            self.db.drop_all()

    def test_db_connection(self):
        with self.app.app_context():
            # Utilizar text() para declarar la expresión SQL
            result = self.db.session.execute(text("SELECT 'Hello World'")).scalar()
            self.assertEqual(result, "Hello World")

if __name__ == "__main__":
    unittest.main()
