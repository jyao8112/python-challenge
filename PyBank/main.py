import os
import csv

bugetdata_csv = os.path.join(".","Resource","budget_data.csv")

months = []
profits = []
max_increase =0
max_decrease =0
total_months = 0
total_profits = 0
total_change = 0
current_change = 0

with open (bugetdata_csv,"r",newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   next(csvfile)

   for row in csvreader:
      if total_months != 0:
         current_change = int(row[1]) - int(prerow[1])
         if current_change > max_increase:
            max_increase = current_change
            maxinc_month = row[0]
         elif current_change < max_decrease:
            max_decrease=current_change
            maxdec_month= row[0]

      total_change = total_change + current_change
      total_months = total_months + 1
      total_profits = total_profits + int(row[1])
         

      prerow = row

outputdata_txt = os.path.join("output_data.txt") 
with open (outputdata_txt,"w") as txtfile:
   txtfile.writelines("Finacial Analysis\n")
   txtfile.writelines("----------------------------------------------\n")
   txtfile.writelines("Total_months:"+str(total_months) + "\n")
   txtfile.writelines("Total profits:"+str(total_profits)+"\n")
   txtfile.writelines("Average Change:"+ str(round(total_change/(total_months -1),2))+"\n")
   txtfile.writelines("Greatest Increase in Profits:" + maxinc_month + ": "+ str(max_increase)+"\n")
   txtfile.writelines("Greastest Decrease in Profits:"+ maxdec_month + ": "+ str(max_decrease)+"\n")

with open (outputdata_txt,"r") as outputfile:
   print(outputfile.read())

    