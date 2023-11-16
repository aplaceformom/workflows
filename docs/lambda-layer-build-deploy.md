# (.github/workflows/lambda-layer-build-deploy.yaml) Deploy Lambda Layer

## Example

```yaml
name: ExampleService-DEV
on:
  push:
    branches: [main]
jobs:
  build:
    uses: aplaceformom/workflows/.github/workflows/.github/workflows/lambda-layer-build-deploy.yaml@main
    with:
      layer-name: "Name of Lambda Layer"
      function-name: "Name of the Lambda Function to attach layer to"
      description: "Description of Lambda Layer"
      layer-file-path: "lambda-layer/layer1"
```

## inputs

### description

- **description**: Description of Lambda
- **type**: string
- **default**: False
- **required**: True

### function-name

- **description**: Name of the Lambda Function to attach layer to
- **type**: string
- **default**: False
- **required**: True

### layer-name

- **description**: Name of the Lambda Layer
- **type**: string
- **default**: False
- **required**: True

### layer-file-path

- **description**: Relative path to the folder with content for layer
- **type**: string
- **default**: False
- **required**: True

### runtimes

- **description**: A list of compatible function runtimes. E.g. python3.8, nodejs14.x, go1.x, dotnetcore3.1, etc
- **type**: string
- **default**: nodejs18.x
- **required**: False

### deployment-role

- **description**: AWS IAM Role to assume when deploying the layer
- **type**: string
- **default**: False
- **required**: False

### env

- **description**: Target environment. E.g. dev, qa. prod
- **type**: string
- **default**: dev
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
