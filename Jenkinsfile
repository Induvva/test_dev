pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\duvva\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
    }

    stages {

        stage('Build docker image') {
            steps {
                echo "Build a docker image"
                bat "docker build -t induduvva/myregistrationapp:register ."
            }
        }

        stage('Give docker credentials') {
            steps {
                echo "Give docker credentials"

                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_TOKEN'
                )]) {
                    bat "docker login -u %DOCKER_USERNAME% -p %DOCKER_TOKEN%"
                }
            }
        }

        stage('Push the docker image into DockerHub') {
            steps {
                echo "Push docker image into DockerHub"
                bat "docker tag induduvva/myregistrationapp:register induduvva/test_dev:register"
                bat "docker push induduvva/test_dev:register"
            }
        }

        stage('Deploy in Kubernetes') {
            steps {
                echo "Deploying into Kubernetes"
                bat "kubectl apply -f deployment.yaml"
                bat "kubectl apply -f service.yaml"
            }
        }
    }

    post {
        success {
            echo "Successfully completed"
        }

        failure {
            echo "Failed!"
        }
    }
}
