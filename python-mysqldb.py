from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'addcp.cn'
app.config['MYSQL_USER'] = 'peter'
app.config['MYSQL_PASSWORD'] = 'thinkchina'
app.config['MYSQL_DB'] = 'thinkchina'

mysql = MySQL(app)

@app.route('/')
def users():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT user, password FROM user''')
	rv = cur.fetchall()
	return str(rv)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
