from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from settings import tasks_collection

tasks_blueprint = Blueprint('tasks', __name__)

# Criar uma tarefa (C)
@tasks_blueprint.route('/tasks', methods=['POST'])
def create_task():
    task = request.get_json()
    result = tasks_collection.insert_one(task)
    task['_id'] = str(result.inserted_id)
    return jsonify(task), 201

# Obter todas as tarefas (R)
@tasks_blueprint.route('/tasks/<user_id>', methods=['GET'])
def get_tasks(user_id):
    tasks = []
    for task in tasks_collection.find({"user_id": user_id}):  # filtrando as tarefas baseado no usuário autenticado
        task['_id'] = str(task['_id'])
        tasks.append(task)
    return jsonify(tasks), 200


# Atualizar uma tarefa (U)
@tasks_blueprint.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    updated_task = request.get_json()
    updated_task.pop('_id', None)  # Remove o campo '_id' se estiver presente
    tasks_collection.update_one({'_id': ObjectId(task_id)}, {'$set': updated_task})
    return jsonify(updated_task), 200


# Deletar uma tarefa (D)
@tasks_blueprint.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks_collection.delete_one({'_id': ObjectId(task_id)})
    return jsonify({'result': 'Task deleted'}), 200
