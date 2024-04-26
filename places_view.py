from flask import Flask, url_for, Blueprint, render_template, request, jsonify

import weather
from models import Comments
import requests

places_view = Blueprint("places_view", __name__, static_folder="static", template_folder="templates")


@places_view.route('/<string:name>/<string:city>/<string:country>/<float:lat>/<float:lon>/<string:type>', methods=['GET'])
def view_place(name, city, country, lat, lon, type):
    print('a')
    a_quality = ['Good', 'Fair', 'Moderate', 'Poor', 'Very Poor']
    # data = request.json
    # var = {
    #     'name': data.get('name'),
    #     'lat': data.get('lat'),
    #     'lon': data.get('lon'),
    #     'city': data.get('city'),
    #     'country': data.get('country'),
    #     'type': data.get('type')
    # }
    print('b')
    var = {
        'name': name,
        'lat': lat,
        'lon': lon,
        'city': city,
        'country': country,
        'type': type
    }
    print('c')
    # var['lat'] = data.get('lat')
    # var['lon'] = data.get('lon')
    # name = data.get('name')
    # city = data.get('city')
    # country = data.get('country')

    st_lat = "{:.7f}".format(var['lat'])
    st_lon = "{:.7f}".format(var['lon'])

    # base_url = url_for(f"weather.get_weather({st_lat}, {st_lon})", _external=True)
    # base_url = url_for(f"weather.get_weather", _external=True)
    # endpoint2_url = f"{base_url}/{st_lat}/{st_lon}"
    print('a')
    base_url = url_for('weather.get_weather', lat=st_lat, lon=st_lon, _external=True)

    response = requests.get(base_url)

    if response.status_code == 201:
        weather_data = response.json()
        var['temp'] = weather_data.get('temp')
        var['realfeel'] = weather_data.get('realfeel')
        var['wspeed'] = weather_data.get('wspeed')
        var['aqi'] = weather_data.get('aqi')
        var['weather_status'] = weather_data.get('weather_status')
        return render_template('location-details.html', var=var)

