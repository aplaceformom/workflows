# Re-Usable Workflow: Default Config Settings
## inputs
#### application-role
Override the default application role.


- *type*: __string__
#### aws-region
AWS Region to deploy into.


- *default*: __us-west-2__
- *type*: __string__
#### deployment-role
Override the default deployment role.


- *type*: __string__
#### ecr-repo
The URI to the ECR repo to use


- *type*: __string__
#### ecr-root
Use the root ACR repository


- *default*: __True__
- *type*: __boolean__
#### env
Target environment for deploying into


- *default*: __dev__
- *type*: __string__
#### project
Override the default project name.


- *type*: __string__
## outputs
#### account-id
The account-id cooresponding to the target environment.


#### application-role
The role to attach to the application.


#### aws-region
The region to deploy into.


#### deployment-role
The role to use when deploying from this repo.


#### ecr-repo
The URI to the ECR repo to use


#### project
The project name.


#### short-rev
The Git short rev of the sha that triggered the event.

