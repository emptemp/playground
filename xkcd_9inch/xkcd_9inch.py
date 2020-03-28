from imagoPy import *
import requests
import urllib2
import urllib
import re
import cv2
import os
import time
from datetime import datetime

DEBUG_ENABLED = 1
server_adress = "192.168.0.220"
label = "DA0000C1"
ip = ImagoPy(server_adress, DEBUG_ENABLED)

img_h = 960
img_w = 672
b_width = 40
if DEBUG_ENABLED == 1:
    print (img_h/1.0/img_w)

output_name = datetime.now().strftime('imgs/XKCD_%d_%m_%Y.PNG')

def fetchTitleImage():
	response = urllib2.urlopen("https://xkcd.com/")
	page_source = response.read()
	image_name = re.findall(r'.*<div id="comic">\n<img src="//imgs.xkcd.com/comics/(.*)" title.*', page_source)
	image_title = re.findall(r'.*<title>xkcd: (.*)<\/title>', page_source)
	#print image_name
	image_url = "http://xkcd.com/comics/" + image_name[0]
	#print image_url
	urllib.urlretrieve(image_url, image_name[0])
	return image_name[0], image_title[0]

def prepareImage(image, title, img_w, img_h):
    fetched = cv2.imread(image, 1)
    h,w,c = fetched.shape
    if DEBUG_ENABLED == 1:
        print "fetched: h,w ", h, w

    # calculate orientation and dimensions
    ratio = h/1.0/w
    if ratio < 1:
        tmp = img_w
        img_w = img_h
        img_h = tmp

    if DEBUG_ENABLED == 1:
        print ratio

    if ratio < (img_h/1.0/img_w):
        if DEBUG_ENABLED == 1:
            print "fit to width (w, h)"
        scaled = cv2.resize(fetched, (img_w - b_width, int(((img_w-b_width)/1.0/w) * h)))
    else:
        if DEBUG_ENABLED == 1:
            print "fit to height (w, h)"
        scaled = cv2.resize(fetched, (int(((img_h-b_width)/1.0/h) * w), img_h - b_width)) 

    h,w,c, = scaled.shape
    if DEBUG_ENABLED == 1:
        print "scaled: h,w ", h, w

    # pad image with white border
    padded = cv2.copyMakeBorder(scaled,(img_h-h)/2,(img_h-h)/2,(img_w-w)/2,(img_w-w)/2,cv2.BORDER_CONSTANT,value=[255,255,255])

    h,w,c, = padded.shape
    if DEBUG_ENABLED == 1:
        print "padded: h,w ", h, w

    # rotate to portrait 
    #if h < w: 
    #    M = cv2.getRotationMatrix2D((img_w/2,img_h/2),90,1)
    #    padded = cv2.warpAffine(padded, M, (img_h, img_w))

    # scale to given size
    resized = cv2.resize(padded, (img_w, img_h), interpolation = cv2.INTER_AREA)

    h,w,c, = resized.shape
    if DEBUG_ENABLED == 1:
        print "resized: h,w ", h, w

    # convert to greyscale
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    h,w = gray_image.shape
    if DEBUG_ENABLED == 1:
        print "gray_image: h,w ", h, w
    # convert to binary black/white
    retval, bw_image = cv2.threshold(gray_image, 180, 255, cv2.THRESH_BINARY)

    h,w = bw_image.shape
    if DEBUG_ENABLED == 1:
        print "bw_image: h,w ", h, w

    # finally write image
    cv2.imwrite(output_name, bw_image)

    # delete temporary original image
    os.system("rm " + str(image))

    # rotate image if needed
    if h < w:
        os.system("convert -rotate 90 " + output_name + " " + output_name)

# send image to label
def sendImage(output_name):
    transaction = ip.sendImage(label, output_name, 0)
    if DEBUG_ENABLED == 1:
        print ip.isFinished(transaction)

#while 1:
# fetch image from xkcd.com
image, title = fetchTitleImage()
# prepare image for label
prepareImage(image, title, img_w, img_h)
# sendImage
sendImage(output_name)
#time.sleep(43200)
# EOF
