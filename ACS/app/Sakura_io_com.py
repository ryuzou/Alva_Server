import flask
from flask import Flask, jsonify, request
import requests
import json
import re

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
        CHnum["channel"] = int(num)
        CHnum["value"] = float(data[num])
        CHnum["type"] = "f"
        channels.append(CHnum)
    sakura_def_json["payload"] = channels
    sakura_send_json = json.dumps(sakura_def_json)
    requests.post("https://api.sakura.io/incoming/v1/7686a2ac-31f2-4636-bcf7-e491854fc74f", json=sakura_send_json)
    return "send"
