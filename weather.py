from flask import Blueprint, jsonify, session, request, render_template,make_response, render_template_string, url_for, redirect
from models import User, Verification, db
from flask_mail import Mail, Message
import requests

weather = Blueprint("weather", __name__, static_folder="static", template_folder="templates")


@weather.route('/<float:lat>/<float:lon>', methods=['GET'])
def get_weather(lat, lon):
    # data = request.json

    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    # api_key= "12f24bc0eb39a5fcf4e7b2098200ad92"
    api_key = "12f24bc0eb39a5fcf4e7b2098200ad92"  # Replace this with your actual API key
    url = f"{base_url}lat={lat}&lon={lon}&appid={api_key}&units=metric"
    base_url2= "http://api.openweathermap.org/data/2.5/air_pollution?"
    url2 = f"{base_url2}lat={lat}&lon={lon}&appid={api_key}&units=metric"

    response = requests.get(url)
    response2 = requests.get(url2)
    if response.status_code == 200 and response2.status_code == 200:
        weather_data = response.json()
        aqi_data = response2.json()
        temperature = weather_data['main']['temp']
        real_feel = weather_data['main']['feels_like']
        wind_speed = weather_data['wind']['speed']
        # vis_val = weather_data['visibility']
        # rain = weather_data['rain']['1h']
        weather_status = weather_data['weather'][0]['main']
        # if rain > 2.5:
        #     weather_status = 'Shower'
        # elif rain > 10:
        #     weather_status = 'Rainy'
        # elif rain > 50:
        #     weather_status = 'Thunder Storm'
        # elif vis_val<5000:
        #     weather_status = 'Cloudy'

        aqi = aqi_data['list'][0]['main']['aqi']

        # Now you can use these variables as needed
        print("Temperature:", temperature)
        print("Real Feel:", real_feel)
        print("Wind Speed:", wind_speed)
        print("aqi:", aqi)
        response3 = make_response(jsonify({"success": "True",
                                          "temp": temperature,
                                          "realfeel": real_feel,
                                          "wspeed": wind_speed,
                                          "aqi": aqi,
                                           "weather_status": weather_status}), 201)
        return response3
    else:
        return jsonify({'error': 'Failed to fetch weather info'}), response.status_code

