from bs4 import BeautifulSoup
import mechanize
import cookielib
import time
import urllib
import urllib2
import string
import json
import re

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
#br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36]')]

#file = open("links.txt", "w")
print("URL")
#url = raw_input()
##r = br.open('https://boards.4chan.org/b/catalog')
read = open("hot.txt","r")
threads=read.read().splitlines()
read.close()
#threads=[]


#with open('hot.txt') as hot:
#	for line in hot:
#		threads.append(line)
print threads

file = open("picchan.html", "w")
c4 = "https://boards.4chan.org/b/thread/"
for n in range(0, len(threads)):
	url = c4 + threads[n]
	file.write("<h1><a href='" +  url + "'>" + url + "</a></h1>")
	file.write("<br>")

	r=br.open(url)
	html=r.read()
	#print html		
	soup = BeautifulSoup(html)

	id = re.findall(r'<a href="\/\/i(.*?)".*?>(.*?)<\/a>', html)

	for n in range(0,len(id)):
		link = id[n]
		#re.findall(r'[0-9].[a-z]',thumb_link
		print link[0]
		type = re.search(r'.*?\/.\/[0-9]+.(.*?)', link[0])
		thumb = re.sub(r'(.*?\/.\/[0-9]+)(.+)', r'\1s\2',  link[0])
		#print thumb
		img_link = "http://i" + thumb
		img_name = link[1]
		#print thumb[1]
		#thumb_link = thumb[0].encode('utf-8') + ".s" + thumb[1].encode('utf-8')
		#print thumb[0] + "s." + thumb[1]
		#file.write("<img src='http://i."+link[0]+"s.jpg'">
		file.write("<a href='http://i" + link[0] + "'><img src='thumbs/" + img_name + "'></img></a>") 
		file.write(link[1])
		file.write("<br>")	
		#if ".webm" in link[1]:
		print "download " + img_name
			#f = urllib.request.urlopen(img_link)
			#data = f.read()
			#with open("test.webm", "wb") as code:
			#	code.write(data)
		urllib.urlretrieve(img_link, "thumbs/"+img_name) 
	file.write("<br><br><br>")

file.close()

