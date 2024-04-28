from flask import Flask, Blueprint, render_template, request, jsonify
from models import Comments, db

comments = Blueprint("comments", __name__, static_folder="static", template_folder="templates")


@comments.route('/', methods=['POST'])
def add_comment():
    data = request.json
    user_id = data.get('user_id')
    text = data.get("text")
    location_name = data.get("location_name")

    comment = Comments(user_id=user_id, location_name=location_name, text=text)
    db.session.add(comment)
    db.session.commit()
    return jsonify({"success": True, "message": "Comment Added"}), 201
