from flask import Flask,render_template,abort,request,redirect,url_for
app = Flask(__name__)

@app.route('/')
def router():
    return render_template('index.html')

@app.route('/validate',methods=['POST','GET'])
def validate():
    if request.method=='POST' and request.form['ps']=='imrandell':
        return redirect(url_for("success"))
    else:
        abort(401)

@app.route('/success')
def success():
    return render_template('success.html')

if "__main__"==__name__:
    app.run(debug=True)