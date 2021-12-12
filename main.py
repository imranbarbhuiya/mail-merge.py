with open("Input/Letters/starting_letter.txt") as starting_file:
    starting_letter = starting_file.read()

with open("Input/Names/invited_names.txt") as names_file:
    invited_names = names_file.readlines()

for name in invited_names:
    name = name.strip()
    final_file = starting_letter.replace("[name]", name)

    with open(f"Output/ReadyToSend/invite_for_{name}.txt", "w") as output_file:
        output_file.write(final_file)
