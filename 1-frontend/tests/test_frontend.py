import unittest
from flask import url_for
from flask_testing import TestCase
from app import app, db
from app.models import Prizes
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db",
            DEBUG=True,
            SQLALCHEMY_TRACK_MODIFICATIONS = False,
            WTF_CSRF_ENABLED = False
            )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.session.commit()
        db.drop_all()
        db.create_all()
        # Create test prizes
        prize = Prizes(account_number="BIL1234567", prize="Me for a day")
        db.session.add(prize)

        db.session.commit()
    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for("home"))
        self.assertEqual(response.status_code, 200)

class TestFrontend(TestBase):
    def test_prize(self):
        with patch('requests.get') as g:
            g.return_value.text = "ABC"
            g.return_value.text = "123456"
        with patch('requests.post') as g:
            g.return_value.text = "ABC123456"
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
