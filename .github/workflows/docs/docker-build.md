# Re-Usable Workflow: Docker Build
## inputs
#### aws-region
AWS Region to deploy to.


- *default*: __us-west-2__
- *type*: __string__
#### deploy-tag
Add this as an alias tag on the container, for deployments.


- *type*: __string__
#### deployment-role
AWS IAM Role to assume when deploying to ECR.


- *type*: __string__
#### ecr-repo
AWS ECR Repo to push to.


- *type*: __string__
#### push
Enable to push built image to GHCR/ECR


- *type*: __boolean__
#### tag-suffix
Append the tag-suffix to the image tag.


- *type*: __string__
## outputs
#### ecr-repo
Elastic Container Registry URI


#### ghcr-repo
GitHub Container Registry URI


## secrets
#### build-args
Pass arbitrary build_args into the docker-build process. This can be used to pass secrets tokens. WARNING: These tokens will become part of the docker image.


#### token
Auth token to use, default to github.token

