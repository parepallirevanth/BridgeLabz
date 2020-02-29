# 5. Question to find your number
# a. Desc ­> takes a command­line argument N, asks you to think of a number
# between 0 and N­1, where N = 2^n, and always guesses the answer with n
# questions.
# b. I/P ­> the Number N and then recursively ask true/false if the number is between
# a high and low value
# c. Logic ­> Use Binary Search to find the number
# d. O/P ­> Print the intermediary number and the final answer
# --------------------------------------------------------------------------------------


def binarysearch(a, l, h):
    # calling  sorting method to sort array

    if h >= l:
        # find the mid loc of subarray
        mid = l + (h - l) // 2
        # if element found at mid position returns
        print(a[mid], "is ur number ?")
        if input() == 'y':  # a[mid] == num:
            return a[mid]
        # compares element of mid and given element
        # if mid > search element mid is set as high(end loc)
        elif input("is number gt than ur number ?") == 'y':  # a[mid] > num:
            return binarysearch(a, l, mid - 1)
        # if search ele is greater than mid element then mid is set as start
        else:
            return binarysearch(a, mid + 1, h)


if __name__ == '__main__':
    a = [i for i in range(int(input("Enter a range")) + 1)]
    print("Guess a number:")
    l = 0
    h = len(a) - 1
    g = 0
    k = binarysearch(a, l, h)
    if k:
        print(k, "Found")
    else:
        print('ur number is out of range')
