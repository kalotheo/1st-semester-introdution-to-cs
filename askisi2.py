#ask user to give number and then make it integer
print ("Give me a number")
n = int(input())
# Returns floor of square root of x
def floorSqrt(x):

    # Base cases
    if (x == 0 or x == 1):
        return x

    # Staring from 1, try all numbers until
    # i*i is greater than or equal to x.
    i = 1; result = 1
    while (result <= x):

        i += 1
        result = i * i

    return i - 1
# A function to print all prime factors of
# a given number n
def primeFactors(n):

    # Print the number of two's that divide n
    while n % 2 == 0:
        print (2),
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,floorSqrt(n)+1,2):

        # while i divides n , print i ad divide n
        while n % i== 0:
            print (i),
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print (n)

primeFactors(n)
