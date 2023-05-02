#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib .request.urlopen(req) as response:
        doc = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(doc)))
        print("\t- content: {}".format(doc))
        print("\t- utf8 content: {}".format(doc.decode("utf-8")))
