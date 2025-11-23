from flask import Blueprint, request, redirect, current_app
from utils import generate_short_code

shortener_bp = Blueprint("shortener", __name__)

@shortener_bp.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.json
    original_url = data.get("url")

    if not original_url:
        return {"error": "URL is required"}, 400

    db = current_app.config["DB"]

    short_code = generate_short_code()

    db.sortUrlDB.insert_one({
        "short_code": short_code,
        "original_url": original_url,
        "clicks": 0
    })

    return {
        "message": "Short URL created!",
        "short_url": f"http://localhost:5000/api/{short_code}"
    }


@shortener_bp.route("/<short_code>")
def redirect_to_url(short_code):
    db = current_app.config["DB"]
    record = db.sortUrlDB.find_one({"short_code": short_code})

    if not record:
        return {"error": "Invalid short URL"}, 404

    db.sortUrlDB.update_one(
        {"short_code": short_code},
        {"$inc": {"clicks": 1}}
    )

    return redirect(record["original_url"])
