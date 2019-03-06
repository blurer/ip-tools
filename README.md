## ip-tools
* is_subnet.py
* reverse_ptr.py
* subnet_all.py
* subnet_hosts.py

## is_subnet.py
Is the host ip a valid ip address in the subnet you provide?

```
[ec2-user@ip-172-26-4-10 ip-tools]$ ./is_subnet.py 
Is host a valid IP address within subnt A?
Host: 10.26.96.108
Subnet A: 10.26.96.96/29
False
[ec2-user@ip-172-26-4-10 ip-tools]$ ./is_subnet.py 
Is host a valid IP address within subnt A?
Host: 10.26.96.108
Subnet A: 10.26.96.96/28
True
```

## give_ips.py
Specify ip addresses and get the pointer (ptr) dns record entry.

```
[ec2-user@ip-172-26-4-10 ip-tools]$ ./reverse_ptr.py 10.26.96.108 172.26.4.10 192.168.2.232
108.96.26.10.in-addr.arpa
10.4.26.172.in-addr.arpa
232.2.168.192.in-addr.arpa
```

## subnet_hosts.py
Print all of the valid host addresses on a given subnet.

```
[ec2-user@ip-172-26-4-10 ip-tools]$ ./subnet_hosts.py 
------------------------------
Subnet/Mask: 192.168.1.128/29
------------------------------
192.168.1.129
192.168.1.130
192.168.1.131
192.168.1.132
192.168.1.133
192.168.1.134
------------------------------
```

## give_subnet.py
Print all valid ip addresses on a network. 

```
[ec2-user@ip-172-26-4-10 ip-tools]$ ./subnet_all.py 
------------------------------
Subnet/Mask: 192.168.1.128/29
------------------------------
192.168.1.128
192.168.1.129
192.168.1.130
192.168.1.131
192.168.1.132
192.168.1.133
192.168.1.134
192.168.1.135
------------------------------
```
