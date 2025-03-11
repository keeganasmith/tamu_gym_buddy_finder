from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_AUTH_URL = f"{SUPABASE_URL}/auth/v1"

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}


@app.route("/login", methods=["POST"])
def login():
    body = request.get_json()
    res = requests.post(
        f"{SUPABASE_AUTH_URL}/token?grant_type=password",
        headers=HEADERS,
        json={
            "email": body["email"],
            "password": body["password"]
        }
    )
    return jsonify(res.json()), res.status_code


@app.route("/signup", methods=["POST"])
def signup():
    body = request.get_json()
    res = requests.post(
        f"{SUPABASE_AUTH_URL}/signup",
        headers=HEADERS,
        json={
            "email": body["email"],
            "password": body["password"]
        }
    )
    return jsonify(res.json()), res.status_code


@app.route("/me", methods=["GET"])
def get_user():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    user_headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {token}",
    }
    res = requests.get(f"{SUPABASE_AUTH_URL}/user", headers=user_headers)
    return jsonify(res.json()), res.status_code


if __name__ == "__main__":
    app.run(port=8000, debug=True)
