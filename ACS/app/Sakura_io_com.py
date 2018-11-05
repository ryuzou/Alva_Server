import flask
from flask import Flask, jsonify, request
import json

app = flask.Blueprint('sakura_io_com', __name__)

#################################################
'''
Sakura.io Rules
Channel_0 : Command (int)
    """
    """
Channel_N (1 <= N <= 7) : argN (int)
    """
    """
'''


#################################################


@app.route('/Sakuraio', methods=['POST'])
def SakuraioTaskManage():
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return jsonify(res='error'), 400
    data = request.data.decode('utf-8')
    data = json.loads(data)
    return "Hello Sakura!"  # this is a test


@app.route("/api/sakura_iot_send", methods=['POST'])
def Sakuraio_send():
    # todo
    return 0
