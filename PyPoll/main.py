import os
import csv
from collections import Counter


# Specify the filepath of input and output files
csvpath = os.path.join("Resources","election_data.csv")
output_path = os.path.join("Analysis","Polling Analysis.txt")


# Lists to store data
voterid = []
candidate = []

# Assign variables for candidate names
candidate1 = "Khan"
candidate2 = "Correy"
candidate3 = "Li"
candidate4 = "O'Tooley"


# Read data from file
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
	next(csvreader) #skip header


	# Append data from each row to lists
	for row in csvreader:
		voterid.append(row[0])
		candidate.append(row[2])


# Get the Total Number of Votes
total_votes = len(voterid)


# Get Total Votes per Candidate
candidate_votes = Counter((candidate))

candidate1_results = candidate_votes[candidate1]
candidate1_perc	= "{:.3%}".format(candidate1_results / total_votes)

candidate2_results = candidate_votes[candidate2]
candidate2_perc	= "{:.3%}".format(candidate2_results / total_votes)

candidate3_results = candidate_votes[candidate3]
candidate3_perc	= "{:.3%}".format(candidate3_results / total_votes)

candidate4_results = candidate_votes[candidate4]
candidate4_perc	= "{:.3%}".format(candidate4_results / total_votes)



# Determine the winner

key_list = list(candidate_votes.keys())
val_list = list(candidate_votes.values())
winner_votes = max(val_list)
winner_index = val_list.index(winner_votes)
winner_name = key_list[winner_index]



# Write out Summary Analysis

summary_analysis = (
	"Election Results \n"
	"----------------------------\n"
	f"Total Votes: {total_votes}\n"
	"----------------------------\n"
	f"{candidate1}: {candidate1_perc} ({candidate1_results}) \n"
	f"{candidate2}: {candidate2_perc} ({candidate2_results}) \n"
	f"{candidate3}: {candidate3_perc} ({candidate3_results}) \n"
	f"{candidate4}: {candidate4_perc} ({candidate4_results}) \n"
	"----------------------------\n"
	f"Winner: {winner_name}\n"
	"----------------------------\n"
	)


# Print Summary Analysis to Terminal
print(summary_analysis)



# Save Analysis as Text File
output_file = open(output_path,'w')
output_file.write(summary_analysis)

