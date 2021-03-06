from src.adapter.repositories.category_repository import CategoryRepository
from src.adapter.repositories.payment_methods_repository import PaymentMethodsRepository
from src.adapter.repositories.suppliers_repository import SuppliersRepository
from src.adapter.repositories.product_repository import ProductRepository
from src.adapter.repositories.addresses_repository import AddressesRepository
from src.adapter.repositories.coupon_repository import CouponsRepository
from src.adapter.repositories.customers_repository import CustomersRepository
from src.adapter.repositories.payment_methods_repository import PaymentMethodsRepository
from src.adapter.repositories.product_discounts_repository import ProductDiscountsRepository
from src.adapter.repositories.order_repository import OrderRepository
from src.domain.addresses.model import Addresses
from src.domain.category.model import Category
from src.domain.coupons.model import Coupons
from src.domain.customers.model import Customers
from src.domain.product_discounts.model import ProductDiscounts
from src.domain.suppliers.model import Suppliers
from src.domain.payment_methods.model import PaymentMethods
from src.domain.product.model import Product
from src.domain.order.model import Order
from src.adapter.database import Session

class SqlAlchemyUnitOfWork:
  def __init__(self):
      self.session = Session()


  def __enter__(self):
    self.category_repository = CategoryRepository(self.session, Category)
    self.supplier_repository = SuppliersRepository(self.session, Suppliers)
    self.product_repository = ProductRepository(self.session, Product)
    self.addresses_repository = AddressesRepository(self.session, Addresses)
    self.coupons_repository = CouponsRepository(self.session, Coupons)
    self.customers_repository = CustomersRepository(self.session, Customers)
    self.payment_methods_repository = PaymentMethodsRepository(self.session, PaymentMethods)
    self.product_discounts_repository = ProductDiscountsRepository(self.session, ProductDiscounts)
    self.order_repository = OrderRepository(self.session, Order)
    

  def __exit__(self, *args):
    self.session.rollback()
    self.session.close()

  def commit(self):
    self.session.commit()