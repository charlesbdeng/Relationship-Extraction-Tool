from flask import Flask, jsonify, abort, make_response, request, url_for
# from flask_httpauth import HTTPBasicAuth

from relation_extraction import entity_entity, relation_entity, all_ent_rel
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




tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },

    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
# @auth.login_required
def get_tasks():
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# @app.route('/todo/api/v1.0/tasks', methods=['POST'])
# def create_task():
#     if not request.json or not 'title' in request.json:
#         abort(400)
#     task = {
#         'id': tasks[-1]['id'] + 1,
#         'title': request.json['title'],
#         'description': request.json.get('description', ""),
#         'done': False
#     }
#     tasks.append(task)
#     return jsonify({'task': task}), 201


@app.route('/api/entity_entity', methods = ["POST"])
def ent_ent():
    # if not request.json or len(request.json["text"]) == 0:
    #     abort(400)
    object = request.json
    text = object["text"]
    ent1_vals = object['entity_1_values']
    ent2_vals = object['entity_2_values']
    ent1_name = object['entity_1_name']
    ent2_name = object['entity_2_name']
    scope = object['scope']
    entities = entity_entity(ent1_name,ent2_name, ent1_vals,ent2_vals,text,scope)
    # print(type(ent2_vals))
    # print(type(ent1_name))
    return jsonify({"data":entities})


@app.route('/api/relation_entity', methods = ["POST"])
def rel_ent():
    # if not request.json or len(request.json["text"]) == 0:
    #     abort(400)
    object = request.json
    text = object["text"]
    ent_values = object['entity_values']
    rel_values = object['relation_values']
    ent_name = object['entity_name']
    rel_name = object['relation_name']
    scope = object['scope']
    entities = relation_entity(ent_name,rel_name, ent_values, rel_values,text,scope)
    # print(type(ent2_vals))
    # print(type(ent1_name))
    return jsonify({"data":entities})

    # return jsonify({"data":object})


    # return jsonify({"data": object})


@app.route('/api/all_entities_relations', methods = ["POST"])
def all():
    # if not request.json or len(request.json["text"]) == 0:
    #     abort(400)
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
    # print(type(ent2_vals))
    # print(type(ent1_name))
    return jsonify({"data":entities})

    # return jsonify({"text":text}),200
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    return "Testi"

@app.route('/bad')
def bad():
    return "bad"

if __name__ == '__main__':
    app.run(debug=False)
