from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    application = Flask(__name__)
    application.config['SECRET_KEY'] = 'mysecretkey'
    application.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(application)

    from .views import views
    from .auth import auth

    application.register_blueprint(views, url_prefix ='/')
    application.register_blueprint(auth, url_prefix ='/')
    
    from .models import User
    
    create_database(application)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(application)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return application

def create_database(app):
    if not path.exists('website/'+ DB_NAME):
        db.create_all(app=app)


