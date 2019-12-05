pipeline {
    agent any
    stages {
        stage('Build') {
		steps {
                sh 'bash install.sh'
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
			# start the flask app
			sudo systemctl start flask-app
                '''
            }
        }
    }
}
