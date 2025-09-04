from flask import Flask
from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv
uri = os.getenv('MONGO_URI')

# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#creating client database name test
db= client.test

#creating a collection
collection= db['flask_tutorial']

app=Flask(__name__)

@app.route('/api')
def get_list():
    read_file=open("backend.json",'r')
    record=read_file.read()
    return record


if __name__== '__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)


    
