import flask
from flask import Flask, jsonify, request

app = flask.Blueprint('sakura_io_com', __name__)


@app.route('/Sakuraio', methods=['GET'])
def SakuraioTaskManage():
    # todo
    return "Hello Sakura!"  # this is a test


@app.route("/api/sakura_iot_send")
def Sakuraio_send():
    # todo
    return 0
