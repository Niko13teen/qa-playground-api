import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask import Flask, render_template, request
from flask_restful import Api, Resource, reqparse
from models import Users


app = Flask(__name__)
api = Api()

@app.route('/')
def index():
    return render_template('index.html')

api.add_resource(Users, "/api/users/<int:user_id>")
api.init_app(app)


if __name__ == '__main__':
    app.run(debug=True, port=3000)

