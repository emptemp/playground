from acrcloud.recognizer import ACRCloudRecognizer
import re

config = {
    'host': 'identify-eu-west-1.acrcloud.com',
    'access_key': '26a8a872b1759449e87266260df80f21',
    'access_secret': 'L1pLC7iXLLLDpF87ICBw9fOBFaNLS4fYJ0hU4udV',
    'debug': True,
    'timeout': 10
}

acrcloud = ACRCloudRecognizer(config)

print "file?\n"
file = raw_input()
dirty = acrcloud.recognize_by_file(str(file), 0)
found = re.findall(r"\":\"(.*?)\"", dirty);
#names = re.findall(r"name\":\"(.*?)\"", dirty);

for k in found:
	print k
#	print "\n"
#print title
print "\n"
