# 6 . Binary Search the Word from Word List
# a. Desc ­> Read in a list of words from File. Then prompt the user to enter a word to
# search the list. The program reports if the search word is found in the list.
# b. I/P ­> read in the list words comma separated from a File and then enter the word
# to be searched
# c. Logic ­> Use Arrays to sort the word list and then do the binary search
# d. O/P ­> Print the result if the word is found or not
# --------------------------------------------------------------------------------------
# Function for WordSearch In list from file


def words_read():
    file = open("readable", "r")
    words_list = []
    for i in file:
        str_x = i.split()
        for j in str_x:
            words_list.append(j)
    file.close()
    search_word = input("Enter word to be searched: ")
    print(binaryserach_words(words_list, 0, len(words_list), search_word))


def binaryserach_words(word_list, l, h, word):
    # word_list
    word_list.sort()
    if h >= l:
        # find the mid loc of subarray
        mid = l + (h - l) // 2
        # if element found at mid position returns
        if word_list[mid] == word:
            return 'word is found'
        # compares element of mid and given element
        # if mid > search element mid is set as high(end loc)
        elif word_list[mid] > word:
            return binaryserach_words(word_list, l, mid - 1, word)
        # if search ele is greater than mid element then mid is set as start
        else:
            return binaryserach_words(word_list, mid + 1, h, word)
    else:
        return 'word not found'

# driver program
if __name__ == '__main__':
    words_read()
