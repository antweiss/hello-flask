pipeline {
    agent {node {label 'builder'}}

    stages {
        stage('checking out the code') {
            steps {
                checkout scm
            }
        }
        
        stage('build') {
            steps {
                sh '''
                python add-build-num.py  ${BUILD_NUMBER}
                '''
            }
        }
        
        stage ('archiving the artifacts') {
            steps {
                sh '''
                tar zcvf hello-${BUILD_NUMBER}.tar.gz application.py requirements.txt  
                '''
            }
        }
    }        
    post {
        success {
            archiveArtifacts artifacts: '*.tar.gz'
            }
        }
}
