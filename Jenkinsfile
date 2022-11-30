pipeline {
    agent any

    stages {
      
        stage('clone and build') {
            agent {label "dev"}
            steps {
                git 'https://github.com/mins98/ProyectoModulo5'
                sh "docker compose build"
                sh "docker compose up -d"
            }
        }
        stage('Dev test') {
            agent {label "dev"}
            steps {
                sh "docker ps"
                sh "docker stop ejemplo-web1-1" 
                sh "docker stop ejemplo-storybook-1" 
                sh "docker rm ejemplo-web1-1" 
                sh "docker rm ejemplo-storybook-1"
            }
        }
        stage('QA') {
            agent {label "qa"}
            steps {
                git 'https://github.com/mins98/ProyectoModulo5'
                sh "docker compose up -d"
            }
        }
        stage('QA test') {
            agent {label "qa"}
            steps {
                sh "docker ps"
                sh "docker stop ejemplo-web1-1" 
                sh "docker stop ejemplo-storybook-1" 
                sh "docker rm ejemplo-web1-1" 
                sh "docker rm ejemplo-storybook-1"
            }
        }
        stage('Despliegue en PROD') {
            agent {label "prod"}
            steps {
                git 'https://github.com/mins98/ProyectoModulo5'
                sh "docker compose up -d"
            }
        }
    }
}
