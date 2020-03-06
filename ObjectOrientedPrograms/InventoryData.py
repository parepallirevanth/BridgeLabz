# importing json
import json
#  inventory function
def inventory():
    # reading json file consists of inventory
    file = open("Inventory_data",'r')
    # loading data into object
    data = json.load(file)
    file.close()
    # iterating the data and extracting data from obj
    for key, value in data.items():
        print(f"The {key} details are as follows: ")
        for dictionary in value:
            for keys, values in dictionary.items():
                print(f"{keys} : {values}")
        print()
inventory()
