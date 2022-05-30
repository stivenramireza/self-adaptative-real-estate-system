from flask import request, jsonify
from flask.wrappers import Response

from src.app import create_app
from src.services.property_service import PropertyService


app = create_app()


@app.route('/')
def index() -> Response:
    return (
        jsonify(
            {
                'message': 'Self-adaptative real estate API is running successfully'
            }
        ),
        200,
    )


@app.route('/api/v1/control', methods=['POST'])
def control_property_variables() -> Response:
    property_id = request.json.get('property_id')

    property_service = PropertyService()
    property = property_service.control_property_variables(property_id)

    return jsonify(property), 200


@app.errorhandler(404)
def not_found() -> Response:
    return jsonify({'message': 'Resource not found'}), 404


@app.errorhandler(500)
def internal_server_error() -> Response:
    return jsonify({'message': 'Internal server error'}), 500
