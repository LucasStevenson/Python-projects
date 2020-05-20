import requests
import sys
import json

if len(sys.argv) == 1:
    print("You need to provide an IP the an argument\nUsage: python3 ipgeolocator.py IPADDRESS")
    exit()

IP = sys.argv[1]

r = requests.get("http://ip-api.com/json/" + IP)
responseObj = r.json()
if responseObj["status"] == "success":
    filteredData = {}
    r_info = ["query", "country", "regionName", "city", "zip", "lat", "lon", "timezone", "isp"]
    for i in r_info:
        filteredData[i] = responseObj[i]
    filteredData["Google Maps"] = "https://www.google.com/maps/@" + str(responseObj["lat"]) + "," + str(responseObj["lon"]) + ",14z"
    print(json.dumps(filteredData, indent=2))

else:
    print(json.dumps(responseObj, indent=2))
