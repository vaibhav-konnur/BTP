import csv

def get_data():
	input_file = csv.DictReader(open("cars.csv"))
	data_list = []
	for row in input_file:
		data_list.append(row)

	return data_list

# print(data_list[3]['Origin'])

# print(type(data_list))

# print(type(data_list[2]))