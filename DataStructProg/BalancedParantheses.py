# Simple Balanced Parentheses
# a. Desc ­> Take an Arithmetic Expression such as
# (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3) where parentheses are used to order the
# performance of operations. Ensure parentheses must appear in a balanced
# fashion.
# b. I/P ­> read in Arithmetic Expression such as (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)
# c. Logic ­> Write a Stack Class to push open parenthesis “(“ and pop closed
# parenthesis “)”. At the End of the Expression if the Stack is Empty then the
# Arithmetic Expression is Balanced. Stack Class Methods are Stack(), push(),
# pop(), peak(), isEmpty(), size()
# d. O/P ­> True or False to Show Arithmetic Expression is balanced or not.
# -------------------------------------------------------------------------------------
# balanced parantheses
from DataStructProg.Stack import *
# function Balanced para
def balancepara():
    # creating a empty stack
    exprstack = Stack()
    # taking a input
    Expression = input("Enter the expression to check balanced () or not:")
    # iterates to the length of given expression
    for i in range(len(Expression)):
        # if open para then push operation performs
        if Expression[i] == '(':
            exprstack.push(Expression[i])
            # if closed para then pop operation performs
        elif Expression[i] == ')':
            exprstack.pop()
        # checks weathers stack is empty or not
    if exprstack.isEmpty():
        # if stack is empty balanced
        return ("Balanced paranthses")
    else:
        # else unbalanced
        return ("Unbalanced parantheses")

if __name__ == '__main__':
    print(balancepara())
exprstack = Stack()

