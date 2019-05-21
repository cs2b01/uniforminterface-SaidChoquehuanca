from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/usuarios')
def users():
    db_session = db.getSession(engine)
    users = db_session.query(entities.User)
    data = users[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype = 'application/json')

@app.route('/create_test_books', methods = ['GET'])
def create_test_books():
    db_session = db.getSession(engine)
    book = entities.user(codigo="201810223",nombre="Billy", apellido="Quispe", password="pepino82")
    db_session.add(book)
    db_session.commit()
    return "Test Usuarios created!"

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('0.0.0.0'))
