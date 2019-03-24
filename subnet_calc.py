#!/usr/bin/env python3

import ipaddress
import sys
print('------------------------------')
subnet = input("Subnet/Mask: ")
print('------------------------------')
for x in (ipaddress.IPv4Network(subnet)):
    print(x)
print('------------------------------')
