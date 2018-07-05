from source.dbconnection import db,Inventory,Bill,Customer

'''
This function returns bills where payment is pending
'''
def duePaymentList():
    new = []
    customer_due = Bill.query.filter_by(has_payed=False).all()
    for name in customer_due:
        inventory_name = Inventory.query.filter_by(id=name.inventory_id).all()
        customer_name = Customer.query.filter_by(id=name.customer_id).all()
        if inventory_name and customer_name:
            due_payment = [name.id, inventory_name[0].name, customer_name[0].name]
            new.append(due_payment)
    return new

'''
This function fetches bill_id from client application and update the "Bill" table and return successful message
"PAYMENT SUCCESSFUL
'''
def paid(bill_value):
    billid = Bill.query.filter_by(id=bill_value).one()
    billid.has_payed = True
    db.session.add(billid)
    db.session.commit()
    return "PAYMENT SUCCESSFUL", 201