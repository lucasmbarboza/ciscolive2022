import math
import random
import requests
import json
import uuid
import datetime
import sys
import time
from time import sleep

def generate_trace_analysis(api_url, trace): 	
	headers = {
		'Content-Type': 'application/json; charset=utf-8'
	}
	r= requests.post( "{}:30003/api/telemetry".format(api_url), headers=headers,  data=trace)
	if r.status_code >= 200 and r.status_code < 300:
		print(r, 'Resquest successful')
		return 0
	else:
		return r.status_code

if __name__== '__main__':
	# Cria a primeira trace
	APICLARITY_URL = 'http://198.18.133.10'
	now = datetime.datetime.now()
	source = "10.1.1.1:3333"
	destination = "101.22.2.32:8080"
	method = "GET"
	path = "/api/dashboard/apiUsage/mostUsed"
	reqtime = now - datetime.timedelta(milliseconds=100)
	reptime = now 

	first_trace = json.dumps({
		"requestID": f"{uuid.uuid4()}",
		"scheme": "http",
		"destinationAddress": "32.45.66.51:8000",
		"destinationNamespace": "XXXDESTNAMESPACEXXX",
		"sourceAddress": "10.116.207.197:8000",
		"request": {
			"method": "GET",
			"path": "/pet/000000000010",
			"host": "petstore.com",
			"common": {
			"version": "1",
			"time": 1000 * int(time.mktime(reqtime.timetuple())),
			"headers": [
				{
				"key": "authorization",
				"value": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjowfQ.i6i-xl0NxSyZBWVm-KFlqLN70w-QfRro5X2c1oTxSxfs_3OROBGdywHZMtgSpl2M"
				}
			],
			"body": "",
			"TruncatedBody": False
			}
		},
		"response": {
			"statusCode": "200",
			"common": {
			"time":  1000 * int(time.mktime(reptime.timetuple())),
			"version": "1",
			"headers": None,
			"body": "eyJjdnNzIjpbeyJzY29yZSI6Ny44LCJ2ZWN0b3IiOiJBVjpML0FDOkwvUFI6Ti9VSTpSL1M6VS9DOkgvSTpIL0E6SCJ9XX0=",
			"TruncatedBody": False
			}
			}
		}
	)
   
	second_trace = json.dumps({
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
		}
	)
	exit_code = '0'
	while (not exit_code =='q'):
		generate_trace_analysis(APICLARITY_URL,first_trace)
		generate_trace_analysis(APICLARITY_URL,second_trace)
		exit_code = input("Type q to exit: ")