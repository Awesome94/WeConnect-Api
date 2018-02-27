import os, random
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
    business = weconnect.get_business(int(businessId))
    if business is None:
        abort(404)
    return jsonify({'business': business})

@app.route('/api/v1/businesses', methods=['POST'])
def register_business():
    """Registers a business"""
    if not request.json or not 'name' in request.json:
        abort(400)
    name = request.json['name']
    location = request.json['location']
    description = request.json['description']
    category = request.json['category']
    new_business = weconnect.create_business(random.randint(1, 500), name, location, category, description)
    return jsonify({'business': new_business}), 201


@app.route('/api/v1/businesses/<businessId>', methods=['PUT'])
def update_business(businessId):
    """Updates a business"""
    if int(businessId) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and isinstance((request.json['name']), str)  == False:
        abort(400)
    if 'description' in request.json and isinstance((request.json['description']), str) == False:
        abort(400)
    if 'location' in request.json and isinstance((request.json['location']), str) == False:
        abort(400)
    if 'category' in request.json and isinstance((request.json['category']), str) == False:
        abort(400)

    name = request.json['name']
    description = request.json['description']
    location = request.json['location']
    category = request.json['category']

    if name is not None or description is not None or location is not None or category is not None:
        business = weconnect.update_business(int(businessId), name, location, description, category)
        return jsonify(business)

@app.route('/api/v1//businesses/<businessId>', methods=['DELETE'])
def delete_business(businessId):
    """Deletes a business"""
    if int(businessId) == 0:
        abort(404)
   # if not request.json:
       # abort(400)

    delete_business = weconnect.delete_business(int(businessId))
    if delete_business:
        return jsonify({'message': 'Business deleted'})

@app.errorhandler(404)
def not_found(error):
    """This is the error handler"""
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)