# Desc ­> Read .a List of Numbers from a file and arrange it ascending Order in a
# Linked List. Take user input for a number, if found then pop the number out of the
# list else insert the number in appropriate position
# b. I/P ­> Read from file the list of Numbers and take user input for a new number
# c. Logic ­> Create a Ordered Linked List having Numbers in ascending order.
# d. O/P ­> The List of Numbers to a File.
# ---------------------------------------------------------------------------------------
# importing Ordered list
from DataStructProg.OrderedList import *


# Orderd insert function
def OrderdInsert():
    # def words_read():
    file = open("Orderlist_num", "r")
    # created a linked list
    words_list = OrderedList()
    # storing the elements into list
    for i in file:
        # str_x =re.split(',|\n| \t',i)
        str_x = i.split(',')
        for j in str_x:
            # STORING DATA  into list
            words_list.insertorder(int(j))
    file.close()
    #print(type(words_list))
    return words_list


# search function
def searchList(doc_list):
    search_key = int(input("Enter a number to search:"))
    # seraching a key from using utility search function from linked list class
    sk = doc_list.search(search_key)
    # if found then
    # poping the element from list
    if sk:
        doc_list.pop(doc_list.indexOf(search_key))
        # if word not found
        # adding word to the list
    else:
        doc_list.insertorder(search_key)
        #doc_list.append(search_key)
    return doc_list


if __name__ == '__main__':
    # creating a Ordered empty list
    a = OrderdInsert()
    a.printlist()
    b = searchList(a)
    b.printlist()
