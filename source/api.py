from flask_restplus import Resource, Api
from source import app
from flask import json,request
from controllers.customer import addCustomerDB,getCustomerList
from controllers.inventory import getInventoryList,addInventoryDB
from controllers.payment import duePaymentList,paid
from controllers.SellInventory import sellInventoryToCustomer

api = Api(app, version='1.0', title='Inventory Management System API', description='Inventory Management System')

'''
This function returns Customer Lists. 
'''
@api.route('/customerList')
class CustomerList(Resource):
  def get(self):
      try:
          return getCustomerList()
      except Exception as exe:
          print(exe.args[0])

'''
This Function fetches the name from client application and inserts the values into Customer Table 
and return successful message "Customer added sucessfully".
'''
@api.route('/addcustomer')
class AddCustomer(Resource):
    def post(self):
        try:
            jsondata = request.get_json()
            name = json.loads(jsondata)
            return addCustomerDB(name)
        except Exception as exe:
            print(exe.args[0])

'''
This function returns Inventory Lists.
'''
@api.route('/inventoryList')
class InventoryList(Resource):
  def get(self):
      try:
          return getInventoryList()
      except Exception as exe:
          print(exe.args[0])

'''
This function fetches name, description, price from client side and insert values into "Inventory" table 
and return successful message "Inventory added sucessfully"
'''
@api.route('/addInventory')
class AddInventory(Resource):
    def post(self):
        try:
            jsondata = request.get_json()
            inventory_data= json.loads(jsondata)
            name=inventory_data[0]
            description=inventory_data[1]
            price=inventory_data[2]
            return addInventoryDB(name,description,price)
        except Exception as exe:
            print(exe.args[0])


'''
This function returns bills where payment is pending
'''
@api.route('/paymentdue')
class PaymentDue(Resource):
   def get(self):
       try:
           return duePaymentList()
       except Exception as exe:
           print(exe.args[0])

'''
This function fetches bill_id from client application and update the "Bill" table and return successful message
"PAYMENT SUCCESSFUL
'''
@api.route('/payment')
class Payment(Resource):
    def post(bill_id):
        try:
            jsondata = request.get_json()
            bill_value = json.loads(jsondata)
            return paid(bill_value)
        except Exception as exe:
            print(exe.args[0])

'''
This function fetches the inventory and customer id form client application and insert values into "Bill" table
and return the successful message "Item Sold To Customer"
'''
@api.route('/SellToCustomer')
class SellToCustomer(Resource):
    def post(self):
        try:
            jsondata = request.get_json()
            sell_details = json.loads(jsondata)
            inventory_id = sell_details[0]
            customer_id = sell_details[1]
            return sellInventoryToCustomer(inventory_id,customer_id)
        except Exception as exe:
            print(exe.args[0])
