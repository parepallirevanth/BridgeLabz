# 2. Flip Coin and print percentage of Heads and Tails
# a. I/P ­> The number of times to Flip Coin. Ensure it is positive integer .
# b. Logic ­> Use Random Function to get value between 0 and 1. If < 0.5 then tails or
# heads
# c. O/P ­> Percentage of Head vs Tails
# ---------------------------------------------------------------------------------
import random


# Function for coin flip to calculate percentage of wins and loss

def CoinFlip():
    head = 0
    tail = 0
    if times >= 0:  # checks entered times is positive or not
        for i in range(0, times):
            if random.random() >= 0.5:  # increments Head when random number is gt 0.5
                head = head + 1
            else:  # increments Tails when random number is lt 0.5
                tail = tail + 1
        print("\n", "No.of Heads: ", head, "\n", "Head Percentage: ", head * 100 / times, "\n",
              # prints percentage of win and loss
              "No.of Tails:", tail, "\n", "Tail percentage: ", (tail * 100) / times)
    else:
        print("Enter only positive number")


if __name__ == '__main__':
    times = int(input("Enter number of times to flip coin "))  # takes input as integer
    CoinFlip()
