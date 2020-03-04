# Queue
# creating a node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#  creating a class for queue
class Queue:
    # function
    def __init__(self):
        self.rear = self.front = None
        self.count = 0

    # function to add elements to queue
    def enque(self, item):
        # creating as node
        node = Node(item)
        # if queue is empty
        # front and rare are at first pos
        if self.rear is None:
            self.front = self.rear = node
        # if ele are present in queue then
        # ele is added at end and rear part is updated
        else:
            self.rear.next = node
            self.rear = node

        self.count = self.count + 1

    # function to delete elements from queue
    def deque(self):
        # if queue is empty
        if self.front is None:
            return "queue is empty"
        # if only one element in queue
        elif self.front.next is None:
            self.front = None
            self.count = self.count - 1
        else:
            self.front = self.front.next
            self.count = self.count - 1

    # function isEmpty()
    # to check is the queue empty or not
    def isEmpty(self):
        # if front is none
        # no ele is present in Queue return True
        if self.rear is None:
            return True
        else:
            return False

    # function size
    def size(self):
        # find the size of queue
        if self.count > 0:
            return self.count
        else:
            return -1

    # function to print queue
    def printqueue(self):
        sf = self.front
        if sf == None:
            print("None")
        else:
            while sf.next is not None:
                print(sf.data, end=' ')
                sf = sf.next
            print(sf.data)


"""
# driver program
if __name__ == '__main__':
    que = Queue()
    print(que.isEmpty())
    print(que.size())
    que.dequeue()
    que.enqueue(10)
    que.enqueue(20)
    que.enqueue(30)
    que.enqueue(40)
    que.printqueue()
    print(que.size())
    print(que.isEmpty())
    que.dequeue()
    que.printqueue()
    print(que.isEmpty())
"""
