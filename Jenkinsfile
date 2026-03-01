pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/jenish11052004/scientific-calculator.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install --upgrade pip'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'source venv/bin/activate && pytest -v'
            }
        }
    }

    post {
        success {
            echo 'Build SUCCESS: All tests passed!'
        }
        failure {
            echo 'Build FAILED: Check test errors.'
        }
    }
}