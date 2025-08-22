import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from config import Config

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    login_manager.login_view = 'auth.login'

    # 🚨 Move this block *after* blueprint registration to avoid circular import issues
    from .routes import main
    from .auth import auth_bp
    app.register_blueprint(main)
    app.register_blueprint(auth_bp)

    # ✅ Import models *after* registering blueprints
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        print(">> user_loader called with user_id:", user_id)  # For debug
        return User.query.get(int(user_id))

    return app

