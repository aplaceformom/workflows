# Re-Usable Workflow: Perform MongoDB Checks
## inputs
#### action
NPM action to run


- *required*: __True__
- *type*: __string__
#### commit
Git commit to checkout


- *default*: __${{ github.event.pull_request.head.sha }}__
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
The NODE_ENV we are targetting


- *default*: __development__
- *type*: __string__
#### node-version
Node.js version to use. Default: auto-detected


- *type*: __string__
#### repo
Git repository to pull from


- *default*: __${{ github.repository }}__
- *type*: __string__