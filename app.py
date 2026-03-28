from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

COOKIE = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzZXNzaW9uSWQiOiI5Mjc2YTk2My03OTc5LTQwODEtYTBkMy0wMzYxOGFiM2Q4OGMiLCJjcmVhdGVkQXQiOjE3NzQxMDk2MjIsInVzZXJJZCI6MzU5NH0.kdQ6Ic_teyTtOIB36WyV3qPYdEIccsfbSmIYgNyJzOMsk797UZYTpA-Qsa4W49njKY_op9hiz_1NLJAv_scihg"

@app.route("/")
def home():
    with open("index.html") as f:
        return f.read()

@app.route("/generate_robux", methods=["POST"])
def generate_robux():
    data = request.get_json()
    amount = data.get("amount")
    api_url = "https://www.caelus.lol/games/api/generate_robux"
    headers = {"Cookie": COOKIE, "Content-Type": "application/json"}
    payload = {"amount": amount}
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        return jsonify({"message": "Robux generated successfully!"})
    else:
        return jsonify({"message": "Failed to generate Robux."}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)
