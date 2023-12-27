from flask import request
from flask_restful import Resource

from dbconfig import db
from models import Task


class Welcome(Resource):
    @staticmethod
    def get():
        return "Welcome to Flask task-app"


class GetTasks(Resource):
    @staticmethod
    def get():
        try:
            tasks = Task.query.all()
            tasks_list = [
                {
                    'task_name': task.task_name,
                    'created_date': task.created_date.strftime('%Y-%m-%d %H:%M:%S') if task.created_date else None
                }
                for task in tasks
            ]
            return tasks_list
        except Exception as e:
            return str(e)


class AddTask(Resource):
    @staticmethod
    def post():
        try:
            data = request.json
            task = Task(task_name=data.get('task_name'))
            db.session.add(task)
            db.session.commit()
            return GetTasks.get(), 201
        except Exception as e:
            return str(e)


class UpdateTask(Resource):
    @staticmethod
    def put():
        try:
            data = request.json
            task_id = request.args.get('id')
            task = Task.query.filter_by(id=task_id).first()
            task.task_name = data['task_name']
            db.session.commit()
            return GetTasks.get()
        except Exception as e:
            return str(e)


class DeleteTask(Resource):
    @staticmethod
    def delete():
        try:
            task_id = request.args.get('id')
            task = Task.query.filter_by(id=task_id).first()
            db.session.delete(task)
            db.session.commit()
            return GetTasks.get()
        except Exception as e:
            return str(e)
