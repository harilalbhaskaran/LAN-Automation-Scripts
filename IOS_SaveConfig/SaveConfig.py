#!/usr/bin/env python
from netmiko import ConnectHandler
from datetime import datetime

platform = 'cisco_ios'
username = '#########' # Replace with SSH Username.
password = '#########' # Replace with SSH Password.
i = datetime.now()

#  Open file with list of switches
f = open ("Switchlist.txt")

#  Loop and SSH connectivity
for line in f:
	print "Trying to connect " + (line) + "\n"
	HOST = line.strip()
#  print HOST
	device = ConnectHandler(device_type=platform, ip=HOST, username=username, password=password)
	print "SSH Connection established to :" + (line) + "\n"

	filename = HOST + '-' + str(i) + '.txt'
	device.send_command('terminal length 0')
	showrun = device.send_command('show run')
	showvlan = device.send_command('show vlan')
	showver = device.send_command('show ver')
#  Writing IOS configurations to file
	print "Copying configurations of " + (line) + "\n"
	log_file = open(filename, "a")   # in append mode
	log_file.write(showrun)
	log_file.write("\n")
	log_file.write(showvlan)
	log_file.write("\n")
	log_file.write(showver)
	log_file.write("\n")

	device.disconnect()
	print "SSH Connection Closed !" + "\n"
