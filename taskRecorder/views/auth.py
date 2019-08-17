from flask import Blueprint, render_template, redirect, url_for, flash, g
from taskRecorder.forms import LoginForm, RegisterForm
from taskRecorder.models import User, db, login_manager
from flask_login import login_user, current_user


auth = Blueprint('auth', __name__, template_folder='templates', url_prefix='/')


@auth.route('/')
@auth.route('/login', methods=['post', 'get'])
def login():
    login_form = LoginForm()
    if login_form.is_submitted():
        email = login_form.username.data
        password = login_form.password.data
        user = User.query.filter_by(email=email).first()
        if not user or password != user.password_hash:
            flash("Wrong username or password")
        else:
            login_user(user, 1)
            g.user = user
            # print(g.user.user_id)
            # print(current_user)
            return redirect('/mytask')
    return render_template('login.html', login_form=login_form)


@auth.route('/register', methods=['post', 'get'])
def register():
    register_form = RegisterForm()
    if register_form.is_submitted():
        if register_form.validate():
            new_user = User(first_name=register_form.first_name.data,
                            last_name=register_form.last_name.data,
                            email=register_form.email.data,
                            password_hash=register_form.password.data,
                            role='default')
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')
        else:
            flash("Failed. Please try again.")
            print(register_form.errors)

    return render_template('register.html', register_form=register_form)
