def is_palindrome(number):
    # Convert the number to a string to easily compare its characters
    number_str = str(number)
    
    # Check if the string is equal to its reverse
    return number_str == number_str[::-1]

# Function to get a valid integer input from the user
def get_valid_input():
    while True:
        try:
            num = int(input("Enter a number: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Main program
if __name__ == "__main__":
    num = get_valid_input()
    
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
