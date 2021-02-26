pipeline{
        agent any
        environment {
            app_version = 'v1'
            rollback = 'false'
        }
        stages{
                        stage('Build Image & Tag'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            sh "docker-compose build --parallel --build-arg APP_VERSION=${app_version}"
                            
                        }
                    }
                }
            }
            stage('Push'){
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
            stage("configuration management ansible"){
                steps{
                    script{
                        sh "cd ansible && ansible-playbook -i inventory.yaml playbook.yaml"
                    }
                }
            }
            stage('Deploy App'){
                steps{
                    sh "docker-compose pull && docker-compose up -d"
                }
            }
        }
}
