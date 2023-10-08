def is_palindrome(input_string):
   
    input_string = input_string.replace(" ", "").lower()
    return input_string == input_string[::-1]


user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
