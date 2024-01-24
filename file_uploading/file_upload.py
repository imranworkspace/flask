from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def file_upload():
    return render_template('file_upload.html')

@app.route('/success',methods=['POST','GET'])
def success():
    myfile=''
    if request.method=='POST':
        myfile = request.files['file']
        myfile.save(myfile.filename)

    return render_template('success.html',myfile=myfile.filename)

if "__main__"==__name__:
    app.run(debug=True)