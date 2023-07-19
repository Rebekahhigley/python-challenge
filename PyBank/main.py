#hello
# Modules
import os
import csv

# Prompt user for title lookup

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
txtpath = os.path.join("analysis", "budget_analysis.txt")


# Set variable to check if we found the video
total_months = 0
net_total = 0
month_list = []
change_list = []
average_change = 0
great_increase = ["", 0.0]
great_decrease = ["", 0.0]

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    first = next(csvreader)
    total_months = total_months + 1
    net_total += int(first[1])
    previous = int(first[1])
    # Loop through verifying
    for row in csvreader:
       total_months = total_months + 1
       net_total += int(row[1])
       net_change = int(row[1])-previous

       month_list += [row[0]]
       change_list += [net_change]
       previous = int(row[1])

average_change = sum(change_list)/len(change_list)
great_increase[1] = max(change_list)
great_decrease[1] = min(change_list)
index_great = change_list.index(great_increase[1])
great_increase[0] = month_list[index_great]
index_less = change_list.index(great_decrease[1])
great_decrease[0] = month_list[index_less]

output = (
    f"Financial Analysis\n"
    f"--------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change} \n"
    f"Greatest Increase in Profits: {great_increase[0]} (${great_increase[1]})\n"
    f"Greatest Decrease in Profits: {great_decrease[0]} (${great_decrease[1]})\n"
)        
print(output)
with open(txtpath, "w") as txtfile:
    txtfile.write(output)


# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)