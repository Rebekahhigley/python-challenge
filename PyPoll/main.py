# hello
# Modules
import os
import csv

# Prompt user for title lookup

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
txtpath = os.path.join("analysis", "election_analysis.txt")

#varailbe
total_votes = 0
l_candidates = []
d_candidates = {}
l_winner = ["", 0]

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    first = next(csvreader)
    for row in csvreader:
        total_votes += 1

        if row[2] not in l_candidates:
            l_candidates.append(row[2])
            d_candidates[row[2]] = 0
        d_candidates[row[2]] += 1


output = (
    f"Election Analysis\n"
    f"--------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"--------------------------\n"
   
)        
print(output)
with open(txtpath, "w") as txtfile:
    txtfile.write(output)

    for x in l_candidates:
        votes = d_candidates.get(x)
        percentage = votes/total_votes*100
        candidate = f"{x}: {percentage:.3f}% ({votes})"
        print(candidate)
        txtfile.write(candidate)


# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette