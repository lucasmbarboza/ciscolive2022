# for i in {000000000000001..20}
# do
#     curl -X POST --data-binary @- -H 'Content-Type: application/json' -H 'Accept: application/json' ${telemetry}/api/telemetry <<END_OF_TRACE
DTRACE=[{
   "requestID": "bla",
   "scheme": "http",
   "destinationAddress": "32.45.66.51:8000",
   "destinationNamespace": "XXXDESTNAMESPACEXXX",
   "sourceAddress": "10.116.207.197:8000",
   "request": {
     "method": "GET",
     "path": "/pet/0000000000",
     "host": "petstore.com",
     "common": {
       "version": "1",
       "time": 0,
       "headers": [
       ],
       "body": "",
       "TruncatedBody": False
     }
   },
   "response": {
     "statusCode": "200",
     "common": {
       "time": 0,
       "version": "1",
       "headers": None,
       "body": "eyJjdnNzIjpbeyJzY29yZSI6Ny44LCJ2ZWN0b3IiOiJBVjpML0FDOkwvUFI6Ti9VSTpSL1M6VS9DOkgvSTpIL0E6SCJ9XX0=",
       "TruncatedBody": False
     }
   }
 }]
# END_OF_TRACE
# done 

#### Weak Basic Auth, SHORT and KNOWN password
FTRACES = [
 {"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":"","sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/weakbasicauth/SHORT_AND_KNOWN","host":"traceanalyzer.test.example.com","common":{"version":"","time": 0,"headers":[{"key":"authorization", "value":"Basic dXNlcjE6cGFzcw=="}],"body":"","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},
 #### Weak Basic Auth, KNOWN password
 {"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":"","sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/weakbasicauth/KNOWN","host":"traceanalyzer.test.example.com","common":{"version":"","time": 0,"headers":[{"key":"authorization", "value":"Basic dXNlcjE6bG9uZ2xvbmdsb25n"}],"body":"","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},


# #### Weak Basic Auth, SAME password

{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":"","sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/weakbasicauth/SAME","host":"traceanalyzer.test.example.com","common":{"version":"","time": 0,"headers":[{"key":"authorization", "value":"Basic dXNlcjE6cGFzc3dvcmRtb3JldGhhbjg="}],"body":"","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},


{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":"","sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/weakbasicauth/SAME","host":"traceanalyzer2.test.example.com","common":{"version":"","time": 0,"headers":[{"key":"authorization", "value":"Basic dXNlcjE6cGFzc3dvcmRtb3JldGhhbjg="}],"body":"","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},


{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":"","sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/weakbasicauth/SAME","host":"traceanalyzer3.test.example.com","common":{"version":"","time": 0,"headers":[{"key":"authorization", "value":"Basic dXNlcjE6cGFzc3dvcmRtb3JldGhhbjg="}],"body":"","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},


# #### JWT_NO_EXPIRE_CLAIM
#
{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":"","sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/weakjwt/NO_EXPIRE_CLAIM","host":"traceanalyzer.test.example.com","common":{"version":"","time": 0,"headers":[{"key":"authorization", "value":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIn0.Q6CM1qIz2WTgTlhMzpFL8jI8xbu9FFfj5DY_bGVY98Y"}],"body":"","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},
# 

# #### JWT_SENSITIVE_CONTENT_IN_CLAIMS
#
{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":"","sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/weakjwt/JWT_SENSITIVE_CONTENT_IN_CLAIMS","host":"traceanalyzer.test.example.com","common":{"version":"","time": 0,"headers":[{"key":"authorization", "value":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjowLCJwYXNzd29yZCI6ImJsYSJ9.HoI84Px0J9oVujFgBvY42PF9xaBz0xCDJzuono4qo40"}],"body":"","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},
# 

# #### JWT_NO_ALG_FIELD
#
{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":"","sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/weakjwt/JWT_NO_ALG_FIELD","host":"traceanalyzer.test.example.com","common":{"version":"","time": 0,"headers":[{"key":"authorization", "value":"Bearer eyJ0eXAiOiJKV1QifQ.eyJsb2dnZWRJbkFzIjoiYWRtaW4iLCJpYXQiOjE0MjI3Nzk2Mzh9.HoI84Px0J9oVujFgBvY42PF9xaBz0xCDJzuono4qo40"}],"body":"","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},
# 

# #### JWT_SENSITIVE_CONTENT_IN_CLAIMS
#
{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":"","sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/weakjwt/JWT_SENSITIVE_CONTENT_IN_CLAIMS","host":"traceanalyzer.test.example.com","common":{"version":"","time": 0,"headers":[{"key":"authorization", "value":"Bearer eyJ0eXAiOiJKV1QifQ.eyJsb2dnZWRJbkFzIjoiYWRtaW4iLCJpYXQiOjE0MjI3Nzk2Mzh9.HoI84Px0J9oVujFgBvY42PF9xaBz0xCDJzuono4qo40Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzc24iOiI5OTk5IiwiaXAiOiIxOTIuMS4xLjEiLCJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.bySqmwlwljWpXLWZ4jlkb_ST3VtuPK2Sui79jkGUEIE"}],"body":"","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},
# 

# #### JWT_SENSITIVE_CONTENT_IN_HEADERS_AND_CLAIMS
#
{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":"","sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/weakjwt/JWT_SENSITIVE_CONTENT_IN_HEADERS_AND_CLAIMS","host":"traceanalyzer.test.example.com","common":{"version":"","time": 0,"headers":[{"key":"authorization", "value":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImNvdmlkX3Bvc2l0aXZlIjp0cnVlfQ.eyJzc24iOiI5OTk5IiwiaXAiOiIxOTIuMS4xLjEiLCJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.kiDLC2Kl-3diNJ_8k-LAdQpNjWmPzmJ1YXvh-p2J9T4"}],"body":"","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},
# 

# #### JWT_WEAK_SYMETRIC_SECRET, JWT_NOT_RECOMMENDED_ALG
#
{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":"","sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/weakjwt/JWT_WEAK_SYMETRIC_SECRET_JWT_NOT_RECOMMENDED_ALG", "host":"traceanalyzer.test.example.com","common":{"version":"","time": 0,"headers":[{"key":"authorization", "value":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjowfQ.uzPFbqIJ2akC2gmGxN3KlXU_zhMFvE__N5kKwejY19reMaDaaDT21hmy1mMCZZY2"}],"body":"","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},
# 

# #### JWT_WEAK_SYMETRIC_SECRET_JWT_EXP_TOO_FAR
#
{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":"","sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/weakjwt/JWT_WEAK_SYMETRIC_SECRET_JWT_EXP_TOO_FAR", "host":"traceanalyzer.test.example.com","common":{"version":"","time": 0,"headers":[{"key":"authorization", "value":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiZXhwIjo5OTk5OTk5OTk5fQ.X5NwJulKmNzdC2vW9J1UOMsaKikgzQbmFBWslfDNqZE"}],"body":"","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},


