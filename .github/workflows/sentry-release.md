# Re-Usable Workflow: Sentry Release
## inputs
#### environment
- *default*: dev
- *description*: Deployment environment
- *type*: string
#### sourcemaps
- *description*: Sentry sourcemaps to upload.
- *required*: True
- *type*: string
## secrets
#### token
- *descriptions*: Sentry Auth Token
- *required*: True