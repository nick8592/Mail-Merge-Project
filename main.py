#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

# extract name from invited_name.txt
with open("Input/Names/invited_names.txt") as invited_names_file:
    invited_names = invited_names_file.readlines()
for line in range(len(invited_names) - 1):
    name = invited_names[line].strip()
    invited_names[line] = name
    # print(invited_names[line])

    # replace invited_name into invited_letter
    with open("Input/Letters/starting_letter.txt") as starting_letter_file:
        starting_letter = starting_letter_file.readlines()
    invited_letter = starting_letter
    invited_letter[0] = invited_letter[0].replace(PLACEHOLDER, f"{invited_names[line]}")
    # print(invited_letter)

    # create invited_letter.txt with invited_letter
    with open(f"Output/ReadyToSend/letter_for_{invited_names[line]}.txt", mode="w") as ready_to_send_file:
        for _ in invited_letter:
            ready_to_send_file.write(_)


