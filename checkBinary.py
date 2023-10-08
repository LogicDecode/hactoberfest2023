# function to Check if binary representations
# of two numbers are anagram
from collections import Counter
 
def checkAnagram(num1,num2):
 
    # convert numbers into in binary
    # and remove first two characters of 
    # output string because bin function 
    # '0b' as prefix in output string
    bin1 = bin(num1)[2:]
    bin2 = bin(num2)[2:]
 
    # append zeros in shorter string
    zeros = abs(len(bin1)-len(bin2))
    if (len(bin1)>len(bin2)):
         bin2 = zeros * '0' + bin2
    else:
         bin1 = zeros * '0' + bin1
 
    # convert binary representations 
    # into dictionary
    dict1 = Counter(bin1)
    dict2 = Counter(bin2)
 
    # compare both dictionaries
    if dict1 == dict2:
         print('Yes')
    else:
         print('No')
 
# Driver program
if __name__ == "__main__":
    num1 = 8
    num2 = 4
    checkAnagram(num1,num2)
