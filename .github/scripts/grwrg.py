#!/usr/bin/env python
"""
The following exit status codes have meaning:
0 - Success
1 - File not found
2 - Not Required but no default
3 - Required and has default
4 - No description
5 - No type
"""

# Stdlib imports
import os
import sys

# 3rd party imports
import yaml


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        args = sys.argv[1:]
        args.sort()
        for arg in args:
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
                aKeys = list(data[top]["workflow_call"].keys())
                aKeys.sort()
                for itm_t in aKeys:
                    lines.append(f"## {itm_t}")
                    ktypes = list(data[top]["workflow_call"][itm_t].keys())
                    ktypes.sort()
                    for itm in ktypes:
                        lines.append(f"#### {itm}")
                        try:
                            lines.append(
                                f"{data[top]['workflow_call'][itm_t][itm]['description']}"
                            )
                            lines.append("\n")
                        except Exception:
                            print(
                                f"ERROR: {arg}: on->workflow_call->{itm_t}->{itm} has no description."
                            )
                            sys.exit(4)
                        _td = data[top]["workflow_call"][itm_t][itm]
                        # Some sanity checks
                        if _td.get("required", False) and _td.get("default", False):
                            print(
                                f"ERROR: {arg}: on->workflow_call->{itm_t}->{itm} cannot be required and have a default."
                            )
                            sys.exit(3)
                        elif (
                            _td.get("required", None) == None
                            and _td.get("default", None) == None
                        ):
                            print(
                                f"WARNING: {arg}: on->workflow_call->{itm_t}->{itm} not required and has no default."
                            )
                            # sys.exit(2) Sometimes the defaults are dynamic and not implicit
                        elif not _td.get("type", False) and itm_t == "inputs":
                            print(
                                f"ERROR: {arg}: on->workflow_call->{itm_t}->{itm} has no type."
                            )
                            sys.exit(5)
                        keys = ("required", "default", "type")
                        for k in keys:
                            _tda = data[top]["workflow_call"][itm_t][itm].get(k, False)
                            if _tda:
                                lines.append(f"- *{k}*: __{_tda}__")
                with open(name, "w+") as fp:
                    fp.write("\n".join(lines))
