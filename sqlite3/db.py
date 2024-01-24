import sqlite3

con = sqlite3.connect("employees.db")
print('database created ')

con.execute('create table emptb(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT UNIQUE NOT NULL,address TEXT NOT NULL )')
print('table created successfully ')
con.close()