from flask import Blueprint, render_template, jsonify
from app.core.services import get_app_info

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/info")
def info():
    return jsonify(get_app_info())
