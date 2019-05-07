from scapy.all import *
import sys
from colorama import Fore


# SSDP Packet
def ssdp():
	payload = "M-SEARCH * HTTP/1.1\r\n" \
	"HOST: 239.255.255.250:1900\r\n" \
	"MAN: \"ssdp:discover\"\r\n" \
	"MX: 1\r\n"\
	"ST: upnp:rootdevice\r\n\r\n"
 
	ssdpRequest = IP(dst='239.255.255.250') / UDP(sport=1900, dport= 1900) / payload
	print(Fore.CYAN+"[+] Send : SSDP Packet REQUEST"+Fore.RESET)
	response=sr1(ssdpRequest, verbose=0, timeout=time)
	print

# NBNS Packet
#payload='\x82(\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00 CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x00!\x00\x01'
def nbns():
	payload="\x82\x28\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x20\x43\x4b\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x00\x00\x21\x00\x01"
	nbnsRequest = IP(dst=target) / UDP(sport=137, dport='netbios_ns') / payload
	print(Fore.CYAN+"[+] Send : NBNS Packet REQUEST"+Fore.RESET)
	response=sr1(nbnsRequest, verbose=0, timeout=time)
	print

# MNDS Packet
def mdns():
	mdnsRequest = pk=IP(dst='224.0.0.251')/UDP(sport=5353, dport='mdns')/DNS(opcode='QUERY', rd=0,rcode='ok', qdcount=1, qd=DNSQR(qname='_http._tcp.local.',qtype='PTR', qclass='IN')/DNSQR(qname='_services._dns-sd._udp.local.',qtype='PTR', qclass='IN'))
	print(Fore.CYAN+"[+] Send : MDNS Packet REQUEST"+Fore.RESET)
	response=sr1(mdnsRequest, verbose=0, timeout=time)
	print

# SNMP Packet
def snmp():
	snmpRequest = IP(dst=target)/UDP(sport=161)/	SNMP(community="public",PDU=SNMPget(varbindlist=[SNMPvarbind(oid="1.3.6.1.2.1.1.1.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.2.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.4.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.5.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.6.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.7.0")]))

	print(Fore.CYAN+"[+] Send : SNMP Packet REQUEST"+Fore.RESET)
	response=sr1(snmpRequest, verbose=0, timeout=time)
	print

if __name__=="__main__":
	if len(sys.argv) is not 2:
		print(Fore.YELLOW+"[-] Example : python fingbox.py <TargetIP>"+Fore.RESET)
		sys.exit()

	time=1
	target=sys.argv[1]
	print(Fore.YELLOW+"------------Target : "+target+"-------------"+Fore.RESET)
	print

	ssdp()
	nbns()
	mdns()
	snmp()
