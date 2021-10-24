from flask import Flask, make_response, render_template
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

###########################################################################

# Using a browser
@app.route("/simple/<int:ttl>")
def simple(ttl):
    now = datetime.now().isoformat()

    response = make_response(render_template("simple.html", now=now, ttl=ttl))
    response.headers["Cache-control"] = "no-cache"
    return response

# SPLITTING THE PAGE

@app.route("/page/content/<int:ttl>")
def only_content(ttl):
    now = datetime.now().isoformat()

    response = make_response(render_template("_content.html", now=now, ttl=ttl))
    response.headers["Cache-control"] = f"public, max-age={ttl}"

    return response

@app.route("/iframe/<int:ttl>")
def using_iframe(ttl):
    now = datetime.now().isoformat()

    response = make_response(render_template("using_iframe.html", now=now, ttl=ttl))
    response.headers["Cache-control"] = f"public, max-age={ttl}"

    return response

@app.route("/esi/<int:ttl>")
def using_esi(ttl):
    now = datetime.now().isoformat()

    response = make_response(render_template("using_esi.html", now=now, ttl=ttl))
    response.headers["Cache-control"] = f"public, max-age={ttl}"

    return response
