from flask import Flask
from flask import request
from flask_cors import CORS

import json

import plot

app = Flask(__name__)
CORS(app)
app.config["JSON_AS_ASCII"] = False

@app.route("/print", methods=['POST','GET'])
def receive_data():
    try:
        json_data = request.get_json()
        data = json.loads(json_data)

        print(data)
        return json_data
    
    # Error handling
    except Exception as e:
        return str(e)

@app.route("/plot", methods=['POST','GET'])
def plot_data():
    try:
        json_data = request.get_json()
        data_dict = json.loads(json_data)

        # Convert dict to list
        dataname = list(data_dict.keys())
        data = list(data_dict.values())
        plot.plot_xyz(dataname,data)

    # Error handling
    except Exception as e:
        return str(e)
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
