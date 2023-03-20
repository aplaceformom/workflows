# Re-Usable Workflow: ECS Deploy
## inputs
#### aws-region
- *description*: AWS Region to deploy in
- *required*: True
- *type*: string
#### container-name
- *description*: The name of the container defined in the containerDefinitions section of the ECS task definition
- *required*: True
- *type*: string
#### environment-variables
- *description*: Variables to add to the container. Each variable is of the form KEY=value, you can specify multiple variables with multi-line YAML strings.
- *required*: False
- *type*: string
#### image
- *description*: The URI of the container image to insert into the ECS task definition
- *required*: True
- *type*: string
#### task-definition
- *description*: The path to the ECS task definition JSON file
- *required*: True
- *type*: string
## secrets
#### token
- *description*: Auth token to use, default to github.token
- *required*: False