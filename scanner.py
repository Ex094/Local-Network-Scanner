#Coded by Ex094
#http://www.procurity.wordpress.com

import socket, os, re
from ping import *

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com', 0))

ip = s.getsockname()[0]

#Get the Local IP
end = re.search('^[\d]{1,3}.[\d]{1,3}.[\d]{1,3}.[\d]{1,3}', ip)

#Chop down the last IP Digits
create_ip = re.search('^[\d]{1,3}.[\d]{1,3}.[\d]{1,3}.', ip)

#Print IP to the user
print "Your IP Address is: " + str(end.group(0))

#Pinging the IP
def ping(ip):
	if verbose_ping(ip) == True:
		print ip, 'is Online'

#Check IP 
def CheckLoopBack(ip):
	if (end.group(0) == '127.0.0.1'):
		return True
		print "Either your IP is a Loop Back or it does not belong in local IP range"

print "Pinging IP's..."


if(CheckLoopBack(create_ip)):
	print "Either your IP is a Loop Back or it does not belong in local IP range"
else:
	for i in range(1, 244):
		ping(str(create_ip.group(0)) + str(i))
	os.system('clear')
