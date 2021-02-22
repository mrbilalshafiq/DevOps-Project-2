from flask import render_template, redirect, url_for, request
from app import app, db
from app.models import Prizes
from app.forms import IndexForm
import requests

@app.route('/', methods=['GET', 'POST'])
def home():
    form = IndexForm()
    if request.method == 'POST':
        char = requests.get("http://chargen:5001/get_chargen")
        num = requests.get("http://numgen:5002/get_numgen")
        prize = requests.post("http://prizegen:5003/prize", json={"account_number" : char.text + num.text})

        account_number = char.text + num.text
        account_prize = Prizes(account_number = account_number, prize = prize.text)
        db.session.add(account_prize)
        db.session.commit()
        prizes = Prizes.query.limit(10).all()

        return render_template('index.html', form=form, account = char.text+num.text, message = prize.text, prizes = prizes)
    return render_template('index.html', form=form, message = "")
