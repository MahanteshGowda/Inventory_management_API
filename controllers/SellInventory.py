from source.dbconnection import db,Bill
'''
This function fetches the inventory and customer id form client application and insert values into "Bill" table
and return the successful message "Item Sold To Customer"
'''
def sellInventoryToCustomer(inventory_id,customer_id):
        soldInventory = Bill(inventory_id=inventory_id, customer_id=customer_id, has_payed=False)
        db.session.add(soldInventory)
        db.session.commit()
        return "Item Sold To Customer", 201