import requests
from flask import Flask, Blueprint, render_template, session, redirect, request, make_response, jsonify

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


@find_places.route('/local', methods=['POST'])
def find_local_places():
    data = request.json
    lat = data.get('lat')
    lon = data.get('lon')
    radius = data.get('radius')
    type = data.get('type')
    places = Place.query.all()  # Fetch all places from the database
    places_result = []

    for place in places:
        if place.calculate_distance(lat=lat, lon=lon) <= radius and type == place.type:
            places_result.append({
                'name': place.name,
                'lat': place.latitude,
                'lon': place.longitude,
                'city': place.city,
                'country': place.country
                # Add more fields as needed
            })

    # Construct the JSON response
    if not places_result:
        return jsonify({"success": True, "message": "No Such place"}), 204

    else:
        response_data = jsonify(places_result)
        # Set the status code to 201
        response = make_response(response_data, 201)
        return response

