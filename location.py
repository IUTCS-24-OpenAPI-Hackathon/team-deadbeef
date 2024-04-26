from flask import Flask, request, Blueprint
from flask_restful import Resource, Api

places_view = Blueprint("places_view", __name__, static_folder="static", template_folder="templates")

api = Api(app)


class Location(Resource):
    def post(self):
        data = request.get_json()
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        if latitude is None or longitude is None:
            return {"error": "Latitude and longitude are required"}, 400
        return {"latitude": latitude, "longitude": longitude}

api.add_resource(Location, '/location')
