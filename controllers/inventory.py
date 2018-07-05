from source.dbconnection import db,Inventory

'''
This function returns Inventory Lists.
'''
def getInventoryList():
    inventory_list_json = []
    inventory_list = Inventory.query.all()
    for item in inventory_list:
        inventory_data = {}
        inventory_data['id'] = item.id
        inventory_data['name'] = item.name
        inventory_data['description'] = item.description
        inventory_data['price'] = item.price
        inventory_list_json.append(inventory_data)
    return inventory_list_json

'''
This function fetches name, description, price from client side and insert values into "Inventory" table 
and return successful message "Inventory added sucessfully"
'''
def addInventoryDB(name,description,price):
    newInventory = Inventory(name=name, description=description, price=price)
    db.session.add(newInventory)
    db.session.commit()
    return 'Inventory added sucessfully', 201