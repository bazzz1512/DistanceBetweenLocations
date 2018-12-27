import requests
import geopy.distance


Cities = input("Input the cities, seperated with a comma: ").split(",")
ApiKey = input("Input the API Key of google GeoCoder: ")
listParams = []
for x in range(0,2):
    listParams.append({'address': Cities[x], "key": ApiKey})

url = 'https://maps.googleapis.com/maps/api/geocode/json'
listLocations = []
for x in range(0,2):
    y = requests.get(url, params=listParams[x]).json()['results'][0]['geometry']['location']
    listLocations.append((y['lat'], y['lng']))

print(geopy.distance.distance(listLocations[0], listLocations[1]).km)
