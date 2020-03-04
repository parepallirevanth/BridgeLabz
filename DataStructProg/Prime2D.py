# Take a range of 0 ­ 1000 Numbers and find the Prime numbers in that range. Store
# the prime numbers in a 2D Array, the first dimension represents the range 0­100,
# 100­200, and so on. While the second dimension represents the prime numbers in
# that range
# ---------------------------------------------------------------------------------

# importing required packages
from DataStructProg.Primes_util import *

prime_obj = Prime()

lis = []
iterator = 0
for num in range(0, 1000, 100):
    prime_lis = prime_obj.prime(num, num + 100)
    iterator += 1
    lis.append(prime_lis)
prime_obj.print2d(iterator)
