from sys import argv
import urllib2
import json

script, filename = argv


packageName = 'com.ea.games.r3_row'      # package com.whatsapp for WhatsApp
apiKey      = '632d8213e75114849070c80c16b4dcd5'  # your API key

url = 'http://api.playstoreapi.com/v1.1/apps/{0}?key={1}'

response = urllib2.urlopen(url.format(packageName, apiKey))

data = json.load(response)   

ls = data['topReviews']

target=open(filename, 'w')

target.truncate()


for i, test in enumerate(ls):
		target.write(test['reviewText'])
		target.write("\n")
		
target.close()
		