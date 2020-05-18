pipeline {
    agent { docker { image 'python:3.5.1' } }
    parameters {
        string(name: 'GUESS', defaultValue: '', description: 'Please enter a number from 1 to 10.')
    }
    stages {
        stage('test') {
            steps {
                sh 'python --version'
                sh 'echo "Hello world!"'
            }
        }
        stage('run') {
            steps {
                sh 'echo \$GUESS | python hello.py'
            }
        }
    }
}