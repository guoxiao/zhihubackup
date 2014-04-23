#!/usr/bin/env python
import argparse
import requests
from bs4 import BeautifulSoup
from html2text import html2text

body_class = 'zu-main-content-inner'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="a script to download zhihu answer as md")
    parser.add_argument('url', metavar='url', type=str, help="url of answer page")
    parser.add_argument('filename', metavar='filename', type=str, help="output file name")
    args = parser.parse_args()
    r = requests.get(args.url);
    soup = BeautifulSoup(r.text)
    body = soup.select('.' + body_class)
    f = open(args.filename, 'w', encoding="utf-8")
    f.write(html2text(body[0].prettify()))

    f.close()
