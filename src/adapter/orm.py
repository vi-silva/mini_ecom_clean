from re import T
from sqlalchemy import Table
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import DATE, FLOAT, Boolean, Float, Integer, String
from src.adapter.database import Base
from src.domain.addresses.model import Addresses
from src.domain.customers.model import Customers
from src.domain.product.model import Product
from src.domain.product_discounts.model import ProductDiscounts
from src.domain.suppliers.model import Suppliers
from src.domain.coupons.model import Coupons
from src.domain.category.model import Category
from src.domain.payment_methods.model import PaymentMethods

metadata = Base.metadata

table_product = Table(
  'products', 
  metadata, 
  Column('id', Integer, primary_key=True, autoincrement=True),
  Column('description', String(100)),
  Column('technical_details', String(255)),
  Column('price', Float(10, 2)),
  Column('visible', Boolean),
  Column('suppliers_id',ForeignKey('suppliers.id')),
  Column('categories_id',ForeignKey('categories.id'))
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
  Column('expire_at', DATE),
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

table_product_discounts = Table(
  'product_discounts',
  metadata,
  Column('id', Integer, primary_key=True, autoincrement=True),
  Column('products_id', ForeignKey('products.id')),
  Column('payment_methods_id', ForeignKey('payment_methods.id')),
  Column('mode',String(45)),
  Column('value',FLOAT)
)

table_addresses = Table(
  'addresses',
  metadata,
  Column('id', Integer, primary_key=True, autoincrement=True),
  Column('address',String(255)),
  Column('city',String(45)),
  Column('state',String(2)),
  Column('number',String(10)),
  Column('zipcode',String(6)),
  Column('neighbourhood',String(45)),
  Column('primary',Boolean),
  Column('customer_id',String(45), ForeignKey('customers.id'))
)

table_customers = Table(
  'customers',
  metadata,
  Column('id', Integer, primary_key=True, autoincrement=True),
  Column("first_name",String(45)),
  Column("last_name",String(45)),
  Column("phone_number",String(15)),
  Column("genre",String(45)),
  Column("document_id",String(45)),
  Column("birth_date",DATE),
)

def start_mapper():
  category_mapper = mapper(Category, table_category)
  supplier_mapper = mapper(Suppliers, table_suppliers)
  payment_methods_mapper = mapper(PaymentMethods, table_payment_methods)
  product_discount_mapper = mapper(ProductDiscounts, table_product_discounts, properties={
    'payment_methods': relationship(payment_methods_mapper)
  })
  mapper(Coupons, table_coupons)
  mapper(Product, table_product, properties={
    'categories':relationship(category_mapper),
    'suppliers': relationship(supplier_mapper),
    'discounts': relationship(product_discount_mapper)
  })
  addresses_mapper = mapper(Addresses, table_addresses)
  mapper(Customers, table_customers, properties={
    'addresses':relationship(addresses_mapper)
  })