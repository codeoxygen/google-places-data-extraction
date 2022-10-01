import googlemaps
import pandas as pd
import pprint

apiKey = open('API.txt').read()

client_ = googlemaps.Client(apiKey)
response = client_.places('pumps in india')

print(response['results'][0].keys())

