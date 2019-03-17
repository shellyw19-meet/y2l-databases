from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name, price, quality, description, used):
	if quality > 5:
		return "error"
	if quality < 1:
		return "error"
	product = Products(name = name, price = price, quality = quality, description = description, used = used)
	session.add(product)
	session.commit()
	return "success"

def update_product(id):
	product = session.query(Products).filter_by(id=id).first()
	product.price += 1
	product.quality -= 1
	session.commit()



def delete_product(id):
	session.query(Products).filter_by(id=id).delete()
	session.commit()

def get_product(id):
	product = session.query(Products).filter_by(id = id).first()
	return product

# create_product("chair", 20, 5, "very strong", False)
# # delete_product(1)
# update_product(1)
print(get_product(2))
