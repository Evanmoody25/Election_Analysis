# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter.
total_votes = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
    
    #3. Print the total votes.
    print(total_votes)


    #THIS IS ALL TXT FILE SKRIPT
    # Create a filename variable to a direct or indirect path to the file.
    file_to_save = os.path.join("analysis", "election_analysis.txt")

    # Using the open() function with the "w" mode we will write data to the file.
    open(file_to_save, "w")

    # Create a filename variable to a direct or indirect path to the file.
    file_to_save = os.path.join("analysis", "election_analysis.txt")

    # Using the with statement open the file as a text file.
    with open(file_to_save, "w") as txt_file:

    #Creating a header row and then a line in election_analysis.txt
        txt_file.write("Counties in the Election\n")
        txt_file.write("------------------------\n")

   # Write three counties to the file.
        txt_file.write("Arapahoe\nDenver\nJefferson")
    # END TXT FILE SKRIPT



