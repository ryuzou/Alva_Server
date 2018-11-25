from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS
import json
import os
import sys
import requests_unixsocket
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
app.register_blueprint(BookShelf_CMD.app)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/ACStaskrmd/ACSTaskreminder/', methods=['POST'])
def ACSTASK():
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return jsonify(res='error'), 400
    data = request.data.decode('utf-8')
    data = json.loads(data)
    print(data)
    Lchannels = data["payload"]["channels"]
    print(Lchannels)

    for cHannel in Lchannels:
        if int(cHannel["channel"]) == 126 and int(cHannel["value"]) == 9:
            Ncmd = int(COMMNADGrid.CMDGRID.PopCOMMANDGrid_least())
            ThisTASKGrid = TASKGrid.TaskGrid(Ncmd)
            while True:
                Dtask = ThisTASKGrid.PopTASKGrid_least()
                if Dtask == "NULL":
                    break
                print(Dtask)
                ret_json = json.dumps(Dtask)
                requests.post("http://nginx/ACStaskrmd/Sakuraio", json=ret_json)
        elif int(cHannel["channel"]) == 126 and int(cHannel["value"]) == 9:
            pass

    return request.data

if __name__ == "__main__":
    app.run()
