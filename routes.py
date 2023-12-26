from flask_restful import Api

from controller import (GetTasks, Welcome)


def generate_routes(app):
    # Create api.
    api = Api(app)
    api.add_resource(Welcome, '/')
    api.add_resource(GetTasks, '/tasks')
