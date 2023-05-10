# (.github/workflows/docker-win-build.yaml) Docker Build (windows)

## Example

```yaml
name: ExampleService-DEV
on:
  push:
    branches: [main]
jobs:
  build:
    uses: aplaceformom/workflows/.github/workflows/.github/workflows/docker-win-build.yaml@main
```

## inputs

### deployment-role

- **description**: AWS IAM Role to assume when deploying to ECR.
- **type**: string
- **default**:
- **required**: False

### aws-region

- **description**: AWS Region to deploy to.
- **type**: string
- **default**: us-west-2
- **required**: False

### context

- **description**: Path to Dockerfile. Defaults to `.`
- **type**: string
- **default**: .
- **required**: False

### env

- **description**: Target environment for deploying into
- **type**: string
- **default**: dev
- **required**: False

### ecr-repo

- **description**: AWS ECR Repo to push to.
- **type**: string
- **default**:
- **required**: False

### ecr-root

- **description**: Use the current account ECR repo or the root account ECR repo.
- **type**: boolean
- **default**: True
- **required**: False

### deploy-tag

- **description**: Add this as an alias tag on the container, for deployments.
- **type**: string
- **default**: latest
- **required**: False

### tag-suffix

- **description**: Append the tag-suffix to the image tag.
- **type**: string
- **default**: False
- **required**: False

### push

- **description**: Enable to push built image to GHCR/ECR
- **type**: boolean
- **default**: False
- **required**: False

### windows-version

- **description**: Select which version of Windows to use.
- **type**: string
- **default**: latest
- **required**: False

## secrets

### build-args

- **description**: Pass arbitrary build_args into the docker-build process. This can be used to pass secrets tokens. WARNING: These tokens will become part of the docker image.
- **type**: False
- **default**: False
- **required**: False

### token

- **description**: Auth token to use, default to github.token
- **type**: False
- **default**: False
- **required**: False
