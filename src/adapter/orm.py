from sqlalchemy import Table
from sqlalchemy.orm import mapper
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import DATETIME, FLOAT, Boolean, Float, Integer, String
from src.adapter.database import Base
from src.domain.product.model import Coupons, PaymentMethods, Product, Category, Suppliers

metadata = Base.metadata

table_product = Table(
  'products', 
  metadata, 
  Column('id', Integer, primary_key=True, autoincrement=True),
  Column('description', String(100)),
  Column('technical_details', String(255)),
  Column('price', Float(10, 2)),
  Column('visible', Boolean),
  Column('supplier_id',ForeignKey('suppliers.id')),
  Column('category_id',ForeignKey('categories.id'))
)

table_category = Table(
  'categories',
  metadata,
  Column('id', Integer, primary_key=True, autoincrement=True),
  Column('name', String(45))
)

table_suppliers = Table(
  'suppliers',
  metadata,
  Column('id', Integer, primary_key=True, autoincrement=True),
  Column('name', String(45))
)

table_coupons = Table(
  'coupons',
  metadata,
  Column('id', Integer, primary_key=True, autoincrement=True),
  Column('code', String(10)),
  Column('expire_at', DATETIME),
  Column('limit', Integer),
  Column('type', String(15)),
  Column('value', FLOAT),
  
)

table_payment_methods = Table(
  'payment_methods',
  metadata,
  Column('id', Integer, primary_key=True, autoincrement=True),
  Column('name', String(45)),
  Column('enabled', Boolean)
)

def start_mapper():
  mapper(Product, table_product)
  mapper(Category, table_category)
  mapper(Suppliers, table_suppliers)
  mapper(Coupons, table_coupons)
  mapper(PaymentMethods, table_payment_methods)