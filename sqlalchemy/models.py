import sys
sys.path.insert(0, "")

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Unicode
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, backref

from database.connector import engine, session

Base = declarative_base()

# I"m using alchemy database from MySQL.
# Now, I want to create tables

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), index=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    products = relationship("Product", back_populates="category")
    
    def __repr__(self):
        return f"Category {self.name}"

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), index=True)
    cell_phone = Column(Unicode(20))
    country = Column(String(255))
    state = Column(String(255))
    street = Column(String(255))
    number = Column(Integer)
    additionals = Column(String(255))
    orders = relationship("Order", back_populates="costumer")
    items = relationship("Item", back_populates="costumer")

    def __repr__(self):
        return f"Customer {self.name}"

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    total_price = Column(Float(50))
    order_id = Column(Integer, ForeignKey("order.id"))
    order = relationship("Order", back_populates="item")
    product_id = Column(Integer, ForeignKey("product.id"))
    product = relationship("Product", back_populates="item")

    def __repr__(self):
        return f"Item {self.name}"

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    status = Column(String(255))
    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates="order")
    items = relationship("Item", back_populates="order")

    def __repr__(self):
        return f"Order {self.name}"

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    number = Column(Float(50), index=True)
    category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship("Category", back_populates="product")

    def __repr__(self):
        return f"Product {self.name}"

Base.metadata.create_all(engine)