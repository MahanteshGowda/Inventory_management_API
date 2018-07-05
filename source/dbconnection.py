
from flask_sqlalchemy import SQLAlchemy
from source import app
app.config['SQLALCHEMY_DATABASE_URI']='postgresql:///InventoryAPI'

db=SQLAlchemy(app)

class Inventory(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	description =db. Column(db.String(250))
	price = db.Column(db.Integer, nullable=False)


class Customer(db.Model):

	name = db.Column(db.String(80), nullable=False)
	id = db.Column(db.Integer, primary_key=True)

class Bill(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'))
   customer_id  = db.Column(db.Integer,db.ForeignKey('customer.id'))
   has_payed = db.Column(db.BOOLEAN, default = False)

if __name__=='__main__':
	db.create_all()
	app.run(debug=True)