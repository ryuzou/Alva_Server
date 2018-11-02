from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS
import json
import os
import sys
import requests_unixsocket

try:
    from ..app import Sakura_io_com
    from ..app import BookShelf_CMD
    from .db_controler import XYTGrid
    from .db_controler import TASKGrid
    from .db_controler import COMMANDGrid
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


@app.route('/ACS_taskreminder', methods=['POST'])
def ACSTaskReminder():
    data = request.data.decode('utf-8')
    data = data.split(" ")

@app.route('/ACS_command-manager', methods=['POST'])
def ACSTaskManager():
    data = request.data.decode('utf-8')
    tasks = data.split(" ")
    ret = json.dumps(tasks)
    retval = None
    prefix = tasks[0]

    def showinfo(Lsufix):
        return Lsufix[1:]

    def getData(Lsufix, *args):
        return Lsufix[1:]

    def mov(Lsufix, count=0):
        countnum = count  # count is the count of "prefix" number in which the function is dealing with

        def func(val):  # todo
            return val

        def Fbookshelf(val, Idf_Insert_Eject):
            Idf_Insert_Eject = str(Idf_Insert_Eject)
            Coordinate = int(val)
            NOWCoordinate = getData("NOWcoordinate")
            TASKGrid.InsertTASKGrid_least("MOVARM", NOWCoordinate, Coordinate)
            if Idf_Insert_Eject.lower() == "insert":  # todo   #must check the vailder of the book
                TASKGrid.InsertTASKGrid_least("INSERTBOOK")
            elif Idf_Insert_Eject.lower() == "eject":
                TASKGrid.InsertTASKGrid_least("EJECTBOOK")
            else:
                return -1
            return 0

        def Fbookname(val, Idf_Insert_Eject):
            Coordinate = getData("BOOKSHELFcoordinate", val)
            return Fbookshelf(Coordinate, Idf_Insert_Eject)

        def Fbookid(val, Idf_Insert_Eject):
            Coordinate = getData("BOOKIDcoordinate", val)
            return Fbookshelf(Coordinate, Idf_Insert_Eject)

        prefix1_map = {
            "bookname": Fbookname,
            "bookshelf": Fbookshelf,
            "bookid": Fbookid
        }
        prefix2_map = {
            "bookshelf": Fbookshelf
        }
        ret = None
        if count == 0:  # in this case it is dealing with cmd "MOV"
            pass
        elif count == 1:  # in this case "prefix1"
            try:
                ret = prefix1_map[Lsufix[0]](Lsufix[1], "INSERT")
                Lsufix.pop(0)
            except KeyError as e:
                return "syntacs error"
        elif count == 2:  # in this case "TO"
            if Lsufix[0] == "TO":
                pass
            else:
                return "syntacs error"
        elif count == 3:  # in this case "prefix2"
            try:
                ret = prefix2_map[Lsufix[0]](Lsufix[1], "EJECT")
                Lsufix.pop(0)
            except KeyError as e:
                return "syntacs error"
        elif count == 4:
            return "success"
        countnum = countnum + 1
        return mov(Lsufix[1:], count=countnum)

    prefix_map = {
        "show": showinfo,
        "getdata": getData,
        "MOV": mov
    }
    try:
        ret = prefix_map[prefix](tasks)
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
    ret = requests.post("http://nginx/ACS_command-manager", cmd)
    print(ret.text)
    return ret.text


if __name__ == "__main__":
    app.run()
