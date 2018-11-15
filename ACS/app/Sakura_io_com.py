import flask
from flask import Flask, jsonify, request
import requests
import json
import re
import websocket
import os

app = flask.Blueprint('sakura_io_com', __name__)

#################################################
'''
Sakura.io Rules:
Channel_0 : Command (int)
    """
    """
Channel_N (1 <= N <= 7) : argN (int)
    """
    """
'''
'''
Sakura.io val Rules:
val = "id(len = 5)" + val
'''
#################################################

@app.route('/Sakuraio', methods=['POST'])
def SakuraioTaskManage():
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return jsonify(res='error'), 400
    data = request.data.decode('utf-8')
    data = json.loads(data)
    ret = {}
    Match_CMD_Sakura_dict = {
        "INSERT": 1,
        "EJECT": 2,
        "MOVARM": 3,
        "NONE": 0
    }
    try:
        if Match_CMD_Sakura_dict[data["CMD"]] == 0:
            return "None"
        ret[0] = Match_CMD_Sakura_dict[data["CMD"]]
    except KeyError as e:
        print("eroor")  # todo
    del data["CMD"]
    for name in data:
        num = int(re.split("arg", name)[1])
        ret[num] = data[name]
    ret_json = json.dumps(ret)
    return requests.post("http://nginx/api/sakura_iot_send", json=ret_json)

@app.route("/api/sakura_iot_send", methods=['POST'])
def Sakuraio_send():
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return jsonify(res='error'), 400
    data = request.data.decode('utf-8')
    data = json.loads(data)
    sakura_def_json = {
        "type": "channels",
        "module": "fRpa8YcKHR",  # Specific val
        "payload": {}
    }
    channels = []
    CHnum = {}
    for num in data:
        val = float(str("{:.5f}".format(float("0." + str(os.getpid()).zfill(5)))) + str(data[num]))
        CHnum["channel"] = int(num)
        CHnum["value"] = val
        CHnum["type"] = "d"
        channels.append(CHnum)
    sakura_def_json["payload"] = channels
    sakura_send_json = json.dumps(sakura_def_json).encode("utf-8")
    ws = websocket.create_connection("wss://api.sakura.io/ws/v1/82d979f0-309d-4683-ad70-195d7af53314")
    ws.send(sakura_send_json)
    return "send"


@app.route("/api/sakura_iot_recieve", methods=['GET', 'POST'])  # Secret key is Alva63th
def Sakuraio_recieve():
    pass  # todo
