#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import os, sys
from acrcloud.recognizer import ACRCloudRecognizer
from acrcloud.recognizer import ACRCloudRecognizeType
import acrcloud.recognizer
import re
import time
import datetime

config = {
    'host': 'identify-eu-west-1.acrcloud.com',
    'access_key': '26a8a872b1759449e87266260df80f21',
    'access_secret': 'L1pLC7iXLLLDpF87ICBw9fOBFaNLS4fYJ0hU4udV',
    'debug': True,
    'timeout': 10
}

stream_url = 'http://worldwidefm.out.airtime.pro:8000/worldwidefm_a'
acrcloud = ACRCloudRecognizer(config)

def listen(stream_url):
	r = requests.get(stream_url, stream=True)
	i = 0
	print("listening now...\n")
	with open('stream.mp3', 'wb') as f:
	    for block in r.iter_content(512):
	                f.write(block)
		        #print i
                        i=i+1
		        if i == 420:
			    break

def analyse():
	print "recognize now...\n"
	dirty = acrcloud.recognize_by_file("stream.mp3", 0)
	found = re.findall(r"\":\"(.*?)\"", dirty);
	for k in found:
		print(k)
	if found[0] != "Success":
		return 0
	else:
		return found

def add(found, ts):
	with open('output.txt', 'r') as f:
		lines = f.read().splitlines()
	if lines[-1] != found[0]:
		f = open("/var/www/html/playlist.txt","a+")
		f.write('{};'.format(ts))
		for k in found:
			f.write('{};'.format(k))
		f.write("\n")	
		f.close()
		print("added new track!")
	else:
		print("track already in list")
	
while 1:
	ts = datetime.datetime.now().strftime('%d-%m-%Y;%H:%M:%S')
	print("rec starting,", listen(stream_url))
	print("rec finished,")
	
	#found = analyse()
	analyse()
	found = 0	
	if found:
		add(found,ts)	

	time.sleep(30)
