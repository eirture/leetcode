#!/usr/bin/env python3
# coding=utf-8

import argparse
import http.client
import json
import os
import urllib.parse

__author__ = "Jie Liu <eirture@gmail.com>"


LEETCODE_URL = "https://leetcode-cn.com/graphql/"

CONTENT_GRAPHQL = '''query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    boundTopicId
    title
    titleSlug
    content
    translatedTitle
    translatedContent
    isPaidOnly
    difficulty
   similarQuestions
    topicTags {
      name
      slug
      translatedName
      __typename
    }
    status
    sampleTestCase
   exampleTestcases
    __typename
  }
}'''

template = '''
## Solutions

'''


def get_slug(url):
    # type: (str) -> str
    slugs = url.split('/')
    for i in reversed(slugs):
        if i:
            return i
    return ''


def get_content(url):
    slug = get_slug(url)
    if not slug:
        err("unsupported url {}", url)

    data = {
        "operationName": "questionData",
        "variables": {
            "titleSlug": slug
        },
        "query": CONTENT_GRAPHQL
    }

    p = urllib.parse.urlparse(LEETCODE_URL)
    clazz = http.client.HTTPSConnection if p.scheme == 'https' else http.client.HTTPConnection
    conn = clazz(p.hostname, p.port)
    conn.request(
        "POST", p.path, json.dumps(data),
        {'Content-Type': 'application/json', 'origin': 'https://leetcode-cn.com'}
    )
    resp = conn.getresponse()

    if resp.status // 100 != 2:
        err(resp.reason)
    return json.loads(resp.read()).get("data", {}).get("question") or {}


def err(fmt, *args):
    print("err: {}".format(fmt.format(*args)))
    exit(-1)


def write2file(url, output):
    data = get_content(url)
    if not data:
        err("have no content of {}", url)

    qid = data.get('questionId')
    title = data.get('translatedTitle') or data.get('titleSlug')
    content = data.get('translatedContent') or data.get('content')

    filename = "{}-{}.md".format(qid, data.get('titleSlug'))
    filepath = os.path.join(output, filename)
    print(filepath)

    with open(filepath, 'w+') as f:
        f.write('# [{}. {}]({}) - {}\n\n'.format(qid, title, url, data.get('difficulty', '').lower()))
        f.write(content)
        f.write('\n')
        f.write(template)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="the url address of leetcode")
    parser.add_argument("-o", "--out", default="", help="the output directory path")
    args = parser.parse_args()
    write2file(args.url, args.out)


if __name__ == '__main__':
    main()
