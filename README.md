# Baisc IP tools written in Python.

* is_subnet.py - Is the host within a valid subnet? 
* give_ips.py - Give a subnet, this prints all IPv4 addresses (> /24)
* revese.py - Give an IP address, prints a PTR record.

## is_subnet.py example:

```
 root @ devbox in ~/ip_tools [6:04:49] 
$ ./is_subnet.py  
Is host a valid IP address within subnt A?
Host: 192.168.1.10
Subnet A: 192.168.1.0/24
True

# root @ devbox in ~/ip_tools [6:04:56] 
$ ./is_subnet.py
Is host a valid IP address within subnt A?
Host: 192.168.2.10
Subnet A: 192.168.1.0/24
False

# root @ devbox in ~/ip_tools [6:05:08] 
$ ./is_subnet.py
Is host a valid IP address within subnt A?
Host: 172.17.223.228
Subnet A: 172.17.223.128/25
True
```

## give_ips.py example

```
# root @ devbox in ~/ip_tools [6:10:11] 
$ ./give_ips.py
Priting a list of the IPv4 addresses for a given subnet
Subnet: 172.17.1.128/29
172.17.1.128
172.17.1.129
172.17.1.130
172.17.1.131
172.17.1.132
172.17.1.133
172.17.1.134
172.17.1.135
```

## reverse.py example
```
[ec2-user@ip-172-26-13-171 ip-tools]$ ./reverse.py 
Specify IP for reverse record generation
IP: 192.168.52.96
96.52.168.192.in-addr.arpa
```
