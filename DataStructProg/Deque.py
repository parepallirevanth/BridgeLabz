# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Deque class

class Deque:
    # creating front, rare, count variables
    def __init__(self):
        self.front = None
        self.rare = None
        self.count = 0

    # function to inserting elements in front position
    def insertFront(self, data):
        # creating a node
        node = Node(data)
        # if the inserted element is 1st element then  front_element = rare_element = given 1st element
        if self.front is None:
            self.front = self.rare = node
        # the element will add in front possession
        node.next = self.front
        self.front = node
        self.count += 1

    # creating a function to inserting elements in rare position
    def insertRare(self, data):
        # creating a node
        node = Node(data)
        # if the given element is first element rare_element = front_element = given element
        if self.rare is None:
            self.rare = self.front = node
        # the given element is added at the end and assigned as rare element
        self.rare.next = node
        self.rare = node
        self.count += 1

    # creating a function to check is empty or not if it is empty return true
    def isEmpty(self):
        if self.front is None:
            return True
        else:
            return False

    # Function for getting size of the queue
    def size(self):
        # if the count is < 0 there is an error
        if self.count < 0:
            return -1
        # else return size = count
        else:
            return self.count

    # Function for remove element from front
    def removeFront(self):
        # if the size of the queue is 0 there is no elements to remove
        if Deque.size(self) == 0:
            return None
        # if there is only one one element present
        else:
            if self.front.next is None:
                n = self.front.data
                self.front = None
                return n
            # else remove the front element and assign next element as front
            else:
                n = self.front.data
                self.front = self.front.next
                self.count -= 1
                return n

    # Function for removing data from rare
    def removeRare(self):
        # if the size of the queue is 0 there is no element to remove
        if Deque.size(self) == 0:
            return None
        # else remove the rare element and assign next element as rare
        else:
            # traversing upto last but one element and assigned it as rare
            length = Deque.size(self)
            temp = self.front
            for i in range(0, length - 1):
                temp = temp.next
            n = temp.data
            self.rare = temp
            self.count -= 1
            return n
