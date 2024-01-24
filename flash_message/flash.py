from flask import Flask,redirect,render_template,request,flash,url_for
app = Flask(__name__)
app.secret_key='imran'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success',methods=['POST','GET'])
def success():
    if request.method=='POST':
        name = request.form['nm']
        if request.form['ps']!='imrandell':
            error= 'invalid password try again'
            redirect(url_for('home'))
        else:
            flash('you are successfully logged in')
            return 'welcome %s'%name
    return render_template('login.html',error=error)

@app.route('/login')
def loginp():
    return render_template('login.html')

if "__main__"==__name__:
    app.run(debug=True)