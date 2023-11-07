# import os module
import os
#import csv module
import csv
#create variable for total months
#create variable for total profit
#create variable for total loss
#create variable for the average change
total_months = []
total_amount = []
average_change = []

#read csv
csvpath = os.path.join('C:/Repos/My_Repo/Python-challenge/PyBank/Resources/budget_data.csv')
print(csvpath)

#open csv for use & enter encoding (windows)
with open(csvpath,encoding="utf-8") as csvfile:
    #delimited by commas
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    #ignore headers
    csv_header = next(csvreader)
   #append rows for month count and sum total 
    for row in csvreader:

        total_months.append(row[0])
        total_amount.append(int(row[1]))
        #loop through each profit change to calculate average change
    for i in range(len(total_amount)-1):
        average_change.append(total_amount[i+1]-total_amount[i])
#create variables for greatest increase and greatest decrease
greatest_increase = max(average_change)
greatest_decrease = min(average_change)   
#attach greatest increase/decrease for corresponding months
#add 1 for max & min to month after calculation
greatest_increase_month = average_change.index(max(average_change)) + 1
greatest_decrease_month = average_change.index(min(average_change)) + 1

#print analysis 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months : {len(total_months)}" )
print(f"Total: ${sum(total_amount)}")
#calculate average change, round to two decimal points; (sum of changes/amount of changes)
print(f"Average Change: ${round(sum(average_change)/len(average_change),2)}")
#make greatest increase/decrease values as string, + dollar sign, attach the months
print(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))})")
        
#export to text file
analysis = os.path.join('C:/Repos/My_Repo/Python-challenge/PyBank/Analysis/Financial_Analysis.txt')
with open(analysis,"w") as file:

    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months : {len(total_months)}" )
    file.write("\n")
    file.write(f"Total: ${sum(total_amount)}")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(average_change)/len(average_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))})")
