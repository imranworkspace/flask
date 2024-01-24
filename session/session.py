from flask import Flask,session,render_template,request,make_response
app=Flask(__name__)
app.secret_key = "imran"  

@app.route('/',methods=['POST','GET'])
def login():
    return render_template('login.html')

@app.route('/success',methods=['POST','GET'])
def success():
    if request.method=='POST':
        session['email']=request.form['email']
    resp = make_response(render_template('success.html'))
    return resp
    

@app.route('/profile')
def profile():
    if session['email'] is None:
        return render_template('login.html')
    else:
        email = session['email']
        return render_template('profile.html',email=email)

@app.route('/logout')
def logout():
    session.pop('email',None)
    return render_template('logout.html',)
if "__main__"==__name__:
    app.run(debug=True)