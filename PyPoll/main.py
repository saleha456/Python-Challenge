import os
import csv
from collections import Counter

os.system('clear')

# Specify the filepath of input and output files
csvpath = os.path.join("Resources","election_data.csv")
output_path = os.path.join("Analysis","Analysis.txt")


# Lists to store data
voterid = []
county = []
candidate = []

# Assign candidate names as variables
candidate1 = "Khan"
candidate2 = "Correy"
candidate3 = "Li"
candidate4 = "O'Tooley"


# Read data from file
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
	next(csvreader) #skip header


	#Append data from each row to all 3 lists
	for row in csvreader:
		voterid.append(row[0])
		county.append(row[1])
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
winner = candidate_votes.most_common(1)


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
	f"Winner: {winner}\n"
	"----------------------------\n"
	)


# Print Summary Analysis
print(summary_analysis)



# Save Analysis as Text File
output_file = open(output_path,'w')
output_file.write(summary_analysis)

