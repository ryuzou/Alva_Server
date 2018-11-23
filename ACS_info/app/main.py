from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS
import json
import os
import sys
import requests_unixsocket
import requests
import time

try:
    from ..app import BookShelf_CMD
    from .db_controler import XYTGrid
    from .db_controler import TASKGrid
    from ..app import acs_taskreminder
except Exception:
    sys.path.append("/app/db_controler")
    sys.path.append("/app")
    import BookShelf_CMD
    import XYTGrid
    import TASKGrid
    import acs_taskreminder

app = Flask(__name__)
CORS(app)

app.register_blueprint(BookShelf_CMD.app)
app.register_blueprint(acs_taskreminder.app)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/ACSinfo/', methods=['POST', 'GET'])
def ACSTASK():
    print("ACSinfo/came")
    return "/ACSinfo/acsinfo"

if __name__ == "__main__":
    app.run()
