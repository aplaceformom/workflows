# Re-Usable Workflow: Perform Apollo Schema Check
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
#### action
- *description*: NPM action to run
- *type*: string
- *required*: True
#### schema-file
- *description*: Path to schema file
- *type*: string
- *required*: True
#### service-name
- *description*: Name of the service
- *type*: string
- *required*: True
#### service-url
- *description*: URL to service GraphQL endpoint
- *type*: string
- *required*: True
## secrets
#### apollo-key
- *description*: The Apollo Key
- *required*: True