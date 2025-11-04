from flask import Flask, request, jsonify

app = Flask(__name__)
workouts = []

def calculate_calories(duration):
    return duration * 5

@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({"status": "error", "message": f"Internal Error: {str(e)}"}), 500

@app.route('/add_workout', methods=['POST'])
def add_workout():
    data = request.get_json()
    workout = data.get("workout")
    duration = data.get("duration")

    if not workout or duration is None:
        return jsonify({"status": "error", "message": "Workout and duration required"}), 400

    duration = int(duration)
    calories = calculate_calories(duration)
    workouts.append({"workout": workout, "duration": duration, "calories": calories})
    return jsonify({"status": "success", "message": "Workout added", "data": workouts[-1]}), 201

@app.route('/workouts')
def get_workouts():
    return jsonify({"status": "success", "data": workouts}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
