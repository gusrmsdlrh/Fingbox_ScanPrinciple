# Fingbox_ScanPrinciple
Fingbox에서 사용되는 스캔 원리를 분석하여 시나리오를 짜보며 Scapy로 파이썬 코드를 작성하여 직접 수행해본다.

# Scan Flow
아래의 절차는 스캔하는 여러 과정을 스니핑하여 예상되는!! 시나리오이다.

Step 1. 스캔을 시도하는 디바이스의 ARP 테이블을 확인하여 아이피와 MAC Address을 매핑하여 어플 화면에 뿌려준다.

Step 2. MAC Address에 해당하는 제조사을 확인하여 어플 화면에 뿌려준다. 
        (핸드폰 같은 경우엔 MAC Address만으로 모델명까지 알 수 있다고 함.)

Step 3. UDP 프로토콜(SSDP, NBNS, MDNS, SNMP)을 이용하여 장치들의 정보를 긁어온다.

Step 4. UDP 프로토콜을 사용했음에도 불구하고 장치들의 정보를 못 알아내면 아이피, MAC Address, 제조사만 출력을 한다.
