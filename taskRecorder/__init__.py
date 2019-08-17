from flask import Flask
from taskRecorder.views import auth, mytask
from . import config
from .models import db, login_manager


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth.auth)
    app.register_blueprint(mytask.task)
    app.config.from_object(config)
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    login_manager.init_app(app)
    return app
