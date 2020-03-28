import base64
import requests
import re
import time
#import threading

class ImagoPy:
	def __init__(self, server_adress, debug):
		self.debug = debug
		self.server_adress = server_adress
		self.headers = {'Content-Type': 'application/xml'}
		self.server_post_url = "http://" + server_adress + ":8001/service/task"
		self.server_get_url = "http://" + server_adress + ":8001/service/updatestatus/label/"
	
	def getConfig(self, label_id, config):
		# TODO
		return 0
		
	def getCounter(self, label_id, counter):
		# TODO
		return 0
		
	def ping(self, label_id, priority="NORMAL"):
		# ping task to label
		xml = ( "<TaskOrder title='Ping'>"
				"<PingTask labelId='" + str(label_id) + "' "
				"taskPriority='" + str(priority) + "' "
				"externalId='0815'/>"
				"</TaskOrder>")
		r = requests.post(self.server_post_url, data=xml, headers=self.headers)
		transaction_id = re.findall(r'<Transaction id="(.*)"/>', r.text)
		time.sleep(1)
		return (label_id, transaction_id[0])
		
	def sendImage(self, label_id, image_file, page=0, preload=0, skip_equal=0, priority="NORMAL"):
		# sends given image to specificed label
		# generates xml data from parameters and sends post request to server
		# returns transcation_id for label
		xml = ( "<TaskOrder title='SendImage'>"
				"<ImageTask page='" + str(page) + "' "
				"preload='" + str(preload) + "' "
				"skipOnEqualImage='" + str(skip_equal) +"' "
				"labelId='" + str(label_id) + "' "
				"taskPriority='" + str(priority) + "' "
				"><Image>" + convertImage(image_file) + "</Image>"
				"</ImageTask></TaskOrder>")
		r = requests.post(self.server_post_url, data=xml, headers=self.headers)
		transaction_id = re.findall(r'<Transaction id="(.*)"/>', r.text)
		time.sleep(1)
		return (label_id, transaction_id[0])
		
		
	def switchPage(self, label_id, page, priority="NORMAL"):
		# sends switch page command
		# generates xml data from parameters and send post request to server
		# returns transcation_id for label
		xml = ( "<TaskOrder title='SendImage'>"
				"<SwitchPageTask page='" + str(page) + "' "
				"labelId='" + str(label_id) + "' "
				"taskPriority='" + str(priority) + "' "
				"externalId='0815'/></TaskOrder>")
		r = requests.post(self.server_post_url, data=xml, headers=self.headers)
		transaction_id = re.findall(r'<Transaction id="(.*)"/>', r.text)
		time.sleep(1)
		return (label_id, transaction_id[0])
	
	def flashLED(self, label_id, color="WHITE", pattern="PATTERN_2", repeat="2", priority="NORMAL"):
		xml = ( "<TaskOrder title='Ping'>"
				"<FlashingTask labelId='" + str(label_id) + "' "
				"taskPriority='" + str(priority) + "'>"
				"<BasicLED color='" + str(color) + "' "
				"pattern='" + str(pattern) + "' "
				"repeatCount='" + str(repeat) + "'/>"
				"</FlashingTask></TaskOrder>")
		r = requests.post(self.server_post_url, data=xml, headers=self.headers)
		transaction_id = re.findall(r'<Transaction id="(.*)"/>', r.text)
		time.sleep(1)
		return (label_id, transaction_id[0])

	def isFinished(self, (label_id, transaction_id)):
		# get server status for specificed transaction_id
		# returns status of transaction
		# TODO : create thread for every status request to get answers in parallel
		answer = []
		while answer == [] or answer[0] == "WAITING" or answer[0] == "DELAYED":
			r = requests.get(self.server_get_url + label_id)
			regex = ".*<TransactionId>" + str(transaction_id) + "<\/TransactionId><Status>(.*)<\/Status>.*"
			answer = re.findall(r''+ regex + '', r.text)
			if self.debug == 1: 
				print "\t#debug_", (label_id, answer)
				time.sleep(1)
			else:
				time.sleep(5)
		return (label_id, answer)
		
''' HELPER FUNCTIONS '''
def convertImage(file_name):
	# converts image to base64
	with open(file_name, "rb") as image_file:
		encoded_string = base64.b64encode(image_file.read())
	return encoded_string


