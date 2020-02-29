# 3. Extend the above program to find the prime numbers that are Anagram and
# Palindrome
# ---------------------------------------------------------------------------
# primenumber function
from AlgorithmProg.PrimeNumbers import PrimeNumber


# checks the anagrams in primes
def Prime_Anagram(primes):
    for i in range(0, len(primes)):
        for j in range(0, len(primes)):
            if i != j and (sorted(primes[i]) == sorted(primes[j])):
                print(primes[i], "is an anagram")


# driver program
if __name__ == '__main__':
    # primesnum_obj=PrimeNumber()
    Range_of_primes = int(input("Enter the range of prime number to check anagram:"))
    Prime_Anagram((PrimeNumber(Range_of_primes)))
