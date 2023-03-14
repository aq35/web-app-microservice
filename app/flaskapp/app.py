from flask import Flask, render_template, send_from_directory, request, session
from flask_cors import CORS
from utils.logging_utils import logger
from helper import app_json_response
from Service.UserService import UserService

app = Flask(__name__)

# frontend (vite+vue)のリソースを渡すのが役目
app.static_folder = "./frontend/dist/assets"
app.template_folder = "./frontend/dist"

CORS(app, origins=["http://localhost:5173"])  # CORS 対応

@app.after_request
def after_request(response):
    response.headers.update(
        {
            "Access-Control-Allow-Headers": "Content-Type, Authorization",
            "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,OPTIONS",
        }
    )
    return response

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    logger.info('Hello World!')
    return render_template("index.html")

@app.route("/<path:filename>", methods=["GET"])
def resource(filename):
    return send_from_directory("./frontend/dist", filename)

@app.route("/assets/<path:filename>", methods=["GET"])
def assets_resource(filename):
    return send_from_directory("./frontend/dist/assets", filename)

@app.route("/api/user", methods=["POST"])
def get_user():
    user_service = UserService()
    user = user_service.create_user('John', 'john@example.com')
    return app_json_response(user)

app.add_url_rule('/api/user', view_func=get_user, endpoint='get_user')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)