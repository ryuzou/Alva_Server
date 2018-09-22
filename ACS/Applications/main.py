from flask import Flask, jsonify, request
import json
import Sakura_io_com


app = Flask(__name__)

app.register_blueprint(Sakura_io_com.app)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"


@app.route('/TaskManager', methods=['POST'])
def TaskManage():
    data = json.loads(request.data)
    prefix = data['Prefix']
    retdata = data
    del retdata["Prefix"]
    if prefix == "BookShelf_CMD":
        pass


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
