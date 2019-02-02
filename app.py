from flask import Flask, jsonify, abort, make_response, request
from extraction_functions import entity_entity, relation_entity, all_ent_rel
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
#extracts relation if two entities are given
@app.route('/api/entity_entity', methods = ["POST"])
def ent_ent():
    if not request.json:
        abort(400)
    text = request.json["text"]
    ent1_vals = request.json['entity_1_values']
    ent2_vals = request.json['entity_2_values']
    ent1_name = request.json['entity_1_name']
    ent2_name = request.json['entity_2_name']
    scope = request.json['scope']
    entities = entity_entity(ent1_name,ent2_name, ent1_vals,ent2_vals,text,scope)
    return jsonify({"data":entities})

#extracts an entity related to another entity if an entity and relation are given
@app.route('/api/relation_entity', methods = ["POST"])
def rel_ent():
    if not request.json:
        abort(400)
    text = request.json["text"]
    ent_values = request.json['entity_values']
    rel_values = request.json['relation_values']
    ent_name = request.json['entity_name']
    rel_name = request.json['relation_name']
    scope = request.json['scope']
    entities = relation_entity(ent_name,rel_name, ent_values, rel_values,text,scope)
    return jsonify({"data":entities})

#extracts all sentences containing the given entity, relation, and entity
@app.route('/api/all_entities_relations', methods = ["POST"])
def find_all():
    if not request.json:
        abort(400)
    text = request.json["text"]
    ent1_vals = request.json['entity_1_values']
    ent2_vals = request.json['entity_2_values']
    ent1_name = request.json['entity_1_name']
    ent2_name = request.json['entity_2_name']
    relation_vals = request.json["relation_values"]
    rel_name = request.json["relation_name"]
    scope = request.json['scope']
    entities = all_ent_rel(ent1_name, ent2_name, rel_name, ent1_vals,ent2_vals, relation_vals, text, scope)
    return jsonify({"data":entities})

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=False)
