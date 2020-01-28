from flask import Flask
from flask import jsonify
from flask import request
from services.tokenServices import TokenServices

app = Flask(__name__)


@app.route('/predict', methods = ["POST"])
@TokenServices.token_required
def predict(current_user):

    #get request data
    req_data = request.get_json()
    
    return jsonify({"Message":current_user})

@app.route('/auth', methods = ["POST"])
def auth():
 
    try:
        #get request data
        req_data = request.get_json()
        
        #auth
        if(TokenServices.auth(req_data["user"], req_data["password"]) is False):
            return jsonify({"Message":"User not found!"})    
        
        token = TokenServices.GenerateToken()
        return token

    except Exception as e:
        print(e)
        return jsonify({"Message":"Internal Error!"})
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)