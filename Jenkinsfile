pipeline {
    agent any

    stages {
      
        stage('clone and build') {
            agent {label "dev"}
            steps {
                echo 'DESCARGANDO EN DEV'
                git 'https://github.com/mins98/ProyectoModulo5'
                echo 'INICIANDO CONTENEDORES EN DEV'
                sh "docker compose build"
                sh "docker compose up -d"
            }
        }
        stage('Dev test') {
            agent {label "dev"}
            steps {
                echo 'INICIANDO TESTS EN DEV'
                sh "docker ps"
                echo 'TESTS EN DEV FINALIZADOS'
                sh "docker stop \$(docker ps -aq)" 
                sh "docker rm \$(docker ps -aq)" 
            }
        }
        stage('QA') {
            agent {label "qa"}
            steps {
                git 'https://github.com/mins98/ProyectoModulo5'
                echo 'INICIANDO CONTENEDORES EN QA'
                sh "docker compose up -d"
            }
        }
        stage('QA test') {
            agent {label "qa"}
            steps {
                echo 'INICIANDO TESTS EN QA'
                sh "docker ps"
                echo 'TESTS EN QA FINALIZADOS'
                sh "docker stop \$(docker ps -aq)" 
                sh "docker rm \$(docker ps -aq)" 
            }
        }
        stage('Despliegue en PROD') {
            agent {label "prod"}
            steps {
                git 'https://github.com/mins98/ProyectoModulo5'
                echo 'INICIANDO CONTENEDORES EN PRODUCCION'
                sh "docker compose up -d"
            }
        }
    }
}
