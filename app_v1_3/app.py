from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
workouts = []

# ✅ Standard JSON response format
def success_response(message, data=None):
    return jsonify({
        "status": "success",
        "message": message,
        "data": data
    })

def error_response(message, code=400):
    return jsonify({
        "status": "error",
        "message": message
    }), code

@app.route('/')
def home():
    return success_response("ACEest Fitness API v1.3 is running")

# ✅ POST: Add Workout
@app.route('/add_workout', methods=['POST'])
def add_workout():
    try:
        data = request.get_json()
        if not data or "workout" not in data or "duration" not in data:
            return error_response("Workout and duration are required", 400)

        workout = data["workout"]
        duration = int(data["duration"])

        workouts.append({"workout": workout, "duration": duration})
        return success_response("Workout added successfully", {"workout": workout, "duration": duration}), 201

    except Exception as e:
        return error_response(str(e), 500)

# ✅ GET: All Workouts
@app.route('/workouts', methods=['GET'])
def get_workouts():
    return success_response("Workouts fetched successfully", workouts)

# ✅ POST: BMI Calculation
@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    try:
        data = request.get_json()
        if "weight" not in data or "height" not in data:
            return error_response("Weight and height are required", 400)

        weight = float(data["weight"])
        height = float(data["height"]) / 100 

        bmi = weight / (height * height)
        status = ""

        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi < 24.9:
            status = "Normal weight"
        else:
            status = "Overweight"

        return success_response("BMI calculated successfully", {
            "bmi": round(bmi, 2),
            "status": status
        })

    except Exception as e:
        return error_response(str(e), 500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
