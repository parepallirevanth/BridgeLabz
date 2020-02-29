# 9.
# 2D Array
# a. Desc ­> A library for reading in 2D arrays of integers, doubles, or booleans from
# standard input and printing them out to standard output.
# b. I/P ­> M rows, N Cols, and M * N inputs for 2D Array. Use Java Scanner Class
# c. Logic ­> create 2 dimensional array in memory to read in M rows and N cols
# d. O/P ­> Print function to print 2 Dimensional Array. In Java use PrintWriter with
# OutputStreamWriter to print the output to the screen.
# ----------------------------------------------------------------------------------------

# functions for twod array for reading int, double and bool type
def TwoDArray(rows, cols):
    # created an array with row * col size
    Multi_Datatype_Array = [[0 for i in range(cols)] for j in range(rows)]

    # initialising array with int,double and bool type dynamically
    for i in range(rows):
        for j in range(cols):
            Multi_Datatype_Array[i][j] = float(input("Enter float value:"))
            j = j + 1
            Multi_Datatype_Array[i][j] = int(input("Enter int value"))
            j = j + 1
            Multi_Datatype_Array[i][j] = bool(input("Enter bool value"))
            break
    # prints the two dimensional array
    for i in range(rows):
        for j in range(cols):
            print(Multi_Datatype_Array[i][j],end=' ')
            # print(type(arr[i][j]))
        print()

if __name__ == '__main__':
    TwoDArray(3, 3)
