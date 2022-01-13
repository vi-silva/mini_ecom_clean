from src.domain.product_discounts.model import ProductDiscounts
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork
from src.services.product_discount.product_discounts_dto import ProductDiscountsDTO

def create_product_discounts(product_discount_dto: ProductDiscountsDTO, uow: SqlAlchemyUnitOfWork):
  with uow:
    prod = uow.product_repository.get(id=product_discount_dto.product_id)
    if not prod:
      raise Exception()
    payment = uow.payment_methods_repository.get(id=product_discount_dto.payment_methods_id)
    if not payment:
      raise Exception()
    if payment.enabled == False:
      raise Exception()
    product_discount_dto.product = prod
    product_discount_dto.payment_method = payment
    uow.product_discounts_repository.add(ProductDiscounts(**product_discount_dto.__dict__))
    uow.commit()