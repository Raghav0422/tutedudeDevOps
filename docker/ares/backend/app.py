from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route('/',methods=['GET'])
def names():
    f=open('./a.txt')
    da=f.read()
    data={
        'data':da
    }
    return data

@app.route('/submit',methods=['POST'])
def submittolist():
    form_data=dict(request.form)
    # collection.insert_one(form_data)
    return jsonify(form_data)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')