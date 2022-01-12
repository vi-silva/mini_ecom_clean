from src.domain.product_discounts.model import ProductDiscounts
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class ProductDiscountsRepository(SqlAlchemyRepository[ProductDiscounts]):
  def __init__(self, session):
      super().__init__(session)

  def add(self, model: ProductDiscounts):
    return super().add(model)

  def get_by_product_and_payment(self, products_id, payment_methods_id):
    return self.session.query(ProductDiscounts).filter_by(products_id = products_id, payment_methods_id = payment_methods_id).first()