"""App entry point."""

import flask_login
from flask import request
from flask import url_for
from flask import redirect

from movie import create_app
from movie.domain.model import Director, User


app = create_app()
login_manager = flask_login.LoginManager(app)
user_pass = {}

@login_manager.user_loader
def load_user(email):
    return user_pass.get(email, None)


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    stored_user = user_pass.get(email, None)
    if stored_user and password == stored_user.password:

        flask_login.login_user(stored_user)
        print(stored_user.is_active, 'login')
        return redirect(url_for('account'))
    else:
        print('login fail')
    return redirect(url_for('home_bp.home',pagenum=1))


@app.route("/register", methods=["POST"])
def register():
    email = request.form.get("email")
    pw1 = request.form.get("password")
    pw2 = request.form.get("password2")
    if not pw1 == pw2:
        return redirect(url_for('home_bp.home',pagenum=1))
    # if DB.get_user(email):
    if email in user_pass:
        print('already existed user')
        return redirect(url_for('home_bp.home',pagenum=1))
    # salt = PH.get_salt()
    # hashed = PH.get_hash(pw1 + salt)
    print('register', email, pw1)
    user = User(email, pw1)
    user_pass[email] = user
    print('register', user_pass, '#'*5)
    return redirect(url_for('home_bp.home',pagenum=1))


@app.route("/logout")
def logout():
    flask_login.logout_user()
    return redirect(url_for('home_bp.home',pagenum=1))


@app.route("/account")
@flask_login.login_required
def account():
    return "You are logged in"

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'

if __name__ == "__main__":
    app.run(host='localhost', port=5000, threaded=False)

