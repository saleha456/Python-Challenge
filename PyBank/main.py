import os
import csv


#Specify the filepath of input and output files
csvpath = os.path.join("Resources","budget_data.csv")
output_path = os.path.join("Analysis","Financial Analysis.txt")

# Lists to store data
month = []
profitloss = []
profitchange = []


#Set initial value of monthly change to 0
profit1 = 0
profit2 = 0


#Read the data
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
	next(csvreader) #skip header


	#Append data from each row to all 3 lists
	for row in csvreader:
		month.append(row[0])
		profitloss.append(int(row[1]))

		
		#calculate profit/loss change from previous month	
		profit2 = int(row[1])
		change = profit2 - profit1
		profitchange.append(change)
		profit1 = profit2   



# Calculate Total Profit	
netprofitloss = sum(profitloss)

# Calculatee Total Number of Months 
totalmonths = len(month)

# Get Min and Max value from Profit Change list
greatestincrease = max(profitchange)
max_index = profitchange.index(greatestincrease)
max_month = month[max_index]

greatestdecrease = min(profitchange)
min_index = profitchange.index(greatestdecrease)
min_month = month[min_index]


# Calculate Average Change in Profit ########################
#Replace first value/index in ProfitChange list with 0 
#Divide the sum of ProfitChange list by Total Number of Months (exluding first month)
profitchange[0] = 0
num_rows = totalmonths - 1
averagechange = round(float(sum(profitchange) / num_rows),2)


# Write out analysis to be printed

summary_analysis = (
	"Financial Analysis \n"
	"----------------------------\n"
	f"Total Months: {totalmonths}\n"
	f"Total: ${netprofitloss}\n"
	f"Average Change: ${averagechange} \n"
	f"Greatest Increase in Profits: {max_month} (${greatestincrease})\n"
	f"Greatest Decrease in Profits: {min_month} (${greatestdecrease})\n"
	)


# Print Analysis to Terminal
print(summary_analysis)


# Save analysis as text file
output_file = open(output_path,'w')
output_file.write(summary_analysis)
