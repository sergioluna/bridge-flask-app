from flask import Flask
app = Flask('bridge-app')

@app.route('/')
def hello():
  return "Hello World!\n"

@app.route('/api')
def api_sanity_check():
    return "API sanity check successful!"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
