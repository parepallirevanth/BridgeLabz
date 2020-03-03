# Node class
class Node:
    # creating a node
    def __init__(self, data):
        self.data = data
        self.next = None
# stack class\
class Stack:
    # making a top 0
    def __init__(self):
        self.top = None
        self.count = 0

    # push function
    # push the element to top of stack
    def push(self,item):
        node = Node(item)
        # if stack is empty then
        # pushed element will be top element
        if self.top is None:
            self.top = node
            self.count = self.count + 1
        # if stack is not empty then
        # element will be aded to top
        else:
            node.next = self.top
            self.top = node
            self.count = self.count + 1

    # pop function
    # pops the top element
    def pop(self):
        # if stack is empty return false
        if self.top is None:
            return "No elemnt in stack"
        # if stack has one element then
        # pop the element
        elif self.top.next is None:
            self.top = None
            self.count = self.count - 1
        # if stack has more than one element then
        # top second element will be the top of stack
        else:
            self.top = self.top.next
            self.count = self.count - 1

    # Peek function
    # return top of the stack
    def peek(self):
        return self.top.data

    # isEmpty functio
    # return is the stack is empty or not
    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False
    # size function
    # return size of the stack
    def size(self):

        if self.count > 0:
            return self.count
        else:
            return "stack is empty"
    # print a stack
    def printstack(self):
        topele = self.top

        while topele is not None:
            print(topele.data,end =' ')
            topele = topele.next
'''# driver program
if __name__ == '__main__':
    stk = Stack()
    stk.push(10)
    stk.push(20)
    stk.push(30)
    stk.push(40)
    print(stk.peek())
    print(stk.isEmpty())
    stk.printstack()
    print("\n",stk.size())
    stk.pop()
    print(stk.size())
    stk.printstack()
'''
