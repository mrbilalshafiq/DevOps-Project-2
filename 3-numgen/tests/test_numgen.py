from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService3(TestBase):
    def test_get_num_gen(self):
        response = self.client.get(url_for('numgen'))
        self.assertEqual(response.status_code, 200)
