#!/usr/bin/env python3

import sys

print("Printing out User Data:\n")

for x in sys.stdin:
    words = x.replace('\n','').split(':')
    if words[0][0] == '#':
        print(words[0][1:] + " is skipped because it starts with a hashtag (is commented out")
    else:
        print("The user " + words[0] + " has a password of " + words[1] + " and has userid " + words[2] + " and groupid " + words[3])

print("\nEnd of User Data")
