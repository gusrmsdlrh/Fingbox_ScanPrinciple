from scapy.all import *

mdnsRequest = pk=IP(dst='224.0.0.251')/UDP(sport=5353, dport='mdns')/DNS(opcode='QUERY', rd=0,rcode='ok', qdcount=1, qd=DNSQR(qname='_http._tcp.local.',qtype='PTR', qclass='IN')/DNSQR(qname='_services._dns-sd._udp.local.',qtype='PTR', qclass='IN'))
response=sr1(mdnsRequest, verbose=0, timeout=1)
