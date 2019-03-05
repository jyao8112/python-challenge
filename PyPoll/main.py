import os
import csv

d = dict()
total_vote = 0
max_vote = 0

electiondata_csv = os.path.join(".","Resource","election_data.csv")

with open (electiondata_csv,"r",newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   next(csvfile)

   for row in csvreader:
      total_vote = total_vote + 1
      d[row[2]] = d.get(row[2], 0) + 1
print("Election Results")
print("------------------------------")  
print("Total vote: ", total_vote)
print("------------------------------") 
 
for key in d:
   percentage = round(d[key] / total_vote,2)
   if d[key] > max_vote:
      max_vote = d[key]
      max_key = key
   print(key+":"+"{:0%}".format(percentage)+"("+str(d[key])+")")


print("------------------------------")  

print("Winner is:"+ max_key)
print("------------------------------")  