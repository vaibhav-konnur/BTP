import csv

def get_data():
	input_file = csv.DictReader(open("cars.csv"))
	data_list = []
	for row in input_file:
		data_list.append(row)

	return data_list	