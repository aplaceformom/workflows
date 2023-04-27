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
import json
import argparse
from types import SimpleNamespace

# 3rd party imports
import yaml


class DocumentError(Exception):
    pass


class Document:
    _lines = []
    _filename = False
    _base = "./docs"

    def __init__(self, fn=False, base="./docs"):
        if fn and os.path.isdir(dirname(fn)):
            self._filename = fn
            self._base = base
        else:
            raise IOError

    def add_lines(self, lns=False):
        if lns and type(lns) in (list, tuple):
            for ln in lns:
                self.add_line(ln)

    def add_line(self, ln=False):
        if ln and type(ln) == str:
            self._lines.append(ln)
        else:
            raise DocumentError("Invalid data given.")

        def dump_file(self):
            pass


class Workflow:
    __raw = False
    __name = False
    __infn = False
    __outfn = False
    __outdn = "./docs"
    __top = None
    __inputs = []
    __valid = False
    __data = {"inputs": [], "secrets": []}

    def to_markdown(self):
        if self.__outfn:
            obj = Document(f"{self.__outdn}/{self.__outfn}", self.__outdn)
            obj.add_line(f"# {self.__name}")
            obj.add_line(f"Example:")
            obj.add_line
        else:
            raise AttributeError("Invalid output filename.")

    def __init__(
        self,
        fn=False,
        dn=False,
    ):
        if dn and os.path.isdir(dn):
            self.__outdn = dn

        if fn and os.path.isfile(fn):
            self.__outfn = f'{fn.split(".ya")[0]}.md'
            self.__infn = fn
            # print(f"Parsing {self.__infn} and generating {self.__outdn}/{self.__outfn}")
            with open(fn, "r") as fp:
                self.__raw = yaml.safe_load(fp.read())
            self._validate_workflow_name()
            self._validate_workflow_call()
            self._validate_inputs_and_secrets()
            self.__valid = True
            print(json.dumps(self.__data, indent=2))

    @property
    def valid(self):
        return self.__valid

    @property
    def inputs(self):
        return self.__data["inputs"]

    @property
    def secrets(self):
        return self.__data["secrets"]

    def _validate_workflow_name(self):
        try:
            if "name" not in self.__raw.keys():
                raise DocumentError(
                    "No name element in this workflow. If indeed, that is what it is."
                )
            else:
                self.__name = self.__raw["name"]
        except Exception:
            self.__valid = False

    def _validate_workflow_call(self):
        try:
            if "on" not in self.__raw.keys() and True in self.__raw.keys():
                self.__top = True
            elif "on" in self.__raw.keys() and True not in self.__raw.keys():
                self.__top = "on"
            else:
                raise DocumentError("`on` section is not present.")
            if (
                type(self.__raw[self.__top]) != dict
                or "workflow_call" not in self.__raw[self.__top].keys()
            ):
                raise DocumentError("`on->workflow_call` section is not present.")
        except Exception:
            self.__valid = False

    def _validate_inputs_and_secrets(self):
        try:
            # separate the inputs and secrets if they're there
            for k, v in {"inputs": {}, "secrets": {}}.items():
                if k in self.__raw[self.__top]["workflow_call"].keys():
                    for k2, v2 in self.__raw[self.__top]["workflow_call"][k].items():
                        _td = {
                            "name": k2,
                            "description": v2.get("description", False),
                            "type": v2.get("type", False),
                            "default": v2.get("default", False),
                            "required": v2.get("required", False),
                        }
                        if not _td.get("description"):
                            raise Exception(
                                f"{self.__infn}:on->workflow_call->{k}->{_td['name']} has no description."
                            )
                        if k == "inputs" and not _td.get("type"):
                            raise Exception(
                                f"{self.__infn}:on->workflow_call->{k}->{_td['name']} has no type."
                            )
                        # print(_td)
                        self.__data[k].append(_td)
        except Exception:
            self.__valid = False


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        parser = argparse.ArgumentParser(
            prog=sys.argv[0],
            description="Generates documentation for Github Actions Re-usable Workflows",
        )
        parser.add_argument(
            "-d", "--outdir", help="Specify the output directory (default: `./docs/`)."
        )
        parser.add_argument(
            "inputs",
            metavar="inputs",
            type=str,
            nargs="+",
            help="The space separated list of files to parse.",
        )
        args = parser.parse_args()
        args.inputs.sort()

        # Now that we've parsed any commandline args, we can parse all of our workflows and build
        # a list of objects to dump to individual files. That's the fun part.
        flows = []
        print(args.inputs)
        for arg in args.inputs:
            try:
                obj = Workflow(arg, args.outdir)
                if obj.valid:
                    flows.append(obj)
            except DocumentError as err:
                print(f"DEBUG: {arg}")
                print(err)

        # Ok, now that all of our workflows are parsed and ready we can start to build our outputs
