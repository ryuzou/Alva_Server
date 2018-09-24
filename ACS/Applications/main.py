from flask import Flask, jsonify, request
import json
import Sakura_io_com
import requests

app = Flask(__name__)

app.register_blueprint(Sakura_io_com.app)

@app.route("/", methods=['GET'])

def hello():
    return "Hello World!"


@app.route('/ACS', methods=['GET'])  # Frontend first connects to this at first
def ACSTaskManager():
    # todo
    return 0

@app.route('/TaskManager', methods=['POST'])
def TaskManage():
    data = json.loads(request.data)
    prefix = data['Prefix']
    retdata = data
    del retdata["Prefix"]
    retjson = jsonify(retdata)
    url = None
    if prefix == "BookShelf_CMD":
        url = '127.0.0.1:3031/cmd/bookshelf'
    # elif prefix == ""
    requests.post(url, json=retjson)


@app.route('/reply', methods=['POST'])
def reply():
    data = json.loads(request.data)
    answer = "Yes, it is %s!\n" % data["keyword"]
    result = {
        "Content-Type": "application/json",
        "Answer": {"Text": answer}
    }
    # return answer
    return jsonify(result)


if __name__ == "__main__":
    app.run()
