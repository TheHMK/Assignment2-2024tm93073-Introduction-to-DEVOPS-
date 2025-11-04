import json
import pytest
from app_v1_3.app_v1_3 import app   # Importing the Flask app

# Fixture to create a test client
@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

# ✅ Test Home Route
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "ACEest Fitness API" in data["message"]

# ✅ Test Adding Workout
def test_add_workout(client):
    response = client.post('/add_workout', json={
        "workout": "Running",
        "duration": 30
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["status"] == "success"
    assert data["data"]["workout"] == "Running"
    assert data["data"]["duration"] == 30

# ✅ Test Get Workouts
def test_get_workouts(client):
    response = client.get('/workouts')
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert isinstance(data["data"], list)

# ✅ Test Add Workout Missing Fields
def test_add_workout_missing_fields(client):
    response = client.post('/add_workout', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"

# ✅ Test BMI Calculation
def test_bmi_calculation(client):
    response = client.post('/calculate_bmi', json={
        "weight": 70,
        "height": 175
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert round(data["data"]["bmi"], 2) == round(70 / (1.75 * 1.75), 2)

# ✅ Test BMI Missing Parameters
def test_bmi_missing_fields(client):
    response = client.post('/calculate_bmi', json={"weight": 70})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
