from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3
app = Flask(__name__)
app.secret_key='imrans'
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/success',methods=['POST','GET'])
def success():
    if request.method=='POST':
        # try:
        name=request.form['nm']
        email=request.form['em']
        address=request.form['ad']
        if name!='' and email!='' and address!='':
            with sqlite3.connect("employees.db") as con:
                cur = con.cursor()
                cur.execute("insert into emptb(name,email,address) values(?,?,?)",(name,email,address))
                con.commit()
                # con.close()
            flash('form submitted successfully')
            return render_template('success.html')
        else:
            error='please fill all fields'
            return render_template('success.html',error=error)
    else:
        return render_template('login.html')

@app.route('/view')
def view():  
    con = sqlite3.connect("employees.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from emptb")  
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)  
if "__main__"==__name__:
    app.run(debug=True)