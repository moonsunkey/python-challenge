#using a different approach to read csv file 

import csv

total_months = 0	
total_profit_loss = 0
total_change = 0
greatest_increase = ["",0]
greatest_decrease = ["",99999999999999999999]

my_report = open('budget_data.txt', 'w') #create the report.

pybank = csv.reader(open('Resources/budget_data.csv'))
header = next(pybank)  # Skip the header row
first_row = next(pybank)
total_months += 1
total_profit_loss += int(first_row[1])
previous_profit_loss = int(first_row[1])

for row in pybank:
	total_months += 1
	total_profit_loss += int(row[1])
	change = int(row[1]) - previous_profit_loss
	total_change += change
	#need to update the previous_profit_loss variable inside the loop

	previous_profit_loss = int(row[1])

# Determine greatest increase: if change (current) is the greatest, then the date will be the value in row[0].
        # The greatest increase will be the $$ in the current calculation.
	if change > greatest_increase[1]:
		greatest_increase[0] = row[0]
		greatest_increase[1] = change

        # Determine greatest decrease: similar if the current change is smaller than the greatest decrease,
        # then we get the date value of the row and the current decrease.
	if change < greatest_decrease[1]:
		greatest_decrease[0] = row[0]
		greatest_decrease[1] = change

# Calculate average change (total months minus the first month)
average_change = total_change / (total_months - 1)

output = f'''
Financial Analysis
-------------------------
Total Months: {total_months}
Total: ${total_profit_loss}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
'''

print(output)

my_report.write(output)

my_report.close()

print("Report has been saved to 'budget_data.txt'.")
