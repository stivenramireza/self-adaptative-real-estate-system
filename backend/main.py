import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, request
from flask import jsonify


def create_app():
    app = Flask(__name__)
    return app


app = create_app()

# Initialize Firestore DB
cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)
# default_app = initialize_app(cred)
db = firestore.client()
properties = db.collection('Inmuebles')


@app.route('/api/v1/control/', methods=['POST'])
def create_user():
    body = request.json
    property_id = body.get('property_id')

    property = properties.document(property_id).get().to_dict()
    visits = property.get('Visits')

    property.update({'Visits': visits + 1})

    properties.document(property_id).update(property)

    property = properties.document(property_id).get().to_dict()

    if property.get('Visits') % 5 == 0:
        price = property.get('Price')
        property.update({'Price': price + 100_000})
        properties.document(property_id).update(property)

    return jsonify(property), 200


if __name__ == '__main__':
    app.run()
