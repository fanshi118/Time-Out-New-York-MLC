#!/usr/bin/python

import sys

for line in sys.stdin:
    user_id = line.strip().split(',')[0]
    if user_id.isdigit():
        print user_id
