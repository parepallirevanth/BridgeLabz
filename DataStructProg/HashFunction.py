# Hashing Function to search a Number in a slot
# a. Desc ­> Create a Slot of 10 to store Chain of Numbers that belong to each Slot to
# efficiently search a number from a given set of number
# b. I/P ­> read a set of numbers from a file and take user input to search a number
# c. Logic ­> Firstly store the numbers in the Slot. Since there are 10 Numbers divide
# each number by 11 and the reminder put in the appropriate slot. Create a Chain
# for each Slot to avoid Collision. If a number searched is found then pop it or else
# push it. Use Map of Slot Numbers and Ordered LinkedList to solve the problem.
# In the Figure Below, you can see number 77/11 reminder is 0 hence sits in the 0
# slot while 26/11 remainder is 4 hence sits in slot 4
# d. O/P ­> Save the numbers in a file
# ----------------------------------------------------------------------------------------

hash_table = [[] for _ in range(11)]


# hash function
def hashing_func(key):
    return key % 11 #len(hash_table)


# function to append
def insert( hash_table,key,value):
    hash_key = hashing_func(key)
    hash_table[hash_key].append(value)

if __name__ == '__main__':
    print(len(hash_table))
    print (hashing_func(10))
    print (hashing_func(20))
    print (hashing_func(25))
    # inser
    insert(hash_table,10,'Nepal')
    print(hash_table)
    insert(hash_table,25,'USA')
    print(hash_table)
    insert(hash_table,20,'India')
    print(hash_table)
