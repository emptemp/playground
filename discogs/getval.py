import io
import json
import sys
import urllib
import urlparse
import time
from datetime import date
import oauth2 as oauth

consumer_key = 'uvHqhbuQVYIeSbHnZXGl'
consumer_secret = 'dxbDcVNBYgNJYixbGfCaQxPmCJDoZHJy'

oauth_token        = "ojfCworuyffXtjdulImvLYwAtPBKihdftJEtUZHN"
oauth_token_secret = "SIwhhVbFcDjMNIQUkpywuHjHSmILqqYcGxpEeZhZ"

consumer = oauth.Consumer(consumer_key, consumer_secret)

token = oauth.Token(key=oauth_token,
        secret=oauth_token_secret)
discogsclient = oauth.Client(consumer, token)

resp, value = discogsclient.request('https://api.discogs.com//users/emptemp/collection/value')
if resp['status'] != '200':
    sys.exit('Invalid API response {0}.'.format(resp['status']))

pvalue = json.loads(value)
print pvalue['minimum']
print pvalue['median']
print pvalue['maximum']
with open('data.txt', 'a') as outfile:
	outfile.write(str(date.today()))
	outfile.write("\t")
	json.dump(value, outfile, ensure_ascii=False)
	outfile.write("\n")
outfile.close()
