from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Products(Base):
	__tablename__ = "products"
	id = Column(Integer, primary_key = True)
	name = Column(String)
	price = Column(Integer)
	quality = Column(Integer)
	description = Column(String)
	used = Column(Boolean)

	def __repr__(self):
		return "\nname: " + self.name + "\nprice: " + self.price + "\nquality: " + self.quality + "\ndescription: " + self.description + "\nused: " + self.used