
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# save the letters in the folder "ReadyToSend"

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    # print(names_file.readlines())
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        # print(stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as n:
            updated_content = content.replace(PLACEHOLDER, stripped_name)
            n.write(updated_content)
