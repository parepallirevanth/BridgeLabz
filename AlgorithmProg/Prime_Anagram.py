# 3. Extend the above program to find the prime numbers that are Anagram and
# Palindrome
# ---------------------------------------------------------------------------
# primenumber function
from AlgorithmProg.PrimeNumbers import primeNumber


# checks the anagrams in primes
def Prime_Anagram(primes):
    for i in range(0, len(primes)):
        for j in range(0, len(primes)):
            if i != j and (sorted(primes[i]) == sorted(primes[j])):
                print(primes[i], "is an anagram")


# driver program
if __name__ == '__main__':
    # primesnum_obj=PrimeNumber()
    try:
        min_range = int(input("Enter the min range of prime number to check anagram:"))
        max_range = int(input("Enter the min range of prime number to check anagram:"))
        Prime_Anagram((primeNumber(min_range,max_range)))
    except Exception:
        print("Error: enter integer numbers only")
