# 1. An Anagram Detection Example
# a. Desc ­> One string is an anagram of another if the second is simply a
# rearrangement of the first. For example, 'heart' and 'earth' are anagrams...
# b. I/P ­> Take 2 Strings as Input such abcd and dcba and Check for Anagrams
# c. O/P ­> The Two Strings are Anagram or not....
# 2. Take a range of 0 ­ 1000 Numbers and find the Prime numbers in that range.
# 3. Extend the above program to find the prime numbers that are Anagram and
# Palindrome
# ------------------------------------------------------------------------------

# Anagram function
def Anagram(string1, string2):
    # sort the string and compare the strings
    # if equal strings are anagram else not anagram
    if sorted(string2) == sorted(string1):
        print("Strings are Anagram")
    else:
        print("Strings are not anagram")

#main
if __name__ == '__main__':
    string1 = input("Enter first string")
    string2 = input("Enter second string")
    Anagram(string1, string2)
