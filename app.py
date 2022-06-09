from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>SmartApply Backend</h1>"