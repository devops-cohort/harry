pipeline {
    agent any
    stages {
        stage('Build') {
		steps {
                sh 'bash install-development.sh'
            }
	}
	stage('Test') {
            steps {
                sh 'bash test.sh'
            }
        }
        stage('Run') {
            steps {
                sh '''
			# start the flask app development
			sudo systemctl start flask-app-development
                '''
            }
        }
    }
}
