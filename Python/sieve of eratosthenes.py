# theoram to find prime noo

# time com = o (nloglogn)


from math import *


def prime_nikalo(n):
    p = [True] * (n + 1)
    #  boolean array banaya hai jo true hoga n+1 tak
    p[0] = False
    p[1] = False
    for i in range(2, int(sqrt(n) + 1)):
        if p[i] == True:
            for j in range(i * i, n + 1, i):
                p[j] = False

    for j in range(0, n + 1):
        if p[j] == True:
            # print('prime')
            print(j, end=" ")
            print("prime")


t = int(input("enter tetscases: "))
while t:
    n = int(input("enter a no "))
    prime_nikalo(n)
    t = t - 1
