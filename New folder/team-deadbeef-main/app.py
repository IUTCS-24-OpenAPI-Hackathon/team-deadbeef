from flask import Flask, request, render_template, redirect, session, jsonify, render_template_string
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import InputRequired, Length, ValidationError
import bcrypt
from flask_mail import Mail, Message
import random
import string
import re
import json

from auth import auth
from login import login
from dashboard import dashboard
from find_places import find_places
# from all_users import all_users
# from users import users
# from profile import profile
from security import security
# from rbac import rbac
# from roles import roles
from models import db, User
# from sts import sts
# from landfill import landfill
# from vehicle import vehicle
# from unassigned import unassigned
# from bill_view import bill_view
# from bills import bills
from weather import weather
from comments import comments
from places_view import places_view
from add_place import add_place


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'deadbeefedfrfr@gmail.com'
app.config['MAIL_PASSWORD'] = 'wbrlyrvjaeqgybcs'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False


db.init_app(app)
mail = Mail(app)
app.secret_key = 'secret_key'


app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(login, url_prefix="/login")
app.register_blueprint(dashboard, url_prefix="/dashboard")
app.register_blueprint(find_places, url_prefix="/find_places")
# app.register_blueprint(all_users, url_prefix="/all_users")
# app.register_blueprint(users, url_prefix="/users")
app.register_blueprint(security, url_prefix="/security")
# app.register_blueprint(profile, url_prefix="/profile")
# app.register_blueprint(rbac, url_prefix="/rbac")
# app.register_blueprint(roles, url_prefix="/roles")
# app.register_blueprint(sts, url_prefix="/sts")
# app.register_blueprint(landfill, url_prefix="/landfill")
# app.register_blueprint(vehicle, url_prefix="/vehicle")
# app.register_blueprint(unassigned, url_prefix="/unassigned")
# app.register_blueprint(bill_view, url_prefix='/bill-view')
# app.register_blueprint(bills, url_prefix='/bills')
app.register_blueprint(weather, url_prefix='/weather')
app.register_blueprint(comments, url_prefix='/comments')
app.register_blueprint(places_view, url_prefix='/places_view')
app.register_blueprint(add_place, url_prefix='/add-place')


with app.app_context():
    db.create_all()
    # admin = Role("admin", [1, 2, 3, 4])
    # unassigned = Role("unassigned", [2])
    # db.session.add(unassigned)
    # db.session.add(admin)
    db.session.commit()
# init_db(app)


@app.route('/', methods=['GET'])
def ind():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
