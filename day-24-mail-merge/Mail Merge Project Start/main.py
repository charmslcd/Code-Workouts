#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


with open("./Input/Letters/starting_letter.txt", mode="r") as start_file:
    start_letter = start_file.read()

#store names in list

with open("./Input/Names/invited_names.txt", mode="r") as names:
    name_list = [line.strip() for line in names.readlines()]

print(name_list)

#replace [name] in letter and create output letter

for name in name_list:
    new_letter = start_letter.replace("[name]", name)
    letter_name = f"letter_for_{name}"
    with open(f"{letter_name}", mode="w") as file:
        file.write(new_letter)
