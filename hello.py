# // WSGT object
from flask import Flask
# initialize Flask
app = Flask(__name__) # constructor

@app.route('/name/<name>')
def hello(name):
    return 'hello my name is %s'%name

@app.route('/age/<age>/')
def age(age):
    return 'my age is %d'%age

@app.route('/rev/<revNo>') 
def revision(revNo): 
   return 'Revision Number %f' % revNo 


if '__main__'==__name__:
    app.run(debug=True)