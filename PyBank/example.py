import os
import csv

file_path = os.path.join('raw_data', 'budget_data_1.csv')

#file_path = 'raw_data/budget_data_1.csv'
# initialize variables to store information
months = 0
revenue = 0

with open(file_path) as csvfile:
	# read the csv as a dictionary
	reader = csv.DictReader(csvfile)

	# loop through each row inside the csv file
	for row in reader:
		months += 1

		print('***********************************')
		print(row["Date"])
		print(row["Revenue"])


print("the total number of months recorded: ", months)