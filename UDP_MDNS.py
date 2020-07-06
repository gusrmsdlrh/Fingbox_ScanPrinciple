from scapy.all import *

mdnsRequest= pk=IP(dst='224.0.0.251')/UDP(sport=5353, dport=5353)/DNS(opcode='QUERY',qdcount=11,qd=DNSQR(qname='_http._tcp.local.', qtype='PTR', qclass='IN')
			/DNSQR(qname='_rtsp._tcp.local.', qtype='PTR', qclass='IN')
			/DNSQR(qname='_https._tcp.local.', qtype='PTR', qclass='IN')
			/DNSQR(qname='_services._dns-sd._udp.local', qtype='PTR', qclass='IN')
			/DNSQR(qname='_svnp._tcp.local', qtype='PTR', qclass='IN')
			/DNSQR(qname='_adisk._tcp.local', qtype='PTR', qclass='IN')
			/DNSQR(qname='_afpovertcp._tcp.local', qtype='PTR', qclass='IN')
			/DNSQR(qname='_workstation._tcp.local', qtype='PTR', qclass='IN')
			/DNSQR(qname='_CGI._tcp.local', qtype='PTR', qclass='IN')
			/DNSQR(qname=reverse[3]+'.'+reverse[2]+'.'+reverse[1]+'.'+reverse[0]+'.in-addr.arpa', qtype='PTR', qclass='IN')
			/DNSQR(qname='_psia._tcp.local', qtype='PTR', qclass='IN'))
	print(Fore.CYAN+"[+] Send : MDNS Packet REQUEST"+Fore.RESET)
	response=sr(mdnsRequest, verbose=0, timeout=time)
	print response

