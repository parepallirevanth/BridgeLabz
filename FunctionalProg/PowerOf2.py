# 4. Power of 2
# a. Desc ­> This program takes a command­line argument N and prints a table of the
# powers of 2 that are less than or equal to 2^N.
# b. I/P ­> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int
# c. Logic ­> repeat until i equals N.
# d. O/P ­> Print the year is a Leap Year or not.
# ----------------------------------------------------------------------------------------
# Function to calculate power of 2 upto given range
def PowerOf2(n):
    if n < 31 and n >= 0:
        for i in range(0, n + 1):  # iterates upto given num
            print(2 ** i)  # prints power upto given num
    else:
        print("Number must between 0 and 31")


if __name__ == '__main__':
    n = int(input("Enter a number between 0 and 31: "))  # input
    PowerOf2(n)  # Function call
