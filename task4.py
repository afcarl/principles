import json, sys, datetime, csv
import requests

URL = "https://nycopendata.socrata.com/views/"

r = requests.get(URL + sys.argv[1])

with open(sys.argv[1]) as f:
    j = json.load(f)

with open(sys.argv[2], 'wb') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(['Name', 'Lon', 'Lat'])
    for station in j['stationBeanList']:
        if station['statusKey'] != 1 and "Coming soon" in station['stationName']:
            csvwriter.writerow([station['stationName'], station['longitude'], station['latitude']])