from flask import Flask, Blueprint, render_template, request, jsonify
from models import Comments, db

comments = Blueprint("comments", __name__, static_folder="static", template_folder="templates")


@comments.route('/', methods=['POST'])
def add_comment():
    data = request.json
    user_id = data.get('user_id')
    text = data.get("text")
    location_id = data.get("location_id")

    comment = Comments(user_id=user_id, location_id=location_id, text=text)
    db.session.add(comment)
    db.session.commit()
    return jsonify({"success": True, "message": "Comment Added"}), 201