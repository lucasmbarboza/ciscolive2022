import math
import random
import requests
import json
import uuid
import datetime
import sys
import time
from time import sleep

class ApiClarityClient(object):
	def __init__(self, apiurl, internalurl):
		self._apiurl = apiurl
		self._internalurl = internalurl
		self._session = None
	 
	def _api_url(self, url):
		return self._apiurl + url
	
	def _internal_url(self, url):
		return self._internalurl + url
  
	def get_inventory_item(self, apiId):
		rep = requests.get(self._api_url(f"/apiInventory/{apiId}"))
		if rep.status_code >= 200 < 300: b = rep.json()
		else: b = rep.text
		
		print(f"inventory:{rep} {b}")
		
	def post_trace(self, source, destination, method, path, reqtime, reptime):
		payload = json.dumps({
			"requestID": f"{uuid.uuid4()}",
			"scheme": "http",
			"destinationAddress": destination,
			"destinationNamespace": "XXXDESTNAMESPACEXXX",
			"sourceAddress": source,
			"request": {
				"method": method,
				"path": path,
				"host": "www.httpbin.org:8000",
				"common": {
					"time": 1000 * int(time.mktime(reqtime.timetuple())),  #.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
					"version": "1",
					"headers": [],
					"body": "",
					"TruncatedBody": False
				}
			},
			"response": {
				"statusCode": "200",
				"common": {
					"time": 1000 * int(time.mktime(reptime.timetuple())),  #.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
					"version": "1",
					"headers": None,
					"body": "",
					"TruncatedBody": False
				}
			}
		})
		headers = {
			'Content-Type': 'application/json'
		}
		r = requests.post(self._internal_url("/telemetry"), headers=headers, data=payload)
		
		if r.status_code >= 200 and r.status_code < 300:
			b = r.json()
		else:
			b = r.text
		
		print(f"{reqtime} {reptime} trace:{r} {b}")
def get_api_id(api_url,api_name): 
	headers = {
		'Content-Type': 'application/json; charset=utf-8'
	}
	r = requests.get(api_url+":30002/api/apiInventory?type=EXTERNAL&page=1&pageSize=10&sortKey=name&sortDir=ASC", headers=headers)
	if r.status_code >= 200 and r.status_code < 300: 
		b = r.json()
	
		for i in b["items"]:
			if i["name"] == api_name:
				return i["id"]
	else: 
		print(r)
		return -1
def reqpersec(sec): # Taxa de requisicoes per second
	freq = 0.5
	offset = 20
	amplitude = 10
	
	reqpersec = int(round(amplitude * math.sin(freq*sec) + offset))
	reqpersec += random.randint(int(-0.05*reqpersec), int(0.05*reqpersec))
	if reqpersec <= 0: reqpersec = 0
	return reqpersec

def generate_trace(apiclarity_base, apiId):
	now = datetime.datetime.now()
	minutes = 2
	print(f"{apiclarity_base}")
	client = ApiClarityClient(f"{apiclarity_base}:30002/api", f"{apiclarity_base}:30003/api")
	source = "10.1.1.1:3333"
	destination = "101.22.2.32:8080"
	method = "GET"
	path = "/api/dashboard/apiUsage/mostUsed"
	
	reqtime = now - datetime.timedelta(hours=1, minutes=minutes, seconds=1)
	reptime = reqtime + datetime.timedelta(milliseconds=233)
	
	for sec in range(minutes*60):
		nreq = reqpersec(sec)
		if nreq == 0:
			reqtime += datetime.timedelta(seconds=1)
			continue
		delta = int(round(1000 / nreq))
		for r in range(nreq):
			art = getrtime(sec)
			if sec > minutes*60 - 3:
				art = art*5
			reptime = reqtime + datetime.timedelta(milliseconds=random.randint(art-50, art+50)) # Variacao do tempo de requisicoes
			client.post_trace(source, destination, method, path, reqtime=reqtime, reptime=reptime)
			reqtime += datetime.timedelta(milliseconds=delta)
	print(reqtime,reptime)
def getrtime(sec):
	return 3*sec+100

if __name__ == "__main__":
	APICLARITY_URL = 'http://198.18.133.10'
	apiId = get_api_id(APICLARITY_URL,"www.httpbin.org")
	generate_trace(APICLARITY_URL, apiId)
	exit_code = '0'
	while (not exit_code =='q'):
		exit_code = input("Press q to exit")
