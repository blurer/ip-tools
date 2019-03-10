#!/usr/bin/python3

import netaddr
import ipaddress

print('Is host a valid IP address within subnt A?')
host = input('Host: ')
subnet_a = input('Subnet A: ')

print(netaddr.IPNetwork(host) == netaddr.IPNetwork(subnet_a).cidr)

