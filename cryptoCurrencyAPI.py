from flask import Flask
from flask import jsonify
from flask import request
from services.tokenServices import TokenServices
from services.dataServices import DataServices

app = Flask(__name__)


@app.route('/predict', methods = ["POST"])
@TokenServices.token_required
def predict(current_user):

    #get request data
    req_data = request.get_json()
    data = req_data["data"]

    result = False
    if(DataServices.validateData(data)):
        result = DataServices.predict(data)
    else:
        return jsonify({"message":"invalid data"}), 500
    
    return jsonify({"result":result})

@app.route('/auth', methods = ["POST"])
def auth():
    try:
        #get request data
        req_data = request.get_json()
        print(req_data)
        
        #auth
        if(TokenServices.auth(req_data["user"], req_data["password"]) is False):
            return jsonify({"Message":"User not found!"}), 404
        
        token = TokenServices.GenerateToken()
        return token

    except Exception as e:
        print(e)
        return jsonify({"Message":"Internal Error! {}".format(e)})
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)