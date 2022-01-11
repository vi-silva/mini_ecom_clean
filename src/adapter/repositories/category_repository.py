from src.domain.product.model import Category
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class CategoryRepository(SqlAlchemyRepository[Category]):
  pass