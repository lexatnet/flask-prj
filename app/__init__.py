import os

from flask import Flask
from flask import render_template

def create_app(test_config=None):
    app = Flask(__name__)
    
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    
    from app import films
    from app import index
    from app import auth
    
    app.register_blueprint(films.bp)
    app.register_blueprint(index.bp)
    app.register_blueprint(auth.bp)
    
    return app