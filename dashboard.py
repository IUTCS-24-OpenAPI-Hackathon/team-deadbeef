from flask import Flask, Blueprint, render_template, session, redirect

from models import User, db

dashboard = Blueprint("dashboard", __name__, static_folder="static", template_folder="templates")


@dashboard.route('/')
def dashboard_view():
    if 'email' in session:
        return render_template('dashboard.html')

    else:
        return redirect('/')
