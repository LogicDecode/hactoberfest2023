import os

<<<<<<< HEAD

def First_Letter_Capatilise(ls):
    ls = ls.split(" ")
    final = ""
    b = 1
    for i in range(len(ls)):
        if b != 1:
            final += " "
        a = 1
        b += 1
        for j in ls[i]:
            if a == 1:
                final += j.upper()
            else:
                final += j
            a += 1
    return final


a = input("Enter File Whole Path:")
a = a[1 : len(a) - 1]
final = []

with open(rf"{a}") as t:
    temp = t.readlines()
    for i in temp:
        _ = First_Letter_Capatilise(i)
        final.append(_)

with open(rf"{a}", "w") as t:
    t.write("")

with open(rf"{a}", "a") as t:
    for i in final:
        t.write(i)
=======
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
>>>>>>> 0eaf03475a171f486a61ec62439dada704ba20b6
