#!/usr/bin/env bash

set -e

export FILES=$(git status --short | awk '{print $2}')

MSG=`python <<EOF
import os, re

def main():
    files = os.getenv("FILES").split()
    lines = []
    for f in files:
        name = f.split('/')[-1]
        if not re.match('^[0-9]+.*', name):
            continue
        lines.append(name.replace('-', '. ', 1).replace('-', ' ').replace('.md', ''))

    print('\n'.join(lines))

main()
EOF
`

git add -A
git commit -m "$MSG"