#import os  
import os
#import csv 
import csv 

#read csv
csvpath = os.path.join('C:/Repos/My_Repo/Python-challenge/PyPoll/Resources/election_data.csv')
print(csvpath)
#create variable for total votes cast
#create variables for votes cast for each candidate
total_votes = []
stockham_votes = 0
degette_votes = 0
doane_votes = 0

#open csv for use 
with open(csvpath,encoding="utf-8") as csvfile:
    #delimited by commas
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    #ignore headers
    csv_header = next(csvreader)
    for row in csvreader:
        #count number of votes 
        total_votes.append(row[0])
        
        #count the votes for each candidate
        if row[2] == "Charles Casper Stockham":
            stockham_votes +=1
        elif row[2] == "Diana DeGette":
            degette_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            doane_votes +=1

#make dictionaries out of lists to get the winner
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
candidate_votes = [stockham_votes, degette_votes, doane_votes]
#zip candidates and votes to get the max and find the winner
votes_dict = dict(zip(candidates, candidate_votes))
winner = max(votes_dict, key=votes_dict.get)

#create variable for total votes as integer 
total_vote_count = len(total_votes)
#caculate the percent for each candidate
stockham_percent = (stockham_votes/total_vote_count) * 100
degette_percent = (degette_votes/total_vote_count) * 100
doane_percent = (doane_votes/total_vote_count) * 100

#print analysis 
print("Election Results")
print("-------------------------")
print(f"Total Votes : {len(total_votes)}" )
print("-------------------------")
#print the percentage/number of votes for each candidate rounded 3 decimals
print(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
print(f"Diana Degette: {degette_percent:.3f}% ({degette_votes})")
print(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#create text file for results
analysis = os.path.join('C:/Repos/My_Repo/Python-challenge/PyPoll/Analysis/Election_Analysis.txt')
with open(analysis,"w") as file:

    file.write("Election Results")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Total Votes : {len(total_votes)}" )
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
    file.write("\n")
    file.write(f"Diana Degette: {degette_percent:.3f}% ({degette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write("-------------------------")
