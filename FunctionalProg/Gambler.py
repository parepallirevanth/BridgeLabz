# 7. Gambler
# a. Desc ­> Simulates a gambler who start with $stake and place fair $1 bets until
# he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
# times he/she wins and the number of bets he/she makes. Run the experiment N
# times, averages the results, and prints them out.
# b. I/P ­> $Stake, $Goal and Number of times
# c. Logic ­> Play till the gambler is broke or has won
# d. O/P ­> Print Number of Wins and Percentage of Win and Loss.
# ------------------------------------------------------------------------------------
import random


# class Gambler:
# Gambler function
def gambler(stake, goal, times):
    bet = 1
    win = loss = temp = 0
    for i in range(1, times + 1):
        if (
                random.random() >= 0.5):  # if generated random is gt 0.5 gamer wins then stake incremnts by 1  and bets again
            win = win + 1
            stake = stake + bet
            if (stake == goal):
                break
        else:  # if generated random is lt 0.5 games loose then stake decrements by 1
            loss = loss + 1
            stake = stake - bet
            if (stake == 0):
                break
        temp = i

    if (temp <= times and stake == goal):  # if reached goal with in times of play then loop breaks  and player wins
        print("Hurray!!! goal has be reached")
    elif (temp == times and stake != goal):  # if goal not reached within time then loop breaks and player loose
        print("Times up ,Goal not reached")
    else:  # if stake is zero then loop breaks
        print("No more Stake")

    print("No.of Wins:", win)
    print("Win percentage:", win * 100 / temp)  # prints winning percentage
    print("No.of Loss:", loss)
    print("Loss percentage", loss * 100 / temp)  # prints loss percentage


if __name__ == '__main__':
    # gambler_object=Gambler()
    # gambler_object.gambler()
    stake = int(input("Enter stake amount: "))
    goal = int(input("Enter Goal to be reached: "))
    times = int(input("Enter number of times to be played: "))
    gambler(stake, goal, times)  # calls gambler function
