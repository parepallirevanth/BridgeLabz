# Write Binary.java to read an integer as an Input, convert to Binary using toBinary
# function and perform the following functions.
# i. Swap nibbles and find the new number.
# ii. Find the resultant number is the number is a power of 2.
# ------------------------------------------------------------------------------------
from AlgorithmProg.ToBinary import *


# swapping nibbles
def swap_nibbles(swap_b):
    # padded the binary number with zeros
    padd_binary = padding_binary(swap_b)
    # displaying padded binary
    display(padd_binary)
    # iterates to swap nibbles
    i = 0
    while i < len(padd_binary):
        j = i
        while j < i + 4:
            temp = padd_binary[j]
            padd_binary[j] = padd_binary[j + 4]
            padd_binary[j + 4] = temp
            j = j + 1
        i = i + 8

    display(padd_binary)
    # calling function to find decimal value of swapped nibbles
    BinarytoDec(padd_binary)

    return padd_binary


# display function

def display(bin_dis):
    for i in bin_dis:
        print(i, end=' ')
    print()


# Function to convert binary to decimal
def BinarytoDec(btod):
    sum_dec = 0
    for i in range(0, len(btod)):
        if btod[i] == 1:
            sum_dec = sum_dec + (2 ** (32 - i - 1))
    print(sum_dec)


# driver program
if __name__ == '__main__':
    # calling function from dec to binary file
    b = dec_to_binary1()
    display(b)
    swap_nibbles(b)
