# (.github/workflows/apollo-check.yaml) Perform Apollo Schema Check

## Example

```yaml
name: ExampleService-DEV
on:
  push:
    branches: [main]
jobs:
  build:
    uses: aplaceformom/workflows/.github/workflows/.github/workflows/apollo-check.yaml@main
    with:
      action: "NPM action to run"
      schema-file: "Path to schema file"
      service-name: "Name of the service"
      service-url: "URL to service GraphQL endpoint"
```

## inputs

### environment

- **description**: Target environment
- **type**: string
- **default**: dev
- **required**: False

### install-command

- **description**: Command to use to perform a Npm/Yarn/etc install. Default: npm install --production=false
- **type**: string
- **default**: npm ci --production=false
- **required**: False

### node-version

- **description**: Node.js version to use. Default: auto-detected
- **type**: string
- **default**: False
- **required**: False

### node-env

- **description**: The NODE_ENV we are targeting. Default: development
- **type**: string
- **default**: development
- **required**: False

### action

- **description**: NPM action to run
- **type**: string
- **default**: False
- **required**: True

### schema-file

- **description**: Path to schema file
- **type**: string
- **default**: False
- **required**: True

### service-name

- **description**: Name of the service
- **type**: string
- **default**: False
- **required**: True

### service-url

- **description**: URL to service GraphQL endpoint
- **type**: string
- **default**: False
- **required**: True

## secrets

### apollo-key

- **description**: The Apollo Key
- **type**: False
- **default**: False
- **required**: True
