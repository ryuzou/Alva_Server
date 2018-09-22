import flask
from flask import Flask, jsonify, request
import json

app = flask.Blueprint('book_cmd', __name__)


@app.route("/cmd/bookshelf", methods=['GET'])
def RouteBookShelfMiddleCMD():
    date = json.loads(request.data)
