from flask import Flask, render_template, send_from_directory, jsonify, request
from flask_cors import CORS

# frontend (vite+vue)のリソースを渡すのが役目
app = Flask(__name__, static_folder='./frontend/dist/assets', template_folder='./frontend/dist')

CORS(app, origins=["http://localhost:5173"]) # CORS 対応
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@app.route('/<path:filename>', methods=['GET'])
def resource(filename):
    return send_from_directory("../frontend/dist", filename)

@app.route('/assets/<path:filename>', methods=['GET'])
def assets_resource(filename):
    return send_from_directory("../frontend/dist/assets", filename)

# WEB-API定義
@app.route('/api/user', methods=['POST'])
def get_user():
    return jsonify({"message": "aa43"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)