# Re-Usable Workflow: Deploy Lambda
## inputs
#### artifact
- *description*: The name of the lambda artifact to upload.
#### function-name
- *description*: Name of the Lambda Function
- *type*: string
- *required*: True
#### function-role
- *description*: Name of AWS IAM role the lambda should executre as.
- *type*: string
- *required*: True
#### description
- *description*: Description of Lambda
- *type*: string
- *required*: True
#### runtime
- *description*: The Lambda's runtime. E.g. python3.8, nodejs14.x, go1.x, dotnetcore3.1, etc
- *type*: string
- *required*: True
#### timeout
- *description*: The amount of time (in seconds) that Lambda allows a function to run before stopping it. The default is 3 seconds.  The  maximum  allowed value is 900 seconds. For more information, see Lambda execution en- vironment .
- *type*: number
- *default*: 3
#### memory
- *description*: The amount of memory available to the function at runtime.  Increasing  the  function memory also increases its CPU allocation. The default value is 128 MB. The value can be any multiple of 1 MB.
- *type*: number
- *default*: 128
#### publish
- *description*: Set to true to publish the first version of the function during creation/update.
- *type*: boolean
- *default*: False
#### subnets
- *description*: Attach lambda to one of these subnets. NOTE This is not usually required.
- *type*: string
- *required*: False
#### security-groups
- *description*: List security-groups to attach to the Lambda when launching on a VPC.
- *type*: string
- *required*: False
#### deployment-role
- *description*: AWS IAM Role to assume when deploying the lambda
- *type*: string
- *required*: True
#### aws-region
- *description*: AWS Region to deploy the Lambda to.
- *type*: string
- *default*: us-west-2
## secrets
#### token
- *description*: Auth token to use, default to github.token
- *required*: False