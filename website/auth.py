from flask import Blueprint, render_template,request,flash, redirect, url_for,session
from flask.wrappers import Request
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user,login_required,logout_user, current_user
import shutil
import os


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST','GET'])
def login():
    if request.method =='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                session["data"] = []
                session["user"] = current_user.id
                path = os.getcwd()
                path = path +"/website/static/nirs/"+ str(current_user.id)
                if os.path.exists(path):
                    return redirect(url_for('views.home'))
                else:
                    os.mkdir(path)
                    return redirect(url_for('views.home'))
            else:
                flash('Wrong password! Try again.', category='error')
        else:
            flash('Email does not exist!', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    path = os.getcwd()
    path = path +"/website/static/nirs/"+ str(current_user.id) 
    for f in os.listdir(path):
        os.remove(os.path.join(path,f))
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['POST','GET'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password = request.form.get('password')
        passwordConfirm = request.form.get('passwordConfirm')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exist',category='error')
        elif len(email) <=4:
            flash('Email must be at least 4 characters', category='error')
        elif len(first_name) <2:
            flash('First Name must be at least 4 characters', category='error')
        elif password != passwordConfirm:
            flash('Passwords don\'t match', category='error')
        elif len(password) <7:
            flash('Password must be at least 7 characters', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password,method='sha256'),)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created', category='success')
            path = os.getcwd()
            path = path +"/website/static/nirs/"+ str(current_user.id)
            if os.path.exists(path):
                return redirect(url_for('views.home'))
            else:
                os.mkdir(path)
                return redirect(url_for('views.home'))
    return render_template("sign_up.html", user=current_user)