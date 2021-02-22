from app import db
from sqlalchemy import Table, Column, Integer

class Prizes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(12))
    prize = db.Column(db.String(100))
