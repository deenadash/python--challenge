import os
import csv

# here's my election data - it's in a folder called resources in that lives at the same level as main.py
PyPollcsv = os.path.join( 'Resources', 'election_data.csv')

# total rows (not including the header is the total of votes)
totalVotes = 0 


votesPerCandidate = {}

# open up election_data
with open(PyPollcsv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first
    csv_header = next(csvreader)
  

    # Read each row of data after the header
    for row in csvreader:
        totalVotes += 1
        if row[2] not in votesPerCandidate:
            votesPerCandidate[row[2]] = 1
        else:
            votesPerCandidate[row[2]] += 1   
        
        


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalVotes))
print("-------------------------")

for candidate, votes in votesPerCandidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    
print("-------------------------") 

winner = max(votesPerCandidate, key=votesPerCandidate.get)

print("The winner is" " " f"{winner}")

output_file = os.path.join("analysis", "PyPoll_output.txt")
with open(output_file, 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Election Results"+ "\n")
    text.write("----------------------------------------------------------\n")
    text.write("  Total Votes: " + str(totalVotes)+ "\n")
    text.write("-----------------------------------------------------------\n")
    for candidate, votes in votesPerCandidate.items():
        text.write(   candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")" +"\n")
        
    text.write('------------------------------------------------------------\n')
    text.write(   f"Winner: {winner}" + "\n")
   
    text.write("----------------------------------------------------------\n")
