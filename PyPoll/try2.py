import os
import csv

election_data_csv = os.path.join( 'Resources', 'election_data.csv')

totalvotes = 0
votespercandidates = {}
candidatelist= []
votepercent = []
uniquecandidate = []
votescount = []


with open (election_data_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)
    csv_header = next(csvreader)
    
    for row in csvreader:
        totalvotes +=1
        candidatelist.append(row[2])
        
    for x in set(candidatelist):
        uniquecandidate.append(x)
        # y is the total number of votes per candidate
        y = candidatelist.count(x)
        votescount.append(y)
        #z is the percent of votes
        z = "(:.3%)". format(y/totalvotes)      
        
winning_vote = max(votescount)
winner = uniquecandidate[votescount.index(winning_vote)]

    


print ("winner:" + (winner))   
       
print ("----------------")
print ("Total Votes:" + str(totalvotes))
print(f"winner : (winner)")

print( "uniquecandidate:" + "+ " str(z) + "+" str(y))
