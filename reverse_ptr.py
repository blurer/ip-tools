#!/usr/bin/env python3

import ipaddress
import sys


in_file = sys.argv[1:]

for x in in_file:
    print(ipaddress.ip_address(x).reverse_pointer);
