import requests
from acrcloud.recognizer import ACRCloudRecognizer
import re
import time
import os

config = {
    'host': 'identify-eu-west-1.acrcloud.com',
    'access_key': '26a8a872b1759449e87266260df80f21',
    'access_secret': 'L1pLC7iXLLLDpF87ICBw9fOBFaNLS4fYJ0hU4udV',
    'debug': True,
    'timeout': 10
}

stream_url = 'http://worldwidefm.out.airtime.pro:8000/worldwidefm_a'
acrcloud = ACRCloudRecognizer(config)

while 1:
	print "rec starting",
	r = requests.get(stream_url, stream=True)
	i = 0
	print "listening now..."
	with open('stream.mp3', 'wb') as f:
	    for block in r.iter_content(512):
	        	f.write(block)
			#print i
			i=i+1
			if i == 420:
				break

	print "rec finished, recognize now...\n"
	dirty = acrcloud.recognize_by_file("stream.mp3", 0)
	found = re.findall(r"\":\"(.*?)\"", dirty);

	for k in found:
		print k

