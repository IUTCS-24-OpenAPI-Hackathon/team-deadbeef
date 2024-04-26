from flask import Flask, Blueprint, render_template

login = Blueprint("login", __name__, static_folder="static", template_folder="templates")


@login.route('/')
def login_view():
    return render_template('login.html')


@login.route('/register/')
def registration_view():
    return render_template('register.html')
