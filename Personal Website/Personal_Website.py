from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home_page():
    return render_template("home.html")

@app.route("/projects")
def project_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template("project.html", items=items)

