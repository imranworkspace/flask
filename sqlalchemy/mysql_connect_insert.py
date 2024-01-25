import mysql.connector
from flask import *
app = Flask(__name__)
conn = mysql.connector.connect(host='localhost',user='root',
password='admin',database='imrandb')

cur = conn.cursor()
# try:
#     cur.execute('show databases')
# except:
#     conn.rollback()
# else:
#     for x in cur:
#         print(x)
# finally:
#     conn.close()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/users', methods=['GET'])
def get_all_users():
    cur.execute("SELECT * FROM tb ")
    data = cur.fetchall()
    cur.close()
    return jsonify(users=data)

@app.route('/api/insert',methods=['POST','GET'])
def insert():
    if request.method=='POST':
        name = request.form['nm']
        mobile = request.form['mo']
        sql = 'insert into tb values(NULL,%s,%s)'
        val=(name,mobile)
        cur.execute(sql,val)
        conn.commit()
        return 'form submitted'

# @app.route('/delpage')
# def delpage():
#     return render_template('dele.html')


@app.route('/api/remove',methods=['POST','GET'])
def delete():
    if request.method=='POST':
        id = request.form['id']
        sql='delete from tb where id=%s'
        val=(id,)
        print('val======',val)
        cur.execute(sql,val)
        conn.commit()
        return f'{id} record deleted'
    else:
        return render_template('dele.html')


if "__main__"==__name__:
    app.run(debug=True)