#!/usr/bin/python3

import ipaddress

print('Is host a valid IP address within subnt A?')
host = input('Host: ')
subnet_a = input('Subnet A: ')

print(ipaddress.IPv4Address(host) in ipaddress.IPv4Network(subnet_a))

