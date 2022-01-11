from src.domain.product.model import Suppliers
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class SuppliersRepository(SqlAlchemyRepository[Suppliers]):
  pass