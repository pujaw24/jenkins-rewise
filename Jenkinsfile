pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'pujadocker1999/my-first-docker-image'
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t ${DOCKER_IMAGE}:latest .
                '''
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login \
                            -u "$DOCKER_USERNAME" \
                            --password-stdin
                    '''
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh '''
                    docker push ${DOCKER_IMAGE}:latest
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker rm -f hello-container || true

                    docker run -d \
                        --name hello-container \
                        -p 8000:8000 \
                        ${DOCKER_IMAGE}:latest
                '''
            }
        }

        stage('Test Application') {
            steps {
                sh '''
                    sleep 3
                    curl -f http://localhost:8000
                '''
            }
        }
    }
}
