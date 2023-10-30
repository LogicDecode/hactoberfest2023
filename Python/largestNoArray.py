# Function to find the largest number in an array with O(n) time complexity
def find_largest_number(arr):
    if not arr:
        return None  # Return None for an empty array

    largest_number = arr[0]

    for num in arr:
        if num > largest_number:
            largest_number = num

    return largest_number

# Get input from the user and convert it to a list of integers
input_str = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in input_str.split()]

# Find the largest number in the array
largest_number = find_largest_number(numbers)

if largest_number is not None:
    print(f"The largest number in the array is: {largest_number}")
else:
    print("No valid numbers entered in the array.")
