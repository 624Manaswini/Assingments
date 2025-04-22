from flask import Flask, jsonify
import random
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the weather app!"

def get_forecast():
    forecast_data = []
    today = datetime.utcnow()

    for i in range(10):
        date = today + timedelta(days=i)
        high_temp = random.randint(27, 38)
        low_temp = random.randint(17, high_temp - 1)

        forecast_data.append({
            "code": str(random.choice([23, 28, 30, 31, 34, 26])),
            "date": date.strftime("%d %b %Y"),
            "day": date.strftime("%a"),
            "high": str(high_temp),
            "low": str(low_temp),
            "text": random.choice([
                "Clear", "Breezy", "Cloudy",
                "Mostly Cloudy", "Partly Cloudy", "Mostly Sunny"
            ])
        })

    return forecast_data

@app.route('/weather/<city>')
def weather(city):
    now = datetime.utcnow()

    data = {
        "query": {
            "count": 1,
            "created": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "lang": "en-IN",
            "results": {
                "channel": {
                    "title": f"Yahoo! Weather - {city}, Unknown",
                    "location": {
                        "city": city,
                        "country": "Unknown",
                        "region": "Unknown"
                    },
                    "units": {
                        "temperature": "F",
                        "distance": "mi",
                        "speed": "mph",
                        "pressure": "in"
                    },
                    "wind": {
                        "chill": str(random.randint(0, 10)),
                        "direction": str(random.randint(0, 360)),
                        "speed": str(random.randint(10, 30))
                    },
                    "atmosphere": {
                        "humidity": str(random.randint(60, 90)),
                        "pressure": "1007.0",
                        "rising": "0",
                        "visibility": "16.1"
                    },
                    "astronomy": {
                        "sunrise": "7:06 am",
                        "sunset": "10:56 pm"
                    },
                    "item": {
                        "title": f"Conditions for {city} at {now.strftime('%I:%M %p')}",
                        "condition": {
                            "code": "31",
                            "date": now.strftime("%a, %d %b %Y %I:%M %p"),
                            "temp": str(random.randint(15, 35)),
                            "text": "Clear"
                        },
                        "forecast": get_forecast()
                    }
                }
            }
        }
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run()
