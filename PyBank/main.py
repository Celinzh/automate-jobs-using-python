# Import csv file
from pathlib import Path
import csv

csvpath = Path('./budget_data.csv')

# Initialise variables
months_number = 0
net_total = 0
profit_loss_changes = 0
profit_loss_changes_previous = 0
changes_average = 0
maximum_key = 0
maximum_value = 0
minimum_key = 0
minimum_value = 0

profit_loss_list = []
profit_loss_changes_list = []    
date_list = []

# Open the csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:

        # Iterate the data into lists
        date = row[0]
        profit_loss = int(row[1])
        date_list.append(date)
        profit_loss_list.append(profit_loss)

        # Net total
        months_number = months_number + 1
        net_total = net_total + profit_loss

        # Average changes in profit and loss
        profit_loss_changes = profit_loss - profit_loss_changes_previous
        profit_loss_changes_previous = profit_loss
        profit_loss_changes_list.append(profit_loss_changes)
        changes_average = sum(profit_loss_changes_list)/months_number

        # Maximum and minimum
        if profit_loss > maximum_value:
                maximum_value = profit_loss
        elif profit_loss < minimum_value:
                minimum_value = profit_loss
    
    max_index = profit_loss_list.index(maximum_value)
    maximum_key = date_list[max_index]
    
    min_index = profit_loss_list.index(minimum_value)
    minimum_key = date_list[min_index]


   
# Print output
print("Financial Analysis")
print("--------------------------------------------------------------------------------")
print(f"Total Months: {months_number}.")
print(f"The total profit over the entire period is ${net_total}.")
print(f"The average of the total profit over the entire period is ${changes_average}")
print(f"The greatest increase is ${maximum_value}, and its date is {maximum_key}")
print(f"The greatest decrease is ${minimum_value}, and its date is {minimum_key}")

# Print output to a text file
file = open("file.txt", "w")
file.write("Financial Analysis\n")
file.write("--------------------------------------------------------------------------------\n")
file.write(f"Total Months: {months_number}.\n")
file.write(f"The total profit over the entire period is ${net_total}.\n")
file.write(f"The average of the total profit over the entire period is ${changes_average}.\n")
file.write(f"The greatest increase is ${maximum_value}, and its date is {maximum_key}.\n")
file.write(f"The greatest decrease is ${minimum_value}, and its date is {minimum_key}.\n")
file.close()
