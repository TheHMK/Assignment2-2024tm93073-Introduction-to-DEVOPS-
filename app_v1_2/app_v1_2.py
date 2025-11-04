from flask import Flask, request, jsonify

app = Flask(__name__)

workouts = []

def calculate_calories(duration):
    return duration * 5  # Simple logic

def add_to_workouts(workout, duration, calories):
    workouts.append({"workout": workout, "duration": duration, "calories": calories})

@app.route('/')
def home():
    return jsonify({"message": "ACEest Fitness API v1.2 - Calorie Tracking Added"})

@app.route('/add_workout', methods=['POST'])
def add_workout():
    data = request.get_json()
    workout = data.get("workout")
    duration = data.get("duration")
    calories = data.get("calories")

    if not workout or not duration:
        return jsonify({"error": "Workout and duration are required"}), 400

    try:
        duration = int(duration)
        calories = int(calories) if calories else calculate_calories(duration)
        add_to_workouts(workout, duration, calories)
        return jsonify({"message": "Workout added", "calories": calories}), 201
    except ValueError:
        return jsonify({"error": "Duration and calories must be integers"}), 400

@app.route('/workouts', methods=['GET'])
def get_workouts():
    return jsonify(workouts if workouts else {"message": "No workouts logged yet"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
