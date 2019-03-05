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
      
print("Finacial Analysis")
print("---------------------------------------------------------")
print("Total_months:",total_months)
print("Total profits:", total_profits)
print("Average Change:",total_change/(total_months -1))
print("Greatest Increase in Profits:" ,maxinc_month, max_increase)
print("Greastest Decrease in Profits:",maxdec_month,max_decrease)

      #months.append(row[0])
      #profits.append(row[1])
      
      #for j in range(len(months)):
      #	if profits[j] >= max_increase:
      #	   max_increase = profits[j]
      #	   inc_month = months [j]
      #	elif profit[j]<=max_decrease:
      #	     max_decrease = revenue[j]
      #	     dec_month = months[j]

   #total_month=len(months)
   #total_profits = sum(int(i) for i in profits)        
   #print (total_month,total_profits,average,max_increase,max_decrease,inc_month,dec_month)
