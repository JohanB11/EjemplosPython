#!/usr/bin/env python
#_*_ coding: utf8 _*_

import urllib
import json

def main():
	#url = "https://ipinfo.io/186.28.29.40/json"
	url = "https://ipinfo.io/172.217.9.4/json"
	v = urllib.urlopen(url)
	j = json.loads(v.read())

	for dato in j:
		print(dato + " : " + j[dato])

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()