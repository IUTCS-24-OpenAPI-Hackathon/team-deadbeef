from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, time
import json
import re
import math

# from app import db
db = SQLAlchemy()


def remove_int(input_string, integer_to_remove):
    # Define a regular expression pattern to find integers within square brackets
    pattern = r"\[(\d+),(\d+),(\d+)\]"

    # Find all integers within square brackets
    matches = re.findall(pattern, input_string)

    # If matches are found, remove the specified integer
    if matches:
        # Loop through all matches
        for match in matches:
            # Convert match to integers
            integers = [int(x) for x in match]
            # Check if specified integer is present
            if integer_to_remove in integers:
                # Remove the specified integer from the list
                integers.remove(integer_to_remove)
                # Reconstruct the modified string
                modified_string = "[" + ",".join(str(x) for x in integers) + "]"
                # Replace the original string with the modified one
                modified_string = re.sub(pattern, modified_string, input_string)
                # Return the modified string
                return modified_string
    # If no matches are found or the specified integer is not present, return the original string
    return input_string


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(100))
    role_id = db.Column(db.Integer, nullable=False)
    verified = db.Column(db.Integer)

    def __init__(self, email, password, role_id, name="Shreya", contact="01552393972"):
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.role_id = 0
        self.verified = 0

    def update_password(self, new_password):
        self.password_hash = generate_password_hash(new_password)
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Verification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    code = db.Column(db.String)
    timestamp = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, email, code, timestamp=datetime.now()):
        self.email = email
        self.code = code
        self.timestamp = timestamp

    def update_code(self, code, timestamp=datetime.now()):
        self.code = code
        self.timestamp = timestamp


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,  db.ForeignKey('user.id'), nullable=False)
    location_id = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(100))

    def __init__(self, user_id, location_id, text=""):
        self.user_id = user_id
        self.location_id = location_id
        self.text = text


class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float, unique=True)
    lon = db.Column(db.Float)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String)
    country = db.Column(db.String)
    type = db.Column(db.String)

    def __init__(self, lat, lon, name, type, city, country):
        self.lat = lat
        self.lon = lon
        self.name = name
        self.type = type
        self.city = city
        self.country = country

    def calculate_distance(self, lat, lon):
        R = 6371.0  # Radius of the Earth in kilometers
        lat1 = math.radians(lat)
        lon1 = math.radians(lon)
        lat2 = math.radians(self.lat)
        lon2 = math.radians(self.lon)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c

        return distance
    