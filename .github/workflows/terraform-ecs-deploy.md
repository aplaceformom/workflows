# Re-Usable Workflow: Terraform ECS Deploy
## inputs
#### autoscaling
- *description*: Enable/disable autoscaling
- *type*: boolean
- *default*: False
#### autoscaling_min
- *description*: Minimum number of nodes to keep running when autoscaling enabled.
- *default*: 1
#### autoscaling_max
- *description*: Maximum number of nodes to scale-out to when autoscaling is enabled.
- *default*: 3
#### email
- *description*: Email address of code owners/team.
- *type*: string
- *required*: True
#### environ
- *description*: A string describing the application environ in `{ key1="/ssm/path/to/value1", key2="/ssm/path/to/value2" }` format.
- *type*: string
- *required*: False
#### certificate
- *description*: The name of an existing AWS ACM certificate to use. This cert must already exist.
- *type*: string
- *required*: False
#### certificate_alt_names
- *description*: A comma separated list of subjective alternative names to add to the SSL certificate. Ignored if `certificate` is specific.
- *type*: string
- *required*: False
#### cpu
- *description*: Allocated per-container CPU time quanta in AWS vCPU units.
- *type*: number
- *default*: 256
#### mem
- *description*: Allocated per-container memory size for the target application.
- *type*: number
- *default*: 512
#### owner
- *description*: Team owning project.
- *type*: string
- *required*: True
#### public
- *description*: Enable to place the application container into a publicly accessible network.
- *type*: boolean
- *default*: False
#### stage
- *description*: CI/CD promotion stage. E.g. dev, qa, prod
- *type*: string
- *default*: dev
#### task-name
- *description*: Name of the ECS task. Defaults to using th repository name.
- *type*: string
- *requird*: False
#### destroy
- *description*: Destroy the existing stack before deployment.
- *type*: boolean
- *default*: False
#### debug
- *description*: Enable/disable build action debugging.
- *type*: boolean
- *default*: False
## secrets
#### token
- *description*: Auth token to use, default to github.token
- *required*: False