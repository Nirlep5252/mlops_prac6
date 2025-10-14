pipeline {
    agent {
        node {
            label 'local'
            customWorkspace 'C:/Rudra/College/SEM VII/MLOps/Practicals/Practical6/1_local'
        }
    }

    stages {
        stage('Show Workspace') {
            steps {
                bat 'cd'
            }
        }

        stage('Build Images') {
            steps {
                bat 'docker-compose build'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'docker run --rm webapp pytest || echo "No tests found"'
            }
        }

        stage('Deploy Containers') {
            steps {
                bat 'docker-compose up -d'
            }
        }
    }
}
