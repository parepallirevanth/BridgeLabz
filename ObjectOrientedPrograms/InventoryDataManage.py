import json

class Inventory:
    def __init__(self,dictionary):
        self.brand = dictionary.get("name")
        self.brand_price = dictionary.get("price")
        self.brand_weight = dictionary.get("weight")

class InventoryManager:
    def __init__(self):
        self.lst = []
    def calculate_price(self):
        sum = 0
        for obj in self.lst:
            sum +=obj.brand_price * obj.brand_weight
        return sum
obj_inventory_mgr = InventoryManager()
file = open("Inventory_data",'r')
data = json.load(file)
file.close()

for key,value in data.items():
    for dictionary in value:
        obj = Inventory(dictionary)
        obj_inventory_mgr.lst.append(obj)
print(f"the total inventory price of stock we have: {obj_inventory_mgr.calculate_price()} rs/-")
