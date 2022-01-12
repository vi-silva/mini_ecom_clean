from src.domain.product_discounts.model import ProductDiscounts
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork

def create_product_discounts(product , mode, value, payment_method, uow: SqlAlchemyUnitOfWork):
  with uow:
    uow.product_discounts_repository.add(ProductDiscounts(product=product,  mode=mode, value=value, payment_method=payment_method))
    uow.commit()