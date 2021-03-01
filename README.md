# DevOps-Project-2
> Building on the skills used in Project 1 by implementing a CI/CD pipeline using Jenkins, Ansible, Docker & Github.

As part of the second project, we were required to create a service-orientated architecture for my application, which must be composed of at least 4 services that work together. 

### Service 1
The core service – this will render the Jinja2 templates you need to interact with your application, it will also be responsible for communicating with the other 3 services, and finally for persisting some data in an SQL database.

### Service 2 
This service generates a 3 random letters to form part of the account number

### Service 3
This service generates a 7 digit number to form part of the account number.

### Service 4
This service combines the objects from service 2 and service 3 to produce an account number, which then is given a prize based on logic to determine if the account number should be given a small prize or a big prize.

## Scope

The requirements of the project are as follows:

 - An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project: For this I used a trello board to track the progress and status of development & deployment stages and to also track any issues and problems.
 - An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine: For this I used GitHub which sent the code to Jenkins to be built and deployed on Google Cloud Platform virtual machines.
 - If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application.
 - The project must follow the Service-oriented architecture that has been asked for.
 - The project must be deployed using containerisation and an orchestration tool: For this I used Docker, Docker-Compose & Docker Swarm.
 - As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
 - The project must make use of a reverse proxy to make your application accessible to the user: For this I used NGINX.

## Constraints

 - Kanban Board: Trello
 - Version Control: Git
 - CI Server: Jenkins
 - Configuration Management: Ansible
 - Cloud server: GCP virtual machines
 - Containerisation: Docker
 - Orchestration Tool: Docker Swarm
 - Reverse Proxy: NGINX
 
 ## Finished Kanban Board
 ![kanban](https://github.com/mrbilalshafiq/Project2/blob/main/images/KANBAN.jpg)
 
 ## Architecture
 ![Architecture](https://github.com/mrbilalshafiq/Project2/blob/main/images/Architecture.jpeg)
 
 ## CI/CD
 ![DevOps](https://github.com/mrbilalshafiq/Project2/blob/main/images/DevOps%20Lifecycle.jpeg)
 
 ## Jenkins Pipeline Stages
 ![Jenkins](https://github.com/mrbilalshafiq/Project2/blob/main/images/JenkinsPipelineStages.jpg)
 
 ## Database
 ![mysql](https://github.com/mrbilalshafiq/Project2/blob/main/images/database-table.jpeg)
 
 ## Testing: 83.5%
 ![Testing](https://github.com/mrbilalshafiq/Project2/blob/main/images/Testing.jpg)
 
 ## Building Image, Tagging & Finally Pushing Using Docker Compose
 ![BuildPushTag](https://github.com/mrbilalshafiq/Project2/blob/main/images/buildtagpush.jpg)
 
 ## Using Ansible For Configuration Management
 ![Ansible](https://github.com/mrbilalshafiq/Project2/blob/main/images/AnsibleConfiguration.jpg)
  
 # Deploying The Application Using Docker Swarm Stack
 ![DeployStack](https://github.com/mrbilalshafiq/Project2/blob/main/images/deployswarmstack.jpg)
 
 ## Using Reverse Proxy On Manager Node & Worker Node To Remove The Need To Specify A Port Number
 ![Reverseproxy](https://github.com/mrbilalshafiq/Project2/blob/main/images/reverseproxy.jpg)
 
 ## Scaling Micro-Services By Editing docker-compose.yaml
 ![Scalability](https://github.com/mrbilalshafiq/Project2/blob/main/images/scalability.jpg)
 
 ## Performing Rolling Update Using GitHub Webhook To Deploy On Jenkins With No Downtime
 ![RollingUpdate](https://github.com/mrbilalshafiq/Project2/blob/main/images/rollingupdate.jpg)
 
 ## Risk Assessment
 ![RiskAssessment](https://github.com/mrbilalshafiq/DevOps-Project-2/blob/main/images/Risk%20Assessment.jpg)
 
 ## Analysis
 During this project, I prioritised according to the objectives. All the constraints and  the scope was fully met with my web-application, aiming for a minimum viable product. Like the DevOps way of working, my work was not isolated to a portion of the pipeline and instead I was responsible for the whole pipeline from end-to-end. Being in control of the operational functions bring alot of advantages, mainly the assurance that the code isn't faulty due to the testing and configuration that happens within Jenkins. Having an automated system for running tasks means that the tasks are less tedious and time consuming, allowing me to be more efficient and productive with my time.
 
 As well as doing continuous integration and continious delivery, this project facilitated contiuous learning of the DevOps tools and practices. I was able to share what I've learnt and where I went wrong with the rest of the team, openly discussing failures in order to share my learning. The project also helped me identify which skills I needed to improve and, even better, helped me improve those very same skills. I was able to learn from the first project by examining how I complete my work and how effectively I complete it. This has helped give me a baseline of how much time it takes to complete parts of the project which allows me to manage my time better.
 
 I completed this project within 7 days and this was achieved by working in an iterative format, slowly building my application layer-by-layer. Everytime I discovered a defect I would stop development and prioritise its repair. Having automated testing prior to automated production deployment allows us to correct any issues before releasing to the public. The configuration of systems is automated allowing for minimal error once the 'infrastructure as code' is complete and correct. During my work on this application I followed agile development practices, regularly examining the constraints in the project. I maintained a backlog of tasks on my kanban board, and for this I used Trello. 
 
 In conclusion, I know that I still have alot more to learn however, I am proud of what I have accomplished thus far, as stated in the message for myself at the end of my Jenkinsfile.
