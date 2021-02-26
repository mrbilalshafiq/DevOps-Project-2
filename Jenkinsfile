pipeline{
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
            stage('Build Image & Tag'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            sh "sudo docker-compose build --parallel --build-arg APP_VERSION=${app_version}"
                            
                        }
                    }
                }
            }
            stage('Push'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            docker.withRegistry('', 'docker-hub-credentials'){
                                sh "sudo docker-compose push"
                                sh "sudo docker system prune -af"
                            }
                            
                        }
                    }
                }
            }
            stage("configuration management ansible"){
                steps{
                    script{
                        sh "cd ansible && ansible-playbook -i inventory.yaml playbook.yaml"
                    }
                }
            }
        }
}
 
