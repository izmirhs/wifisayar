#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
12.2014 izmir hackerspace
"""
from __future__ import print_function
import sys
import nmap
import arrow
exceptions =[('192.168.0.1', 'Router', 'always on'), #ip, host, reason
             ('192.168.0.13', 'Raspi1', "it's me"),
            ]

htmlFile = '/mnt/mekansshfs/mekan.html' # uzak sunucudaki html dosyası
try:
    nm = nmap.PortScanner()
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(0)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(0)

print "izmir hackerspace mekan uygulaması"
print('Scanning network for active hosts...')

nm.scan(hosts='192.168.0.0/24', arguments=' -n -sP -PE')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

for host, status in hosts_list:
    print('{0}:{1}'.format(host, status))

hostsCount = len(hosts_list)
dtnow = arrow.now()
exceptionsCount = len(exceptions)

print "İstisnalar ({}) dahil {} cihaz bağlı".format(str(exceptionsCount), str(hostsCount))
print "İstisnalar ({}) hariç {} cihaz bağlı".format(str(exceptionsCount), str(hostsCount -exceptionsCount))

if (hostsCount - exceptionsCount) < 1:
	message =  "Kapalı"
	print (message)
else:
	message =  "Açık, {} cihaz bağlı".format(str(hostsCount-exceptionsCount))
	print (message)

file = open(htmlFile,'w')
htmlBody =  message + "<BR/><small>Güncelleme: " + dtnow.format('DD.MM.YYYY HH:mm') +  "</small>" 
file.write(htmlBody)
file.close()
