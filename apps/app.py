from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Index</h1><p>This is the index.</p>"


@app.route("/handle_ttl/<int:ttl>")
def details(ttl):
    now = datetime.now().isoformat()
    return f"Setting this TTL to {ttl}. Date: {now}\n", {
        "Cache-control": f"public, max-age={ttl}"
    }


@app.route("/esi/complete_page")
def other():
    now = datetime.now().isoformat()

    return f'This is other ({now})\n\n<esi:include src="/footer" />', {
        "Cache-control": "public, max-age=1"
    }

# ADD example with iframe / without iframe


@app.route("/footer")
def footer():
    now = datetime.now().isoformat()

    return f'THIS IS THE FOOTER ({now})', {
        "Cache-control": "public, max-age=10"
    }
