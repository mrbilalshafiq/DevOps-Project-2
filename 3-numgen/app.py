from flask import Flask
from flask import render_template, redirect, url_for, request, Response
import random
import string

app = Flask(__name__)

@app.route('/get_numgen', methods=['GET'])
def numgen():
    rand = random.randint(6,8)
    final_num = ''
    for i in range(rand):
        num = random.randrange(0,9)
        i += 1
        final_num += str(num)
    return Response(final_num , mimetype ='text/plain')

if __name__ == '__main__':
    app.run(debug=True, port=5002, host='0.0.0.0')
