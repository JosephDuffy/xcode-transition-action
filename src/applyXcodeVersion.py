#!/usr/bin/env python3

from ruamel.yaml import YAML
import argparse
import pathlib
import sys
from functools import reduce
from operator import getitem

# Credit: https://stackoverflow.com/a/14692747/657676
def getFromDict(dataDict, mapList):
    return reduce(getitem, mapList, dataDict)


def setInDict(dataDict, mapList, value):
    getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value


parser = argparse.ArgumentParser(description="Apply Xcode version to YAML file")
parser.add_argument("yaml_key", nargs="+", help="Key in YAML file to update")
parser.add_argument("--yaml_value", nargs="+", help="Value to set key to")
parser.add_argument(
    "--yaml_file",
    type=str,
    help="The file to update. If not provided will read from stdin and write to stdout",
)

args = parser.parse_args()

key = args.yaml_key
value = args.yaml_value

yaml = YAML()
# Do not modify long lines
yaml.width = 9999999
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=4, offset=2)

yaml_file = None

if args.yaml_file:
    yaml_file = pathlib.Path(args.yaml_file)
    file = yaml.load(yaml_file)
else:
    file = yaml.load(sys.stdin)

existing_value = getFromDict(file, key[:-1])[key[-1]]

if yaml_file:
    print("Existing key", key, "has value", existing_value)

if existing_value != value:
    setInDict(file, key, value)
elif yaml_file:
    print("Key has not changed")

if yaml_file:
    yaml.dump(file, yaml_file)
else:
    yaml.dump(file, sys.stdout)
