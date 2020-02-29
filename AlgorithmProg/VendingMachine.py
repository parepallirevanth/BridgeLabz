# 10. Find the Fewest Notes to be returned for Vending Machine
# a. Desc ­> There is 1, 2, 5, 10, 50, 100, 500 and 1000 Rs Notes which can be
# returned by Vending Machine. Write a Program to calculate the minimum number
# of Notes as well as the Notes to be returned by the Vending Machine as a
# Change
# b. I/P ­> read the Change in Rs to be returned by the Vending Machine
# c. Logic ­> Use Recursion and check for largest value of the Note to return change
# to get to minimum number of Notes.
# ------------------------------------------------------------------------------------

def vendingmachine(money):
    count2 = 0
    for denomination in [1000, 500, 100, 50, 10, 5, 2, 1]:
        count = 0
        while money // denomination != 0:
            count = count + 1
            count2 = count2 + 1
            money = money - denomination
        print(denomination, " ", count)
    return count2


if __name__ == '__main__':
    money = int(input("Enter amount to withdraw:"))
    print("No.of notes:", vendingmachine(money))
