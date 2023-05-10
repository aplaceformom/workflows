# (.github/workflows/git-commit-message.yaml) git-commit-check

## Example

```yaml
name: ExampleService-DEV
on:
  push:
    branches: [main]
jobs:
  build:
    uses: aplaceformom/workflows/.github/workflows/.github/workflows/git-commit-message.yaml@main
```

## inputs

## secrets

### token

- **description**: Auth token to use, default to github.token
- **type**: False
- **default**: False
- **required**: False