# #### JWT_WEAK_SYMETRIC_SECRET_JWT_SENSITIVE_CONTENT_IN_CLAIMS_JWT_NOT_RECOMMENDED_ALG_JWT_EXP_TOO_FAR
#
{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":"","sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/weakjwt/JWT_WEAK_SYMETRIC_SECRET_JWT_SENSITIVE_CONTENT_IN_CLAIMS_JWT_NOT_RECOMMENDED_ALG_JWT_EXP_TOO_FAR", "host":"traceanalyzer.test.example.com","common":{"version":"","time": 0,"headers":[{"key":"authorization", "value":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiZXhwIjo5OTk5OTk5OTk5OSwicGFzc3dvcmQiOiJibGEifQ.tCIFaW7882WmxIGednahpwN-1jEqOkkwgS0W1x5F35psVTACPcpbPw-P8K9CfQM3"}],"body":"","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},
# 


# #### JWT_WEAK_SYMETRIC_SECRET_JWT_SENSITIVE_CONTENT_IN_CLAIMS_JWT_EXP_TOO_FAR
#
{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":"","sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/weakjwt/JWT_WEAK_SYMETRIC_SECRET_JWT_SENSITIVE_CONTENT_IN_CLAIMS_JWT_EXP_TOO_FAR", "host":"traceanalyzer.test.example.com","common":{"version":"","time": 0,"headers":[{"key":"authorization", "value":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiZXhwIjo5OTk5OTk5OTk5OSwicGFzc3dvcmQiOiJibGFibHUifQ.SLWwRavOnos1ihyRJUPeG3xjKRy8eIBvUOD6VqW20WU"}],"body":"","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},
# 


