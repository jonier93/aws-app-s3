from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='frontend/static', template_folder='frontend/templates')
from routes.routes import *

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 3000
    app.run(host, port, debug=True) 

