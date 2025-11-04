from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage
workouts = []

# ✅ Modular function to add workout
def add_to_workouts(workout, duration):
    workouts.append({"workout": workout, "duration": duration})
    return True

@app.route('/')
def home():
    return jsonify({"message": "ACEest Fitness API v1.1 - Modular Version"})

# ✅ Add workout (POST API)
@app.route('/add_workout', methods=['POST'])
def add_workout():
    data = request.get_json()

    # Input validation
    if not data:
        return jsonify({"error": "JSON body is required"}), 400

    workout = data.get("workout")
    duration = data.get("duration")

    if not workout or duration is None:
        return jsonify({"error": "Workout and duration fields are required"}), 400

    try:
        duration = int(duration)
        add_to_workouts(workout, duration)
        return jsonify({"message": f"{workout} added successfully", "duration": duration}), 201

    except ValueError:
        return jsonify({"error": "Duration must be an integer"}), 400

# ✅ Get workouts (GET API)
@app.route('/workouts', methods=['GET'])
def get_workouts():
    if not workouts:
        return jsonify({"message": "No workouts available"}), 200
    return jsonify(workouts), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
