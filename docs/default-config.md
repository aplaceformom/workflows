# (.github/workflows/default-config.yaml) Default Config Settings

## Example

```yaml
name: ExampleService-DEV
on:
  push:
    branches: [main]
jobs:
  build:
    uses: aplaceformom/workflows/.github/workflows/.github/workflows/default-config.yaml@main
```

## inputs

### application-role

- **description**: Override the default application role.
- **type**: string
- **default**: False
- **required**: False

### aws-region

- **description**: AWS Region to deploy into.
- **type**: string
- **default**: us-west-2
- **required**: False

### ecr-repo

- **description**: The URI to the ECR repo to use
- **type**: string
- **default**: False
- **required**: False

### env

- **description**: Target environment for deploying into
- **type**: string
- **default**: dev
- **required**: False

### deployment-role

- **description**: Override the default deployment role.
- **type**: string
- **default**: False
- **required**: False

### project

- **description**: Override the default project name.
- **type**: string
- **default**: False
- **required**: False

### ecr-root

- **description**: Use the root ACR repository
- **type**: boolean
- **default**: True
- **required**: False

## secrets
