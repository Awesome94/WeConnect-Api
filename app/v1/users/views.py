import os
import random
from flask import Flask, abort, jsonify, make_response, request
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, get_raw_jwt,
                                jwt_required)

from app import app
from app.v1.models import WeConnect

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
def register_user():
    data = request.get_json()
    email = data['email']
    first_name = data['first_name']
    last_name = data['last_name']
    password = data['password']
    if not data or not email:
        abort(400)
    if email is None:
        abort(400)
    new_user = weconnect.register_user(random.randint(1, 500),
                                       first_name, last_name, email, password)
    if new_user:
        return jsonify({'message': 'Successfully created user'}), 200


@app.route('/api/v1/auth/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data['email']
    password = data['password']
    if not data or not email:
        abort(400)
    user = weconnect.login_user(email, password)
    if user:
        access_token = create_access_token(identity=user)
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
def reset_password():
    data = request.get_json()
    email = data['email']
    password = data['password']
    new_password = data['new_password']
    if not data or not email or not password or not new_password:
        return jsonify(
            {'message': 'Supply your password and/or a new password'}), 401
    user = weconnect.reset_password(email, password, new_password)
    if user:
        return jsonify({'message': 'Successfully updated password'}), 200
    else:
        return jsonify(
            {'message': 'Supply your password and/or a new password'}), 401


@app.errorhandler(404)
def not_found(error):
    """This is the error handler"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
