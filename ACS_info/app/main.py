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
except Exception:
    sys.path.append("/app/db_controler")
    sys.path.append("/app")
    import BookShelf_CMD
    import XYTGrid
    import TASKGrid

app = Flask(__name__)
CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/ACSinfo/', methods=['POST', 'GET'])
def ACSTASK():
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return jsonify(res='error'), 400
    Rdict = request.json
    print(Rdict)
    if type(Rdict) == str:
        Rdict = json.loads(Rdict)
    BOOKINFO = None
    if Rdict["Idf"] == "bookid":
        BOOKINFO = BookShelf_CMD.BDB.GetBookInfo(BookFullID=Rdict["name"])
    elif Rdict["Idf"] == "bookname":
        BOOKINFO = BookShelf_CMD.BDB.GetBookInfo(BookFullID=Rdict["name"])
    if Rdict["img"] == "YES":
        BOOKIMG = BookShelf_CMD.BDB.GetBookIMG(BOOKINFO["bookid"])
        BOOKINFO["img"] = BOOKIMG
    BOOKCOD = BookShelf_CMD.BDB.GetBookIdealCOD(BOOKINFO["bookid"])
    BOOKINFO.update(BOOKCOD)
    RetJson = json.dumps(BOOKINFO)
    print(RetJson)
    return RetJson


@app.route('/ACSinfo/XYC', methods=['POST'])
def ACSXYCM():
    return "done"  # todo


if __name__ == "__main__":
    app.run()
