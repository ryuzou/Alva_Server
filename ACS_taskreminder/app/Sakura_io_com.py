import flask
from flask import Flask, jsonify, request
import requests
import json
import re
import websocket
import os
import copy
import threading

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

@app.route('/ACStaskrmd/Sakuraio', methods=['POST'])
def SakuraioTaskManage():
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return jsonify(res='error'), 400
    data = json.loads(json.loads(request.data))
    ret = {}
    Match_CMD_Sakura_dict = {
        "INSERTBOOK": "1",
        "EJECTBOOK": "2",
        "MOVARM": "3",
        "NONE": "0"
    }
    try:
        if Match_CMD_Sakura_dict[data["CMD"]] == 0:
            return "None"
        ret[0] = Match_CMD_Sakura_dict[data["CMD"]]
    except KeyError as e:
        print("error about command matching during sakuraio-send phase" + str(data))  # todo
    del data["CMD"]
    prioriry = int(data["priority"])
    del data["priority"]
    for name in data:
        num = int(re.split("arg", name)[1])
        ret[num] = data[name]
    ret["p"] = prioriry
    ret_json = json.dumps(ret)
    print("send to sakura-iot-send this" + str(ret_json))
    requests.post("http://nginx/ACStaskrmd/api/sakura_iot_send", json=ret_json)
    return "sakuraio finish"


@app.route("/ACStaskrmd/api/sakura_iot_send", methods=['POST'])
def Sakuraio_send():
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return ("error about none data" + str(request.data)), 400
    data = json.loads(json.loads(request.data))
    sakura_def_json = {
        "type": "channels",
        "module": "uEAfevTXx6db",  # Specific val
        "payload": {}
    }
    lchannels = []
    CHnum = {}
    priority = int(data["p"])
    del data["p"]
    for num in data:
        val = float(str("{:.5f}".format(float("0." + str(priority).zfill(5)))) + data[num])
        CHnum["channel"] = int(num)
        CHnum["value"] = val
        CHnum["type"] = "d"
        val = copy.deepcopy(CHnum)
        lchannels.append(val)
    channels = {
        "channels": lchannels
    }
    sakura_def_json["payload"] = channels
    sakura_send_json = json.dumps(sakura_def_json).encode("utf-8")
    print("i am sending this to sakuraio   " + str(sakura_send_json))
    ws = websocket.create_connection("wss://api.sakura.io/ws/v1/82d979f0-309d-4683-ad70-195d7af53314")
    ws.send(sakura_send_json)
    print("send" + str(sakura_send_json))
    return "sakuraiotsend finish"
