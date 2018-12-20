from flask import Flask, request, url_for, render_template
from model import User


app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world!'

@app.route('/user/<id>', methods=['POST'])
def user_id(id):
    return 'hello' + id

@app.route('/query_user')
def query_user():
        id=request.args.get('id')
        return 'query user: ' + id

@app.route('/user')
def user():
    return render_template("hello2.html", user="peterhello2")

@app.route('/object')
def object():
    user1 = User(1,'thinkchina')
    return render_template("object.html", user=user1)

@app.route('/query_url')
def query_url():
    return 'query_url is : ' + url_for('index')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)