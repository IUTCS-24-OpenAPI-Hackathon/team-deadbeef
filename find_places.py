from flask import Flask, Blueprint, render_template, session, redirect

from models import User, db

find_places = Blueprint("find_places", __name__, static_folder="static", template_folder="templates")

@find_places.route('/')
def find_page_view():
    if 'email' in session:
        return render_template('newtest.html')

    else:
        return redirect('/')

@find_places.route('/cities/')
def find_city_view():
    if 'email' in session:
        return render_template('citytest.html')

    else:
        return redirect('/')

