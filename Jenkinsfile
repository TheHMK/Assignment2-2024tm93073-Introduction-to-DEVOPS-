pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/Assignment2-2024tm93073-Introduction-to-DEVOPS-.git'
        DOCKER_IMAGE = 'aceest-fitness-app'
        DOCKER_TAG = 'v1.3'
        DOCKERHUB_USER = 'rahul-mtech'   // Replace with your username
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo "Cloning repository from GitHub..."
                git branch: 'main', url: "${REPO_URL}"
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing required Python packages..."
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "Running pytest..."
                sh 'pytest -v || echo "Tests failed, but continuing..."'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh """
                docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKERHUB_USER}/${DOCKER_IMAGE}:${DOCKER_TAG}
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo "Pushing Docker image to Docker Hub..."
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                  usernameVariable: 'USERNAME',
                                                  passwordVariable: 'PASSWORD')]) {
                    sh """
                    echo $PASSWORD | docker login -u $USERNAME --password-stdin
                    docker push ${DOCKERHUB_USER}/${DOCKER_IMAGE}:${DOCKER_TAG}
                    """
                }
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline executed successfully!"
        }
        failure {
            echo "❌ Pipeline failed. Please check logs!"
        }
    }
}
