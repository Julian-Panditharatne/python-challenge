import os
import csv

# Set up relative Paths; code sourced from colleague Thet Win on 02-ask-the-class channel of Slack.
cwd = os.path.abspath(__file__)
dir_name=os.path.dirname(cwd)
election_data_csv = os.path.join(dir_name, 'Resources', 'election_data.csv') # Path to collect data from the Resources folder.
results_txt = os.path.join(dir_name,'analysis', 'results.txt') # Path to outputting results file in the analysis folder

# A function that extracts all the necessary information and statistics from the poll data set and stores it in a dictionary, integer, and string.
def get_votes_dict():
	# Initialize the dictionary, integer, and string here, so that they remain after the relevant information from the CSV file has been read and copied into the dictionary and the necesssary calculations are made and stored in a (dictionary, integer, and string) tuple.
	vote_results = {} 
	total = 0
	winner = ""
	# Read in the CSV file
	with open(election_data_csv, "r") as elections:
		ElectionData = csv.reader(elections, delimiter=',') # Split the data on commas.
		next(ElectionData) # Skip the header row.
		votes = [row[2] for row in ElectionData] # Get a copy of the "Candidate" column in election_data.csv, without the header, in order to count the total votes cast and the total votes each candidate won.
		candidates = {row for row in votes} # Get a set of all the candidates who received votes from the votes list.
		vote_results = {candidate: votes.count(candidate) for candidate in sorted(candidates)} # The dictionary now has each candidate as a key and its associated value as the total votes the candidate won.
		# NOTE: It is assumed here that only one candidate has the popular vote.
		# Code sourced from https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary?page=1&tab=scoredesc#tab-top
		winner = list(vote_results.keys())[list(vote_results.values()).index(max(list(vote_results.values())))] # Find the key, i.e., candidate name, that is associated with the maximum value, i.e., the popular vote, in the dictionary and store it in winner variable.
		total = len(votes) # Add the total votes cast into the total variable.
	return (vote_results, total, winner)

Vote_Results, Total, Winner = get_votes_dict() # Unpack tuple and store the values in these variables.

# Store the output in a list that will then get printed on the terminal and then written to a text file.
results = []
results.append("Election Results\n-------------------------\n")
results.append(f"Total Votes: {Total}\n-------------------------\n")
for candidate, vote_count in Vote_Results.items():
	results.append(f"{candidate}: {round(((vote_count/Total)*100),3)}% ({vote_count})\n")
results.append(f"-------------------------\nWinner: {Winner}\n-------------------------\n")

for line in results:
	print(line)

with open(results_txt, "w") as wtxt:
	wtxt.writelines(results)