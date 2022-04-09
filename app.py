from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with
import jsonify

app = Flask(__name__)
api = Api(app)

resource_fields = {
    'task':   fields.String
}

class TodoDao:
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'

class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')

class Todos(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return TODOS_ALL


class CountryDao:
    def __init__(
        self, name: str, alpha_2_code: str, alpha_3_code: str, currencies: list
    ):
        self.name = name
        self.alpha_2_code = alpha_2_code
        self.alpha_3_code = alpha_3_code
        self.currencies = currencies


COUNTRIES = [
    CountryDao("United States of America", "US", "USA", ["USD"]),
    CountryDao("Ukraine", "UA", "UKR", ["UAH"]),
]

TODOS_ALL = [
    TodoDao("1", "laundry"),
    TodoDao("2", "dishes")
]

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

class CountryResource(Resource):
    def get(self):
        return TODOS

api.add_resource(CountryResource, "/countries")
api.add_resource(Todo, "/todo")
api.add_resource(Todos, "/todos")

if __name__ == "__main__":
    app.run(debug=True)
