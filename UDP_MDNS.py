from scapy.all import *
from timeit import default_timer as timer

#https://cnpnote.tistory.com/entry/PYTHON-%EC%96%B4%EB%96%BB%EA%B2%8C-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-UDP-%EB%A9%80%ED%8B%B0-%EC%BA%90%EC%8A%A4%ED%8A%B8%ED%95%A9%EB%8B%88%EA%B9%8C
#https://wiki.python.org/moin/UdpCommunication
 
 
#start timer
start = timer()


#Unicast MDNS
def mdns(reverse):    
    lens=[]
    for i in reverse:
       lens.append(len(i))
    var_3=binascii.unhexlify('0'+str(lens[3]))
    var_2=binascii.unhexlify('0'+str(lens[2]))
    var_1=binascii.unhexlify('0'+str(lens[1]))
    var_0=binascii.unhexlify('0'+str(lens[0]))

    global start
    mdns_pkt='\x00\x00\x01\x00\x00\x0e\x00\x00\x00\x00\x00\x00' \
    '\x05_http\x04_tcp\x05local\x00\x00\x0c\x00\x01' \
    '\x05_rtsp\x04_tcp\x05local\x00\x00\x0c\x00\x01' \
    '\x04_smb\x04_tcp\x05local\x00\x00\x0c\x00\x01' \
    '\x0c_device-info\x04_tcp\x05local\x00\x00\x0c\x00\x01' \
    '\t_services\x07_dns-sd\x04_udp\x05local\x00\x00\x0c\x00\x01' \
    '\x05_svnp\x04_tcp\x05local\x00\x00\x0c\x00\x01' \
    '\x06_adisk\x04_tcp\x05local\x00\x00\x0c\x00\x01' \
    '\x0b_afpovertcp\x04_tcp\x05local\x00\x00\x0c\x00\x01' \
    '\x0c_workstation\x04_tcp\x05local\x00\x00\x0c\x00\x01' \
    '\x04_CGI\x04_tcp\x05local\x00\x00\x0c\x00\x01' \
    '\x05_psia\x04_tcp\x05local\x00\x00\x0c\x00\x01' \
    '\x06_dhnap\x04_tcp\x05local\x00\x00\x0c\x00\x01' \
    '\x06_audio\x04_tcp\x05local\x00\x00\x0c\x00\x01' \
    +var_3+reverse[3]+var_2+reverse[2]+var_1+reverse[1]+var_0+reverse[0]+'\x07in-addr\x04arpa\x00\x00\x0c\x00\x01'
 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(time)
    print("========= Unicast MDNS Packet REQUEST =========")
    try:
        s.connect((target, 5353))
        s.send(mdns_pkt)
        print s.recv(1024)+"\n"
    except socket.timeout as timeerror:
        print timeerror
        #start=start+time
    except socket.error as err:
        print str(err)+"\n"

if __name__=="__main__":
        #set value
        time=0.3
	 
        target=sys.argv[1]
        reverse=(target.split('.'))
	 
        mdns(reverse)
	 
        #end timer
        end=timer()
        print ("Time Stamp ---> "+str(end-start))
