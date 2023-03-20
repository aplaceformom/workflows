#!/usr/bin/env python

# Stdlib imports
import os
import sys

# 3rd party imports
import yaml


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        for arg in sys.argv[1:]:
            sys.stdout.write(f"Processing {arg} ... ")
            sys.stdout.flush()
            if os.path.isfile(arg):
                name = f'{arg.split(".y")[0]}.md'
                lines = []
                data = {}
                with open(arg, "r") as fp:
                    data = yaml.safe_load(fp.read())
                if "name" not in data.keys():
                    raise Exception(
                        "No name element in this workflow. If indeed, that is what it is."
                    )
                lines.append(f"# Re-Usable Workflow: {data['name']}")
                top = None
                if "on" not in data.keys() and True in data.keys():
                    top = True
                elif "on" in data.keys() and True not in data.keys():
                    top = "on"
                else:
                    raise Exception("`on` section is not present.")
                if "workflow_call" not in data[top].keys():
                    raise Exception("`on->workflow_call` section is not present.")
                for itm_t in data[top]["workflow_call"].keys():
                    lines.append(f"## {itm_t}")
                    for itm in data[top]["workflow_call"][itm_t].keys():
                        lines.append(f"#### {itm}")
                        for k, v in data[top]["workflow_call"][itm_t][itm].items():
                            lines.append(f"- *{k}*: {v}")
                with open(name, "w+") as fp:
                    fp.write("\n".join(lines))
            print("ok")
