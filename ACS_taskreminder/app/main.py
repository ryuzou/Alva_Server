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
    from ..app import acs_taskreminder
except Exception:
    sys.path.append("/app/db_controler")
    sys.path.append("/app")
    import Sakura_io_com
    import BookShelf_CMD
    import XYTGrid
    import TASKGrid
    import acs_taskreminder

app = Flask(__name__)
CORS(app)

app.register_blueprint(Sakura_io_com.app)
app.register_blueprint(BookShelf_CMD.app)
app.register_blueprint(acs_taskreminder.app)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def error():
    return 0

ActivatedIDF = 0

@app.before_first_request
def activate_acs_taskreminder():
    global ActivatedIDF
    if ActivatedIDF != 1:
        ActivatedIDF = 1
        thread = acs_taskreminder.activate_acs_RM()
        thread2 = Sakura_io_com.activate_sakura()
        thread2.start()
        thread.start()
    return "activated"

if __name__ == "__main__":
    app.run()
