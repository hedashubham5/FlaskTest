from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/demo")
def demo():
    return "Demo site website"

@app.route('/test')
def test():
    return "Testing environment"
