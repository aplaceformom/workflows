# Re-Usable Workflow: Perform Apollo Schema Check
## inputs
#### action
NPM action to run


- *required*: __True__
- *type*: __string__
#### environment
Target environment


- *default*: __dev__
- *type*: __string__
#### install-command
Command to use to perform a Npm/Yarn/etc install. Default: npm install --production=false


- *default*: __npm ci --production=false__
- *type*: __string__
#### node-env
The NODE_ENV we are targetting. Default: development


- *default*: __development__
- *type*: __string__
#### node-version
Node.js version to use. Default: auto-detected


- *type*: __string__
#### schema-file
Path to schema file


- *required*: __True__
- *type*: __string__
#### service-name
Name of the service


- *required*: __True__
- *type*: __string__
#### service-url
URL to service GraphQL endpoint


- *required*: __True__
- *type*: __string__
## secrets
#### apollo-key
The Apollo Key


- *required*: __True__