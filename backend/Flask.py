from flask import Flask

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://kumarraghav561:tuteduderv@cluster0.9hirqwz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

#creating a database name test
db=client.test
#creating collection inside the database
collection=db['flask-tutorial']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment You successfully connected to MongoDB!")
except Exception as e:
    print(e)
app=Flask(__name__)

@app.route('/submittodoitem',methods=['POST'])
def submittolist():
    form_data=dict(request.form)
    collection.insert_one(form_data)
    return form_data

if __name__=='__main__':
    app.run(port=8000,debug=True,host='0.0.0.0')