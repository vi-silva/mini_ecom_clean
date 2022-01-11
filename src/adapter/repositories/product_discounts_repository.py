from src.domain.product.model import ProductDiscounts
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class ProductDiscountsRepository(SqlAlchemyRepository[ProductDiscounts]):
  pass