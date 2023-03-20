# Re-Usable Workflow: Perform Apollo Schema Check
## inputs
#### action
- *description*: NPM action to run
- *required*: True
- *type*: string
#### environment
- *default*: dev
- *description*: Target environment
- *type*: string
#### install-command
- *default*: npm ci --production=false
- *description*: Command to use to perform a Npm/Yarn/etc install. Default: npm install --production=false
- *type*: string
#### node-env
- *default*: development
- *description*: The NODE_ENV we are targetting. Default: development
- *type*: string
#### node-version
- *description*: Node.js version to use. Default: auto-detected
- *required*: False
- *type*: string
#### schema-file
- *description*: Path to schema file
- *required*: True
- *type*: string
#### service-name
- *description*: Name of the service
- *required*: True
- *type*: string
#### service-url
- *description*: URL to service GraphQL endpoint
- *required*: True
- *type*: string
## secrets
#### apollo-key
- *description*: The Apollo Key
- *required*: True