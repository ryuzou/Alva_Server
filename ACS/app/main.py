from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS
import json
import os
import sys
import requests_unixsocket

try:
    from ..app import Sakura_io_com
    from ..app import BookShelf_CMD
except Exception:
    import Sakura_io_com
    import BookShelf_CMD

import requests

app = Flask(__name__)
CORS(app)

app.register_blueprint(Sakura_io_com.app)
app.register_blueprint(BookShelf_CMD.app)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def error():
    return 0


@app.route('/ACS', methods=['POST'])
def ACSTaskManager():
    data = request.data.decode('utf-8')
    tasks = data.split(" ")
    ret = json.dumps(tasks)
    retval = None
    prefix = tasks[0]

    def showinfo(Lsufix):
        return Lsufix

    def getData(Lsufix):
        return Lsufix
    prefix_map = {
        "show": showinfo,
        "getdata": getData
    }
    try:
        ret = prefix_map[prefix](tasks[1:])
        retval = json.dumps(ret)
    except KeyError as e:
        retval = ret
    return retval


@app.route('/', methods=['POST'])
def TaskManage():
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return jsonify(res='error'), 400
    data = request.data.decode('utf-8')
    data = json.loads(data)
    cmd = data['cmd']
    ret = requests.post("http://nginx/ACS", cmd)
    print(ret.text)
    return ret.text


if __name__ == "__main__":
    app.run()
