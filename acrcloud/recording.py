import requests
import re
import time
import os


stream_url = 'http://worldwidefm.out.airtime.pro:8000/worldwidefm_a'

while 1:
	print "rec starting\n",
	r = requests.get(stream_url, stream=True)
	print "recording now..."
	with open('worldwide_fm.mp3', 'wb') as f:
	    for block in r.iter_content(512):
	        	f.write(block)
			

