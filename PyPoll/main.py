
import csv

# data = csv.reader(open('../Resources/election_data.csv')) #This line returns in list format

data = csv.DictReader(open('Resources/election_data.csv')) #Returns in dictionary format
my_report = open('Election_Report.txt', 'w') #create the report.

votes = 0
#each row is defined as below
can_list = {}

# next(data)

for row in data:
# 	votes = votes + 1
	votes += 1

#call out the key instead of counting which row number is for candidates.
	can = row['Candidate']

#Check if the current candidate (can) is not already in the can_list dictionary. If the candidate is not present, it means that this is the first vote being counted for this candidate.
	if can not in can_list.keys():
		can_list[can] = 0

	can_list[can] += 1

#f with '''
output = f'''
Election Results
-------------------------
Total Votes: {votes:,}
-------------------------
'''

# to count the number of votes of each candidate, set 0 to start
win_votes = 0

for can in can_list.keys():
	can_votes = can_list[can]

#output of mathematical calculation of total votes of a candidate divide by total votes of all candidate and convert to %
# :, added the separator for number in thousands. #"\n" means return.

#output += is adding to the original output above

	output += f'{can}: {can_votes/votes*100:.3f}% ({can_votes:,})\n'

#find the candidate with the most votes

	if can_votes > win_votes:
		winner = can
		win_votes = can_votes

#output += is adding to the original output above
output += f'-------------------------\nWinner: {winner} \n-------------------------'


print(output)
#export the codes to the report created
my_report.write(output)

my_report.close()








































