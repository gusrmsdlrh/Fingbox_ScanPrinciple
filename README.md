# Fingbox_ScanPrinciple
Fingbox에서 사용되는 스캔 원리를 분석하여 시나리오를 짜보며 Scapy로 파이썬 코드를 작성하여 직접 수행해본다.

Scapy로 작성하는 과정에서 팁을 적어본다.

먼저 wireshark에서 해당 payload에 대한 show bytepacket한다음에 raw로 변환후 복사하여 python에서 아래를 수행하면 변환이 된다.
> import binascii 
> binascii.unhexlify('') 


# Scan Flow
아래의 절차는 스캔하는 여러 과정을 스니핑하여 예상되는!! 시나리오이다.

Step 1. 스캔을 시도하는 디바이스의 ARP 테이블을 확인하여 아이피와 MAC Address을 매핑하여 어플 화면에 뿌려준다.

Step 2. MAC Address에 해당하는 제조사을 확인하여 어플 화면에 뿌려준다. 
        (핸드폰 같은 경우엔 MAC Address만으로 모델명까지 알 수 있다고 함.)

Step 3. UDP 프로토콜(SSDP, NBNS, MDNS, SNMP)을 이용하여 장치들의 정보를 긁어온다.

Step 4. UDP 프로토콜을 사용했음에도 불구하고 장치들의 정보를 못 알아내면 아이피, MAC Address, 제조사만 출력을 한다.


# UDP_SSDP
UPnP 프로토콜이 활성화 되어있는 장비에 한해서 정보를 긁어올 때 사용되는 것 ex) 라우터

![image](https://user-images.githubusercontent.com/40857478/52392837-f99a6280-2ae6-11e9-87f7-47caaa0732bf.png)
![image](https://user-images.githubusercontent.com/40857478/52392851-03bc6100-2ae7-11e9-9c42-b1d2109cf71c.png)


# UDP_NBNS
OS가 윈도우인 장치의 정보를 얻어올 때 사용되는 프로토콜이다.

![image](https://user-images.githubusercontent.com/40857478/52392979-86452080-2ae7-11e9-901f-dca5272ef44e.png)


# UDP_MDNS
맥 OS인 경우에는 MDNS 프로토콜에 반응을 하여 Response에서 정보들을 긁어오게 된다.


# UDP_SNMP
SNMP 프로토콜이 활성화 되어있는 장치에 전송하여 Response 패킷에 담겨져있는 정보들을 긁어오게 된다.

![image](https://user-images.githubusercontent.com/40857478/52392987-90ffb580-2ae7-11e9-9b1e-95f3ab3f803b.png)


# 문제점
핸드폰 모델명을 알아내는 과정이 시원치 않다. 추후 알아내면 작성할 
