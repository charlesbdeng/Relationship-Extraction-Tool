from flask import Flask, jsonify, abort, make_response, request, url_for
# from flask_httpauth import HTTPBasicAuth

from extraction_functions import entity_entity, relation_entity, all_ent_rel
from flask_cors import CORS

# auth = HTTPBasicAuth()
# @auth.get_password
# def get_password(username):
#     if username == "charles":
#         return 'sick'
#     return None
# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify({"error":"Unauthorized access"}), 401)

app = Flask(__name__)
CORS(app)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api/entity_entity', methods = ["POST"])
def ent_ent():
    if not request.json or len(request.json["text"]) == 0:
        abort(400)
    object = request.json
    text = object["text"]
    ent1_vals = object['entity_1_values']
    ent2_vals = object['entity_2_values']
    ent1_name = object['entity_1_name']
    ent2_name = object['entity_2_name']
    scope = object['scope']
    entities = entity_entity(ent1_name,ent2_name, ent1_vals,ent2_vals,text,scope)
    return jsonify({"data":entities})


@app.route('/api/relation_entity', methods = ["POST"])
def rel_ent():
    object = request.json
    text = object["text"]
    ent_values = object['entity_values']
    rel_values = object['relation_values']
    ent_name = object['entity_name']
    rel_name = object['relation_name']
    scope = object['scope']
    entities = relation_entity(ent_name,rel_name, ent_values, rel_values,text,scope)
    return jsonify({"data":entities})

@app.route('/api/all_entities_relations', methods = ["POST"])
def all():
    if not request.json:
        abort(400)
    if 'text' in request.json and type(request.json['text']) != unicode:
        abort(400)
    object = request.json
    text = object["text"]
    ent1_vals = object['entity_1_values']
    ent2_vals = object['entity_2_values']
    ent1_name = object['entity_1_name']
    ent2_name = object['entity_2_name']
    relation_vals = object["relation_values"]
    rel_name = object["relation_name"]
    scope = object['scope']
    entities = all_ent_rel(ent1_name, ent2_name, rel_name, ent1_vals,ent2_vals, relation_vals, text, scope)
    return jsonify({"data":entities})

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=False)
