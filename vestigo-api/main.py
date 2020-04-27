from flask import Flask
from flask import jsonify
from api import mongo
import json

app = Flask(__name__)

@app.route('/mongo')
def mongoTest():
    result = mongo.getServerStatus()
    if not result:
        result = {"error":"mongo connection problems"}
    else:
        result = json.loads(json.dumps(result, default=str))
    return jsonify(result)

@app.route('/')
def hello_world():
    result = {"ping": "HelloWorld"}
    return jsonify(result)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5092)