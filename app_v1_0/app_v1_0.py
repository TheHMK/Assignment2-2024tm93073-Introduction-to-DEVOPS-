from flask import Flask, request, jsonify

app = Flask(__name__)

workouts = []  # In-memory list to store workouts

@app.route('/')
def home():
    return jsonify({"message": "Welcome to ACEest Fitness & Gym API"})

@app.route('/add_workout', methods=['POST'])
def add_workout():
    data = request.get_json()
    workout = data.get("workout")
    duration = data.get("duration")

    if not workout or not duration:
        return jsonify({"error": "Workout and duration are required"}), 400

    try:
        duration = int(duration)
        workouts.append({"workout": workout, "duration": duration})
        return jsonify({"message": f"{workout} added successfully"}), 201
    except ValueError:
        return jsonify({"error": "Duration must be an integer"}), 400

@app.route('/workouts', methods=['GET'])
def get_workouts():
    if not workouts:
        return jsonify({"message": "No workouts logged yet"}), 200
    return jsonify(workouts), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
