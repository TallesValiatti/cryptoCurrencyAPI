from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/', methods = ["POST"])
def verify_data():

    #get request data
    req_data = request.get_json()
    obj = classReturn("YES")
    print(req_data)
    return jsonify({"value":obj.result, "asas":obj.a})
    
class classReturn:
    def __init__(self, value):
        self.result = value
        self.a = [1,23,3,3,3,3,3,3,3]



if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)