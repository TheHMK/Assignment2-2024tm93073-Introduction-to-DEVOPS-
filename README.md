# ACEest Fitness & Gym – DevOps Assignment

![CI](https://github.com/TheHMK/Assignment2-2024tm93073-Introduction-to-DEVOPS-/actions/workflows/ci.yml/badge.svg)

This is a Flask-based Fitness Tracking API developed as part of DevOps learning. It demonstrates CI/CD pipelines, Dockerization, Kubernetes deployment, and automation using Jenkins.

---

## ✅ Features (Version v1.3 – Final)

✔ Add Workout (with duration & calorie calculation)  
✔ Get All Workouts  
✔ BMI Calculator (weight + height)  
✔ Standardized API responses (v1.2.2+)  
✔ Global error handling (v1.2.3)  
✔ Containerized with Docker  
✔ CI/CD using Jenkins  
✔ Kubernetes deployment supported  

---

## 📁 Project Structure

ACEest-Fitness-DevOps/
├── app_v1_0/ → Basic Flask App
├── app_v1_1/ → Modular Version
├── app_v1_2/ → Added Calorie Tracking
├── app_v1_3/ → ✅ Final Production Version (BMI, API response model)
├── tests/ → Pytest Unit Test Cases
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
└── kubernetes/
 ├── deployment.yml
 ├── service.yml
 ├── rolling-update.yml
 ├── blue-green.yml
 └── canary.yml

---

## 🚀 How to Run Locally

### 1️⃣ Install Dependencies:
pip install -r requirements.txt

### 2️⃣ Run the Flask Application:
python app_v1_3/app.py

### API will be available at:
http://localhost:5000/

---

## 🐳 Run Using Docker

docker build -t aceest-fitness:v1.3 .
docker run -p 5000:5000 aceest-fitness:v1.3

---

## ✅ Run Test Cases

pytest -v

---

## ⚙️ CI/CD Pipeline – Jenkins

This project includes a **Jenkinsfile** with the following pipeline stages:

✔ Checkout Code from GitHub  
✔ Install Dependencies  
✔ Run Pytest  
✔ Build Docker Image  
✔ Push to DockerHub (if credentials configured)  

---

## ☸️ Kubernetes Deployment (Optional)

To deploy on Kubernetes:

kubectl apply -f kubernetes/deployment.yml
kubectl apply -f kubernetes/service.yml

For Blue-Green Deployment:
kubectl apply -f kubernetes/blue-green.yml

For Canary Deployment:
kubectl apply -f kubernetes/canary.yml

---

## 👨‍💻 Author

**ACEest Fitness DevOps Project**  
Rahul Harmalkar
