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
    if int(Lchannels[0]["channel"]) == 9 and int(Lchannels[0]["value"]) == 0:
        Ncmd = int(COMMNADGrid.CMDGRID.PopCOMMANDGrid_least())
        ThisTASKGrid = TASKGrid.TaskGrid(Ncmd)
        while True:
            Dtask = ThisTASKGrid.PopTASKGrid_least()
            if Dtask == {}:
                break
            print(Dtask)
    return request.data

if __name__ == "__main__":
    app.run()
