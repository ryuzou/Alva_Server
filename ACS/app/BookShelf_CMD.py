import flask
from flask import Flask, jsonify, request
import json

app = flask.Blueprint('book_cmd', __name__)

@app.route("/cmd/bookshelf", methods=['POST'])
def RouteBookShelfCMD():
    data = json.loads(request.data)
    prefix = data[0]
    prefix_map = {

    }
