from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    product = Column(String, nullable=False, unique=True)
    stock_qty = Column(Integer, nullable=False)