import os
import csv

# Set up relative Paths; code sourced from colleague Thet Win on 02-ask-the-class channel of Slack.
cwd = os.path.abspath(__file__)
dir_name=os.path.dirname(cwd)
election_data_csv = os.path.join(dir_name, 'Resources', 'election_data.csv') # Path to collect data from the Resources folder.
results_txt = os.path.join(dir_name,'analysis', 'results.txt') # Path to outputting results file in the analysis folder

# A function that extracts all the necessary information and statistics from the poll data set and stores it in a dictionary.
def get_votes_dict():
	vote_results = {} # Initialize the dictionary here, so that it remains after the relevant information from the CSV file has been read and copied into it and the necesssary calculations are made and stored in it.
	# Read in the CSV file
	with open(election_data_csv, "r") as elections:
		ElectionData = csv.reader(elections, delimiter=',') # Split the data on commas.
		next(ElectionData) # Skip the header row.
		candidates = [row[2] for row in ElectionData if row[2] not in candidates] # Get a list of all the candidates who received votes from the "Candidate" column in election_data.csv.
		votes = [row[2] for row in ElectionData] # Get a copy of the "Candidate" column in election_data.csv, without the header, in order to count the total votes cast and the total votes each candidate won.
		vote_results = {candidate: votes.count(candidate) for candidate in sorted(candidates)} # The dictionary now has each candidate as a key and its associated value as the total votes the candidate won.
		vote_results['Total'] = len(votes) # Add the total votes cast into the dictionary as a value of key 'Total'.
		vote_results['Winner'] = list(vote_results.keys())[list(vote_results.values()).index(max(list(vote_results.values())))] # Code ssourced from https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary?page=1&tab=scoredesc#tab-top
	return vote_results

Vote_Results = get_votes_dict()


results = []
results.append("Election Results\n-------------------------\n")
