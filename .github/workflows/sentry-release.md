# Re-Usable Workflow: Sentry Release
## inputs
#### environment
- *type*: string
- *default*: dev
- *description*: Deployment environment
#### sourcemaps
- *type*: string
- *required*: True
- *description*: Sentry sourcemaps to upload.
## secrets
#### token
- *descriptions*: Sentry Auth Token
- *required*: True