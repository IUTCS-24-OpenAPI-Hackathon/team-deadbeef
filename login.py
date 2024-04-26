from flask import Flask, Blueprint, render_template

login = Blueprint("login", __name__, static_folder="static", template_folder="templates")


@login.route('/')
def login_view():
    return render_template('login.html')


@login.route('/first-login/<string:email>')
def first_login(email: str):
    print(email)
    return render_template('first_login.html', email=email)


@login.route('/register/')
def registration_view():
    return render_template('register.html')
