# 14. Cross Game or Tic­Tac­Toe Game
# a. Desc ­> Write a Program to play a Cross Game or Tic­Tac­Toe Game. Player 1 is
# the Computer and the Player 2 is the user. Player 1 take Random Cell that is the
# Column and Row.
# b. I/P ­> Take User Input for the Cell i.e. Col and Row to Mark the ‘X’
# c. Logic ­> The User or the Computer can only take the unoccupied cell. The Game
# is played till either wins or till draw...
# d. O/P ­> Print the Col and the Cell after every step.
# e. Hint ­> The Hints is provided in the Logic. Use Functions for the Logic...
# -----------------------------------------------------------------------------------

# importing numpy and random array
import numpy as np
import random

# taking a numpy array initialising with zero
array = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])


# player function
def Player():
    # 1.checks weather array has empty places or not
    IsEmpty()
    # 2.Displays the array
    Display()
    # 3.takes the input position of player
    m = int(input("Enter row:"))
    n = int(input("Enter col"))
    # 4. checks weather entered position is empty or not if empty then it occupies with player
    if array[m][n] == 0:
        array[m][n] = 1
        # checks the winning condition and display the array
        if Winning(1):
            Display()
            exit()  # if wins then exit
        #print("Tie")
        Computer()  # after player chance goes to computer
    else:
        print("filled")  # if playerd choosen position is not empty then it again calls player untill crct input
        Player()


# computer function
def Computer():
    # Again checks weather array has empty places or not
    IsEmpty()
    # Displays the array
    Display()
    temp = 0
    # iterates until loop breaks
    while temp == 0:
        # Generates random input with in range
        m = random.randint(0, 2)
        n = random.randint(0, 2)
        # checks random position is empty or not
        # if empty then it ocuupied by computer
        if array[m][n] == 0:
            array[m][n] = 2
            break
            # if occupied by player then again it calls computer
        else:
            Computer()
    # checks winning condition of computer
    if Winning(2):
        # if wins then it display the array and exits
        Display()
        exit()
    # otherwise calls player for next choice
    else:
        Player()


# winning function
def Winning(pas):
    letter = pas
    # checks weather any horizantal row has same element or not
    for i in range(0, 3):
        count = 0
        for j in range(0, 3):
            if array[i][j] == letter:
                count = count + 1
        if (count == 3):
            print("win ", letter)
            return True

        count = 0
        # checks weather any vertical column has same element  or not
        for k in range(3):
            if array[k][i] == letter:
                count = count + 1
        if count == 3:
            print("Win", letter)
            return True
        # checks weather daiagonals has same element or not
        if array[0][0] == array[1][1] == array[2][2] == letter or array[0][2] == array[1][1] == array[2][0] == letter:
            print("Win", letter)
            return True
    return False


# Display function
# displays the array
def Display():
    print(array)


# IsEmpty function
# checks weather given array is empty or not and return status
def IsEmpty():
    for i in range(3):
        for j in range(3):
            if array[i][j] == 0:
                return True
    return print("tie", exit())


# Driver program Main function
if __name__ == '__main__':
    Player()
