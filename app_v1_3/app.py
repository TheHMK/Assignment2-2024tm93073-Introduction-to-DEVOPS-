from flask import Flask, request, jsonify

app = Flask(__name__)
workouts = []

def calculate_calories(duration):
    return duration * 5

def calculate_bmi(weight, height):
    h = height / 100
    return round(weight / (h * h), 2)

@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({"status": "error", "message": f"Internal Error: {str(e)}"}), 500

@app.route('/calculate_bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    weight = data.get("weight")
    height = data.get("height")

    if not weight or not height:
        return jsonify({"status": "error", "message": "Weight and height required"}), 400

    bmi_value = calculate_bmi(float(weight), float(height))
    return jsonify({"status": "success", "bmi": bmi_value}), 200

# (Workout APIs same as v1_2_3)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
