from flask import Flask, url_for, redirect

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secret"

    from .blueprints.home import home
    app.register_blueprint(home, url_prefix="/")

    return app