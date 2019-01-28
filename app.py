from flask import Flask, jsonify, abort, make_response, request, url_for
from flask_httpauth import HTTPBasicAuth

from relation_extraction import relex
from flask_cors import CORS
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, World!"
if __name__ == "__main__":
    app.run(debug=True)
