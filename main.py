from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Welcome to my website</h1>"

@app.route("/contact")
def contact_Page():
    return render_template("contact.html")

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