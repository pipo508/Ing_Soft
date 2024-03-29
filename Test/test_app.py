import unittest
from flask import current_app
from app import create_app

class AppTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
    def tearDown(self) -> None:
        self.app_context.pop()
    def test_app(self):
        self.assertIsNotNone(current_app)
    
if __name__ == "__main__":
        unittest.main()