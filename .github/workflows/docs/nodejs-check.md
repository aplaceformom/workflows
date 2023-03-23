# Re-Usable Workflow: Run a Node.js command (deprecated)
## inputs
#### environment
Target environment


- *default*: __dev__
- *type*: __string__
#### install-command
Command to use to perform a Npm/Yarn/etc install. Default: npm install --production=false


- *default*: __npm ci --production=false__
- *type*: __string__
#### node-version
Node.js version to use. Default: auto-detected


- *type*: __string__
#### run
Which checks to run. E.g. checks


- *required*: __True__
- *type*: __string__