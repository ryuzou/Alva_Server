import flask
from flask import Flask, jsonify, request

app = flask.Blueprint('sakura_io_com', __name__)

@app.route("/api/sakura_iot")
def Sakura_io_com():
    return 0
