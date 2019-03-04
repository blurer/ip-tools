#!/usr/bin/python3

import ipaddress

print('Priting a list of the IPv4 addresses for a given subnet')
subnet = input('Subnet: ')

for addr in ipaddress.IPv4Network(subnet):
    print(addr)
