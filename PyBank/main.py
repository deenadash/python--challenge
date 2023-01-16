
# Objective 1: Import modules os and csv

import os
import csv
import statistics


# Objective 2: Set the path for the CSV file in PyBank.csv

PyBankcsv = os.path.join("Resources","budget_data.csv")

# Objective 3: Create the lists to store data. 

monthCount = 0
totalVolume = 0
greatestIncrease = 0
bestMonth = ''
greatestDecrease = 0
worstMonth = ''


date = []
profit = []
monthToMonthChange = []


# Open the CSV using the set path PyBankcsv

with open(PyBankcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #calculate total months and total profits
    for row in csvreader:    
        monthCount += 1
        date.append(row[0])
        totalVolume += int(row[1])
    
        profit.append(int(row[1]))

  
# track monthly changes
for i in range(len(profit)-1):
    monthlyChange = (profit[i+1] - profit[i])
    monthToMonthChange.append(monthlyChange)   

averageChange = statistics.mean(monthToMonthChange)

#Find the max and min monthly change and the corresponding dates these changes were obeserved
greatestIncrease = max(monthToMonthChange)
greatestDecrease = min(monthToMonthChange)

bestMonth = date[monthToMonthChange.index (greatestIncrease)]
worstMonth = date[monthToMonthChange.index (greatestDecrease)]

print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(monthCount))
print("Total Profits: " + "$" + str(totalVolume))
print("Average Change: " + "$" + str(round(averageChange, 2)))
print("Greatest Increase in Profits: " + str(bestMonth) + " ($" + str(greatestIncrease) + ")")
print("Greatest Decrease in Profits: " + str(worstMonth) + " ($" + str(greatestDecrease)+ ")")
print("----------------------------------------------------------")

output_file = os.path.join("analysis", "PyBank_output.txt")
with open(output_file, 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(monthCount) + "\n")
    text.write("    Total Profits: " + "$" + str(totalVolume) +"\n")
    text.write("    Average Change: " + '$' + str(round(averageChange, 2)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(bestMonth) + " ($" + str(greatestIncrease) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(worstMonth) + " ($" + str(greatestDecrease) + ")\n")
    text.write("----------------------------------------------------------\n")