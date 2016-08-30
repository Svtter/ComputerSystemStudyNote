#!/usr/bin/env python3
# Convert list of hex numbers into decimal

import sys

for x in sys.argv[1:]:
    print(x + "\t = " + hex(int(x)))
