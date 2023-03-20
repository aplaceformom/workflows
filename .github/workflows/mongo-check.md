# Re-Usable Workflow: Perform MongoDB Checks
## inputs
#### action
- *description*: NPM action to run
- *required*: True
- *type*: string
#### commit
- *default*: ${{ github.event.pull_request.head.sha }}
- *description*: Git commit to checkout
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
- *description*: The NODE_ENV we are targetting
- *type*: string
#### node-version
- *description*: Node.js version to use. Default: auto-detected
- *required*: False
- *type*: string
#### repo
- *default*: ${{ github.repository }}
- *description*: Git repository to pull from
- *type*: string