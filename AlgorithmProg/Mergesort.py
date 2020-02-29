# 9. Merge Sort ­ Write a program with Static Functions to do Merge Sort of list of
# Strings.
# a. Logic ­> To Merge Sort an array, we divide it into two halves, sort the two halves
# independently, and then merge the results to sort the full array. To sort a[lo, hi),
# we use the following recursive strategy:
# b. Base case: If the subarray length is 0 or 1, it is already sorted.
# c. Reduction step: Otherwise, compute mid = lo + (hi ­ lo) / 2, recursively sort the
# two subarrays a[lo, mid) and a[mid, hi), and merge them to produce a sorted
# result.
# ------------------------------------------------------------------------------------
# Function for Merge sort

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code to test the above code
if __name__ == '__main__':
    arr = [1, 43, 65, 2, 34, 19, 32, 44]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
