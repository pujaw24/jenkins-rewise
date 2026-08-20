pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building application...'
                sh 'echo Build completed'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'echo Tests passed'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'

                sh '''
                    echo "Jenkins build completed!" > /tmp/jenkins-build.txt
                    echo "Build number: ${BUILD_NUMBER}" >> /tmp/jenkins-build.txt
                    echo "Build time: $(date)" >> /tmp/jenkins-build.txt
                '''

                sh 'echo Deployment successful'
            }
        }
    }
}
