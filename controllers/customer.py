from source.dbconnection import db,Customer

'''
This function returns Customer Lists.
'''
def getCustomerList():
    customer_list_json = []
    customer_list = Customer.query.all()
    for item in customer_list:
        customer_data = {}
        customer_data['id'] = item.id
        customer_data['name'] = item.name
        customer_list_json.append(customer_data)
    return customer_list_json

'''
This Function fetches the name from client application and inserts the values into Customer Table 
and return successful message "Customer added sucessfully".
'''
def addCustomerDB(name):
    addcustomer = Customer(name=name)
    db.session.add(addcustomer)
    db.session.commit()
    return 'Customer added sucessfully', 201