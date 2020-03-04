# 2. Take a range of 0 ­ 1000 Numbers and find the Prime numbers in that range.
# ------------------------------------------------------------------------------

# primenumber function

def primeNumber(min_range,max_range):
        primes = []
        # Iterates upto the given range
        for num in range(min_range, max_range + 1):

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
    try:
        min_range = int(input("Enter the min range of prime number needed:"))
        max_range  = int(input("Enter the max range of prime number needed:"))
        print(primeNumber(min_range,max_range))
    except Exception:
        print("Error: Enter numbers only")


