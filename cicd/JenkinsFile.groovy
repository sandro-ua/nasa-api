pipeline {
    agent any
    environment {
        PATH = "/usr/local/bin:$PATH" // Add the path to pipenv
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
                    sh ". venv/bin/activate && pytest tests/epic_tests.py --alluredir=target/allure-results'"
                }
            }
        }
        
        stage('Generate Allure Report') {
            steps {
                echo 'Generating Allure report...'
                sh 'allure generate target/allure-results -o target/allure-report'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
            // Additional steps to be executed on success
        }
        
        failure {
            echo 'Pipeline failed!'
            // Additional steps to be executed on failure
        }

        always {
            allure([
                includeProperties: false,
                jdk: '',
                properties: [],
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'target/allure-results']]
            ])
        }
    }
}
