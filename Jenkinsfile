pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDENTIALS = credentials('dockerhub-id')
        IMAGE_NAME = "souravl13/multi-tenant-dashboard"
    }
    stages {
        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/souravl13/multi-tenant-dashboard.git', branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                script { docker.build("${IMAGE_NAME}:latest", ".") }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_HUB_CREDENTIALS}") {
                        docker.image("${IMAGE_NAME}:latest").push()
                    }
                }
            }
        }
        stage('Deploy with Docker Compose') {
            steps {
                sh """
                docker-compose down
                docker-compose up -d --build
                """
            }
        }
    }
    post { always { echo 'Pipeline finished.' } }
}
