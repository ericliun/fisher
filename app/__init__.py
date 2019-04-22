from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app

def register_blueprint(app1):
    from app.web.book import web
    app1.register_blueprint(web)