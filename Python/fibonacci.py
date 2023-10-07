# A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....

# The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms.This means to say the nth term is the sum of (n-1)th and (n-2)th term.


# Python program to display the Fibonacci sequence


<<<<<<< HEAD
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)

=======
#It is more efficient than the recursive approach for larger values of nterms.
>>>>>>> 0eaf03475a171f486a61ec62439dada704ba20b6

nterms = 10

# Check if the number of terms is valid
if nterms <= 0:
<<<<<<< HEAD
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))
=======
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   a, b = 0, 1  # Initialize the first two Fibonacci numbers
   for i in range(nterms):
       print(a)
       a, b = b, a + b  # Update a and b to calculate the next Fibonacci number

       
       
       
>>>>>>> 0eaf03475a171f486a61ec62439dada704ba20b6
