PyBank
Main problems to solve:

1. Open an CSV file.
2. 1) Import CSV module
   2) Need to make sure the file path is correct
   3) Skip header
3. Define variables. As previously practiced. When we need to calculate totals, we need to initiate o values so that we can use loop to add up totals.
4. The calculations.
   1) In this case since there is comparison with the previous month. Need to define the first row. Otherwise the first difference will be the first month value minus 0 (no value exists).
   2) Need to reset previous_profit_loss after each calculation. I missed this initially and the calculation was wrong.
   3) Compare change with greatest increase and greatest decrease.
5. Use f with tripple string to print the format requested. It's a much easier way than printing line by line.
6. Write the report.
7. Close file due to the way I opened it.

PyPoll

Main problems to solve. Steps are pretty similar to PyBank.

1. Open the CSV file as a dictionary
2. Define Variables:
   Total votes as 0 since we need to add up totals
   Candidate list as a dictionary
   Candidate can be pulled by using the key in dictionary instead of row number.
3. Using loop:
   1) Since one line represents one vote for one candidate, loop goes through each line to add a candidate if didn't exist previously, add that candidate and count the respective votes.
   2) Compare win votes and can votes. Greater one is the win votes.
4. Math calculation of percentage votes
5. Combine outputs to print.
6. Write the report.
7. Close the csv file.
