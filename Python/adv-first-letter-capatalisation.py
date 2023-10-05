import os

def capitalize_first_letters(line):
    words = line.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

file_path = input('Enter File Whole Path: ')

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            capitalized_line = capitalize_first_letters(line)
            file.write(capitalized_line)

    print(f"File '{file_path}' has been modified.")
else:
    print(f"File '{file_path}' does not exist.")
