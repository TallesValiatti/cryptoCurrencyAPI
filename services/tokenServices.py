import jwt
from flask import Flask
import datetime
from flask import jsonify
from functools import wraps
from flask import request

class TokenServices(object):

    #private token
    key = "132456789abcdef"
    user = "talles"
    password = "123"

    @staticmethod
    def GenerateToken():
        token = jwt.encode({'username':  TokenServices.user,'exp': datetime.datetime.now() + datetime.timedelta(minutes=181) },TokenServices.key)
        return jsonify({'message': 'Validated successfully', 'token': token.decode('UTF-8'),
                        'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})

    #veify if the user exists
    @staticmethod
    def auth(user, password):
        if(user == TokenServices.user and password ==  TokenServices.password):
            print("true")
            return True
        else:
            print("false")
            return False
    
    def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.args.get('token')
            if not token:
                return jsonify({'message': 'token is missing', 'data': []}), 401
            try:
                data = jwt.decode(token, TokenServices.key)
                current_user = TokenServices.user
            except Exception as e:
                print(e)
                return jsonify({'message': 'token is invalid or expired', 'data': []}), 401
            return f(current_user, *args, **kwargs)
        return decorated
