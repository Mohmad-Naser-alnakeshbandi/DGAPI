from flask import *
import random
import json

app = Flask(__name__)
def readData():
    file= open("Data.json", "r")
    data = json.loads(file.read())
    return data

@app.route('/', methods=['GET'])
def MainPage():
    data = readData()
    data_list = data["data"]
    return   data_list[random.randint(0, len(data_list))]


@app.route('/data/', methods=['GET'])
def NumberDataPage():  # put application's code here
   try:
        dataamount = int(request.args.get("number"))
        data = readData()
        data_list = data["data"]
        return jsonify(data_list[0:dataamount])
   except:
       return "Error"


if __name__ == '__main__':
    app.run()