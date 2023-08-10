# (.github/workflows/docker-build.yaml) Docker Build

## Example

```yaml
name: ExampleService-DEV
on:
  push:
    branches: [main]
jobs:
  build:
    uses: aplaceformom/workflows/.github/workflows/.github/workflows/docker-build.yaml@main
```

## inputs

### submodules

- **description**: Perform submodule checkouts as well.
- **type**: boolean
- **default**: False
- **required**: False

### deployment-role

- **description**: AWS IAM Role to assume when deploying to ECR.
- **type**: string
- **default**: NONE
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

### dockerfile

- **description**: Path and filename for Dockerfile to use. Defaults to `./Dockerfile`
- **type**: string
- **default**: ./Dockerfile
- **required**: False

### env

- **description**: Target environment for deploying into
- **type**: string
- **default**: dev
- **required**: False

### stamp

- **description**: Stamp the build with a consumable file (Default: ${ github.sha })
- **type**: string
- **default**: ${{ github.sha }}
- **required**: False

### stamp_file

- **description**: Specify the build stamp filename (Default: build.stamp)
- **type**: string
- **default**: build.stamp
- **required**: False

### ecr-repo

- **description**: AWS ECR Repo to push to.
- **type**: string
- **default**: NONE
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

### driver-opts

- **description**: Driver-opts to pass to buildx.
- **type**: string
- **default**: False
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

### platform

- **description**: <os-version> to process the build on. E.g. ubuntu-latest
- **type**: string
- **default**: ubuntu-latest
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
