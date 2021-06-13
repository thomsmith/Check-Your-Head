#!/usr/bin/env python3

import argparse
import requests
from termcolor import colored
HEADERS = [
        'x-frame-options',
        'x-content-type-options',
        'content-security-policy',
        'x-permitted-cross-domain-policies',
        'referrer-policy',
        'clear-site-data',
        'cross-origin-embedder-policy',
        'cross-origin-opener-policy',
        'cross-origin-resource-policy',
        'strict-transport-security',
        'expect-ct',
        'feature-policy'
]


parser = argparse.ArgumentParser(prog='head.py')
parser.add_argument("-u", "--uri", help='Target URL e.g https://example.com')
args = parser.parse_args()
URI = args.uri


print('[+] Fetching HTTP Response Headers')
response = requests.get(URI)
print('[+] Server Header:',response.headers['server'])
SET = []
MISSING = []


for m in HEADERS:
    if m in response.headers:
        SET.append(m)
        print(colored(f"[+] {m} is set with: " + response.headers[m], "green"))
    else:
        MISSING.append(m)
        print(colored(f"[-] {m} is not set","red"))

print("[-] More information on HTTP Response header best practice can be found here: https://owasp.org/www-project-secure-headers")
