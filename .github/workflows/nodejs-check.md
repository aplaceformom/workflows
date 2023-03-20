# Re-Usable Workflow: Run a Node.js command (deprecated)
## inputs
#### environment
- *default*: dev
- *description*: Target environment
- *type*: string
#### install-command
- *default*: npm ci --production=false
- *description*: Command to use to perform a Npm/Yarn/etc install. Default: npm install --production=false
- *type*: string
#### node-version
- *description*: Node.js version to use. Default: auto-detected
- *required*: False
- *type*: string
#### run
- *description*: Which checks to run. E.g. checks
- *required*: True
- *type*: string