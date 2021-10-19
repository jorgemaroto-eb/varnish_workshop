from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Index</h1><p>This is the index.</p>"


@app.route("/details/<int:product_id>")
def details(product_id):
    return f'<h1>Product ##{product_id}</h1><p>This is the page for product {product_id}.</p>'
