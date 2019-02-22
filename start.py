from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def __init__(self):

        self.additional_string = "Hello"

    def get(self, x):

        return x + self.additional_string



api.add_resource(Employees, '/employees/<x>')  # Route_1


if __name__ == '__main__':
    app.run(port=5003)