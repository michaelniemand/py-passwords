from flask import Flask, request, jsonify
import secrets
import string
import os

app = Flask(__name__)

# get defaults from env vars
DEFAULT_LENGTH = os.getenv('DEFAULT_LENGTH', '12')
DEFAULT_SPECIAL = os.getenv('DEFAULT_SPECIAL', '0')
DEFAULT_NUMBERS = os.getenv('DEFAULT_NUMBERS', '0')
DEFAULT_COUNT = os.getenv('DEFAULT_COUNT', '1')
MAXLENGTH = os.getenv('MAXLENGTH', '64')
MAXCOUNT = os.getenv('MAXCOUNT', '100')

@app.route('/get-password')

def get_pw():
# get URL params
    param_length = request.args.get('length')
    param_special = request.args.get('special')
    param_numbers = request.args.get('numbers')
    param_pwcount = request.args.get('pwcount')

# use defaults if no params heve been provided
    param_length = DEFAULT_LENGTH if param_length is None else param_length
    param_special = DEFAULT_SPECIAL if param_special is None else param_special
    param_numbers = DEFAULT_NUMBERS if param_numbers is None else param_numbers
    param_pwcount = DEFAULT_COUNT if param_pwcount is None else param_pwcount

# validations: Integer, sane values
    try:
        param_length = int(param_length)
    except ValueError:
        msg = 'The length parameter must be an integer'
        return jsonify(msg), 400

    try:
        param_special = int(param_special)
    except ValueError:
        msg = 'The special parameter must be an integer'
        return jsonify(msg), 400

    try:
        param_numbers = int(param_numbers)
    except ValueError:
        msg = 'The numbers parameter must be an integer'
        return jsonify(msg), 400

    try:
        param_pwcount = int(param_pwcount)
    except ValueError:
        msg = 'The pwcount parameter must be an integer'
        return jsonify(msg), 400

    if param_special + param_numbers > param_length:
        msg = 'The length must not be smaller than the sum of numbers and special'
        return jsonify(msg), 400

    if param_length > int(MAXLENGTH):
        msg = 'The length must not be bigger than %s' % MAXLENGTH
        return jsonify(msg), 400

    if param_pwcount > int(MAXCOUNT):
        msg = 'The pwcount must not be bigger than %s' % MAXCOUNT
        return jsonify(msg), 400

    passwords = []

    for i in range(param_pwcount):

        alphabet_letters = string.ascii_letters
        alphabet_digits = string.digits
        alphabet_special = string.punctuation

        alphabet = alphabet_letters + alphabet_digits + alphabet_special

        while True:
            password = ''
            for i in range(param_length):
                password += ''.join(secrets.choice(alphabet))

            if (sum(char in alphabet_special for char in password)==param_special and 
                sum(char in alphabet_digits for char in password)==param_numbers and 
                not password.__contains__('\"') and
                not password.__contains__('\'')):
                    break

        passwords.append(password)

    return passwords

if __name__ == '__main__':
    app.run()
