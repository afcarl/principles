import json, sys, datetime
import requests

URL = "https://nycopendata.socrata.com/views/"

r = requests.get(URL + sys.argv[1])

#with open(sys.argv[1]) as f:
#    j = json.load(f)
    
print datetime.datetime.fromtimestamp(r.json()['createdAt'])