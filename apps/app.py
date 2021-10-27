from flask import Flask, make_response
from datetime import datetime

app = Flask(__name__)

# HEello World! with Varnish
@app.route("/")
def index():
    return "Hello World!"


@app.route("/ttl/<int:ttl>")
def ttl(ttl):
    now = datetime.now().isoformat()

    response = make_response(f"Setting TTL to {ttl}.\nNow it's {now}.")
    response.headers["Cache-control"] = f"public, max-age={ttl}"

    return response
