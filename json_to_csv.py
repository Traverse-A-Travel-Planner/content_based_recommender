# Python program to convert
# JSON file to CSV


import json
import csv


with open('src\location_recommender\dataset\places.json') as json_file:
	data = json.load(json_file)

place_data = data['place_details']

data_file = open('src\location_recommender\dataset\places.csv', 'w')

csv_writer = csv.writer(data_file)

count = 0

for place in place_data:
	if count == 0:
		header = place.keys()
		csv_writer.writerow(header)
		count += 1
	csv_writer.writerow(place.values())

data_file.close()
