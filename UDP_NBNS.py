from scapy.all import *
from timeit import default_timer as timer
 
 
#start timer
start = timer()

#Unicast NBNS
def nbns():    
    global start
    nbns_pkt="\x82\x28\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00" \
    "\x20\x43\x4b\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41" \
    "\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x00\x00\x21\x00\x01"
 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(time)
    print("========= Unicast NBNS Packet REQUEST =========")
    try:
        s.connect((target, 137))
        s.send(nbns_pkt)
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
        nbns()
	 
        #end timer
        end=timer()
        print ("Time Stamp ---> "+str(end-start))
