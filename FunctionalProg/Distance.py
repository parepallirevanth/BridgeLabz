# 11. Write a program Distance.java that takes two integer command­line arguments x
# and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
# formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function
# -----------------------------------------------------------------------------------------
from cmath import sqrt


# function to find  distance
def Distance(x, y):
    # calculate distance using sqrt(x**2 + y**2) and returns
    return sqrt(x ** 2 + y ** 2)


if __name__ == '__main__':
    x = float(input("Enter x point"))
    y = float(input("Enter y point"))
    print(Distance(x, y))  # calls the function
