"""Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird"""


n = int(input())

if (n%2 != 0) or (6 <= n and n <= 20):
    print(" Weird")

else:
    print (" Not Weird")    