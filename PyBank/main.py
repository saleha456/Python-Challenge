import os
import csv

os.system('clear')

#Specify the filepath of input and output files
csvpath = os.path.join("Resources","budget_data.csv")
output_path = os.path.join("Analysis","Analysis.csv")

# Lists to store data
month = []
profitloss = []


#Read the data
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')

	csv_header = next(csvreader)
	print(f"CSV Header: {csv_header}")

	for row in csvreader:

		print(row)



#def list_information(simple_list):
 #   print(f"The values within the list are...")
  #  for value in simple_list:
   #     print(value)
    #print("The length of this list is... " + str(len(simple_list)))


#list_information(list_one)
