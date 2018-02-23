import os
from app import app
from flask import abort, Flask, jsonify, make_response, request
from .app_class import WeConnect

weconnect = WeConnect()

@app.route('/', methods=['GET'])
def test():
    return "Something"

@app.route('/api/v1/auth/register', methods=['POST'])
def register_user():
    pass

@app.route('/api/auth/login', methods=['POST'])
def login_user():
    pass

@app.route('/api/auth/logout', methods=['POST'])
def logout():
    pass

@app.route('/api/auth/reset-password', methods=['POST'])
def reset_password():
    pass

@app.route('/api/v1/businesses', methods=['GET'])
def get_businesses():
    """Returns all businesses"""
    businesses = weconnect.get_businesses()
    return jsonify({'businesses': businesses})

@app.route('/api/v1/businesses/<businessId>', methods=['GET'])
def get_business(businessId):
    """Returns a specific business"""
    business = weconnect.get_business(businessId)
    if len(business) == 0:
        abort(404)
    return jsonify({'business': business[0]})

@app.route('/api/v1/businesses', methods=['POST'])
def register_business():
    """Registers a business"""
    if not request.json or not 'name' in request.json:
        abort(400)
    name = request.json['name']
    location = request.json['location']
    description = request.json['description']
    category = request.json['category']
    user_email = request.json['email']
    new_business = weconnect.create_business(name, location, category, description, user_email)
    return jsonify({'business': new_business}), 201

"""
@app.route('/api/v1/businesses/<businessId>', methods=['PUT'])
def update_business(businessId):
    Updates a business
    business = [business for business in BUSINESSES if business['id'] == businessId]
    if len(business) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and isinstance((request.json['name']), str):
        abort(400)
    if 'description' in request.json and isinstance((request.json['description']), str):
        abort(400)
    if 'location' in request.json and isinstance((request.json['location']), str):
        abort(400)
    if 'category' in request.json and isinstance((request.json['category']), str):
        abort(400)
    business[0]['name'] = request.json.get('name', business[0]['name'])
    business[0]['description'] = request.json.get('description', business[0]['description'])
    business[0]['location'] = request.json.get('location', business[0]['location'])
    business[0]['category'] = request.json.get('category', business[0]['category'])
"""
"""
@app.route('/api/v1//businesses/<businessId>', methods=['DELETE'])
def delete_business(businessId):
    Deletes a business
    business = [business for business in BUSINESSES if business['id'] == businessId]
    if len(business) == 0:
        abort(404)
    BUSINESSES.remove(business[0])
    return jsonify({'result': True})
"""
@app.errorhandler(404)
def not_found(error):
    """This is the error handler"""
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)