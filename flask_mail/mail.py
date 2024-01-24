from flask import Flask
from flask_mail import Mail,Message
app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='imranlatur24studymaterial@gmail.com'
app.config['MAIL_PASSWORD']='zwxjqxrlxofuwmvo'
app.config['MAIL_USE_SSL']=True
app.config['MAIL_USE_TLS']=False


mail = Mail(app)

users = [{'name':'imran','email':'shaikh.novetrics@gmail.com'},
         {'name':'imran2','email':'imran.dtc2@gmail.com'},
         {'name':'imran2','email':'imranlatur24@outlook.com'}]


@app.route('/')
def home():
    with mail.connect() as con:
        for user in users:
            message = 'welcome %s'%user['name']
            msgs=Message(recipients=[user['email']],
                body=message,
                subject='flask testing',
                sender='imranlatur24studymaterial@gmail.com')
            con.send(msgs)
        return "Sent"

if "__main__"==__name__:
    app.run(debug=True)
