
import os
import csv
import statistics


PyBankcsv = os.path.join('Resources', "budget_data.csv")

profit = []
monthly_changes = []
date = []

count = 0
total_profit = 0
monthlyChange = []
profit = []
index = 1

# Open the CSV using the set path PyBankcsv

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Conducting the ask
    for row in csvreader:    
      # Use count to count the number months in this dataset
      count = count + 1 
      total_profit += int(row[1])
    
      profit.append(int(row[1]))

      # Will need it when collecting the greatest increase and decrease in profits
      date.append(row[0])

      # Append the profit information & calculate the total profit
     

      # track monthly changes
    for i in range(len(profit)-1):
      monthlyChange = (profit[i+1] - profit[i])
      monthly_changes.append(monthlyChange)   

      averageChange = statistics.mean(monthly_changes)
      #Calculate the average change from month to month. Then calulate the average monthly change
      #final_profit = int(row[1])
      #monthly_change_profits = final_profit - initial_profit

      #Store these monthly changes in a list
      #monthly_changes.append(monthly_change_profits)

      #total_change_profits = total_change_profits + monthly_change_profits
      #initial_profit = final_profit

      #Calculate the average change in profits
      #average_change_profits = round(sum(monthly_changes)/(count))
      
      #Find the max and min change in profits and the corresponding dates these changes were obeserved
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)] 
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(averageChange)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")