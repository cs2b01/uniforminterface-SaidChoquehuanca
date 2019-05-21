from flask import Flask, render_template, session, request, redirect, url_for
app = Flask(__name__)

@app.route("/") #Estoy dando un routing, trabajando sobre la ruta principal (la raix)
def main():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/post.html")
def post():
    return render_template('post.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')

if __name__  ==  "__main__":
    app.run()