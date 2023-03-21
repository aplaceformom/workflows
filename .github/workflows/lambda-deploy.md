# Re-Usable Workflow: Deploy Lambda
## inputs
#### artifact
The name of the lambda artifact to upload.


#### aws-region
AWS Region to deploy the Lambda to.


- *default*: __us-west-2__
- *type*: __string__
#### deployment-role
AWS IAM Role to assume when deploying the lambda


- *required*: __True__
- *type*: __string__
#### description
Description of Lambda


- *required*: __True__
- *type*: __string__
#### function-name
Name of the Lambda Function


- *required*: __True__
- *type*: __string__
#### function-role
Name of AWS IAM role the lambda should executre as.


- *required*: __True__
- *type*: __string__
#### memory
The amount of memory available to the function at runtime.  Increasing  the  function memory also increases its CPU allocation. The default value is 128 MB. The value can be any multiple of 1 MB.


- *default*: __128__
- *type*: __number__
#### publish
Set to true to publish the first version of the function during creation/update.


- *type*: __boolean__
#### runtime
The Lambda's runtime. E.g. python3.8, nodejs14.x, go1.x, dotnetcore3.1, etc


- *required*: __True__
- *type*: __string__
#### security-groups
List security-groups to attach to the Lambda when launching on a VPC.


- *type*: __string__
#### subnets
Attach lambda to one of these subnets. NOTE This is not usually required.


- *type*: __string__
#### timeout
The amount of time (in seconds) that Lambda allows a function to run before stopping it. The default is 3 seconds.  The  maximum  allowed value is 900 seconds. For more information, see Lambda execution en- vironment .


- *default*: __3__
- *type*: __number__
## secrets
#### token
Auth token to use, default to github.token

