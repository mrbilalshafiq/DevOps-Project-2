from flask import render_template, redirect, url_for, request
from app import app
from app.forms import IndexForm
import requests

@app.route('/', methods=['GET', 'POST'])
def home():
    form = IndexForm()
    if request.method == 'POST':
        char = requests.get("http://service2:5000/get_chargen")
        num = requests.get("http://service3:5000/get_numgen")
        prize = requests.post("http://service4:5000/get_prize", json={"account_number" : char.text + num.text})
        return render_template('index.html', form=form, message = prize.text)
    return render_template('index.html', form=form, message = "")
