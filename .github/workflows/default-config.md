# Re-Usable Workflow: Default Config Settings
## inputs
#### application-role
- *description*: Override the default application role.
- *type*: string
- *required*: False
#### aws-region
- *description*: AWS Region to deploy into.
- *type*: string
- *default*: us-west-2
#### ecr-repo
- *description*: The URI to the ECR repo to use
- *type*: string
- *required*: False
#### env
- *description*: Target environment for deploying into
- *type*: string
- *default*: dev
#### deployment-role
- *description*: Override the default deployment role.
- *type*: string
- *required*: False
#### project
- *description*: Override the default project name.
- *type*: string
- *required*: False
## outputs
#### aws-region
- *description*: The region to deploy into.
- *value*: ${{ inputs.aws-region }}
#### short-rev
- *description*: The Git short rev of the sha that triggered the event.
- *value*: ${{ jobs.config.outputs.short-rev }}
#### account-id
- *description*: The account-id cooresponding to the target environment.
- *value*: ${{ jobs.config.outputs.account-id }}
#### ecr-repo
- *description*: The URI to the ECR repo to use
- *value*: ${{ jobs.config.outputs.repo }}
#### project
- *description*: The project name.
- *value*: ${{ jobs.config.outputs.project }}
#### application-role
- *description*: The role to attach to the application.
- *value*: ${{ jobs.config.outputs.application-role }}
#### deployment-role
- *description*: The role to use when deploying from this repo.
- *value*: ${{ jobs.config.outputs.deployment-role }}