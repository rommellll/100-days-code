#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letter_name_placeholder = "[name]"

with open("./Input/Names/invited_names.txt", "r") as invited_persons:
    for name in invited_persons:
        with open("./Input/Letters/starting_letter.txt", "r") as letter_template:
            template = letter_template.read()
            stripped_name = name.strip()
            new_file = template.replace(letter_name_placeholder, stripped_name)
            with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as new_letter:
                new_letter.write(new_file)
