# Re-Usable Workflow: Run a Node.js command
## inputs
#### environment
- *description*: Target environment
- *type*: string
- *default*: dev
#### install-command
- *description*: Command to use to perform a Npm/Yarn/etc install. Default: npm install --production=false
- *type*: string
- *default*: npm ci --production=false
#### node-version
- *description*: Node.js version to use. Default: auto-detected
- *type*: string
- *required*: False
#### node-env
- *description*: The NODE_ENV we are targetting. Default: development
- *type*: string
- *default*: development
#### run
- *description*: Which checks to run. E.g. checks
- *type*: string
- *required*: True