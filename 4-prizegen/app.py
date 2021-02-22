from flask import Flask, render_template, redirect, url_for, request, Response
import random

app = Flask(__name__)

@app.route("/prize", methods=["GET","POST"])
def prize():
    bigprize = ["Yacht", "Rolls Royce", "£1,000,000", "Holiday to California", "Trip to Mars with SpaceX", "Neuralink Brain Chip"]
    smallprize = ["Vase", "£5 Amazon Gift Card", "Free Birthday Card on your Birthday", "50p", "Water Bottle", "Pencil"]
    account_number = request.get_json()
    if account_number["account_number"].startswith(("A", "E", "I", "O", "U")):
        prize = random.choice(bigprize)
    else:
        prize = random.choice(smallprize)
    return Response(str(prize), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, port=5003, host='0.0.0.0')
