pipeline {
    agent any
    environment {
            app_version = 'v1'
            rollback = 'false'
    }
    stages{
        stage('Testing All 4 Services'){
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
            stage('Build & Tag'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            sh "docker-compose build --parallel --build-arg ${app_version}"

                        }
                    }
                }
            }
            stage('Push Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            docker.withRegistry('', 'docker-hub-credentials'){
                                sh "docker-compose push"
                                sh "docker system prune -af"
                            }
                            
                        }
                    }
                }
            }
            stage("Configuration Management via Ansible"){
                steps{
                    script{
                        sh "cd ansible && ansible-playbook -i inventory.yaml playbook.yaml"
                    }
                }
            }
            stage('Deploy Swarm Stack'){
                steps{
                    sh '''
                    ssh -oStrictHostKeyChecking=no dontchangethisemailplease@34.105.204.33 << EOF
                        rm -rf Project2
                        git clone https://github.com/mrbilalshafiq/Project2.git && cd Project2
                        export app_version=${app_version}
                        docker stack deploy --compose-file docker-compose.yaml flaskapp
                        echo "Well done Bilal, you should be proud of yourself."
                    '''
                }
            }
        }
}
