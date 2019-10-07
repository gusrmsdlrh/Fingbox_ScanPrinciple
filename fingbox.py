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

def ssdp2():
	payload = "M-SEARCH * HTTP/1.1\r\n" \
	"HOST: 239.255.255.250:1900\r\n" \
	"MAN: \"ssdp:discover\"\r\n" \
	"MX: 1\r\n"\
	"ST: upnp:rootdevice\r\n\r\n"
 
	ssdpRequest = IP(dst=target) / UDP(sport=1900, dport= 1900) / payload
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

#DNS Packet
def dns():
	dnsRequest = pk=IP(dst='192.168.1.1')/UDP(dport=53)/DNS(opcode='QUERY', rd=0,rcode='ok', qdcount=1, qd=DNSQR(qname='207.1.168.192.in-addr.arpa',qtype='PTR', qclass='IN')/DNSQR(qname='_services._dns-sd._udp.local.',qtype='PTR', qclass='IN'))
	print(Fore.CYAN+"[+] Send : DNS Packet REQUEST"+Fore.RESET)
	response=sr1(dnsRequest, verbose=0, timeout=time)
	print

# MNDS Packet
def mdns():
	mdnsRequest = pk=IP(dst='224.0.0.251')/UDP(sport=5353, dport='mdns')/DNS(opcode='QUERY', rd=0,rcode='ok', qdcount=1, qd=DNSQR(qname='207.1.168.192.in-addr.arpa',qtype='PTR', qclass='IN')/DNSQR(qname='_services._dns-sd._udp.local.',qtype='PTR', qclass='IN'))
	print(Fore.CYAN+"[+] Send : MDNS Packet REQUEST"+Fore.RESET)
	response=sr1(mdnsRequest, verbose=0, timeout=time)
	print

#MDNS2 Packet
def mdns2():
	payload='\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x06_adisk\x04_tcp\x05local\x00\x00\x0c\x00\x01\x0b_afpovertcp\x04_tcp\x05local\x00\x00\x0c\x00\x01\t_services\x07_dns-sd\x04_udp\x05local\x00\x00\x0c\x00\x01\x0c_workstation\x04_tcp\x05local\x00\x00\x0c\x00\x01'
	mdns2Request = pk=IP(dst='224.0.0.251')/UDP(sport=5353, dport='mdns')/payload
	print(Fore.CYAN+"[+] Send : MDNS2 Packet REQUEST"+Fore.RESET)
	response=sr1(mdns2Request, verbose=0, timeout=time)
	print

#MDNS3 Packet
def mdns3():
	payload='\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x05_http\x04_tcp\x05local\x00\x00\x0c\x00\x01\x05_rtsp\x04_tcp\x05local\x00\x00\x0c\x00\x01\t_services\x07_dns-sd\x04_udp\x05local\x00\x00\x0c\x00\x01\x05_svnp\x04_tcp\x05local\x00\x00\x0c\x00\x01'
	mdns3Request = pk=IP(dst='224.0.0.251')/UDP(sport=5353, dport='mdns')/payload
	print(Fore.CYAN+"[+] Send : MDNS3 Packet REQUEST"+Fore.RESET)
	response=sr1(mdns3Request, verbose=0, timeout=time)
	print

#MDNS4 Packet
def mdns4():
	payload='\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x04_CGI\x04_tcp\x05local\x00\x00\x0c\x00\x01\x06_adisk\x04_tcp\x05local\x00\x00\x0c\x00\x01\x0b_afpovertcp\x04_tcp\x05local\x00\x00\x0c\x00\x01\x05_http\x04_tcp\x05local\x00\x00\x0c\x00\x01\x05_psia\x04_tcp\x05local\x00\x00\x0c\x00\x01\t_services\x07_dns-sd\x04_udp\x05local\x00\x00\x0c\x00\x01\x0c_workstation\x04_tcp\x05local\x00\x00\x0c\x00\x01'
	mdns4Request = pk=IP(dst='224.0.0.251')/UDP(sport=5353, dport='mdns')/payload
	print(Fore.CYAN+"[+] Send : MDNS3 Packet REQUEST"+Fore.RESET)
	response=sr1(mdns4Request, verbose=0, timeout=time)
	print

# SNMP Packet
def snmp():
	snmpRequest = IP(dst=target)/UDP(sport=161)/	SNMP(community="public",PDU=SNMPget(varbindlist=[SNMPvarbind(oid="1.3.6.1.2.1.1.1.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.2.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.4.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.5.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.6.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.7.0")]))

	print(Fore.CYAN+"[+] Send : SNMP Packet REQUEST"+Fore.RESET)
	response=sr1(snmpRequest, verbose=0, timeout=time)
	print

# VSTARCAM Packet
def vstar():
	payload='\x44\x48\x01\x01'
	vstarRequest=IP(dst=target)/UDP(sport=6801, dport=8600)/payload
	print(Fore.CYAN+"[+] Send : VSTARCAM Packet REQUEST"+Fore.RESET)
	response=sr1(vstarRequest, verbose=0, timeout=time)
	print

# Shenzen Packet
def shenzen():
	payload='\xff\x00\x00\x00\x00\x00Z\xa5\x00\x00\x00\x00\x00\x00\x00\x00\n-\x00\x00\x00\x00\x00\x00'
	shenzenRequest = IP(dst=target) / UDP(sport=34567, dport= 34569) / payload
	print(Fore.CYAN+"[+] Send : Shenzen Packet REQUEST"+Fore.RESET)
	resp=sr1(shenzenRequest, timeout=1, verbose=0)
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
	ssdp2()
	nbns()
	dns()
	mdns()
	mdns2()
	mdns3()
	mdns4()
	#snmp()
	#vstar()
	#shenzen()
