# 10. Sum of three Integer adds to ZERO
# a. Desc ­> A program with cubic running time. Read in N integers and counts the
# number of triples that sum to exactly 0.
# b. I/P ­> N number of integer, and N integer input array
# c. Logic ­> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
# d. O/P ­> One Output is number of distinct triplets as well as the second output is to
# print the distinct triplets.
# -----------------------------------------------------------------------------------------

# function for Distinct triplets
def Triplets(array):
    flag = 0
    length = len(array)
    for i in range(0, length - 2):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                if array[i] + array[j] + array[k] == 0:
                    print(array[i], array[j], array[k])
                    flag = 1
    return flag


if __name__ == '__main__':
    Num = int(input("Enter no of elements"))
    array = [0 for i in range(Num)]
    print("Enter distinct numbers to find triplets:")
    for i in range(0, Num):
        array[i] = int(input())
    f = Triplets(array)
    if f == 0:
        print("No distinct triplets")
