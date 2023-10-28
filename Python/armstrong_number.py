def is_armstrong_number(number):
    # Convert the number to a string to find the number of digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return armstrong_sum == number

# Take user input
user_input = input("Enter a number: ")

try:
    # Convert the input to an integer
    user_number = int(user_input)
    
    # Check if it's an Armstrong number
    if is_armstrong_number(user_number):
        print(f"{user_number} is an Armstrong number.")
    else:
        print(f"{user_number} is not an Armstrong number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
