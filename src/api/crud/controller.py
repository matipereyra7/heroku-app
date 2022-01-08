from wsgi import app


# Basic testing routes
@app.route('/')
def index():
    return "<h1>Welcome to CodingX</h1>"


@app.route('/ping')
def ping_pong():
    return "pong"


@app.route('/hi')
def hello_world():
    return "<h1>Hello World!</h1>"


@app.route('/soy-chofa')
def hello_chofa():
    return "<h1>Hola Chofa, soy Mati :)</h1>"
