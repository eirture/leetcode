#!/usr/bin/env python3

import datetime
import os
import re
import subprocess

TITLE_PATTERN = re.compile(r'^# \[([0-9]+)\. (.+)]\((http.+)\) - (.+)$')

TABLE_HEADER = '''
| # | Title | Difficulty | Date |
|---| ----- | ---------- | ---- |
'''

TABLE_ROW_TEMPLATE = '|{no}|[{title}]({file_path})|{level}|{date}|'


def parse_title(path: str):
    with open(path, 'r+') as f:
        for line in f.readlines():
            line = line.strip()
            result = TITLE_PATTERN.findall(line)
            if result:
                return result[0]


def parse_readme(path: str, values: dict):
    new_lines = []
    with open(path, 'r+') as f:
        session = ''
        for i in f.readlines():
            if i.startswith('### '):
                new_lines.append(i)
                session = i.strip().split(' ', 1)[-1]
                vs = values.get(session)
                if not vs:
                    session = ''
                    continue
                new_lines.append(f'{TABLE_HEADER}')
                new_lines.extend([f'{i}\n' for i in vs])

            if session:
                continue
            new_lines.append(i)

    return new_lines


def execute(commands):
    p = subprocess.Popen(
        commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()  # type: bytes, bytes
    if p.returncode != 0:
        raise Exception(
            f'failed to execute the command {commands}. exit code: {p.returncode}. {stderr.decode("utf-8")}')
    return stdout.decode('utf-8'), stderr.decode('utf-8')


def get_file_date(path: str):
    cmd = f'git log -1 --pretty=format:%ad --date=format:%Y/%m/%d -- {path}'
    stdout, _ = execute(cmd.split(' '))
    return stdout or datetime.datetime.now().strftime("%Y/%m/%d")


def do(dir_path: str):
    items = []
    for i in os.listdir(dir_path):
        path = os.path.join(dir_path, i)
        t = parse_title(path)
        items.append({
            'no': t[0],
            'title': t[1],
            'link': t[2],
            'level': t[3],
            'file_path': path,
            'date': get_file_date(path)
        })
    items = sorted(items, key=lambda k: int(k.get('no', 0)), reverse=True)
    for i in items:
        yield TABLE_ROW_TEMPLATE.format(**i)


def main():
    readme_filepath = './README.md'

    result = parse_readme(readme_filepath, {
        'Leetcode Algorithms': do('./algorithms/')
    })
    with open(readme_filepath, 'w+') as f:
        f.writelines(result)


if __name__ == '__main__':
    main()
