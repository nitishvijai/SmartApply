from flask import Flask
import web_scraper

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>SmartApply Backend</h1>"

@app.route("/jobs/<search>")
def get_jobs(search):
    web_scraper.call_from_app(search)
    return "Jobs found."