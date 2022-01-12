from src.domain.product_discounts.model import ProductDiscounts
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork

def create_product_discounts(product_id , mode, value, payment_methods_id, uow: SqlAlchemyUnitOfWork):
  with uow:
    uow.product_discounts_repository.add(ProductDiscounts(product_id=product_id,  mode=mode, value=value, payment_methods_id=payment_methods_id))
    uow.commit()