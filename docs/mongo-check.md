# (.github/workflows/mongo-check.yaml) Perform MongoDB Checks

## Example

```yaml
name: ExampleService-DEV
on:
  push:
    branches: [main]
jobs:
  build:
    uses: aplaceformom/workflows/.github/workflows/.github/workflows/mongo-check.yaml@main
    with:
      action: "NPM action to run"
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

- **description**: The NODE_ENV we are targetting
- **type**: string
- **default**: development
- **required**: False

### action

- **description**: NPM action to run
- **type**: string
- **default**: False
- **required**: True

### repo

- **description**: Git repository to pull from
- **type**: string
- **default**: ${{ github.repository }}
- **required**: False

### commit

- **description**: Git commit to checkout
- **type**: string
- **default**: ${{ github.event.pull_request.head.sha }}
- **required**: False

## secrets
