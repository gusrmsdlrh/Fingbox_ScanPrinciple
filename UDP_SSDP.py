from scapy.all import *
import requests
from timeit import default_timer as timer
import re


#start timer
start = timer()

#Multicast SSDP
def ssdp():    
    global start
    ssdp_pkt= "M-SEARCH * HTTP/1.1\r\n" \
    "HOST: 239.255.255.250:1900\r\n" \
    "MAN: \"ssdp:discover\"\r\n" \
    "MX: 1\r\n"\
    "ST: upnp:rootdevice\r\n\r\n"
 
 
    MCAST_GRP = '239.255.255.250'
    MCAST_PORT = 1900
 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #make the socket multicast-aware and set TTL
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
    sock.settimeout(time)
    #send data
    sock.sendto(ssdp_pkt, (MCAST_GRP, MCAST_PORT))

    mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    print("========= Multicast SSDP Packet REQUEST =========")
    try:
        while 1:
            data, address = sock.recvfrom(1024)
            if target in address:
                ssdp_url = re.search('\w{4}://\w+.\w+.\w+.\w+:\w+/\w+.\w+', data, re.I).group()
                resp=request.get(ssdp_url)

                # Keyword extract
                model_description = scrape(resp.text, '<modelDescription>', '</modelDescription>')
                device_type = scrape(resp.text, '<deviceType>', '</deviceType>')
                friendly_name = scrape(resp.text, '<friendlyName>', '</friendlyName>')
                ssdp_extract_name= device_type+" "+model_description+" "+friendly_name
                print ssdp_extract_name
                break
    except socket.timeout:
        print "NOT Packet\n"
        ssdp2()
        #start=start+time
 
#Unicast SSDP
def ssdp2():    
    global start
    ssdp_pkt= "M-SEARCH * HTTP/1.1\r\n" \
    "HOST: 239.255.255.250:1900\r\n" \
    "MAN: \"ssdp:discover\"\r\n" \
    "MX: 1\r\n"\
    "ST: upnp:rootdevice\r\n\r\n"
 
 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    s.settimeout(time)
    print("========= Unicast SSDP Packet REQUEST =========")
    try:
        s.connect((target, 1900))
        s.send(ssdp_pkt)
        data=s.recv(1024)
        ssdp_url = re.search('\w{4}://\w+.\w+.\w+.\w+:\w+/\w+.\w+', data, re.I).group()
        resp=request.get(ssdp_url)

        # A = Keyword extract
        model_description = scrape(resp.text, '<modelDescription>', '</modelDescription>')
        device_type = scrape(resp.text, '<deviceType>', '</deviceType>')
        friendly_name = scrape(resp.text, '<friendlyName>', '</friendlyName>')
        ssdp_extract_name= device_type+" "+model_description+" "+friendly_name
        print ssdp_extract_name
        print
    except socket.timeout:
        print "NOT Packet\n"
        #start=start+time
    except socket.error as err:
        print str(err)+"\n"

#SSDP URL-Data extraction
def scrape(text, start_trig, end_trig):
    if text.find(start_trig) != -1:
        return text.split(start_trig, 1)[-1].split(end_trig, 1)[0]
    else:
        return False

#def 

if __name__=="__main__":
        #set value
        time=0.3
        request=requests.Session()
	 
        target=sys.argv[1]
	 
        ssdp()
	 
        #end timer
        end=timer()
        print
        print ("Time Stamp ---> "+str(end-start))
