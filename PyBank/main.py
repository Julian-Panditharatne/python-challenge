import os
import csv

# Path to collect data from the Resources folder.
budget_csv = os.path.join('Resources', 'budget_data.csv')

# A function that converts the CSV version of the financial dataset into a Dictionary.
def make_dict():
	budg_dict = {} # Initialize the dictionary here so that it remains after CSV file has been read and copied into it.
	# Read in the CSV file
	with open(budget_csv, "r") as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',') # Split the data on commas.
		next(csvreader) #Skip the header row.
		budg_dict = {int(row[1]): row[0] for row in csvreader} # Add all the CSV file data into this dictionary whose keys are "Profit/Losses"-values and values are "Date"-values.

	return budg_dict

budget = make_dict() # Call the function to get the dictionary version of the financial dataset.
profit_losses = list(budget) # Get a list of keys in budget, which are just the values in "Profit/Losses" column.
changes_in_profit_losses = [profit_losses[i]-profit_losses[i-1] for i in range(1, len(profit_losses))] # Get a list of the changes in "Profit/Losses" over the entire period.

total_months = len(budget) # Calculate the Total months - i.e., the number of rows in budget_data.csv, which is just the amount of items in the dictionary.
Profits_N_Losses = sum(profit_losses) # Calculate net total amount of "Profit/Losses" over the entire period - i.e., the sum of all the values in "Profit/Losses" column.
Average_Change = sum(changes_in_profit_losses) / total_months # Calculate the average change in the "Profit/Losses" over the entire period.
max_profits = max(profit_losses) # Calculate the greatest increase/decrease in profits amounts
min_losses = min(profit_losses)
max_prof_date = budget[max_profits] # Get the greatest increase/decrease in profits dates.
min_loss_date = budget[min_losses]

results = []
results.append("Financial Analysis\n----------------------------\n")
results.append(f"Total Months: {total_months}\n")
results.append(f"Total: ${Profits_N_Losses}\n")
results.append(f"Average Change: ${Average_Change}\n")
results.append(f"Greatest Increase in Profits: {max_prof_date} (${max_profits})\n")
results.append(f"Greatest Decrease in Profits: {min_loss_date} (${min_losses})\n")

for line in results:
	print(line)

with open(os.path.join('analysis', 'results.txt'), "w") as wtxt:
	wtxt.writelines(results)