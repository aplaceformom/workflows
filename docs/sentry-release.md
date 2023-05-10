# (.github/workflows/sentry-release.yaml) Sentry Release

## Example

```yaml
name: ExampleService-DEV
on:
  push:
    branches: [main]
jobs:
  build:
    uses: aplaceformom/workflows/.github/workflows/.github/workflows/sentry-release.yaml@main
    with:
      sourcemaps: "Sentry sourcemaps to upload."
```

## inputs

### environment

- **description**: Deployment environment
- **type**: string
- **default**: dev
- **required**: False

### sourcemaps

- **description**: Sentry sourcemaps to upload.
- **type**: string
- **default**: False
- **required**: True

## secrets

### token

- **description**: Sentry Auth Token
- **type**: False
- **default**: False
- **required**: True
