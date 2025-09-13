from flask import Flask, render_template, request
import requests, os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not found. Please set it in the .env file.")

HISTORY_FILE = "history.txt"

# Load history from file at startup
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r") as f:
        history = [line.strip() for line in f.readlines()]
else:
    history = []

def save_history():
    """Save history to file"""
    with open(HISTORY_FILE, "w") as f:
        f.write("\n".join(history))

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None
    unit = "metric"
    city = None

    if request.method == "POST":
        city = request.form.get("city", "").strip().title()
        unit = request.form.get("unit", "metric")
    else:
        city = request.args.get("city", "").strip().title()

    if city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={unit}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raises HTTPError for bad responses
            data = response.json()
            weather = {
                "city": data["name"],
                "desc": data["weather"][0]["description"].title(),
                "icon": data["weather"][0]["icon"],
                "temp": data["main"]["temp"],
                "feels": data["main"]["feels_like"],
                "wind": data["wind"]["speed"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M:%S"),
                "sunset": datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M:%S"),
            }

            # maintain search history (avoid duplicates, max 5 items)
            if city not in history:
                history.insert(0, city)
            else:
                history.remove(city)
                history.insert(0, city)

            if len(history) > 5:
                history.pop()

            save_history()

        except requests.exceptions.HTTPError:
            error = "City not found. Please check the name."
        except requests.exceptions.RequestException:
            error = "Network error. Please try again later."
    elif request.method == "POST":
        error = "Please enter a valid city name."

    return render_template("index.html", weather=weather, error=error, unit=unit, history=history, city=city)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT
    app.run(host="0.0.0.0", port=port, debug=True)
