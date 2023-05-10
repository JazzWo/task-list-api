from flask import Blueprint, jsonify, make_response, request
from app import db
from app.models.task import Task
from app.helper import validate_id

tasks_bp = Blueprint("tasks", __name__, url_prefix="/tasks")

#get all tasks-"/tasks"-GET(read)
@tasks_bp.route("", methods=["GET"])
def get_all_tasks():
    tasks_response = []
    tasks = Task.query.all()
    for task in tasks:
        tasks_response.append(task.to_dict())
    return jsonify(tasks_response), 200


#get one tasks-"/tasks/1"-GET(read)
@tasks_bp.route("/<id>", methods=["GET"])
def get_task(id):
    task = validate_id(id)
    return jsonify({"task":task.to_dict()}), 200


#create task-"/tasks"-POST(create)
@tasks_bp.route("", methods=["POST"])
def create_task():
    request_body = request.get_json()
    try:
        new_task = Task.create(request_body)
    except KeyError:
        return make_response({"details": "Invalid data"}), 400
    
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"task":new_task.to_dict()}), 201


#update task-"tasks/1"-PUT(update)
@tasks_bp.route("/<id>", methods=["PUT"])
def update_task(id):
    task = validate_id(id)
    request_body = request.get_json()
    task.update(request_body)
    db.session.commit()
    return jsonify({"task":task.to_dict()}), 200


#delete task-"tasks/1"-DELETE(delete)
@tasks_bp.route("/<id>", methods=["DELETE"])
def delete_task(id):
    task = validate_id(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"details": f'Task {id} "{task.to_dict()["title"]}" successfully deleted'})








