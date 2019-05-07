from scapy.all import *

snmpRequest = IP(dst=target)/UDP(sport=161)/SNMP(community="public",PDU=SNMPget(varbindlist=[SNMPvarbind(oid="1.3.6.1.2.1.1.1.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.2.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.4.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.5.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.6.0"),SNMPvarbind(oid="1.3.6.1.2.1.1.7.0")]))
response=sr1(snmpRequest, verbose=0, timeout=1)
