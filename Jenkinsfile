pipeline {
    agent any
    stages{
        stage('testing'){
            steps{
                sh '''
                cd 1-frontend
                pip3 install -r requirements.txt
                python3 -m pytest --cov=app --cov-report=term-missing
                cd ..
                cd 2-chargen
                pip3 install -r requirements.txt
                python3 -m pytest --cov=app --cov-report=term-missing
                cd ..
                cd 3-numgen
                pip3 install -r requirements.txt
                python3 -m pytest --cov=app --cov-report=term-missing
                cd ..
                cd 4-prizegen
                pip3 install -r requirements.txt
                python3 -m pytest --cov=app --cov-report=term-missing
                cd ..
                    '''
                }
            }

        stage('Build') {
            steps {
                sh "docker-compose build"
            }
        }
        stage('Push') {
            steps {
                sh "docker-compose push"
            }
        }
        stage("configuration management ansible"){
                steps{
                    script{
                        sh "cd ansible && ansible-playbook -i inventory.yaml playbook.yaml"
                }
            }
        }
        stage('Deploy') {
            steps {
                sh "docker-compose pull && docker stack deploy --compose-file docker-compose.yaml prizegen"
            }
        }
    }
}
