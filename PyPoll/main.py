import os
import csv

d = dict()
total_vote = 0
max_vote = 0

electiondata_csv = os.path.join(".","Resource","election_data.csv")
outputdata_txt = os.path.join("output_data.txt")

### load data into dictionary
with open (electiondata_csv,"r",newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   next(csvfile)

   for row in csvreader:
      total_vote = total_vote + 1
      d[row[2]] = d.get(row[2], 0) + 1

### write results to file
with open (outputdata_txt,"w") as txtfile:
   txtfile.writelines("Election Results\n")
   txtfile.writelines("------------------------------\n")
   txtfile.writelines("Total vote: " + str(total_vote) + "\n")
   txtfile.writelines("------------------------------\n")
   txtfile.writelines('Finacial Analysis\n')
   txtfile.writelines("------------------------------\n")
   for key in d:
      percentage = round(d[key] / total_vote, 3)
      if d[key] > max_vote:
         max_vote = d[key]
         max_key = key
      txtfile.writelines(key+":"+"{:.3%}".format(percentage)+"("+str(d[key])+")\n")
      #txtfile.writelines(key+":"+"{:.6%}".format(percentage)+"("+str(d[key])+")\n")

   txtfile.writelines("------------------------------\n")
   txtfile.writelines("Winner is:" + max_key + "\n")
   txtfile.writelines("------------------------------")

### print file
with open (outputdata_txt,"r") as outputfile:
   print(outputfile.read())

   