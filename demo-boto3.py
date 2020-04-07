
#to upload file into AWS S3 bucket

from flask import Flask, request

#install boto3 and AWS config for access keys
import boto3


app = Flask(__name__)

@app.route('/')
def index():
    return '''<form method =POST enctype=multipart/form-data action='upload'>
    <input type=file name=myfile>
    <input type=submit>
    </form>'''


@app.route('/upload', methods = ['POST'])    
def upload():
    s3 = boto3.resource('s3')

    s3.Bucket('smartml').put_object(Key='python_file',Body = request.files['myfile'])
    return 'File saved to S3'




if __name__ == "__main__":
     app.run()   