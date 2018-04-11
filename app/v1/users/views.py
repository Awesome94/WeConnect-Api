import os
import random
from flask import Flask, abort, jsonify, make_response, request
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, get_raw_jwt,
                                jwt_required)

from app import app
from app.schemas.user_schema import user_schema
from app.schemas.login_schema import login_schema
from app.schemas.reset_schema import reset_schema
from app.v1.models import WeConnect
from app.v1.validator import validate_schema
from validate_email import validate_email

app.config['JWT_SECRET_KEY'] = os.urandom(23)
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
jwt = JWTManager(app)

blacklist = set()
weconnect = WeConnect()


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist


@app.route('/api/v1/auth/register', methods=['POST'])
@validate_schema(user_schema)
def register_user():
    data = request.get_json()
    email = data['email']
    first_name = data['first_name']
    last_name = data['last_name']
    password = data['password']
    if validate_email(email) == False:
        abort(400)
    new_user = weconnect.register_user(random.randint(1, 500),
                                       first_name, last_name, email, password)
    if new_user:
        return jsonify({'message': 'Success'}), 200


@app.route('/api/v1/auth/login', methods=['POST'])
@validate_schema(login_schema)
def login_user():
    data = request.get_json()
    email = data['email']
    password = data['password']
    user = weconnect.login_user(email, password)
    if user:
        access_token = create_access_token(identity=user)
        if access_token in blacklist:
            return jsonify({'message': 'Invalid token'})
        return jsonify(access_token=access_token), 200
    else:
        abort(404)


@app.route('/api/v1/auth/logout', methods=['POST'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return jsonify({"msg": "Successfully logged out"}), 200


@app.route('/api/v1/auth/reset-password', methods=['POST'])
@jwt_required
@validate_schema(reset_schema)
def reset_password():
    data = request.get_json()
    email = data['email']
    password = data['password']
    new_password = data['new_password']
    user = weconnect.reset_password(email, password, new_password)
    if user:
        return jsonify({'message': 'Successfully updated password'}), 200
    return jsonify(
        {'message': 'Supply your password and/or a new password'}), 401


@app.errorhandler(404)
def not_found(error):
    """This is the error handler"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
