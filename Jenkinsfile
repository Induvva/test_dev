pipeline{
    agent-any
    stages{
        stage('Build docker image'){
            steps{
                echo "Build a docker image"
                bat "docker build -t myregistrationapp:reg ."

            }
        }
        stage('give docker credentials'){
            steps{
                echo "give docker credentials"
                withCredentials([usernamePassword( 
                     credentialsId: 'dockerhub',
                     usernameVariable: 'DOCKER_USERNAME',
                     passwordVariable: 'DOCKER_TOKEN')]) {
                    bat "docker login -u %DOCKER_USERNAME% -p %DOCKER_TOKEN%"
                }
            }
        }
        Stage('Push the docker image into kubernetes'){
            steps{
                echo "Push docker image into dockerhub"
                bat "docker push myregistrationapp:reg induduvva/myregistrationapp:register"
                bat "docker push induduvva/myregistrationapp:register"

            }
        }
        stage("Deploy in kubernetes"){
            steps{
                echo "Deploying into kubernetes"
                bat "kubectl apply -f deployment.yaml"
                bat "kubectl apply -f service.yaml"
            }
        }
    }
    post{
        success{
            echo "Successfully completed"
        }
        failure{
            echo "failed!"
        }
    }
}