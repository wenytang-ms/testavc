#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shutil
import sys
import re
import json
import os
def main():
    print("start")
    try:
        with open(".github/scripts/regexes.json", "r") as allowFile:
            allow = json.loads(allowFile.read())
            for rule in allow:
                allow[rule] = read_pattern(allow[rule])
    except (IOError, ValueError) as e:
        raise("Error reading allow file")
    print("~~~~~~~~~~~~~~~~~~~~")
    regex_check(allow)

def read_pattern(r):
    if r.startswith("regex:"):
        return re.compile(r[6:])
    converted = re.escape(r)
    converted = re.sub(r"((\\*\r)?\\*\n|(\\+r)?\\+n)+", r"( |\\t|(\\r|\\n|\\\\+[rn])[-+]?)*", converted)
    return re.compile(converted)

def regex_check(secret_regexes): 
    try: 
        with open("./src/test.js", "r") as secretsFiles:
            files = secretsFiles.read()
    except (IOError, ValueError) as e:
        raise("Error reading allow file")
    for key in secret_regexes:
        found_strings = secret_regexes[key].findall(files)

main()