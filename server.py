from flask import Flask, request, jsonify
from sms_module import SMS
from db_module import Database
from os import environ

from threading import Thread

import random

app = Flask(__name__)
app.secret_key = environ.get('SECRET_KEY')

# Generate OTP
def generate_otp():
    return random.randint(100000, 999999)

# Home page
@app.route('/')
def index():
    return "Hello, World!"

@app.route('/farmerLogin', methods=['POST'])
def farmer_login():
    data = request.json
    print(data)

    _otp = generate_otp()
    print(_otp)
    # Thread(target=SMS().send_message, args=(_otp, data['mobile'])).start()

    response = {
        'status': 'success',
        'otp': _otp
    }
    return jsonify(response)

@app.route('/buyerLogin', methods=['POST'])
def buyer_login():
    data = request.json
    print(data)



    response = {
        'status': 'success',
        'otp': _otp
    }
    return jsonify(response)

db = Database()

if __name__ == '__main__':
    app.run(debug=True)