from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS
import json
import os
import sys
import requests_unixsocket
import requests
import time
import flask
import threading

try:
    from ..app import Sakura_io_com
    from ..app import BookShelf_CMD
    from .db_controler import XYTGrid
    from .db_controler import TASKGrid
except Exception:
    sys.path.append("/app/db_controler")
    sys.path.append("/app")
    import Sakura_io_com
    import BookShelf_CMD
    import XYTGrid
    import TASKGrid

app = flask.Blueprint('ACStaskreminder', __name__)


class activate_acs_RM(threading.Thread):
    def __init__(self):
        super(activate_acs_RM, self).__init__()
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        requests.post("http://nginx/ACS_taskreminder", data="NEXT")


@app.route('/ACS_taskreminder', methods=['POST'])
def ACSTaskReminder():
    print("TRMD")
    data = request.data.decode('utf-8')
    data = data.split(" ")
    if data[0] != "NEXT":  # This is just a temporary treatment
        return "error of ACS_taskreminder"  # todo
    while True:
        TaskRAW = TASKGrid.PopTASKGrid_least()
        if TaskRAW == "NULL":  # an unexpected value
            continue
        if TaskRAW["CMD"] == "NONE":  # command None
            continue
        Ret = json.dumps(TaskRAW)
        print(str(Ret) + "print ret")
        if Ret == None:  # an unexpected value
            continue
        print("before req to sakura")
        requests.post("http://nginx/Sakuraio", json=Ret)
        break
    requests.post("http://nginx/ACS_taskreminder", data="NEXT")
    return "sended"
