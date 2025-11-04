from flask import Flask, request, jsonify

app = Flask(__name__)
workouts = []

def calculate_calories(duration):
    return duration * 5

def success(message, data=None, status=200):
    res = {"status": "success", "message": message}
    if data is not None:
        res["data"] = data
    return jsonify(res), status

def error(message, status=400):
    return jsonify({"status": "error", "message": message}), status

@app.route('/')
def home():
    return success("ACEest Fitness API v1.2.2 - Standardized Responses")

@app.route('/add_workout', methods=['POST'])
def add_workout():
    data = request.get_json()
    if not data:
        return error("JSON body required")

    workout = data.get("workout")
    duration = data.get("duration")

    if not workout or duration is None:
        return error("Workout & duration required")

    try:
        duration = int(duration)
        calories = calculate_calories(duration)
        workouts.append({"workout": workout, "duration": duration, "calories": calories})
        return success("Workout added", workouts[-1], 201)
    except ValueError:
        return error("Duration must be integer")

@app.route('/workouts')
def get_workouts():
    return success("Data fetched", workouts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
