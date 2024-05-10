import os
import csv

# Path to collect data from the Resources folder.
budget_csv = os.path.join('Resources', 'budget_data.csv')

def make_dict():
	# Read in the CSV file
	with open(budget_csv, "r") as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',') # Split the data on commas

		next(csvreader) #Skip the header row.
		budg_dict = {row[1]: row[0] for row in csvreader} #Add all the CSV file data into this dictionary.

	return budg_dict