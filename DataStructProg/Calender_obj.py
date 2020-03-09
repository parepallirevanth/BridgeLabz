# week Object of calender
# importing required modules and packages
from DataStructProg.Calender import calender
from DataStructProg.Queue import Queue

# Node class
class Node:

    def __init__(self, day, date):
        self.day = day
        self.date = date
        self.next = None

# weak class
class weak:
    # creating head variable and initialize as none
    def __init__(self):
        self.head = None

    # creating the weak day objects
    def add(self, day, date):
        # creating node for day objects
        node = Node(day, date)
        # if the head is none means it starting day of the weak, assign the node to head
        if self.head is None:
            self.head = node
        # else traverse to the end of the list and add the node at end
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = node

    # function for print the weak
    def show(self):
        # Traversing from head to end and Printing the elements
        sh = self.head
        while sh.next is not None:
            print(sh.date, end=" ")
            sh = sh.next
        print(sh.date)

    # function for getting day and dates
    def weak(self, dates):
        # creating a list of days with keys
        days = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
        # declaring an iterator count
        count = 1
        for i in dates:
            weak.add(self, days[count], i)
            count += 1


# Driver program
if __name__ == '__main__':
    # creating an object for Queue class
    que = Queue()
    # getting inputs from user
    try :
        year = int(input("year = "))
        month = int(input("month = "))
        # creating an object for calender to get the dates
        cal = calender()
        dates = cal.month(year, month)
        # declaring months dictionary
        m = {1:"January",2:"February",3:"March",4:"Aprial",5:"May",6:"June",7:"July",8:"Auguest",9:"September",10:"Octomber",11:"November",12:"December"}
        print()
        print("Calender")
        print("year {} {}  ".format(year,m[month]))
        # creating weak objects
        for i in dates:
            w = weak()
            w.weak(i)
            # adding the weak objects in to queue
            que.enque(w.show())
    except Exception:
        print("Enter valid year and month")
