import os
import csv
import counter



#Specify the filepath of input and output files
csvpath = os.path.join("Resources","election_data.csv")
output_path = os.path.join("Analysis","Analysis.csv")



cnt = Counter()
>>> for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
...     cnt[word] += 1
>>> cnt
Counter({'blue': 3, 'red': 2, 'green': 1})