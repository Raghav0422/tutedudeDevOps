from flask import Flask
app=Flask(__name__)

@app.route('api')
def get_list();
    read_file=open("backend.json","r")
    record=read_file.read()
    return record

if __name__=='__main__':
    app.run(debug=True)