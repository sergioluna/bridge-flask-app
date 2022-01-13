from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
  return "Hello World!\n"

from . import api
app.register_blueprint(api.bp)
