from flask import *
import random
import requests


app = Flask(__name__)

def readData():
    try:
        response = requests.get("https://raw.githubusercontent.com/Mohmad-Naser-alnakeshbandi/Data-store/master/out.json?token=GHSAT0AAAAAABW3XUMLLPNGCUOSJMEAHLYAYZDGJQQ")
        response.raise_for_status()
        jsonResponse = response.json()
        return jsonResponse
    except Exception as err:
        print(f'Other error occurred: {err}')
    return  "Error"


@app.route('/', methods=['GET'])
def MainPage():  # put application's code here
    list = readData()
    data_list = list["data"]
    return data_list[random.randint(0, len(data_list))]


@app.route('/data/', methods=['GET'])
def NumberDataPage():  # put application's code here
   try:
        dataamount = int(request.args.get("number"))
        list = readData()
        data_list = list["data"]
        return data_list[0:dataamount]
   except:
       return "Error"


if __name__ == '__main__':
    app.run()
