with open("../Name/invited_names.txt") as names_file:
    with open("starting_letter.txt") as letter_file:
        names = names_file.readlines()
        letter = letter_file.read()
    for name in names:
        name = name.replace("\n", "")
        new_letter = letter.replace("[name]", name)
        with open(rf"C:\PythonProjects\100_python_projects\src\mail_merge\Output\ReadyToSend\letter_for_{name}.txt",
                  "w") as completed_letter:
            completed_letter.write(new_letter)
