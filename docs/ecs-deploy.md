# (.github/workflows/ecs-deploy.yaml) ECS Deploy

## Example

```yaml
name: ExampleService-DEV
on:
  push:
    branches: [main]
jobs:
  build:
    uses: aplaceformom/workflows/.github/workflows/.github/workflows/ecs-deploy.yaml@main
    with:
      task-definition: "The path to the ECS task definition JSON file"
      container-name: "The name of the container defined in the containerDefinitions section of the ECS task definition"
      image: "The URI of the container image to insert into the ECS task definition"
      aws-region: "AWS Region to deploy in"
```

## inputs

### task-definition

- **description**: The path to the ECS task definition JSON file
- **type**: string
- **default**: False
- **required**: True

### container-name

- **description**: The name of the container defined in the containerDefinitions section of the ECS task definition
- **type**: string
- **default**: False
- **required**: True

### image

- **description**: The URI of the container image to insert into the ECS task definition
- **type**: string
- **default**: False
- **required**: True

### environment-variables

- **description**: Variables to add to the container. Each variable is of the form KEY=value, you can specify multiple variables with multi-line YAML strings.
- **type**: string
- **default**: False
- **required**: False

### aws-region

- **description**: AWS Region to deploy in
- **type**: string
- **default**: False
- **required**: True

## secrets

### token

- **description**: Auth token to use, default to github.token
- **type**: False
- **default**: False
- **required**: False
