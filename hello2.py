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

@app.route('/query_user/<user_id>')
def query_user_id(user_id):
    user2 = None
    if int(user_id) == 1:
        user2 = User(1,"peter2")
    return render_template("userif.html", user=user2)

@app.route('/list_user')
def list_user():
    users = []
    for i in range(1,11):
        user = User(i, "peter" + str(i))
        users.append(user)
    return render_template("user_list.html",users = users)

@app.route('/one')
def page1():
    return render_template("base-1.html")

@app.route('/two')
def page2():
    return render_template("base-2.html")

@app.route('/query_url')
def query_url():
    return 'query_url is : ' + url_for('index')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)