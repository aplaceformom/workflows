# Re-Usable Workflow: Default Config Settings
## inputs
#### application-role
- *description*: Override the default application role.
- *required*: False
- *type*: string
#### aws-region
- *default*: us-west-2
- *description*: AWS Region to deploy into.
- *type*: string
#### deployment-role
- *description*: Override the default deployment role.
- *required*: False
- *type*: string
#### ecr-repo
- *description*: The URI to the ECR repo to use
- *required*: False
- *type*: string
#### env
- *default*: dev
- *description*: Target environment for deploying into
- *type*: string
#### project
- *description*: Override the default project name.
- *required*: False
- *type*: string
## outputs
#### account-id
- *description*: The account-id cooresponding to the target environment.
- *value*: ${{ jobs.config.outputs.account-id }}
#### application-role
- *description*: The role to attach to the application.
- *value*: ${{ jobs.config.outputs.application-role }}
#### aws-region
- *description*: The region to deploy into.
- *value*: ${{ inputs.aws-region }}
#### deployment-role
- *description*: The role to use when deploying from this repo.
- *value*: ${{ jobs.config.outputs.deployment-role }}
#### ecr-repo
- *description*: The URI to the ECR repo to use
- *value*: ${{ jobs.config.outputs.repo }}
#### project
- *description*: The project name.
- *value*: ${{ jobs.config.outputs.project }}
#### short-rev
- *description*: The Git short rev of the sha that triggered the event.
- *value*: ${{ jobs.config.outputs.short-rev }}