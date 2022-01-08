from flask import Flask

app = Flask(__name__)

# Import controllers
from src.api.crud.controller import *

if __name__ == "__main__":
    app.run()
