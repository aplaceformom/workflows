# Re-Usable Workflow: Perform MongoDB Checks
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
- *description*: The NODE_ENV we are targetting
- *type*: string
- *default*: development
#### action
- *description*: NPM action to run
- *type*: string
- *required*: True
#### repo
- *description*: Git repository to pull from
- *type*: string
- *default*: ${{ github.repository }}
#### commit
- *description*: Git commit to checkout
- *type*: string
- *default*: ${{ github.event.pull_request.head.sha }}