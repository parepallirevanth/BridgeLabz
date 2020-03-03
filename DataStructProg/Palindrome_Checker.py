# Palindrome­Checker
# a. Desc ­> A palindrome is a string that reads the same forward and backward, for
# example, radar, toot, and madam. We would like to construct an algorithm to
# input a string of characters and check whether it is a palindrome.
# b. I/P ­> Take a String as an Input
# c. Logic ­> The solution to this problem will use a deque to store the characters of
# the string. We will process the string from left to right and add each character to
# the rear of the deque.
# d. O/P ­> True or False to Show if the String is Palindrome or not.
# --------------------------------------------------------------------------------------

# importting required deque
from DataStructProg.Deque import *

# palindrom function
def palindrome_checker():
    # creating a Deque
    pali_deque = Deque()
    # taking an input
    string = input("Enter a string:")
    # inserting elements at rare
    for i in string:
        pali_deque.insertRare(i)
    # finding size of deque
    size = pali_deque.size()

    # take a empty string
    new_string = ""
    for i in range(size):
        new_string = new_string + pali_deque.removeRare()

    # comparing both strings
    if string == new_string:
        print("palindrome strings")
    else:
        print("Not palindrome strings")


# driver program
if __name__ == '__main__':
    palindrome_checker()
