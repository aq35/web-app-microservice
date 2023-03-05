from flask import Flask, render_template
  
# frontend と通信をするのが役目
app = Flask(__name__)
@app.route("/test")
def index():
    return jsonify({"language": "python"})

if __name__ == "__main__":
    app.run(port=8888)