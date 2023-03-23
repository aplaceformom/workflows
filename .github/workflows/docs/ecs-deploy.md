# Re-Usable Workflow: ECS Deploy
## inputs
#### aws-region
AWS Region to deploy in


- *required*: __True__
- *type*: __string__
#### container-name
The name of the container defined in the containerDefinitions section of the ECS task definition


- *required*: __True__
- *type*: __string__
#### environment-variables
Variables to add to the container. Each variable is of the form KEY=value, you can specify multiple variables with multi-line YAML strings.


- *type*: __string__
#### image
The URI of the container image to insert into the ECS task definition


- *required*: __True__
- *type*: __string__
#### task-definition
The path to the ECS task definition JSON file


- *required*: __True__
- *type*: __string__
## secrets
#### token
Auth token to use, default to github.token

