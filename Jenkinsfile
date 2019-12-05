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
                sh '''
			# configure python virtual environment and install dependencies
			sudo su - pythonadm << EOF
			cd ${install_dir}
			source venv/bin/activate
			pytest --cov-config=.coveragerc --cov-report html:cov_html --cov=. testing
			EOF
                '''
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
