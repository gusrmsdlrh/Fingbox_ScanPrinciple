from scapy.all import *
import sys
import os
from colorama import Fore

if len(sys.argv) is not 2:
	print(Fore.YELLOW+"[-] Example : python fingbox.py <TargetIP>"+Fore.RESET)
	sys.exit()

time=1
target=sys.argv[1]
print(Fore.CYAN+"------------Target : "+target+"-------------"+Fore.RESET)
print

# SSDP Packet
payload = "M-SEARCH * HTTP/1.1\r\n" \
"HOST:239.255.255.250:1900\r\n" \
"ST:upnp:rootdevice\r\n" \
"MAN: \"ssdp:discover\"\r\n" \
"MX:2\r\n\r\n"
 
ssdpRequest = IP(dst=target) / UDP(sport=1900, dport= 1900) / payload
print(Fore.CYAN+"[+] Send : SSDP Packet REQUEST"+Fore.RESET)
response=sr1(ssdpRequest, verbose=0, timeout=time)
if (str(type(response)) == "<type 'NoneType'>") or response[IP].proto == 1:
	print(Fore.RED+"[-] FAIL : SSDP Packet Response"+Fore.RESET)
else:
	print(Fore.YELLOW+"[*] Success : SSDP Packet Response"+Fore.RESET)
print
print "----------------------------------"
print

# NBNS Packet
#payload='\x82(\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00 CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x00!\x00\x01'
payload="\x82\x28\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x20\x43\x4b\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x00\x00\x21\x00\x01"
nbnsRequest = IP(dst=target) / UDP(sport=137, dport=137) / Raw(payload)
print(Fore.CYAN+"[+] Send : NBNS Packet REQUEST"+Fore.RESET)
response=sr1(nbnsRequest, verbose=0, timeout=time)

print type(response)
if (str(type(response)) == "<type 'NoneType'>") or response[IP].proto == 1:
	print(Fore.RED+"[-] FAIL : NBNS Packet Response"+Fore.RESET)
else:
	print(Fore.YELLOW+"[*] Success : NBNS Packet Response"+Fore.RESET)
print
print "----------------------------------"
print

# MNDS Packet
mdnsRequest = pk=IP(dst='192.168.123.2')/UDP(sport=80, dport='mdns')/DNS(opcode='QUERY', rd=0,rcode='ok', qdcount=1, qd=DNSQR(qname='_services._dns-sd._udp.local.',qtype='PTR', qclass='IN'))
print(Fore.CYAN+"[+] Send : MDNS Packet REQUEST"+Fore.RESET)
response=sr1(mdnsRequest, verbose=0, timeout=time)
if (str(type(response)) == "<type 'NoneType'>") or response[IP].proto == 1:
	print(Fore.RED+"[-] FAIL : MDNS Packet Response"+Fore.RESET)
else:
	print(Fore.YELLOW+"[*] Success : MDNS Packet Response"+Fore.RESET)
print
print "----------------------------------"
print

# SNMP Packet
snmpRequest = IP(dst=target)/UDP(sport=161)/SNMP(community="public",PDU=SNMPget(varbindlist=[SNMPvarbind(oid="1.3.6.1.2.1.1.1.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.2.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.4.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.5.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.6.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.7.0")]))

print(Fore.CYAN+"[+] Send : SNMP Packet REQUEST"+Fore.RESET)
response=sr1(snmpRequest, verbose=0, timeout=time)
if (str(type(response)) == "<type 'NoneType'>") or response[IP].proto == 1:
	print(Fore.RED+"[-] FAIL : SNMP Packet Response"+Fore.RESET)
else:
	print(Fore.YELLOW+"[*] Success : SNMP Packet Response"+Fore.RESET)
print
print "----------------------------------"
print
