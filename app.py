from flask import Flask, jsonify, abort, make_response, request, url_for
# from flask_httpauth import HTTPBasicAuth
#
from flask_cors import CORS,cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def home():
    return "Hello, World!"
if __name__ == "__main__":
    app.run(debug=True)
