# A Place For Mom Workflow Integrations

## ssm2ecs.py

##### Synopsis

This script takes an `application name` and looks up the SSM configs for said
application. It then builds the `environment` and `secrets` portion of the ECS
Task Definition, and dumps that (along with the rest of the TaskDef empty) out
to JSON. The resulting JSON is dumped to STDOUT directly. There are no other
supported arguments.

##### Help / Options

```
usage: ssm2ecs.py [-h] -A APPNAME

ECS environment and secret configuration generator.

options:
  -h, --help            show this help message and exit
  -A APPNAME, --appName APPNAME
                        Specify the name of the service
```

##### Example

```
./ssm2ecs.py -A community-finance-charges-rest-api > fromLocation.json
```

## grwrg.py (Github Re-usable Workflow Readme Generator)

This simply takes a list of YAML files, which will render a MarkDown formatted
file of the same name (but with a `.md` extension) if they are valid re-usable
workflows and have inputs, outputs, or secrets defined. There are, however,
several requirements, which this tool will signal non-compliance of, via exit
codes. They are as follows:

0. Success
1. File not found
2. Option is not required, but has no default
3. Option is required, and has a default
4. Option has no description
5. Option has no specified type

##### Example

```
.github/scripts/grwrg.py .github/workflows/github-event.yaml .github/workflows/docker-build.yaml
```
