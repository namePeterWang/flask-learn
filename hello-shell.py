import os
import commands

from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def index():
	#return render_template('index.html')
	#file = os.popen('shell.py')
	#os.system('python shell.py')
	status, output = commands.getstatusoutput('python shell.py')
	return output
@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)
app.run(host='0.0.0.0',debug=True)
