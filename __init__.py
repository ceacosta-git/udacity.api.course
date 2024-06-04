from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

def create_app(test_config=None):
    app = Flask(__name__)

    # CORS(app)
    # anyone can access resources under /api/
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    # CORS HEADERS
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route("/")
    def hello():
        return jsonify({"message": "Hello Carlos!"})
    
    @app.route("/smiley")
    def smiley():
        return "=)"
    
    @app.route("/cors_messages")
    @cross_origin()
    def messages():
        return "Getting CORS messages"

    return app
