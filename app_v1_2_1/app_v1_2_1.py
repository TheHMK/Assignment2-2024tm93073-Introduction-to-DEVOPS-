from flask import Flask, request, jsonify

app = Flask(__name__)

workouts = []

def calculate_calories(duration):
    return duration * 5

@app.route('/add_workout', methods=['POST'])
def add_workout():
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body is required"}), 400

    workout = data.get("workout")
    duration = data.get("duration")

    if not workout or duration is None:
        return jsonify({"error": "Workout and duration are required"}), 400

    try:
        duration = int(duration)
        calories = calculate_calories(duration)
        workouts.append({"workout": workout, "duration": duration, "calories": calories})
        return jsonify({"message": "Workout added", "data": workouts[-1]}), 201
    except ValueError:
        return jsonify({"error": "Duration must be an integer"}), 400

@app.route('/workouts')
def get_workouts():
    return jsonify(workouts if workouts else {"message": "No workouts logged"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
