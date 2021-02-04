TO_BE_REPLACED = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    content = letter.read()
    for name in names:
        stripped = name.strip()
        new_letter = content.replace(TO_BE_REPLACED, stripped)
        with open(f"./Output/ReadyToSend/letter_for_{stripped}.docx", mode="w") as ready_letter:
            ready_letter.write(new_letter)