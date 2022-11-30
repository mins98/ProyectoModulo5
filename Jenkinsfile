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
                echo 'Prueba DEV correcta'
                sh "docker stop $(docker ps -aq)" 
                sh "docker rm $(docker ps -aq)" 
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
                echo 'Prueba QA correcta'
                sh "docker stop $(docker ps -aq)" 
                sh "docker rm $(docker ps -aq)" 
            }
        }
        stage('Despliegue en PROD') {
            agent {label "prod"}
            steps {
                git 'https://github.com/mins98/ProyectoModulo5'
                sh "docker compose up -d"
                echo 'Contenedores levantados correctamente en produccion'
            }
        }
    }
}
