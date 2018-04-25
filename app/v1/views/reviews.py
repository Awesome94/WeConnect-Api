import jsonschema
import os
import random
from flask import Flask, abort, jsonify, make_response, request
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, get_raw_jwt,
                                jwt_required)
from app import app
from app.schemas.review_schema import review_schema
from app.v1.models import WeConnect
from app.v1.validator import validate_schema
from app.v1.views import SECRET_KEY

app.config['JWT_SECRET_KEY'] = SECRET_KEY
jwt = JWTManager(app)
weconnect = WeConnect()

@app.route('/api/v1/businesses/<businessId>/reviews', methods=['POST'])
@jwt_required
@validate_schema(review_schema)
def set_review(businessId):
    """Adds a review to a business"""
    data = request.get_json()
    review = data['review']
    business_id = int(businessId)

    new_review = weconnect.add_review(business_id, random.randint(1, 500),
                                      review)
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