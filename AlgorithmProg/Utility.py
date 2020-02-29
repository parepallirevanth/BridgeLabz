# binarySearch method for integer
# binarySearch method for String
# insertionSort method for integer
# insertionSort method for String
# bubbleSort method for integer
# bubbleSort method for String
# ---------------------------------------------------------

class utility():
    # -----------------------Binary search--------------------------#
    # function for binary search of integers
    @staticmethod
    def binarysearch_int(a, l, h, num):
        # calling  sorting method to sort array
        #utility.insertionsort_int(a)
        a.sort()
        if h >= l:
            # find the mid loc of subarray
            mid = l + (h - l) // 2
            # if element found at mid position returns
            if a[mid] == num:
                return 'num is found'
            # compares element of mid and given element
            # if mid > search element mid is set as high(end loc)
            elif a[mid] > num:
                return utility.binarysearch_int(a, l, mid - 1, num)
            # if search ele is greater than mid element then mid is set as start
            else:
                return utility.binarysearch_int(a, mid + 1, h, num)
        else:
            return 'num is not found'

    @staticmethod
    def binaryserach_string(a, l, h, string):
        # calling  sorting method to sort array
        # utility.insertionsort_string(a)
        a.sort()
        if h >= l:
            # find the mid loc of subarray
            mid = l + (h - l) // 2
            # if element found at mid position returns
            if a[mid] == string:
                return 'string is found'
            # compares element of mid and given element
            # if mid > search element mid is set as high(end loc)
            elif a[mid] > string:
                return utility.binaryserach_string(a, l, mid - 1, string)
            # if search ele is greater than mid element then mid is set as start
            else:
                return utility.binaryserach_string(a, mid + 1, h, string)
        else:
            return 'string is not found'

    # ---------------------------------Insertion method-----------------------------#
    @staticmethod
    def insertionsort_int(array):
        # Transverse upto length of array
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            # iterates loop to a[0].....a[n]
            # compares a[j]>a[j+1] if satisfies swaps the elements
            while j > 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key
        return array

    @staticmethod
    # insertion method of strings
    def insertionsort_string(array):
        # Transverse upto length of array
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            # iterates loop to a[0].....a[n]
            # compares a[j]>a[j+1]
            # swaps the elements if greather
            while j > 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key
        return array

    @staticmethod
    # -----------------------------------Bubble sort---------------------------------------#
    def bubblesort_int(array):
        length = len(array)
        for i in range(length):
            for j in range(0, length - i - 1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array

    @staticmethod
    def bubblesort_string(array):
        length = len(array)
        for i in range(length):
            for j in range(0, length - i - 1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array
