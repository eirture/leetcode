#!/usr/bin/env bash

set -e

FILES=$(git status --short | awk '{print $2}')
MSG=''

for fp in $FILES; do
    fn=$(basename $fp)
    # filter files which name start with digits
    if [[ $(echo $fn | grep -Eo '^[0-9]') ]]; then
        MSG="${MSG}$(echo $fn | sed 's/-/. /;s/-/ /g;s/\.md$//')\n"
    fi
done

# remove the empty line
# MSG=$(printf "$MSG" | sed /^$/d)

# printf "$MSG"
git add -A
git commit -F <(printf "$MSG" | sort -n)

