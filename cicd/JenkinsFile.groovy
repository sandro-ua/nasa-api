pipeline {
    agent any
    environment {
        PATH = "/usr/local/bin:$PATH"
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sandro-ua/nasa-api'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install pipenv'
                    sh '. venv/bin/activate && pipenv install --dev'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh ". venv/bin/activate && pytest tests/epic_tests.py"
                }
            }
        }
    }
}
