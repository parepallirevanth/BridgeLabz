# 5. Harmonic Number
# a. Desc ­> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
# b. I/P ­> The Harmonic Value N. Ensure N != 0
# c. Logic ­> compute 1/1 + 1/2 + 1/3 + ... + 1/N
# d. O/P ­> Print the Nth Harmonic Value.
# ------------------------------------------------------------------------\
# Function  to find harmonic number

def Harmonic(harmonic_N):
    harmonic = 0
    for i in range(1, harmonic_N):
        harmonic = harmonic + (1 / i)  # computes 1/1 + 1/2 + 1/3 + ... upto N terms
    print(harmonic)


if __name__ == '__main__':
    harmonic_N = int(input("Enter a nth number to find harmonic: "))  # Takes input as integer
    Harmonic(harmonic_N)  # calls the function Harmonic
