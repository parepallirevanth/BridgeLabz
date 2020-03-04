# Prime Number Program and store only the numbers in that range that are Anagrams.
# For e.g. 17 and 71 are both Prime and Anagrams in the 0 to 1000 range.
# Further store in a 2D Array the numbers that are Anagram and numbers that are not Anagram
# -------------------------------------------------------------------------------------------

from DataStructProg.Primes_util import Prime

# Importing numpy module
from numpy import *

# Creating object for prime class
obj = Prime()

# Creating a empty anagram list
anagram_list = []

# Creating a empty non_anagram list
non_anagram = []

# taking prime numbers
prime_list = obj.prime(0,1000)

# Checking the prime numbers are anagram or not
for num in prime_list:
    if num <= 10:
        non_anagram.append(num)
        continue
    number= obj.anagram(num)
    if obj.prime_check(number) and  0<= number <= 1000:
        anagram_list.append(num)
        anagram_list.append(number)
        prime_list.remove(number)
    else:
        non_anagram.append(num)
# Converting the anagram prime number list to array
anagram_array = array(anagram_list)
# Converting the non anagram prime numbers list to array
non_anagram_array= array(non_anagram)

print("Anagram prime numbers array\n", anagram_array)
print("Non anagram prime numbers array\n", non_anagram_array)
