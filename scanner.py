#Coded by Ex094
#http://www.procurity.wordpress.com

import socket, os, re
from ping import *
from time import sleep

#Fetch the Local IP Address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com', 0))
ip = s.getsockname()[0]

end = re.search('^[\d]{1,3}.[\d]{1,3}.[\d]{1,3}', ip)

print "Your IP Address is: " + str(end.group(0))

#Function toping the IP Address
def ping(ip):
    if  verbose_ping(ip) == True:
        print ip, 'is Online'

def check(ip):

    if (ip[:7] == '192.168') or (ip[:7] == '172.16') or (ip[:7] == '172.31') or (ip[:2] == '10'):
        ping(ip)
    else:
        print "Either your IP is a Loop Back or it does not belong in local IP range"


print "Pinging IP's..."

while True:
    for i in range(0, 4):
        ping(str(end.group(0)) + '.' + str(i))
    os.system('cls')
