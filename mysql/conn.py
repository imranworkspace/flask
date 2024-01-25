from flask import *
from flask_mysqldb import MySQLdb

app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DATABASE']='imrandb'

mysql = MySQLdb(app)

@app.route('/api/users', methods=['GET'])
def get_all_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tb")
    data = cur.fetchall()
    cur.close()
    return jsonify(users=data)

if "__main__"==__name__:
    app.run(debug=True)