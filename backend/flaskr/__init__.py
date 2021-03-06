import os
from flask import Flask, jsonify
from .models import setup_db, db
from flask_cors import CORS
from .promotion_manager.promotion_manager_endpoints import promotion_manager

def create_app(test_config=None):

    app = Flask(__name__)
    app.register_blueprint(promotion_manager)
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

    return app