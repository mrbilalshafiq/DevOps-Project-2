from flask import Flask
from flask import render_template, redirect, url_for, request, Response
import random
import string

app = Flask(__name__)

@app.route('/get_chargen', methods=['GET'])
def chargen():
    rand = random.randint(2,3)
    final_char = ''
    for i in range(rand):
        char = random.choice(string.ascii_letters)
        i += 1
        final_char += char
    return Response(str.upper(final_char), mimetype ='text/plain')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
