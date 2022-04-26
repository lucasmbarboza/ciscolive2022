from traces import FTRACES, DTRACE
import requests
import json
import datetime
import uuid
import time
from time import sleep


def generate_trace_analysis(api_url, trace): 	
	headers = {
		'Content-Type': 'application/json; charset=utf-8'
	}
	r= requests.post( "{}:30003/api/telemetry".format(api_url), headers=headers,  data=trace)
	if r.status_code >= 200 and r.status_code < 300:
		print( r)
		return 0
	else:
		return r.status_code 

if __name__== '__main__':
	APICLARITY_URL = 'http://198.18.133.10'

	for i in FTRACES:
		now = datetime.datetime.now()
		reqtime = now
		reptime = now + datetime.timedelta(milliseconds=200)
		trace = i
		trace["requestID"] = f"{uuid.uuid4()}"
		trace["request"]["common"]["time"] = 1000 * int(time.mktime(reqtime.timetuple()))
		trace["response"]["common"]["time"] = 1000 * int(time.mktime(reptime.timetuple()))
		debug = generate_trace_analysis(APICLARITY_URL,json.dumps(trace))
	if debug == 0: 
		print( 'Success !!')
	exit_code = '0'
	while (not exit_code =='q'):
		exit_code = input("Type q to exit: ")
