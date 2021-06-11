from flask import Flask
from latin import latinizer

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Welcome! Go to /puppy_latin/name to see your name in puppy latin!</p>"

@app.route("/info")
def info():
    return "<p>lorem ipsum</p>"

# @app. route( '/user/<name>')
# def other_page(name):
#     return f'<h1>Hi, User: {name.upper()}!</h1>'

@app. route( '/puppy_latin/<name>')
def other_page(name):
# Later we will see how to use
# this parameter with templates!
    return latinizer(name)

if __name__ == '__main__':
    app.run()  

