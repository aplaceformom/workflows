# Re-Usable Workflow: Docker Build
## inputs
#### name
- *description*: Docker image name in owner/app format. Defaults to github.event.repository.name
- *required*: False
- *type*: string
#### deployment-role
- *description*: AWS IAM Role to assume when deploying to ECR.
- *required*: False
- *default*: 
- *type*: string
#### aws-region
- *description*: AWS Region to deploy to.
- *required*: False
- *default*: us-west-2
- *type*: string
#### ecr-repo
- *description*: AWS ECR Repo to push to.
- *required*: False
- *default*: 
- *type*: string
#### tag-suffix
- *description*: Append the tag-suffix to the image tag.
- *type*: string
#### push
- *description*: Enable to push built image to GHCR/ECR
- *type*: boolean
- *default*: False
## secrets
#### build-args
- *description*: Pass arbitrary build_args into the docker-build process. This can be used to pass secrets tokens. WARNING: These tokens will become part of the docker image.
#### token
- *description*: Auth token to use, default to github.token
- *required*: False
## outputs
#### ecr-repo
- *description*: Elastic Container Registry URI
- *value*: ${{ jobs.build.login-ecr.outputs.registry }}
#### ghcr-repo
- *description*: GitHub Container Registry URI
- *value*: ${{ jobs.build.login-ghcr.outputs.registry }}