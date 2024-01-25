def printCommandResult(String command) {
    script {
        def result = sh(script: ". venv/bin/activate && " + command, returnStdout: true).trim()
        echo "Command: ${command}"
        echo "Command result: ${result}"
    }
}

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
                    printCommandResult('pip list')
                    printCommandResult('echo $PATH')

                    sh '. venv/bin/activate && chmod +x tests/epic_tests.py'
                    sh '. venv/bin/activate && pytest tests/epic_tests.py --html=report.html --self-contained-html'
                }
            }
        }
        
        stage('Generate Report') {
            steps {
                echo 'Generating report...'
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
            echo 'Post steps to be executed'
        }
    }
}