from flask import abort, Flask, jsonify, make_response, request

app = Flask(__name__)

BUSINESSES = [
    {
        'id': 1,
        'name': 'Karunhanga & Sons Hardware Store',
        'description': 'We deal in hardware of all kinds',
        'location': 'Kitojo',
        'category': 'Hardware'
    }
]

@app.route('/api/v1/businesses', methods=['GET'])
def get_businesses():
    """Returns all businesses"""
    return jsonify({'businesses': BUSINESSES})

@app.route('/api/v1/businesses/<businessId>', methods=['GET'])
def get_business(businessId):
    """Returns a specific business"""
    business = [business for business in BUSINESSES if business['id'] == businessId]
    if len(business) == 0:
        abort(404)
    return jsonify({'business': business[0]})

@app.route('/api/v1/businesses', methods=['POST'])
def register_business():
    """Registers a business"""
    if not request.json or not 'name' in request.json:
        abort(400)
    business = {
        'id': BUSINESSES[-1]['id'] + 1,
        'name': request.json['name'],
        'description': request.json.get('description', ""),
        'location': request.json.get('location', ""),
        'category': request.json.get('category', "")
    }
    BUSINESSES.append(business)
    return jsonify({'business': business}), 201

@app.route('/api/v1/businesses/<businessId>', methods=['PUT'])
def update_business(businessId):
    """Updates a business"""
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

@app.route('/api/v1//businesses/<businessId>', methods=['DELETE'])
def delete_business(businessId):
    """Deletes a business"""
    business = [business for business in BUSINESSES if business['id'] == businessId]
    if len(business) == 0:
        abort(404)
    BUSINESSES.remove(business[0])
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    """This is the error handler"""
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
