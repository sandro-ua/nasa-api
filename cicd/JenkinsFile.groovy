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
        stage('Cleanup Workspace') {
            steps {
                deleteDir()
            }
        }

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
                    sh '. venv/bin/activate && pipenv install -r requirements.txt'

                    printCommandResult('cat Pipfile.lock')  // Print contents of the lock file
                    printCommandResult('pipenv --venv')
                    printCommandResult('pipenv run pip list')
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    printCommandResult('echo $PATH')
                    sh '. venv/bin/activate && chmod +x tests/epic_tests.py'
                    sh '. venv/bin/activate && pytest tests/epic_tests.py --html=results/report.html --self-contained-html'
                }
            }
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
            echo 'Post steps to be executed.'

            // Publish the HTML report
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'results', // Specify the directory where your pytest-html report is generated
                reportFiles: 'report.html', // Specify the filename of your pytest-html report
                reportName: 'Pytest HTML Report' // Provide a name for the HTML report
            ])
        }
    }
}