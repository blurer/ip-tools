#!/usr/bin/python3

import ipaddress

print('Specify IP for reverse record generation')
ip = input("IP: ")

print(ipaddress.ip_address(ip).reverse_pointer)
