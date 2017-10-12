import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

try:
	file = sys.argv[1]
	myfile = open(file, "r")
	for url in myfile:
		try:
                        url = url.strip("\n")
                        s = requests.Session()

                        if (url[0:4] == "www."):
                                url1 = "http://" + url + "//yahoo.com/%2F.."
                		url2 = "http://" + url + "//yahoo.com/%2F.."
                        	request = s.head(url1)
                        	req = s.head(url2, verify=False)
                        	print url1, "->",  request.status_code
                        	print url2, "->", req.status_code
                	elif (url[0:7] == "http://"):
                        	url1 = url + "//yahoo.com/%2F.."
                                request = s.head(url1)
                        	print url1, "->",  request.status_code
                	elif (url[0:8] == "https://"):
                        	url2 = url + "//yahoo.com/%2F.."
                        	req = s.head(url2, verify=False)
                        	print url2, "->", req.status_code
                        else:
                                url1 = "http://" + url + "//yahoo.com/%2F.."
                		url2 = "https://" + url + "//yahoo.com/%2F.."
                                request = s.head(url1)
                        	req = s.head(url2, verify=False)
                        	print url1, "->",  request.status_code
                        	print url2, "->", req.status_code

                except:
                        continue

except EOFError:
