# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
#1. Declaire the empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1
        #Print the candidate name from each row.
        candidate_name = row[2]
        #if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #counting votes
        candidate_votes[candidate_name] += 1
    
    #Print the candidates vote dictionary
    print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    #Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    #Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    #Print the candidate name and percentage of votes.
    # To do: print out each candidat's name, vote count, and percentage of
    #votes to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


    #Determine winning vote count and candidate
    #Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # if true then set winning_count = votes and winning_percent =
        # vote _percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
    # To do: print out the winning candidate, vote count and percentage to
    # terminal



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