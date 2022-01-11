from src.domain.product.model import Coupons
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class CouponsRepository(SqlAlchemyRepository[Coupons]):
  pass