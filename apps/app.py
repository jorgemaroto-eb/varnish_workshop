from flask import Flask

app = Flask(__name__)

# HEello World! with Varnish
@app.route("/")
def index():
    return "Hello World!"
