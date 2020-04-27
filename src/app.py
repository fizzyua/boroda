from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'Hello world'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
