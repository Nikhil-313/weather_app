# 🌤️ Weather App
A modern, responsive web-based Weather App built with Flask, HTML/CSS, and the OpenWeatherMap API for real-time weather information.

🌐 **Live Site:** [Weather App on Render](https://weather-app-8lct.onrender.com)

## 🗄️ Data Storage
✅ Local Files
- history.txt: Stores the last 5 searched cities for quick access
- .env: Stores the OpenWeatherMap API key (keep it private, do NOT push to GitHub)

✅ Session Management
- Maintains the current city and selected temperature unit (°C, °F, K) for automatic updates without retyping

## 🛠️ Tech Stack
- Backend: Python, Flask, Requests, python-dotenv
- Frontend: HTML, CSS, Jinja2 Templates
- API: OpenWeatherMap API
- Other: Local file-based history storage

## 🔧 Features
🌡️ Weather Information
- Displays city name, temperature, feels-like temperature, wind speed, humidity, pressure, sunrise, and sunset
- Weather description with icon representation
- Switch temperature units (Celsius, Fahrenheit, Kelvin) and auto-update results

🖥️ User Interface
- Search for cities using an input field
- Maintains search history (last 5 cities) with clickable links
- Dark mode toggle for comfortable viewing
- Responsive design

## 🚀 Getting Started
⚙ Setup
1. Clone the repository:
git clone https://github.com/<your-username>/weather-app.git
cd weather-app
2. Create a virtual environment (optional but recommended):
Use python -m venv venv to create the environment. Activate it with source venv/bin/activate on Linux/Mac or venv\Scripts\activate on Windows.
3. Install dependencies:
Run pip install -r requirements.txt to install all required Python packages.
4. Create a .env file with your OpenWeatherMap API key:
API_KEY=your_openweathermap_api_key
5. Run the Flask app:
Execute python weather_app.py in the terminal.
6. Open your browser at:
http://127.0.0.1:5000/

## 📁 Folder Structure
```

weather_app/
├─ weather_app.py         # Main Flask app
├─ history.txt            # Local search history file
├─ .env                   # API key (do NOT push to GitHub)
├─ requirements.txt       # Python dependencies
├─ static/
│  └─ style.css           # CSS styles
└─ templates/
   └─ index.html          # HTML template

```

## ⚙ Dependencies
- Flask
- Requests
- python-dotenv

Install all dependencies via pip install -r requirements.txt.

## 📝 Notes
- .env and history.txt are ignored in .gitignore to keep them private
- Supports three temperature units: Metric (°C), Imperial (°F), Standard (K)
- Clicking a city from search history fetches its weather instantly
- Dark mode toggle included for better user experience

## 👤 Author
Nikhil Akkenapally    
Full-stack Developer | Python & Flask Enthusiast
