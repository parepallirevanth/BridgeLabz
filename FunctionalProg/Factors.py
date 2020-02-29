# 6. Factors
# a. Desc ­> Computes the prime factorization of N using brute force.
# b. I/P ­> Number to find the prime factors
# c. Logic ­> Traverse till i*i <= N instead of i <= N for efficiency .
# d. O/P ­> Print the prime factors of number N
# ----------------------------------------------------------------------
import math


# Function on Factors
def Factors(Number):
    while Number % 2 == 0:  # prints 2 until num divided by 2
        print(2)
        Number = Number // 2
    for i in range(3, int(math.sqrt(Number)) + 1, 2):  # using Brute force decreased iteration by i*i<=N
        while Number % i == 0:  # for loop is for any odd number that gives remainder zero while dividing
            print(i)  # prints number if remainder is 0
            Number = Number // i
    if Number > 2:  # this loop is for remaining numbers which not gives remainder zero
        print(Number)


if __name__ == '__main__':
    Num = int(input("Enter number to find prime factors of it:"))
    Factors(Num)
