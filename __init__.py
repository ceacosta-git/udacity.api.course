from flask import Flask, jsonify, request, abort
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
    
    @app.route("/url_path_parameters/<int:param_id>")
    def url_path_parameters(param_id: int):
        return jsonify({"param_id": param_id})
    
    @app.route("/url_query_parameters")
    def url_query_parameters():
        page_val = request.args.get("page", type=int)
        return f"Query param [page]={page_val}"
    
    @app.route("/greetings", methods=['GET', 'POST'])
    def greetings():
        if request.method == 'POST':
            return "Creating a greeting!"
        else:
            return "Retrieving a greeting!"
        
    @app.route('/abort_error_handlers')
    def aborts_errors_handles():
        abort(404)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": 'Not found'
        }), 404


    return app
