# Re-Usable Workflow: Docker Build
## inputs
#### aws-region
- *default*: us-west-2
- *description*: AWS Region to deploy to.
- *required*: False
- *type*: string
#### deployment-role
- *default*: 
- *description*: AWS IAM Role to assume when deploying to ECR.
- *required*: False
- *type*: string
#### ecr-repo
- *default*: 
- *description*: AWS ECR Repo to push to.
- *required*: False
- *type*: string
#### name
- *description*: Docker image name in owner/app format. Defaults to github.event.repository.name
- *required*: False
- *type*: string
#### push
- *default*: False
- *description*: Enable to push built image to GHCR/ECR
- *type*: boolean
#### tag-suffix
- *description*: Append the tag-suffix to the image tag.
- *type*: string
## outputs
#### ecr-repo
- *description*: Elastic Container Registry URI
- *value*: ${{ jobs.build.login-ecr.outputs.registry }}
#### ghcr-repo
- *description*: GitHub Container Registry URI
- *value*: ${{ jobs.build.login-ghcr.outputs.registry }}
## secrets
#### build-args
- *description*: Pass arbitrary build_args into the docker-build process. This can be used to pass secrets tokens. WARNING: These tokens will become part of the docker image.
#### token
- *description*: Auth token to use, default to github.token
- *required*: False