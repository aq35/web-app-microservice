from flask import Flask, render_template
  
# frontend (vite+vue)のリソースを渡すのが役目
app = Flask(__name__, static_folder='../frontend/dist/assets', template_folder='../frontend/dist')
from flask import Flask, render_template, send_from_directory

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/<path:filename>', methods=['GET'])
def resource(filename):
    return send_from_directory("../frontend/dist", filename)

@app.route('/assets/<path:filename>', methods=['GET'])
def assets_resource(filename):
    return send_from_directory("../frontend/dist/assets", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)