# add our dependencies:
import csv
import os

os.system('cls||clear')

# Assign a variable to load a file from a path:
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path:
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter:
# (place this before the with open so that everytime the total votes is set =0 everytime before the file is opened)
total_votes = 0
# create new list of candidate options:
candidate_options = []
# declare dictionary to hold all votes for each candidate:
candidate_votes = {}
# winning candidate & winning count tracker (declare variables to hold each):
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row:
    headers = next(file_reader)
    # Print each row in the CSV file:
    for row in file_reader:
        # Add to the total vote count:      
        total_votes += 1
        # Get the candidate name from each row:
        candidate_name = row[2]
        # if the candidate does not match any existing candidate already in the list:
        if candidate_name not in candidate_options:
            # then add the candidate name to the candidate list:
            candidate_options.append(candidate_name)  
            # create each candidate as a key:
            candidate_votes[candidate_name] = 0     
        # add a vote to that candidates count:
        candidate_votes[candidate_name] += 1

# Save results to txt file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    # iterate through the candidate list:
    for candidate_name in candidate_votes:
        # retrieve vote count & % of a candidate
        votes = candidate_votes[candidate_name]       
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # determine winning vote count and candidate:
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if TRUE, then set winning_count = votes & winning_percent = vote_percentage & winning_candidate = candidates name
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

