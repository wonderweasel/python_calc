pipeline {
    agent any
    triggers {
        pollSCM ('* * * * *')
    }
    stages {
        stage("Unit Test") {
            steps {
                sh "python ./src/test_calculator.py"
            }
        }
    }
}