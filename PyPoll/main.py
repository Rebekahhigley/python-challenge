# hello
# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
txtpath = os.path.join("analysis", "election_analysis.txt")

#varaibles
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
#filling list and dictionary of candidates
        if row[2] not in l_candidates:
            l_candidates.append(row[2])
            d_candidates[row[2]] = 0
        d_candidates[row[2]] += 1

#setting up the output
output = (
    f"Election Analysis\n"
    f"--------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"--------------------------\n"
)
#more output and adding it all to the textfile
with open(txtpath, "w") as txtfile:
    txtfile.write(output) 
    print(output)
   

    for x in l_candidates:
        votes = d_candidates.get(x)
        percentage = votes/total_votes*100
        candidate = f"{x}: {percentage:.3f}% ({votes})\n"
        print(candidate)
        txtfile.write(candidate)
        if votes > l_winner[1]:
            l_winner[0] = x
            l_winner[1] = votes

    winner_output = (
    f"--------------------------\n"
    f"Winner: {l_winner[0]}"
    )
    print(winner_output)
    txtfile.write(winner_output)





# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette