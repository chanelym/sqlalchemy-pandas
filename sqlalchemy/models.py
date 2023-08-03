import sys
sys.path.insert(0, '')

from sqlalchemy import Column, Date, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from database.connector import engine, session

Base = declarative_base()

# I'm using alchemy database from MySQL.
# Now, I want to create tables

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(255))
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    products = relationship(Product, backref="users")
    
    def __repr__(self):
        return f'Category {self.name}'

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))
    cell_phone = Column(Unicode(20))
    country = Column(String(255))
    state = Column(String(255))
    street = Column(String(255))
    number = Column(Integer(50))
    additionals = Column(String(255))
    orders = relationship(Order, backref="customers")

    def __repr__(self):
        return f'Customer {self.name}'

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    quantity = Column(Integer(50))
    total_price = Column(Float(50))
    order_id = Column(Integer, ForeignKey('order.id'))
    order = relationship('Order')
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship('Product')

    def __repr__(self):
        return f'Item {self.name}'

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    status = Column(String(255))
    customer_id = Column(Integer, ForeignKey('customer.id'))
    customer = relationship('Customer')
    items = relationship(Order, backref="orders")

    def __repr__(self):
        return f'Order {self.name}'

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(255))
    number = Column(Float(50))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category')
    items = relationship(Order, backref="products")

    def __repr__(self):
        return f'Product {self.name}'

Base.metadata.create_all(engine)