import flask from flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello World!"

@app.route("/Hello")
def hello():
    return render_template('index.html')
