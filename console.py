from src.domain.category.model import Category
from src.domain.suppliers.model import Suppliers
from src.domain.coupons.model import Coupons
from src.domain.product.model import Product
from src.domain.payment_methods.model import PaymentMethods
from src.domain.product_discounts.model import ProductDiscounts
from src.services.address_service import create_address
from src.services.customers_service import create_customer
from src.services.product_discounts_service import create_product_discounts
from src.services.product_service import create_product
from src.services.coupon_service import create_coupon
from src.services.suppliers_service import create_supplier
from src.services.category_service import create_category
from src.services.payment_methods_service import create_payment_method
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork
from src.adapter.database import Session
from src.adapter.orm import start_mapper

from datetime import datetime, timedelta


start_mapper()
uow = SqlAlchemyUnitOfWork(Session())

create_address('Rua dos testes','testelandia','sp','74','18000000','Vale dos testes',True,1,uow)

create_category('teste',uow)

create_coupon('teste',datetime.now(),10,'percentage',19.00,uow)

create_customer('Testonio','testo','159999999','N','19928744',datetime.now()-timedelta(365*18),uow)

create_payment_method('teste', True,uow)

create_product_discounts(1, 'teste', 12, 1,uow)

create_product(description='teste 2', price=10, technical_details='detalhes tecnicos', image='', visible=True,suppliers_id=1,categories_id=1,uow=uow)

create_supplier('teste',uow)

import pdb
pdb.set_trace()
