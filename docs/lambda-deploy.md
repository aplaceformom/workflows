# (.github/workflows/lambda-deploy.yaml) Deploy Lambda

## Example

```yaml
name: ExampleService-DEV
on:
  push:
    branches: [main]
jobs:
  build:
    uses: aplaceformom/workflows/.github/workflows/.github/workflows/lambda-deploy.yaml@main
    with:
      function-name: "Name of the Lambda Function"
      description: "Description of Lambda"
      runtime: "The Lambda's runtime. E.g. python3.8, nodejs14.x, go1.x, dotnetcore3.1, etc"
```

## inputs

### artifact

- **description**: The name of the lambda artifact to upload.
- **type**: string
- **default**: lambda
- **required**: False

### function-name

- **description**: Name of the Lambda Function
- **type**: string
- **default**: False
- **required**: True

### function-role

- **description**: Name of AWS IAM role the lambda should execute as.
- **type**: string
- **default**: lambda_basic_execution
- **required**: False

### description

- **description**: Description of Lambda
- **type**: string
- **default**: False
- **required**: True

### env

- **description**: Target environment. E.g. dev, qa. prod
- **type**: string
- **default**: dev
- **required**: False

### handler

- **description**: Lambda file.entrypoint
- **type**: string
- **default**: index.handler
- **required**: False

### runtime

- **description**: The Lambda's runtime. E.g. python3.8, nodejs14.x, go1.x, dotnetcore3.1, etc
- **type**: string
- **default**: False
- **required**: True

### timeout

- **description**: The amount of time (in seconds) that Lambda allows a function to run before stopping it. The default is 3 seconds.  The  maximum  allowed value is 900 seconds. For more information, see Lambda execution en- vironment .
- **type**: number
- **default**: 3
- **required**: False

### memory

- **description**: The amount of memory available to the function at runtime.  Increasing  the  function memory also increases its CPU allocation. The default value is 128 MB. The value can be any multiple of 1 MB.
- **type**: number
- **default**: 128
- **required**: False

### publish

- **description**: Set to true to publish the first version of the function during creation/update.
- **type**: boolean
- **default**: False
- **required**: False

### subnets

- **description**: Attach lambda to one of these subnets. NOTE This is a comma delimited string
- **type**: string
- **default**: False
- **required**: False

### security-groups

- **description**: List security-groups to attach to the Lambda when launching on a VPC, as a comma delimited string.
- **type**: string
- **default**: False
- **required**: False

### deployment-role

- **description**: AWS IAM Role to assume when deploying the lambda
- **type**: string
- **default**: False
- **required**: False

### aws-region

- **description**: AWS Region to deploy the Lambda to.
- **type**: string
- **default**: us-west-2
- **required**: False

## secrets

### token

- **description**: Auth token to use, default to github.token
- **type**: False
- **default**: False
- **required**: False
