from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS
import json
import os
import sys
import requests
import time

try:
    from ..app import Sakura_io_com
    from ..app import BookShelf_CMD
    from .db_controler import XYTGrid
    from .db_controler import TASKGrid
    from .db_controler import COMMNADGrid
except Exception:
    sys.path.append("/app/db_controler")
    sys.path.append("/app")
    import Sakura_io_com
    import BookShelf_CMD
    import XYTGrid
    import TASKGrid
    import COMMNADGrid

app = Flask(__name__)
CORS(app)

app.register_blueprint(Sakura_io_com.app)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/ACStaskrmd/ACSTaskreminder/', methods=['POST'])
def ACSTASK():
    print("this is acstask")
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return jsonify(res='error'), 400
    data = request.data.decode('utf-8')
    data = json.loads(data)
    print(data)
    Lchannels = data["payload"]["channels"]
    print(Lchannels)
    priority = 0

    for cHannel in Lchannels:
        if int(cHannel["channel"]) == 126 and int(cHannel["value"]) == 9:
            TNcmd = COMMNADGrid.CMDGRID.PopCOMMANDGrid_least()
            if TNcmd == "NULL":
                return "null"
            Ncmd = int(TNcmd)
            ThisTASKGrid = TASKGrid.TaskGrid(Ncmd)
            while True:
                Dtask = ThisTASKGrid.PopTASKGrid_least()
                if Dtask == "NULL":
                    break
                Dtask["priority"] = priority
                priority = priority + 1
                print(Dtask)
                ret_json = json.dumps(Dtask)
                requests.post("http://nginx/ACStaskrmd/Sakuraio", json=ret_json)
        if int(cHannel["channel"]) == 126 and int(cHannel["value"]) == 0:
            dict = {}
            XYdone = 0
            for XYch in Lchannels:
                if int(XYch["channel"]) == 1:
                    dict["X"] = int(cHannel["value"])
                    XYdone = XYdone + 0.5
                if int(XYch["channel"]) == 2:
                    dict["Y"] = int(cHannel["value"])
                    XYdone = XYdone + 0.5
                if int(XYdone) == 1:
                    break
            ret_json = json.dumps(dict)
            requests.post("http://nginx/ACSinfo/XYC", json=ret_json)
    return request.data

if __name__ == "__main__":
    app.run()
