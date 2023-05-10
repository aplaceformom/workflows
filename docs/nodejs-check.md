# (.github/workflows/nodejs-check.yaml) Run a Node.js command (deprecated)

## Example

```yaml
name: ExampleService-DEV
on:
  push:
    branches: [main]
jobs:
  build:
    uses: aplaceformom/workflows/.github/workflows/.github/workflows/nodejs-check.yaml@main
    with:
      run: "Which checks to run. E.g. checks"
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

### run

- **description**: Which checks to run. E.g. checks
- **type**: string
- **default**: False
- **required**: True

## secrets
