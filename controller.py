import logging

from flask import jsonify
from flask_restful import Resource

from models import Task


class Welcome(Resource):
    @staticmethod
    def get():
        return "Welcome to Flask task-app"


class GetTasks(Resource):
    @staticmethod
    def get():
        try:
            # Fetch only the 'task' attribute from all tasks in the database
            tasks = Task.query.with_entities(Task.task).all()

            # Extract 'task' values from the query result
            task_list = [task[0] for task in tasks]

            # Return tasks as JSON response
            return jsonify({'tasks': task_list})
        except Exception as e:
            logging.error("An error occurred: " + str(e))
            return jsonify({'error': 'An error occurred while fetching tasks.'}), 500
