from os import environ

from flask import Flask
from flask_restful import Api

from handlers.errors import *
from resources.index_v4 import IndexResource

app = Flask(__name__)
api = Api(app)


@app.route("/")
def hello():
    """Root route.

    Returns:
        Str: Simple hello world response
    """
    return "Hello World!"

api.add_resource(IndexResource, '/api/v1/index')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(environ.get('PORT', 8080)))
