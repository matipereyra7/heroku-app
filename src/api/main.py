from flask import Flask


app= Flask(__name__)

# Basic testing routes
@app.route('/')
def index():
    return "<h1>Welcome to CodingX</h1>"

@app.route('/hi')
def hello_world():
    return "<h1>Hello World!</h1>"

@app.route('/soy-chofa')
def hello_chofa():
    return "<h1>Hola Chofa, soy Mati :)</h1>"
