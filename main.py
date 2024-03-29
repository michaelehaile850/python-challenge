
import os
import csv

PyBank = []

with open("budget_data.csv" ,"r", encoding ="utf-8") as csvfile:
    # Create a CSV reader object to read the file
    csvreader = csv.reader(csvfile)
    
    # Use list() to read all rows from the CSV reader into a list
    # and use len() to get the number of rows, subtracting 1 for the header row
    number_of_months = len(list(csvreader)) - 1

# Print the total number of months
print(f"Total number of months: {number_of_months}")


##################+++++++++++++++++++++++++++++++#########

net_total = 0
with open("budget_data.csv","r") as csvfile:
    csvreader =csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        Profit_Losses = int(row[1])
        net_total +=Profit_Losses
        
print("net_total:",net_total)
#################++++++++++++++++++++++++++++++++++++++#######################


#Average Change

total_change=0
previous_value= None
changes =[]
 
with open("budget_data.csv", "r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header

        for row in csv_reader:
            if not row:  # Skip empty rows
                continue
            current_value = int(row[1])  # Convert the Profit/Losses value to integer
            
            # Calculate change from previous month, if previous_value is not None
            if previous_value is not None:
                change = current_value - previous_value
                changes.append(change)  # Store the change

            previous_value = current_value  # Update previous_value for the next iteration
         

     # Calculate the average change, if there are any changes recorded
        if changes:
             average_change = sum(changes) / len(changes)
             print(f"Average Change: {average_change}")
        else:
            print("No changes to calculate.")
       
print(average_change)     
     
  ####++++++++++++++++++++++++++++++++++++++++++++++++++++++++################
    
    
#Greatest Increase


previous_value = None
greatest_increase = 0
greatest_increase_month = ""

# Open and read the CSV file
with open("budget_data.csv" ,"r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header

    for row in csv_reader:
        month = row[0]
        current_value = int(row[1])  # Convert the Profit/Losses value to integer
        
        # Calculate change from previous month, if previous_value is not None
        if previous_value is not None:
            change = current_value - previous_value
            
            # Check if the current change is greater than the greatest increase recorded
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = month

        previous_value = current_value  # Update previous_value for the next iteration

print(f"The greatest increase in profits was {greatest_increase} in {greatest_increase_month}.")
    
###########++++++++++++++++++++++++++++++++++################################


#Greatest Decrease in Profits  


previous_value = None
greatest_decrease = 0
greatest_decrease_month = ""

# Open and read the CSV file
with open("budget_data.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header

    for row in csv_reader:
        month = row[0]
        current_value = int(row[1])  # Convert the Profit/Losses value to integer
        
        # Calculate change from previous month, if previous_value is not None
        if previous_value is not None:
            change = current_value - previous_value
            
            # Check if the current change is less than the greatest decrease recorded
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = month

        previous_value = current_value  # Update previous_value for the next iteration

print(f"The greatest decrease in profits was {greatest_decrease} in {greatest_decrease_month}.")  
    
    
###########################++++++++++++++++++++++++++++++#####################  
  



total_votes = 0  
with open("election_data.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header

    for row in csv_reader:
        total_votes += 1  # Increment the total votes count for each row read

print("total_votes: ",total_votes)
    
    
    
    
#####################++++++++++++++++++++####################################
# A complete list of candidates who received votes
candidates = set()

# Open the CSV file and read through each row to extract candidate names
with open("election_data.csv","r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row

    for row in csv_reader:
        candidate_name = row[2]  # Assuming the candidate's name is in the third column
        candidates.add(candidate_name)  # Add the name to the set of candidates

# Convert the set to a list and sort it for display
candidate_list = sorted(list(candidates))

candidate_list

###########################++++++++++++++++++++++#############################

#The percentage of votes each candidates won

# We use a dictionary to keep track of each candidate's vote count. Keys will be candidate names, and values will be the number of votes.
candidate_votes = {}

# We also need a variable to count the total number of votes in the election.
total_votes = 0

# Now, we open the CSV file to read its contents.
with open("election_data.csv","r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # This skips the header row of the CSV file.

    # We loop through each row in the CSV file.
    for row in csv_reader:
        # We assume the candidate's name is in the third column, hence row[2].
        candidate_name = row[2]
        
        # Each row represents a vote, so we add one to our total votes count.
        total_votes += 1
        
        # If the candidate's name is already in our dictionary, we add one to their vote count.
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        # If it's the first time we see this candidate, we add them to the dictionary with a vote count of 1.
        else:
            candidate_votes[candidate_name] = 1

# After counting, we calculate the percentage of votes for each candidate.
# We loop through each candidate in our dictionary.
for candidate, votes in candidate_votes.items():
    # The percentage is the candidate's votes divided by the total votes, multiplied by 100 to get a percentage.
    percentage = (votes / total_votes) * 100
    # Finally, we print the candidate's name, their percentage of votes, and total votes, formatted nicely.
    print(f"{candidate}: {percentage:.3f}% ({votes} votes)")


#################+++++++++++++++++++++++++++################################


#The total number of votes each candidate won

# We'll use a dictionary to keep track of the vote count for each candidate.
candidate_votes = {}

# Open the CSV file to read its contents.
with open("election_data.csv","r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # This skips the header row of the CSV file.

    # Loop through each row in the CSV file.
    for row in csv_reader:
        # Assuming the candidate's name is in the third column (index 2).
        candidate_name = row[2]
        
        # If we've already seen this candidate, add one to their vote count.
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        # If it's the first time we're seeing this candidate, initialize their vote count at 1.
        else:
            candidate_votes[candidate_name] = 1

# Now, we'll print the total votes each candidate won.
print("Total votes for each candidate:")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes} votes")

#####################++++++++++++++++++++++++++++++++########################

#The winner of the election  based on the popular votes

# Use a dictionary to keep track of how many votes each candidate received.
candidate_votes = {}

# Open the CSV file and read its contents.
with open("election_data.csv","r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row.

    # Go through each vote in the file.
    for row in csv_reader:
        # The candidate's name is in the third column.
        candidate_name = row[2]
        
        # If this candidate is already in our dictionary, add one to their vote count.
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        # If this is the first vote for this candidate, add them to the dictionary with a vote count of 1.
        else:
            candidate_votes[candidate_name] = 1

# After counting all votes, find the candidate with the most votes.
max_votes = 0
winner = ""

for candidate, votes in candidate_votes.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print the total votes each candidate won and announce the winner.
print("Total votes for each candidate:")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes} votes")

print(f"\nThe winner of the election based on popular vote is: {winner} with {max_votes} votes.")






