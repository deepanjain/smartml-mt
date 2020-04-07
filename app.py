from flask import Flask, jsonify , request
from flask_cors import CORS

app = Flask(__name__)

# install add CORS in this code to avoid CORS error 
cors = CORS(app)



@app.route('/home', methods = ['GET','DELETE'])
def demo():
    return jsonify('hello world!') 



@app.route('/face/getFaceName', methods=['GET'])
def getFacename():

    return jsonify("Face Id is Identified and person is Mr. jain")


@app.route('/face/analyseFace', methods=['GET'])
def analyseFace():
    return jsonify("Face Smile Confidence Score is 99.8% and Spectacle score is 80%")   


#for POST and GET requests in single function
@app.route('/postdata', methods =['POST','GET'])
def postData():
    if request.method == 'POST':
        #  dataList = []
        #to convert json data to dictionary
         data = request.get_json()
         return jsonify('post successful!')
    else:
        return jsonify('GET request recieved!')
   

   



if __name__ == '__main__':
    app.run()
