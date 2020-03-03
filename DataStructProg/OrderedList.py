class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class OrderedList:
    # the 1st element of the list is called Head
    # intilizing head = None
    def __init__(self):
        self.head = None

    # function to add elements
    def append(self, item):
        # creating a Node
        node = Node(item)
        # if head is None it means the list is empty
        # the first element is to be head
        if self.head == None:
            self.head = node
        # if the list contain elements ,we add the new elements at the end of the list
        else:
            n = self.head
            # traversing to end of the list
            while n.next is not None:
                n = n.next
            n.next = node

    # creating a function to show the elements
    def printlist(self):
        # Traversing from head to end and Printing the elements
        sh = self.head
        while sh.next is not None:
            print(sh.data, end=" ")
            sh = sh.next
        print(sh.data)

    # size of the list
    def size(self):
        # to finding the size of the list by counting each node in the list
        # take a variable and intilize to 0
        sh = self.head
        count = 0
        while sh.next is not None:
            count += 1
            sh = sh.next
        count += 1
        return count

    # creating a function to finding the data in given index
    def index(self, index):
        length = OrderedList.size(self)
        if index < 0 or index >= length:
            print("index out of boundary ")
            return
        sh = self.head
        count = 0
        # Traversing the list upto to the index and return the data
        while sh.next is not None:
            if count == index:
                return sh.data
            sh = sh.next
            count += 1
        # if index is last index in the list return last index data
        if count == length - 1:
            return sh.data

    # creating a function to find the index of the given element
    def indexOf(self, data):
        # for finding the index of the element take a variable and intialize it to 0
        # Traverse the list and increase the variale simultaneously
        sh = self.head
        count = 0
        while sh.next is not None:
            if data == OrderedList.index(self, count):
                return count
            sh = sh.next
            count += 1
        if data == sh.data:
            return count

    # creating a function to search a element
    def search(self, word):
        # searching the node
        # for index , intilize a variable as 0
        sh = self.head
        count = 0
        while sh.next is not None:
            if word == OrderedList.index(self, count):
                return True
            sh = sh.next
            count += 1
        if word == sh.data:
            return True
        else:
            return False

    # remove function to remove an element

    def remove(self, word):
        # finding the index by using IndexOf function
        poss = OrderedList.indexOf(self, word)
        sh = self.head
        # if the word present in head place , change the head to next place
        if poss == 0:
            self.head = sh.next
        else:
            # traversing up to the previous element
            for i in range(0, poss - 1):
                sh = sh.next
            # storing the address of the element into a temp variable
            temp = sh.next
            # delete the element by reffering the next element
            sh.next = temp.next

    # function to insert a element in order
    def insertorder(self, num):
        # creating a node
        node = Node(num)
        # if head is none then inserted ele is head
        if self.head == None:
            self.head = node
        else:
            # if element is less than head data then it is inserted befor head node
            sh = self.head
            if node.data < sh.data:
                self.head = node
                node.next = sh.next
            else:
                # Traversing upto that getting a element greater than or equal to the element
                # after that inserting the element
                while sh.next is not None:
                    if sh.data <= node.data <= sh.next.data:
                        temp = sh.next
                        sh.next = node
                        node.next = temp
                        return
                    sh = sh.next
                # if Traversing reached Last
                # comparing the new_element with last element and inserting
                if sh.data > node.data:
                    temp = sh.next
                    sh.next = node
                    node.next = temp
                    return
                else:
                    OrderedList.append(self, num)

    # pop function
    def pop(self):
        sh = self.head
        previous = None
        length = OrderedList.size(self)
        # iterates the loop upto the ll length
        for i in range(length - 1):
            previous, sh = sh, sh.next
        # assigns none to last second next value
        # poping last ele
        previous.next = None
        return sh.data

    # Function to pop at paticular position
    def pop(self, pos):
        sh = self.head
        if pos == 0:
            self.head = sh.next
        else:
            # traversing up to the previous element
            for i in range(0, pos - 1):
                sh = sh.next
            # storing the address of the element into a temp variable
            temp = sh.next
            # delete the element by reffering the next element
            sh.next = temp.next

    # isEmpty function
    def isempty(self):
        return self.head == None

# to Lower
