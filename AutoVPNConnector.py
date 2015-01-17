#!/usr/bin/env python
# For Linux Systems only
# Fell free to Modify it but The Author :/ :3 Bithces please!

import os, urllib2, sys, time, re

class Coloring:
	def __init__(self):
		self.green = "\033[92m"
		self.bold = "\033[1m"
		self.red = "\033[91m"
		self.die = "\033[0m"

COLOR = Coloring()

if os.getuid() != 0:
	print COLOR.bold + COLOR.red + '\n Error: You are Not root!' + COLOR.die	
	exit()

def clrscr():
	os.system('clear')
	os.system('rm -f vpnbook-us1-*')
	os.system('rm -f VPNBook.com-OpenVPN-US1.zip*')

def banner():
	clrscr()
	TheBanner = '0a0a2b2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2b0a7c204175746f2d56706e2d436f6e6e6563746f722076312e302020202020207c0a7c2020202020202020202020202020202020202020202020202020202020207c0a7c20417574686f72203a2020204d7568616d6d616420416465656c202020207c0a2b2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2b0a0a0a'
	print COLOR.green + COLOR.bold + TheBanner.decode('hex') + COLOR.die
	time.sleep(3)

def LoadFiles():
	print COLOR.bold + '[=] Time Now :  {0}\n'.format(time.ctime()) + COLOR.die
	getFiles = 'wget http://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-US1.zip'
	print COLOR.bold + COLOR.red + ' ---> Downloading Config Files\n\n' + COLOR.die
	os.system(getFiles)

def Unzip():
	LoadFiles()
	uzp = 'unzip VPNBook.com-OpenVPN-US1.zip'
	print COLOR.bold + COLOR.red + '\n ---> Unzipping\n\n' + COLOR.die
	chk = os.path.isfile('VPNBook.com-OpenVPN-US1.zip')
	if chk:
		os.system(uzp)
	else:
		print 'Error: No ZIP Files Found.'

def GetUandP():
	print COLOR.bold + COLOR.red + '\n ---> Getting New Password\n\n' + COLOR.die
	global user, passwd
	user = 'vpnbook'
	try:
		openUrl = urllib2.urlopen('http://www.vpnbook.com/freevpn')
	except urllib2.URLError:
		exit('Error: No Internet Connection is Working.')
	res = openUrl.read()
	regex = '''<li>Password: <strong>(.+?)</strong></li>'''
	temp = re.findall(regex, res)
	if temp:
		passwd = temp[0]
	print COLOR.bold + '''
		\t---> User: {0}
		\t---> Passwd: {1}
	\n'''.format(user, passwd) + COLOR.die

def makeConnection():
	os.system('openvpn --config vpnbook-us1-tcp80.ovpn')

def main():
	banner()
	Unzip()
	GetUandP()
	makeConnection()

if __name__ == '__main__':
	main()
