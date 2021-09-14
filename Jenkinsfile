pipeline{
    agent {node {label 'builder'}}
    stages{
        stage('checking out the code'){
            steps{
            git 'https://github.com/droritzz/hello-flask.git'
                      }
        stage('test'){
            steps{
                sh '''
                cat requirements.txt
                '''
            }
        }
        }
    }
}
    
