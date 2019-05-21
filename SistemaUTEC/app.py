from flask import Flask, render_template, session, request, redirect, url_for
app = Flask(__name__)

@app.route("/",methods=['get','user']) #Estoy dando un routing, trabajando sobre la ruta principal (la raix)
def main():
    return render_template('login.html')

@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/login.html")
def login():
    return render_template('login.html')

if __name__  ==  "__main__":
    app.run()