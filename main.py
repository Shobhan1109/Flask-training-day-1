from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my website"

@app.route("/contact")
def contact():
    return "Contact page"

@app.route("/gallery")
def gallery():
    return "Gallery page"

@app.route("/help")
def help():
    return "Help center"

@app.route("/home")
def homepage():
    return "Home page"

if __name__=="__main__":
    app.run()