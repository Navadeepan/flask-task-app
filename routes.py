from flask_restful import Api

from controller import (GetTasks, Welcome, AddTask, UpdateTask, DeleteTask)


def generate_routes(app):
    # Create api.
    api = Api(app)
    api.add_resource(Welcome, '/')
    api.add_resource(GetTasks, '/tasks')
    api.add_resource(AddTask, '/tasks/add')
    api.add_resource(UpdateTask, '/tasks/update')
    api.add_resource(DeleteTask, '/tasks/delete')
