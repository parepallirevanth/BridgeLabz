# binarySearch method for integer
# binarySearch method for String
# insertionSort method for integer
# insertionSort method for String
# bubbleSort method for integer
# bubbleSort method for String
# --------------------------------------
from AlgorithmProg.Utility import utility
import time

if __name__ == '__main__':
    utility_obj = utility()
    # considering range
    range_array = int(input("Enter no of integer elements to be inserted:"))
    # initialising int array
    int_array = [int(input(' enter integer ele: ')) for i in range(0, range_array)]

    # initialising string array
    string_array = [input("enter string ele:") for i in range(0, range_array)]

    # -----------------Binary serach------------------------------------
    low = 0
    high = range_array - 1
    find_num = int(input( "Enter number to be found:" ))
    find_string = input ( " Enter string to be found:" )
    #   calling and printing binary serach functions
    initial_time = time.time()
    print(utility_obj.binarysearch_int(int_array, low, high, find_num))
    end_time = time.time()
    print("Elapsed time", end_time - initial_time)

    initial_time = time.time()
    print(utility_obj.binaryserach_string(string_array, low, high, find_string))
    end_time = time.time()
    print("Elapsed time", end_time - initial_time)

    #   ---------------InsertionSort----------------------------------------
    initial_time = time.time()
    print(utility_obj.insertionsort_int(int_array))
    end_time = time.time()
    print(" Elapsed time ", end_time - initial_time)

    initial_time = time.time()
    print(utility_obj.insertionsort_string(string_array))
    end_time = time.time()
    print(" Elapsed time ", end_time - initial_time)
    #   ----------------Bubblesort___________________________________________
    initial_time = time.time()
    print(utility_obj.bubblesort_int(int_array))
    end_time = time.time()
    print(" Elapsed time ", end_time - initial_time)

    initial_time = time.time()
    print(utility_obj.bubblesort_string(string_array))
    end_time = time.time()
    print(" Elapsed time ", end_time - initial_time)
