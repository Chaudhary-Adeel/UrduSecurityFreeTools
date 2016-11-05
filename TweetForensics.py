#!/usr/bin/env python

"""
The MIT License (MIT)

Copyright (c) 2014 Chaudhary-Adeel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

try:
	import twitter;from time import sleep;from sys import argv;from os import system
except Exception, e:
	print "\033[91mError: {0}".format(e) + "\033[0m"

class Coloring:
	def __init__(self):
		self.green = "\033[1m\033[92m"
		self.bold = "\033[1m"
		self.red = "\033[91m"
		self.die = "\033[0m"

def banner():
	system('clear')
	print COLOR.green + """
  _____                _     ___                    _    
 |_   _|_ __ _____ ___| |_  | __|__ _ _ ___ _ _  __(_)__ 
   | | \ V  V / -_) -_)  _| | _/ _ \ '_/ -_) ' \(_-< / _|
   |_|  \_/\_/\___\___|\__| |_|\___/_| \___|_||_/__/_\__|
   -------------------------------------------------------
   Author         :    Muhammad Adeel -> \033[91m@Chaudhary1337\033[92m
   Report Bugs    :    Chaudhary1337@gmail.com
   Tool Desc      :    Performing Tweet Analysis
   -------------------------------------------------------
   Commands       :    help - forensic - change - stats
                  :    clear - exit
   -------------------------------------------------------
   """ + COLOR.die

consumer_key = 'yZA8ABXinV6rQlICV3DNyKwHV';consumer_secret = 'D1xMDf3NnDCcYtu5KRcwes8MzQbAWW4pPQHEYL2tHH0T70L9E1';access_token = '1731498314-nPqsTsliicuwDmeBnZplnyM0ZYXR3TAnArZPhdR';access_token_secret = '1Tu4TYpL5ASLOzAFBDqWH721ETxVJUdT8hKnczSLyvWcH'
api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token, access_token_secret=access_token_secret)

COLOR = Coloring()

def PerformAnalysis(tweetID):
	try:
		stats = api.GetStatus(tweetID)
		print COLOR.green + "\n\t--> Tweet Author: @" + COLOR.die + str(stats.user.screen_name) + COLOR.green + "\n\t--> Name: " + COLOR.die + str(stats.user.name) + COLOR.green + "\n\t--> Location: " + COLOR.die + str(stats.user.location) + COLOR.green + "\n\t--> Time Zone: " + COLOR.die + str(stats.user.time_zone) + COLOR.green + "\n\t--> Retweet Count: " + COLOR.die + str(stats.retweet_count) + COLOR.green + "\n\t--> Favourites Count: " + COLOR.die + str(stats.favorite_count) + COLOR.green + "\n\t--> Tweeter\'s Status Count: " + COLOR.die + str(stats.user.statuses_count) + COLOR.green + "\n\t--> Tweet Created At: " + COLOR.die + str(stats.created_at) + COLOR.green + "\n\t--> Tweeter's ID Created: " + COLOR.die + str(stats.user.created_at) + COLOR.green + "\n\t--> Tweet Text: " + COLOR.die + str(stats.text) + COLOR.green + "\n\t--> Author Description: " + COLOR.die + str(stats.user.description) + "\n\n"
	except Exception, e:
		print COLOR.red + "Error: {0}".format(e) + COLOR.die
		exit()

def main():
	banner()
	if len(argv) < 2:
		print COLOR.red + "   --> Usage: {0} <tweetID>".format(argv[0]) + COLOR.die
		print COLOR.red + "   --> Example: {0} 793193666512883712\n".format(argv[0]) + COLOR.die
	else:
		try:
			while True:
				try:
					tweetId = raw_input("   (\033[1mCommands:\033[0m)> ")
					if tweetId == "change":
						tweetId = raw_input("\n   (\033[1mTweetID:\033[0m)> ")
						PerformAnalysis(tweetId);
					elif tweetId == "stats":
						print COLOR.red + COLOR.bold + "\n -- Stats For This Tool are -- \n\n   Code Lines: 96\n   Script Size: 4 KB\n   Extra Module: python-twitter\n   Feature: Colored output without external module\n" + COLOR.die
					elif tweetId == "clear":
						system('clear')
						banner()
					elif tweetId == "forensic":
						print COLOR.bold + "\n   --> Please Wait..." + COLOR.die
						sleep(0.5)
						PerformAnalysis(argv[1])
					elif tweetId == "help":
						print COLOR.bold + """
   -------------------------------
    help   - Show this Meessage
    change - Change Tweet ID
    stats  - Tool Statistics
    clear  - clear the Console
    exit   - quit the tool
   -------------------------------
						""" + COLOR.die
					elif tweetId == "exit":
						print COLOR.bold + "\n  [+] Good Bye.\n" + COLOR.die
						exit()
					else:
						print COLOR.bold + "\n  [-] Invalid Command.\n" + COLOR.die
				except KeyboardInterrupt:
					print COLOR.red + "\nError: KeyboardInterrupt" + COLOR.die
					exit()
		except Exception, e:
			print COLOR.red + "Error: {0}".format(e) + COLOR.die

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print COLOR.red + "\nError: KeyboardInterrupt" + COLOR.die
		exit()
