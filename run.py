from flask import Flask
from flask import request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"



@app.route('/error_denied')
def error_denied():
    abort(401)
@app.route('/error_internal')
def error_internal():
    abort(505)
@app.route('/error_not_found')
def error_not_found():
    abort(404)

if __name__ == '__main__':
 app.run(debug=True)