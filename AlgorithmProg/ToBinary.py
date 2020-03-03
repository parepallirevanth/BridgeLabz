# Write a static function toBinary that outputs the binary (base 2) representation of
# the decimal number typed as the input. It is based on decomposing the number into
# a sum of powers of 2
# -------------------------------------------------------------------------------------
# Function to convert dec to binary

# takes decimal as an input and convert it into binary
def dec_to_binary1():
    dec_num = int(input("Enter decimal number"))
    binary1 = []
    while dec_num > 0:
        binary1.append(dec_num % 2)
        dec_num = dec_num // 2
    binary1.reverse()
    return binary1


# Recursive method of dec to binary conversion
def dec_to_binary(decimal_num):
    # iterates until loop is gt zero
    dec_num = int(input("Enter decimal number"))
    binary1 = []
    if decimal_num > 1:
        dec_to_binary(decimal_num // 2)
    print(decimal_num % 2, end=' ')
    binary.append(decimal_num % 2)


# padding function
def padding_binary(binary):
    # padding binary number
    for i in range(0, 32 - len(binary)):
        binary.insert(i, 0)
    return binary


# decomposed function
def decomposition(binary_decompose):
    padding_binary(binary)
    print("Decomposition:")
    for index in range(0, len(binary_decompose)):
        if binary[index] == 1:
            print(2 ** (32 - index - 1), end=' ')

# function to print binary
def binary_print(binary):
    for i in binary:
        print(i,end='')

# driver program
if __name__ == '__main__':
    # calling dec to binary function
    binary = dec_to_binary1()
    binary_print(binary)
    print()
    # calling function to ensure decomposition
    decomposition(binary)
