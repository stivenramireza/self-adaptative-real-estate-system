from flask import Flask
from flask import jsonify
from firebase_admin import credentials, firestore, initialize_app
import firebase_admin

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

# Initialize Firestore DB
cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)
#default_app = initialize_app(cred)
db = firestore.client()
inmuebles = db.collection('Inmuebles')


@app.route('/api/v1/control/', methods=['POST'])    
def create_user():
    
    all_inmuebles = [doc.to_dict() for doc in inmuebles.stream()]
    return jsonify(all_inmuebles), 200

#    response = {'message': 'successPOST'}
#    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)