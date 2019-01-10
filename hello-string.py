from flask import Flask,request

app = Flask(__name__)
@app.route("/")
def index():
    return "hello world"

@app.route("/<string:name>")
def name(name):
    return "hello, {name}"

@app.route("/hello")
def hello():
    return "hello hello"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)