# a. Desc ­> Create a Program which creates Banking Cash Counter where people
# come in to deposit Cash and withdraw Cash. Have an input panel to add people
# to Queue to either deposit or withdraw money and dequeue the people. Maintain
# the Cash Balance.
# b. I/P ­> Panel to add People to Queue to Deposit or Withdraw Money and dequeue
# c. Logic ­> Write a Queue Class to enqueue and dequeue people to either deposit
# or withdraw money and maintain the cash balance
# ------------------------------------------------------------------------------------
# importing required packages
from DataStructProg.Queue import *

# createing a queue
queue_obj = Queue()
count_persons = int(input("Enter no of persons at begining:"))
for i in range(count_persons):
    queue_obj.enqueue(1)
bankamount = int(input("Enter amount present in bank at begining:"))
while count_persons >0:
    if count_persons == 0:
        break
    print("--------------------------Greetings--------------------------------")
    print("1. Deposit")
    print("2. WithDraw")
    print("3. Add persons to queue")
    print("4. Exit from queue")
    print("5. check bank balance")
    print("6. No. of members in Queue")
    print("7. Exit from bank")
    print("--------------------------------------------------------------------")
    ch = int(input("Enter ur choice:"))

    if ch > 7 or ch < 1:
        print("Enter ur choice between 1 to 7 only")
        # Deposit
    elif ch == 1:
        deposit = int(input("enter the amount to be deposit"))
        queue_obj.dequeue()
        # add the deposited money to total money
        bankamount = bankamount + deposit
        print(deposit, " amount is deposited")
        # withdraw
    elif ch == 2:
        withdraw = int(input("enter the withdraw amount"))
        if withdraw < bankamount:
            queue_obj.dequeue()
            # deducting the withdraw money from total money
            bankamount = bankamount - withdraw
            print(withdraw, "amount is withdrawn")
        else:
            print("Insufficient funds:")
            print("Bank Balance",bankamount)
    elif ch == 3:
        persons = int(input("enter the how many member are to be add into the queue"))
        # increasing the count by persons
        count_persons = count_persons + persons
        # enqueue that persons
        # using the loop to enqueue 1 person at a time
        for i in range(persons):
            queue_obj.enqueue(1)
    elif ch == 4:
        # 4 exit a person from the queue
        queue_obj.dequeue()
        count_persons -= 1
    elif ch == 5:
        # 5 to show the balance money at the cashier
        print("Total Bank balance is: ",bankamount)
    elif ch == 6:
        # 6 total persons in the queue
        print("reaming persons in the queue", queue_obj.size())
    count_persons = queue_obj.size()
