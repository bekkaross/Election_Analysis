# add our dependencies:
import csv
import os


# Assign a variable to load a file from a path:

# this uses a DIRECT path:
#file_to_load = 'Resources/election_results.csv'

# this uses an INDIRECT path:
file_to_load = os.path.join("Resources", "election_results.csv")


# Assign a variable to save the file to a path:
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function:
    # (the variable "file_reader" references the file object, which is stored in memory)
    file_reader = csv.reader(election_data)

    # Read & print the header row:
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file:
    for row in file_reader:
        print(row)





# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
     # Write three counties to the file.
     # \n adds everything after it to a new line
     # txt_file.write("Arapahoe\nDenver\nJefferson")
    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
