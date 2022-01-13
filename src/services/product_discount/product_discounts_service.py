from src.domain.product_discounts.model import ProductDiscounts
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork

def create_product_discounts(product_id , mode, value, payment_methods_id, uow: SqlAlchemyUnitOfWork):
  with uow:
    prod = uow.product_repository.get(id=product_id)
    if not prod:
      raise Exception()
    payment = uow.payment_methods_repository.get(id=payment_methods_id)
    if not payment:
      raise Exception()
    if payment.enabled == False:
      raise Exception()
    uow.product_discounts_repository.add(ProductDiscounts(product_id=product_id,  mode=mode, value=value, payment_methods_id=payment_methods_id, product=prod, payment_method = payment))
    uow.commit()