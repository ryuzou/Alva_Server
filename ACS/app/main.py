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
    from .db_controler import XYTGrid
    from .db_controler import TASKGrid
    from .db_controler import CTGridConductor
except Exception:
    sys.path.append("/app/db_controler")
    sys.path.append("/app")
    import Sakura_io_com
    import XYTGrid
    import TASKGrid
    import CTGridConductor


app = Flask(__name__)
CORS(app)

app.register_blueprint(Sakura_io_com.app)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def error():
    return 0


ActivatedIDF = 0

@app.before_first_request
def activate_acs_taskreminder():
    global ActivatedIDF
    if ActivatedIDF != 1:
        ActivatedIDF = 1
    return "activated"

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
        if type(Lsufix) == list:
            args = tuple(Lsufix[2:])
            Lsufix = Lsufix[1]
        ret = None
        NowC = XYTGrid.XYTGrid.GetXYTGrid_least()
        if Lsufix == "NOWcoordinate":
            ret = str(NowC["X"]) + str(NowC["Y"])
            return ret
        print(Lsufix)
        return -1

    def mov(Lsufix):
        CMD = CTGridConductor.Commands()
        count = 0

        def Fbookshelf(val, Idf_Insert_Eject, ICMD):
            CMD = ICMD
            Idf_Insert_Eject = str(Idf_Insert_Eject)
            Coordinate = str(val)
            NOWCoordinate = getData("NOWcoordinate")
            CMD.InsertCommand("MOVARM", NOWCoordinate, Coordinate)
            if Idf_Insert_Eject.lower() == "insert":  # todo   #must check the vailder of the book
                CMD.InsertCommand("INSERTBOOK")
            elif Idf_Insert_Eject.lower() == "eject":
                CMD.InsertCommand("EJECTBOOK")
            else:
                return -1
            return 0

        def Fbookname(val, Idf_Insert_Eject, ICMD):
            CMD = ICMD
            Coordinate = getData("BOOKSHELFcoordinate", val)
            return Fbookshelf(Coordinate, Idf_Insert_Eject, CMD)

        def Fbookid(val, Idf_Insert_Eject, ICMD):
            CMD = ICMD
            Coordinate = getData("BOOKIDcoordinate", val)
            return Fbookshelf(Coordinate, Idf_Insert_Eject, CMD)

        prefix1_map = {
            "bookname": Fbookname,
            "bookshelf": Fbookshelf,
            "bookid": Fbookid
        }
        prefix2_map = {
            "bookshelf": Fbookshelf
        }
        ret = None
        while True:
            print(Lsufix)
            if count == 0:  # in this case it is dealing with cmd "MOV"
                pass
            elif count == 1:  # in this case "prefix1"
                try:
                    ret = prefix1_map[Lsufix[0]](Lsufix[1], "EJECT", CMD)
                    Lsufix.pop(0)
                except KeyError as e:
                    return "syntacs error1"
            elif count == 2:  # in this case "TO"
                if Lsufix[0] == "TO":
                    pass
                else:
                    return "syntacs error2"
            elif count == 3:  # in this case "prefix2"
                try:
                    ret = prefix2_map[Lsufix[0]](Lsufix[1], "INSERT", CMD)
                    Lsufix.pop(0)
                except KeyError as e:
                    return "syntacs error3"
            elif count == 4:
                break
            count += 1
            Lsufix = Lsufix[1:]
        return "success"

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
    return ret.text

if __name__ == "__main__":
    app.run()
