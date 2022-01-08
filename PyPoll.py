# add our dependencies:
import csv
import os

#clears the terminal each time it's run to clean it up (not part of assignment)
os.system('cls||clear')

# Assign a variable to load a file from a path:

# this uses a DIRECT path:
#file_to_load = 'Resources/election_results.csv'

# this uses an INDIRECT path:
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path:
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter:
# (place this before the with open so that everytime the total votes is set =0 everytime before the file is opened)
total_votes = 0

# create new list of candidate options:
candidate_options = []

# declare dictionary to hold all votes for each candidate:
candidate_votes = {}

# winning candidate & winning count tracker (declare variables to hold each):
# Declare a variable that holds an empty string value for the winning candidate:
winning_candidate = ""
#Declare a variable for the "winning count" equal to zero:
winning_count = 0
#Declare a variable for the "winning_percentage" equal to zero:
winning_percentage = 0


# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function:
    # (the variable "file_reader" references the file object, which is stored in memory)
    file_reader = csv.reader(election_data)

    # Read & print the header row:
    headers = next(file_reader)
    #print(headers)

    # Print each row in the CSV file:
    # (# of rows in the csv file (minus the header row) is how many votes are cast)
    for row in file_reader:

        # 2. Add to the total vote count:
        # same as writing "total_votes = total_votes + 1"
        total_votes += 1

        # Print the candidate name from each row:
        candidate_name = row[2]

        # if the candidate does not match any existing candidate already in the list:
        if candidate_name not in candidate_options:

            # then add the candidate name to the candidate list:
            candidate_options.append(candidate_name)  

            # create each candidate as a key:
            candidate_votes[candidate_name] = 0      

        # add a vote to that candidates count:
        candidate_votes[candidate_name] += 1

# iterate through the candidate list:
for candidate_name in candidate_votes:
    # retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    # calculate the % of votes

    # (this would turn the values into strings to print w one decimal place, if left here the next rpint statement will not work
    # due to these values being convereted to strings instead of floats:
        # vote_percentage = "{:.1f}".format(float(votes) / float(total_votes) * 100) )
    vote_percentage = float(votes) / float(total_votes) * 100

    # print out each candidate's name, vote count, and percentage of votes to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # determine winning vote count and candidate:
    # determine if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # if TRUE, then set winning_count = votes & winning_percent = vote_percentage & winning_candidate = candidates name
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"----------------------------\n")

print(winning_candidate_summary)




# print(f"{candidate_name}: received {vote_percentage}% of the vote.")

# print the candidate vote dictionary:
#print(candidate_votes)

# print the candidate list:
#print(candidate_options)

# 3. Print the total votes:
# print(total_votes)

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
     # Write three counties to the file.
     # \n adds everything after it to a new line
     # txt_file.write("Arapahoe\nDenver\nJefferson")
    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
