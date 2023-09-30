
from scapy.all import *
from miotools import ipaddress, netif
import time
ip = input("your target IP: ")
port = input("your target port: ")
method = "TLS"
 
def main():
    sr(IP(ip)/UDP().destport(port))
  
main()
