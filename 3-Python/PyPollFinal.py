import os
import csv

PyPollPath = os.path.join('.', 'Resources', "election_data.csv")

candidates = []
vote_count = {}
vote_percent = {}
votes = 0

with open(PyPollPath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:
        
        votes = votes + 1        

        if row[2] not in candidates and row[2] not in "Candidate":
            candidates.append(row[2])
            vote_count[row[2]] = 1
        elif row[2] in candidates and row[2] not in "Candidate":
            vote_count[row[2]] = vote_count[row[2]] + 1

    for key, value in vote_count.items():
        vote_percent[key] = str(round(((value/votes)*100),4)) + "%" + " " + "("+str(value) + ")"
    
    winner_count = max(vote_count.keys(), key=(lambda k: vote_count[k]))    
    
    line = "----------------"
    results1 = ("Election Results" + '\n' + line + '\n' + "Total Votes: "+ str(votes) + '\n' + line + '\n')
    results2 = (line + '\n' + "Winner: "+ str(winner_count) + '\n' + line + '\n')
   
    print(results1)
    for key, val in vote_percent.items():
        print(key,": ", val)
    print(results2)
    
    f = open("PyPoll_Final_Results.txt", "w")

    f.write(results1)
    for key, val in vote_percent.items():
         f.write((key + ": " + val) + '\n')
    f.write(results2)
    
    f.close()