{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":"","sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/pet/321654","host":"petstore.com","common":{"version":"","time": 0,"headers":[],"body":"eyJjdnNzIjpbeyJzY29yZSI6Ny44LCJ2ZWN0b3IiOiJBVjpML0FDOkwvUFI6Ti9VSTpSL1M6VS9DOkgvSTpIL0E6SCJ9XX0=","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},



{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":None,"sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/user/john","host":"petstore.com","common":{"version":None,"time": 0,"headers":[],"body":"eyJjdnNzIjpbeyJzY29yZSI6Ny44LCJ2ZWN0b3IiOiJBVjpML0FDOkwvUFI6Ti9VSTpSL1M6VS9DOkgvSTpIL0E6SCJ9XX0=","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},



{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":None,"sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/carts/2021/pet/20","host":"petstore.com","common":{"version":None,"time": 0,"headers":[],"body":"eyJjdnNzIjpbeyJzY29yZSI6Ny44LCJ2ZWN0b3IiOiJBVjpML0FDOkwvUFI6Ti9VSTpSL1M6VS9DOkgvSTpIL0E6SCJ9XX0=","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},



{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":None,"sourceAddress":"10.116.207.197:8000","request":{"method":"DELETE","path":"/pet/65321","host":"petstore.com","common":{"version":None,"time": 0,"headers":[],"body":"eyJjdnNzIjpbeyJzY29yZSI6Ny44LCJ2ZWN0b3IiOiJBVjpML0FDOkwvUFI6Ti9VSTpSL1M6VS9DOkgvSTpIL0E6SCJ9XX0=","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},



{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":None,"sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/auth/21654","host":"petstore.com","common":{"version":None,"time": 0,"headers":[],"body":"eyJjdnNzIjpbeyJzY29yZSI6Ny44LCJ2ZWN0b3IiOiJBVjpML0FDOkwvUFI6Ti9VSTpSL1M6VS9DOkgvSTpIL0E6SCJ9XX0=","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},



{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":None,"sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/pet/10231/name","host":"petstore.com","common":{"version":None,"time": 0,"headers":[],"body":"eyJjdnNzIjpbeyJzY29yZSI6Ny44LCJ2ZWN0b3IiOiJBVjpML0FDOkwvUFI6Ti9VSTpSL1M6VS9DOkgvSTpIL0E6SCJ9XX0=","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},



{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":None,"sourceAddress":"10.116.207.197:8000","request":{"method":"PUT","path":"/users/john","host":"petstore.com","common":{"version":None,"time": 0,"headers":[],"body":"eyJjdnNzIjpbeyJzY29yZSI6Ny44LCJ2ZWN0b3IiOiJBVjpML0FDOkwvUFI6Ti9VSTpSL1M6VS9DOkgvSTpIL0E6SCJ9XX0=","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}},


{"requestID":"req-id","scheme":"http","destinationAddress":"32.45.66.51:8000","destinationNamespace":None,"sourceAddress":"10.116.207.197:8000","request":{"method":"GET","path":"/carts/99874","host":"petstore.com","common":{"time": 0,"version":"1","headers":[],"body":"eyJjdnNzIjpbeyJzY29yZSI6Ny44LCJ2ZWN0b3IiOiJBVjpML0FDOkwvUFI6Ti9VSTpSL1M6VS9DOkgvSTpIL0E6SCJ9XX0=","TruncatedBody":False}},"response": {"statusCode": "200", "common": {"time": 0, "version": "1", "headers": None, "body": "", "TruncatedBody": False}}}
]