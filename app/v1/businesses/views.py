import os
import random
from flask import Flask, abort, jsonify, make_response, request
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, get_raw_jwt,
                                jwt_required)

from app import app
from app.v1.models import WeConnect

app.config['JWT_SECRET_KEY'] = os.urandom(23)
jwt = JWTManager(app)
weconnect = WeConnect()

@app.route('/api/v1/businesses', methods=['GET'])
@jwt_required
def get_businesses():
    """Returns all businesses"""
    businesses = weconnect.get_businesses()
    return jsonify({'businesses': businesses})


@app.route('/api/v1/businesses/<businessId>', methods=['GET'])
@jwt_required
def get_business(businessId):
    """Returns a specific business"""
    business = weconnect.get_business(int(businessId))
    if business is None:
        abort(404)
    return jsonify({'business': business})


@app.route('/api/v1/businesses', methods=['POST'])
@jwt_required
def register_business():
    """Registers a business"""
    data = request.get_json()
    name = data['name']
    location = data['location']
    description = data['description']
    category = data['category']
    current_user = get_jwt_identity()
    user_id = current_user
    if not data or not name:
        abort(400)
    if name is not None or description is not None or location is not None or category is not None:
        new_business = weconnect.create_business(
            user_id, random.randint(
                1, 500), name, location, category, description)
        return jsonify({'business': new_business}), 201
    return jsonify({"response": "Empty value entered"}), 400


@app.route('/api/v1/businesses/<businessId>', methods=['PUT'])
@jwt_required
def update_business(businessId):
    """Updates a business"""
    if int(businessId) == 0:
        abort(404)
    data = request.get_json()
    name = data['name']
    location = data['location']
    description = data['description']
    category = data['category']
    current_user = get_jwt_identity()
    user_id = current_user
    if not data:
        abort(400)
    if name and isinstance(name, str) == False:
        abort(400)
    if description and isinstance(name, str) == False:
        abort(400)
    if location and isinstance(location, str) == False:
        abort(400)
    if category and isinstance(category, str) == False:
        abort(400)

    if name is not None or description is not None or location is not None or category is not None:
        business = weconnect.update_business(
            user_id, int(businessId), name, location, description, category)
        return jsonify(business), 201


@app.route('/api/v1/businesses/<businessId>', methods=['DELETE'])
@jwt_required
def delete_business(businessId):
    """Deletes a business"""
    if int(businessId) == 0:
        abort(404)

    current_user = get_jwt_identity()
    user_id = current_user
    delete_business = weconnect.delete_business(user_id, int(businessId))
    if delete_business:
        return jsonify({'message': 'Business deleted'})


@app.route('/api/v1/businesses/<businessId>/reviews', methods=['POST'])
@jwt_required
def set_review(businessId):
    """Adds a review to a business"""
    data = request.get_json()
    review = data['review']

    if not data or review:
        abort(400)
    business_id = int(businessId)
    new_review = weconnect.add_review(business_id, random.randint(1, 500),
                                      review)
    if new_review is None:
        abort(404)
    return jsonify(new_review), 201


@app.route('/api/v1/businesses/<businessId>/reviews', methods=['GET'])
@jwt_required
def get_reviews(businessId):
    """Returns reviews for the specified business"""
    reviews = weconnect.get_reviews(int(businessId))
    return jsonify({'business': reviews})

@app.errorhandler(404)
def not_found(error):
    """This is the error handler"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
