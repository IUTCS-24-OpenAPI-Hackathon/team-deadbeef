from flask import Blueprint, url_for, make_response, redirect, render_template, request, jsonify
import requests
from models import Place, db

add_place = Blueprint("add_place", __name__, static_folder="static", template_folder="templates")


@add_place.route('/', methods=['POST'])
def add_new_place():
    data = request.json
    lat = data.get('lat')
    lon = data.get('lon')
    name = data.get('name')
    city = data.get('city')
    country = data.get('country')
    type = data.get('type')

    place = Place(lat=lat, lon=lon, name=name, type=type, city=city, country=country)
    place_match = Place.query.filter_by(lat=lat, lon=lon).first()
    if place_match:
        return jsonify({"success": False, "message": "Place already exists"}), 401
    else:
        db.session.add(place)
        db.session.commit()
        return jsonify({"success": True, "message": "Place added"}), 201


@add_place.route('/view')
def add_place_view():
    return render_template("add_place.html")
