import os
import csv

poll = {}

with open('election_data.csv') as file:
    reader = csv.reader(file)

    next (reader)            
    for row in reader:      
        if row[2] in poll:  
            poll[row[2]] += 1 
    else:                    
      poll[row[2]] = 1  
total_votes = reader.line_num - 1 

print ("Election Resuls")
print ("--------------------------")
print ("Total Votes: " + str(total_votes))
print ("--------------------------")

for key, value in poll.items(): 
  print (key + ": " + "{0:.1f}%".format(value/total_votes * 100) + 
         " (" + str(value) + ")")
print ("--------------------------")
print ("Winner: " + max(poll, key=poll.get) ) 
print ("--------------------------")   
