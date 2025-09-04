from flask import Flask,render_template, request,url_for,redirect
##################################################
from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
load_dotenv()
uri = os.getenv('MONGO_URI')

client = MongoClient(uri)

try:
    print("inside try")
    print(uri)
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("inside exception")
    print(e)
print("creating client database name test")
db= client["Test"]
print("database created:  ",db)
print("creating a collection")
collection= db['flask_tutorial']
print("collection created: ",collection)

BACKEND_URL='http://0.0.0.0:9000'
app=Flask(__name__)

@app.route('/')
def home():

    return render_template('./home.html')

@app.route('/submit', methods=['POST'])
def registertation():
    name=str(request.form.get('name'))
    password=str(request.form.get('password'))
    print("getting the form data")
    form_data=dict(request.form)
    print("we got form data is: ",form_data)
    print("now inserting the data in collection: ")
    collection.insert_one(form_data)
    print("data inserted in collection")
    print("you got this ",request.form)

    return redirect(url_for('formSubmitted'))

@app.route('/dataUploaded')
def formSubmitted():
        return render_template('./successful.html')


if __name__== '__main__':
    #app.run(host='0.0.0.0',port=8000,debug=True)
    app.run(debug=True)


    
# from pymongo import MongoClient

# from pymongo.errors import ConnectionFailure
 
#     # Replace <username>, <password>, and <cluster-url> with your actual Atlas details

# CONNECTION_STRING = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.5.3"
 
# try:

#         # Create a MongoClient instance

#         client = MongoClient(CONNECTION_STRING)
 
#         # The ping command is a simple way to test the connection without

#         # needing to access a specific database or collection.

#         client.admin.command('ping')

#         print("Successfully connected to MongoDB Atlas!")
 
#         # You can also try accessing a database or collection to further verify

#         # For example:

#         # db = client.your_database_name

#         # collection = db.your_collection_name

#         # print(f"Successfully accessed database: {db.name}")
 
# except ConnectionFailure as e:

#         print(f"Connection to MongoDB Atlas failed: {e}")

# except Exception as e:

#         print(f"An unexpected error occurred: {e}")

# finally:

#         # Close the connection when done

#         if 'client' in locals() and client:
#             print("clossing the connection")
#             client.close()

#             print("Connection closed.")
 
