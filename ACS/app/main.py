from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
import sys

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


@app.route('/ACS', methods=['POST'])  # Frontend first connects to this at first
def ACSTaskManager():
    print(request.data)
    # todo
    return 0


@app.route('/', methods=['POST'])
def TaskManage():
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return jsonify(res='error'), 400
    data = request.data.decode('utf-8')
    data = json.loads(data)
    cmd = data['cmd']
    requests.post("http://localhost:8182/ACS", cmd)

if __name__ == "__main__":
    app.run()
