# 2. Take a range of 0 ­ 1000 Numbers and find the Prime numbers in that range.
# ------------------------------------------------------------------------------

# primenumber function

def PrimeNumber(primes_range):
    primes = []
    # Iterates upto the given range
    for num in range(0, primes_range + 1):

        # Skip 1 and 0
        # prime nor composite
        if num == 1 or num == 0:
            continue

        # flag variable to tell
        # if i is prime or not
        flag = 1

        for j in range(2, num // 2 + 1):
            if (num % j == 0):
                flag = 0
                break

        # flag = 1 means i is prime
        # and flag = 0 means i is not prime
        if (flag == 1):
            primes.append(str(num))
    return primes


# driver program
if __name__ == '__main__':
    Range_of_primes = int(input("Enter the range of prime number needed:"))
    print(PrimeNumber(Range_of_primes))
