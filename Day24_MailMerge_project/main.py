# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PATTERN_TO_REPLACE = "[name]"

with open("./Input/Names/invited_names.txt") as invitees_file:
    invitees = invitees_file.readlines()
    print(invitees)


with open("./Input/Letters/starting_letter.txt") as letter_template_file:
    letter_text = letter_template_file.readlines()
    letter_template = ""
    for line in letter_text:
        letter_template += line
    print(letter_template)


for name in invitees:
    name = name.replace("\n","")
    unique_letter = letter_template.replace(PATTERN_TO_REPLACE,name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt",mode = "w") as invite:
        invite.write(unique_letter)


