from src.adapter.repositories.product_repository import ProductRepository
from src.adapter.repositories.coupon_repository import CouponsRepository
from src.adapter.repositories.suppliers_repository import SuppliersRepository
from src.adapter.repositories.category_repository import CategoryRepository
from src.domain.product.model import Product, Coupons, Suppliers, Category
from src.adapter.database import Session
from src.adapter.orm import start_mapper

from datetime import datetime


start_mapper()

db = Session()

product_repository = ProductRepository(db)
product = Product(description='descricao 2', price=10, technical_details='detalhes tecnicos', image='', visible=True)
product_repository.add(product)
print(product.id)
print(product.description)

coupon_repository = CouponsRepository(db)
coupon = Coupons('abcde',datetime.now(),10,'percentage',19.00)
coupon_repository.add(coupon)
print(coupon.id)
print(coupon.code)




