import os
from flask import Flask, jsonify
from models import setup_db
from flask_cors import CORS
from models import db

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello" 
        if excited == 'true': greeting = greeting + "!!!!!"
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"
    
    @app.route('/people', methods =['GET'])
    def get_people():
        return jsonify([person.format() for person in db.session.query(People)])

    return app

app = create_app()

if __name__ == '__main__':
    app.run()