# * The net total amount of "Profit/Losses" over the entire period

# * The changes in "Profit/Losses" over the entire period, and then the average of those changes

# * The greatest increase in profits (date and amount) over the entire period

# * The greatest decrease in profits (date and amount) over the entire period

import os
import csv


csvpath = os.path.join("..", "Resources", "budget_data.csv")

total_months =[]
total_profits =[]
profit_changes =0
monthly_changes =[]
previous_value =0
revenue_change = []


with open(csvpath,newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    csv_reader = next(csvreader)

    print("Financial Analysis")
    print("----------------------------")

    for row in csvreader:
# * The total number of months included in the dataset
        total_months.append(row[0])
        total_profits.append(row[1])
    print("Total Months", len(total_months))


# * The net total amount of "Profit/Losses" over the entire period
    total_profits=[int(x) for x in total_profits]
    total_profits_sum=sum(total_profits)
    print ("Total", "$",total_profits_sum)

# (This is saying for a number within the range of 1 to whatever the count is for profit, add the data from the current profit value minus the previous profit value)
    changes = []
    for n in range(1,len(total_profits)):
        changes.append(int(total_profits[n]) - int(total_profits[n-1]))
# (Then, this is just calculating the average using basic math. Add the total changes divided by the count of the changes.)
    average_change = sum(changes) / len(changes)
    
    print("Average change", "$", str(round(average_change,2)))

# * The greatest increase in profits (date and amount) over the entire period
    for i in range(len(total_profits)-1):
   
        revenue_change.append(total_profits[i+1]-total_profits[i])
    
        max_increase_value = max(revenue_change)
        max_decrease_value = min(revenue_change)
  

# * The greatest decrease in profits (date and amount) over the entire period
        max_increase_month = revenue_change.index(max(revenue_change)) + 1
        max_decrease_month = revenue_change.index(min(revenue_change)) + 1 
           
 
    print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")


    #Print to Text File
    print("Financial Analysis", file=open("PyBank.txt", "a"))
    print("----------------------------", file=open("PyBank.txt", "a"))
    print("Total Months", len(total_months), file=open("PyBank.txt", "a"))
    print ("Total", "$",total_profits_sum, file=open("PyBank.txt", "a"))
    print("Average change", "$", str(round(average_change,2)),file=open("PyBank.txt", "a"))
    print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})", file=open("PyBank.txt", "a"))
    print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})", file=open("PyBank.txt", "a"))
