import os
import csv
#import counter



#Specify the filepath of input and output files
csvpath = os.path.join("Resources","election_data.csv")
output_path = os.path.join("Analysis","Analysis.txt")


# Lists to store data
voterid = []
county = []
candidate = []


#Read data from file
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
	next(csvreader) #skip header


	#Append data from each row to all 3 lists
	for row in csvreader:
		voterid.append(row[0])
		county.append(row[1])
		candidate.append(row[2])



total_votes = len(voterid)


# Save analysis as text file
output_file = open(output_path,'w')
output_file.write(
	"Election Results \n"
	"----------------------------\n"
	f"Total Votes: {total_votes}\n"
	"----------------------------\n"
	#f"Total: ${netprofitloss}\n"
	#f"Average Change: ${averagechange} \n"
	#f"Greatest Increase in Profits: {max_month} (${greatestincrease})\n"
	#f"Greatest Decrease in Profits: {min_month} (${greatestdecrease})\n"

	)




#cnt = Counter()
#>>> for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
#...     cnt[word] += 1
#>>> cnt
#Counter({'blue': 3, 'red': 2, 'green': 1})