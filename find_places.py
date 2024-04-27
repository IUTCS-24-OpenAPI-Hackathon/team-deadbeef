import requests
from flask import Flask, Blueprint, render_template, session, redirect, request

from models import User, db, Place

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


@find_places.route('/local')
def find_places():
    data = request.json
    lat = data.get('lat')
    lon = data.get('lon')
    radius = data.get('radius')
    places = Place.query.filter_by().all()
    places_result = []
    for place in places:
        if place.calculate_distance(lat=lat, lon=lon) <= radius:
            places_result.insert(place)

