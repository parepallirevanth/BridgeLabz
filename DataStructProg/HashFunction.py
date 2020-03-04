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

# hash function
def hashing_func(value):
    return hash(value) % len(hash_table)  # len(hash_table) = 11


# function to append
def insert(hash_table, value):
    # finding the pos of the value
    # hk = hash(1) % 11
    hash_key = hashing_func(value)
    # adding values to the hashtable
    hash_table[hash_key].append(value)
    hash_table[hash_key].sort()

# function to search
def search(hash_table, key):
    # finding the pos of value
    hash_key = hashing_func(key)
    bucket = hash_table[hash_key]
    #iterates the list upto end
    for i in enumerate(bucket):
        k, v = i #(0,44) (1,55) (2,77)
        # equates the value
        # if found then pops the value
        if key == v:
            return delete(hash_table, v,k,bucket)
        # else add the value to hashtable
    print('Key {} added'.format(key))
    return insert(hash_table, key)

# function to delete
def delete(hash_table, v,k,bucket):
    # deletes the value at positin
    del bucket[k]
    print('Key {} deleted'.format(v))
    return hash_table

# function to read from file
def readfile():
      try:
        # def words_read():
        file = open("hash_num", "r")
        # created a linked list
        words_list = []
        # storing the elements into list
        for i in file:
            str_x = i.split(',')
            for j in str_x:
                # STORING DATA  into list
                words_list.append(int(j))
        file.close()
      except Exception:
          print("File not found")
      return words_list

# function to write into file

def writefile(words_list):
    # def words_read():
    file = open("hash_num1", "w")
    for i in range(len(words_list)):
        for j in words_list[i]:
            if j:
                file.write("{} ".format(j))
    file.close()

# driver program
if __name__ == '__main__':
    hash_table = [[] for _ in range(11)]
    a = readfile()
    # printing elements in file
    for index in a:
        insert(hash_table, index)
    try:
        # i/p integer to search
        search_key = int(input("Enter a number to search: "))
        print(hash_table)
        # calling function to search
        sk = search(hash_table, search_key)
        print(hash_table)
        print("Written in file: check file hash_num1")
        writefile(hash_table)
    except Exception:
        print("Error: please insert numbers only:")
