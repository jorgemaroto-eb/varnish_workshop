from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Index</h1><p>This is the index.</p>"


@app.route("/handle_ttl/<int:ttl>")
def details(ttl):
    now = datetime.now().isoformat()
    return f'Setting this TTL to {ttl}. Date: {now}\n', {'Cache-control': f'public, max-age={ttl}'}
