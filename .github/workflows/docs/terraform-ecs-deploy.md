# Re-Usable Workflow: Terraform ECS Deploy
## inputs
#### autoscaling
Enable/disable autoscaling


- *type*: __boolean__
#### autoscaling_max
Maximum number of nodes to scale-out to when autoscaling is enabled.


- *default*: __3__
- *type*: __number__
#### autoscaling_min
Minimum number of nodes to keep running when autoscaling enabled.


- *default*: __1__
- *type*: __number__
#### certificate
The name of an existing AWS ACM certificate to use. This cert must already exist.


- *type*: __string__
#### certificate_alt_names
A comma separated list of subjective alternative names to add to the SSL certificate. Ignored if `certificate` is specific.


- *type*: __string__
#### cpu
Allocated per-container CPU time quanta in AWS vCPU units.


- *default*: __256__
- *type*: __number__
#### debug
Enable/disable build action debugging.


- *type*: __boolean__
#### destroy
Destroy the existing stack before deployment.


- *type*: __boolean__
#### email
Email address of code owners/team.


- *required*: __True__
- *type*: __string__
#### environ
A string describing the application environ in `{ key1="/ssm/path/to/value1", key2="/ssm/path/to/value2" }` format.


- *type*: __string__
#### mem
Allocated per-container memory size for the target application.


- *default*: __512__
- *type*: __number__
#### owner
Team owning project.


- *required*: __True__
- *type*: __string__
#### public
Enable to place the application container into a publicly accessible network.


- *type*: __boolean__
#### stage
CI/CD promotion stage. E.g. dev, qa, prod


- *default*: __dev__
- *type*: __string__
#### task-name
Name of the ECS task. Defaults to using th repository name.


- *type*: __string__
## secrets
#### token
Auth token to use, default to github.token

