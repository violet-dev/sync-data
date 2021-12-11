# This source code is a part of project violet-server.
# Copyright (C)2020-2021. violet-team. Licensed under the MIT Licence.

import urllib.request
from urllib.error import URLError, HTTPError

file = open('syncversion.txt', 'r')
Lines = file.readlines()

for line in Lines:
    url = line.split(' ')[2]
    print(url)
    try:
        res = urllib.request.urlopen(url)
        print(res.status)
    except HTTPError as e:
        print(e)