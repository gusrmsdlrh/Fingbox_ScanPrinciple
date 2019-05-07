from scapy.all import *
 
payload = "M-SEARCH * HTTP/1.1\r\n" \
"HOST: 239.255.255.250:1900\r\n" \
"MAN: \"ssdp:discover\"\r\n" \
"MX: 1\r\n"\
"ST: upnp:rootdevice\r\n\r\n"
 
ssdpRequest = IP(dst='239.255.255.250') / UDP(sport=1900, dport= 1900) / payload
sr1(ssdpRequest, verbose=0, timeout=time)
