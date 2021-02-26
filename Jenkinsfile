pipeline {
    agent any
    environment {
            app_version = 'v1'
            rollback = 'false'
    }
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
            stage('Build Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            image = docker.build("mrbilalshafiq/frontend:${app_version}")
                        }
                    }
                }
            }
        }
}
