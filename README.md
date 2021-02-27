# Project2

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
