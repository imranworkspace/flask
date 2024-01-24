from flask import Flask,render_template,request,make_response,redirect
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    return render_template('index.html')

@app.route('/set_cookie',methods=['POST','GET'])
def set_coo():
    if request.method=='POST':
        got_name = request.form['nm']
        got_email = request.form['em']
        got_mobile = request.form['mo']
    resp = make_response(render_template('index.html'))
    resp.set_cookie(
                    'coo_name',got_name,
                    'coo_email',got_email,
                    'coo_mobile',got_mobile
                    )
    return resp

@app.route('/get_cookie')
def get_coo():
    name = request.cookies.get('coo_name')
    email = request.cookies.get('coo_email')
    mobile = request.cookies.get('coo_mobile')
    return f'Welcome {name}! Your email = {email}, and your mobile number = {mobile}.'


if "__main__"==__name__:
    app.run(debug=True)