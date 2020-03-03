# UnOrdered List
# a. Desc ­> Read the Text from a file, split it into words and arrange it as Linked List.
# Take a user input to search a Word in the List. If the Word is not found then add it
# to the list, and if it found then remove the word from the List. In the end save the
# list into a file
# b. I/P ­> Read from file the list of Words and take user input to search a Text
# c. Logic ­> Create a Unordered Linked List. The Basic Building Block is the Node
# Object. Each node object must hold at least two pieces of information. One ref to
# the data field and second the ref to the next node object.
# d. O/P ­> The List of Words to a File.
# -------------------------------------------------------------------------------------------
import re
from DataStructProg.LinkedList import *
# function to read data from file
def words_read():
    file = open("DataStructWordsFile", "r")
    # created a linked list
    words_list = Linkedlist()
    # storing the elements into list
    for i in file:
        str_x = re.split(',| |\.|\n',i.lower())
        for j in str_x:
            # STORING DATA  into list
            words_list.append(j)
    file.close()
    return words_list
# function for searching element in the list
def searchList(doc_list):
    search_key = input("Enter a string to search:")
    search_key  = search_key.lower()
    # seraching a key from using utility search function from linked list class
    sk=doc_list.search(search_key)
    # if found then
    # poping the element from list
    if sk == True:
        doc_list.pop(doc_list.indexOf(search_key))
        # if word not found
        # adding word to the list
    else:
        doc_list.append(search_key)
    return doc_list

# driver program
if __name__ == '__main__':
    # calling function to read the words from a file
    a = words_read()
    # calling search function to search a element from list
    b = searchList(a)
    #a.printlist()
    # printing final list
    b.printlist()

